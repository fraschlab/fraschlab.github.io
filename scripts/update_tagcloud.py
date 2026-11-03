"""Tag cloud data from Frasch MG publications in PubMed -> _data/tagcloud.yml.

Counts words only in article titles, abstracts and author keywords (PubMed XML), so author names,
affiliations, DOIs and PMIDs never enter. STOP removes generic, publishing and geographic words.
"""
import json, re, urllib.request, xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
STOP = set("""
the and for with from that this was were are been being have has had will would could should may might can its our their
these those which where when what how than into also but not all both each more most other some such only very just about
between through during before after above below under over using used use based among within per via two three four five six
new non one first second however well associated related compared showed show shows found results result conclusion
conclusions methods method background objective objectives purpose aim aims introduction discussion study studies patients
patient group groups significant significantly respectively total included including observed demonstrated performed
assessed evaluated measured determined identified reported described presented investigated examined obtained provided
suggested indicated revealed higher lower increased decreased reduced increase decrease high low here there thus therefore
while whether although because due further even many much several various different same similar present potential
possible important specific overall available approach approaches analysis analyses data information research review
evidence role effect effects impact level levels time times use case cases model models system systems test tests total
number rate rates value values may year years day days week weeks month months hour hours min minutes after before during
paper article articles report reports journal authors author copyright rights reserved published publisher elsevier wiley
springer nature frontiers mdpi license licensed creative commons open access online doi pmid pmcid pubmed medline epub print
university department faculty school college institute institutes centre center centres centers hospital hospitals
laboratory lab division program programme foundation clinic clinics
frasch martin
canada canadian usa america american united states kingdom germany german france french italy italian netherlands dutch
switzerland swiss austria china chinese japan japanese australia australian india europe european montreal quebec
toronto ontario seattle washington california boston chicago new york london paris berlin jena munich zurich vienna
sherbrooke saskatoon saskatchewan alberta vancouver
early late response responses activity measure measures series control controls change changes scale findings finding
hypothesized hypothesize hypothesis chronically baseline severe frequency recovery outcome outcomes mechanisms mechanism
suggest suggests suggesting shown known whereas thereby within without across along toward towards
novel point points derived derive future vivo vitro difference differences scales provide provides provided condition conditions correlated correlate correlation detect detected moderate period periods variable variables
""".split())

def get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()

def main():
    ids = json.loads(get(f"{EUTILS}/esearch.fcgi?db=pubmed&term=Frasch+MG[Author]&retmax=400&retmode=json"))["esearchresult"]["idlist"]
    if not ids:
        print("No PubMed IDs found, keeping existing data"); return
    root = ET.fromstring(get(f"{EUTILS}/efetch.fcgi?db=pubmed&id={','.join(ids)}&retmode=xml"))
    text = []
    for art in root.iter("PubmedArticle"):
        for tag in ("ArticleTitle", "AbstractText", "Keyword"):
            text += ["".join(e.itertext()) for e in art.iter(tag)]
    words = [w for w in re.findall(r"[a-z][a-z-]{2,}[a-z]", " ".join(text).lower()) if w not in STOP]
    cnt = Counter(words)
    for w in list(cnt):   # fold plurals into the singular when both occur (fetuses -> fetus, animals -> animal)
        for suf in ("es", "s"):
            if w.endswith(suf) and w[:-len(suf)] in cnt and w in cnt:
                cnt[w[:-len(suf)]] += cnt.pop(w)
    top = cnt.most_common(80)
    if not top:
        print("No words extracted, keeping existing data"); return
    mx = top[0][1]
    out = ["# Research keyword frequencies - extracted from PubMed titles, abstracts and keywords",
           "# Auto-updated monthly via GitHub Actions (scripts/update_tagcloud.py)",
           f"# Last updated: {datetime.now(timezone.utc):%Y-%m-%d}", ""]
    for w, c in top:
        out += [f"- word: {w}", f"  weight: {max(20, int(95 * c / mx))}"]
    open("_data/tagcloud.yml", "w").write("\n".join(out) + "\n")
    print(f"Updated tag cloud with {len(top)} keywords from {len(ids)} publications")

if __name__ == "__main__":
    main()
