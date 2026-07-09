---
layout: default
title: "In Silico"
---

# In Silico Modeling of the Labour Process

The Frasch Lab, in collaboration with applied mathematicians from York University, developed a computational model of the labour process. This simulation provides understanding of cardiovascular and metabolic responses of the fetus during the trial of labour.

## About the Model

This digital model functions as a low-cost testing ground for validation of physiological hypotheses relevant to devising more efficient fetal health monitoring technologies. Newly gathered physiological data can refine the model and help researchers determine variables that cannot be directly measured.

The simulation captures the complex interplay between uterine contractions, umbilical cord compression, and fetal physiological responses, allowing researchers to explore scenarios that would be impossible or unethical to study directly.

## Fetal Twin: The Model, Implemented

The model now runs as open, source-available software: **[Fetal Twin](https://fetaltwin.org/)** — an in-silico testbed for fetal physiological development, and a testing ground for biomarker discovery where clinical data cannot go.

Fetal Twin is a mechanistic Python re-implementation and extension of the original MATLAB model. A 33-state system of ordinary differential equations couples five physiological layers — cardiovascular dynamics, metabolic and acid-base processes, autonomic nervous system activity, heart rate variability with pacemaker models, and gestational development — to generate synthetic cardiotocography (CTG) traces alongside the latent variables that clinicians cannot observe directly, such as pH, lactate, and perfusion pressure.

Because the simulation is built from first principles rather than fitted to data, it supports experiments that are impossible in live subjects: ablating a reflex, removing measurement noise, or changing signal quantization and watching what happens to the biomarker. Early results include the finding that naive beat detectors inject large fractions of spurious beats, and that deceleration area survives 4 Hz CTG sampling while RMSSD requires fetal-ECG acquisition quality.

- Website: [fetaltwin.org](https://fetaltwin.org/)
- Code: [github.com/martinfrasch/fetaltwin](https://github.com/martinfrasch/fetaltwin) (PolyForm Noncommercial License 1.0.0)
- Archive: [doi: 10.5281/zenodo.21158927](https://doi.org/10.5281/zenodo.21158927)

## Key Publication

**Wang Q, Gold N, Frasch MG, Huang H, Thiriet M, Wang S.** "Mathematical modeling of cardiovascular and metabolic responses to umbilical cord occlusions in fetal sheep." *Bulletin of Mathematical Biology.* 2015 Dec;77(12):2264-93. [doi: 10.1007/s11538-015-0122-4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5359013/)

## Call for Collaboration

Much remains to be done. Extending the model to new physiological compartments and pathologies, validating simulated biomarkers against real cohorts, and building interfaces that make the testbed usable by clinicians and trainees are all open work. We welcome collaborations with physiologists, clinicians, applied mathematicians, and data and computer scientists who want to push this forward. [Get in touch.](/about/ask/)
