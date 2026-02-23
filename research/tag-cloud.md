---
layout: default
title: "Tag Cloud"
---

A visualization of research keywords from our publications, weighted by frequency. Updated monthly.

<canvas id="tagcloud" width="800" height="500" style="width:100%; max-width:800px; display:block; margin:0 auto;"></canvas>

<script>
(function() {
  var words = [
    {% for item in site.data.tagcloud %}
    { text: "{{ item.word }}", weight: {{ item.weight }} }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];

  var canvas = document.getElementById('tagcloud');
  var ctx = canvas.getContext('2d');
  var W = canvas.width, H = canvas.height;
  var placed = [];
  var colors = ['#4B2E84','#6B4FA4','#3A2268','#2c5282','#2b6cb0','#1a365d','#553c9a','#44337a','#285e61','#234e52'];

  words.sort(function(a,b){ return b.weight - a.weight; });

  var maxW = words[0].weight, minW = words[words.length-1].weight;

  function fontSize(w) {
    return Math.round(12 + (w - minW) / (maxW - minW) * 36);
  }

  function intersects(r) {
    for (var i = 0; i < placed.length; i++) {
      var p = placed[i];
      if (!(r.x + r.w < p.x || r.x > p.x + p.w || r.y + r.h < p.y || r.y > p.y + p.h)) return true;
    }
    return false;
  }

  for (var i = 0; i < words.length; i++) {
    var w = words[i];
    var size = fontSize(w.weight);
    ctx.font = (w.weight > 70 ? 'bold ' : '') + size + 'px Inter, sans-serif';
    var tm = ctx.measureText(w.text);
    var tw = tm.width + 6;
    var th = size + 4;
    var ok = false;

    for (var attempt = 0; attempt < 500; attempt++) {
      var angle = Math.random() * Math.PI * 2;
      var radius = attempt * 0.6;
      var x = W/2 + Math.cos(angle) * radius - tw/2;
      var y = H/2 + Math.sin(angle) * radius - th/2;
      var rect = {x:x, y:y, w:tw, h:th};

      if (x >= 0 && y >= 0 && x+tw <= W && y+th <= H && !intersects(rect)) {
        ctx.fillStyle = colors[i % colors.length];
        ctx.fillText(w.text, x + 3, y + size);
        placed.push(rect);
        ok = true;
        break;
      }
    }
  }
})();
</script>
