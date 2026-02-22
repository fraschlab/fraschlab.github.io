# Frasch Lab Website

**https://fraschlab.github.io**

Perinatal Neuroscience & Biosensor Research lab website, built with Jekyll and hosted on GitHub Pages.

## Editing Content

All pages are Markdown files. To update content:

1. Edit the relevant `.md` file
2. Commit and push to `main`
3. GitHub Actions will automatically rebuild and deploy the site

## Site Structure

```
index.md                    # Home page
about/
  index.md                  # About / PI / Team
  trainees.md               # Past trainees
  ask.md                    # Contact
research/
  index.md                  # Research overview
  brain/
    stress.md               # Prenatal stress
    neuroinflammation.md    # Neuroinflammation
    ischemia.md             # Brain ischemia
  biosensors/
    ecg.md                  # ECG biosensors
    eeg.md                  # EEG monitoring
  early-life-roi.md         # Early life ROI
  impact.md                 # Research impact
  brain-health.md           # Brain health
  s-index.md                # S Index
  data-sets.md              # Open data sets
  in-silico.md              # Computational models
  preprints.md              # Preprints & protocols
news/
  index.md                  # Current news
  past.md                   # Past news
funding.md                  # Funding sources
networks.md                 # Professional networks
links.md                    # Useful links & tools
blog.md                     # Blog posts
```

## Local Development

```bash
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

## Adding a New Page

1. Create a new `.md` file in the appropriate directory
2. Add front matter at the top:
   ```yaml
   ---
   layout: default
   title: "Your Page Title"
   ---
   ```
3. Add the page to `_data/navigation.yml` if it should appear in the nav
4. Commit and push

## Customization

- **Styling:** `assets/css/style.css`
- **Layout:** `_layouts/default.html`
- **Navigation:** `_data/navigation.yml`
- **Site config:** `_config.yml`
