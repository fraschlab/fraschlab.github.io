---
layout: default
title: "When Does the Model Pay? Postpartum Readmission Economics"
---

# When Does the Model Pay?

An interactive explorer of the decision economics of predicting readmission in the first 14 days after a first birth.

**[Open the explorer →](https://martinfrasch.github.io/postpartum-readmission-economics/)**

## The question

A risk model saves money only if it beats the two strategies that need no model: contact every new mother after discharge, or contact none. Whether it does depends on what one outreach contact costs, how many readmissions a contact prevents, what a readmission costs, and how well the model ranks risk. The explorer lets you set each of these and see where, if anywhere, a model earns its place.

## What you can explore

- **Cost of a contact.** Move it from a few dollars to hundreds, and see when contacting everyone, no one, or only the women the model flags is the better choice.
- **The models.** Logistic regression, gradient boosting, a stacking ensemble and two automated machine learning frameworks, trained on nuMoM2b and scored on an untouched test set. You can also compare them with a hypothetical better model.
- **States.** The test set reweighted to each US state's first births, with each state's Medicaid payment for a home visit or a phone call. This view is post hoc and exploratory.
- **How it was built.** The explorer explains, step by step, how the state estimates were made, including how the nuMoM2b insurance variable links the study to state birth and Medicaid data.

## Data and privacy

The explorer contains no participant-level data. Predictions are grouped so that every group holds at least 11 readmissions and 11 non-readmissions, and states are described only by state-level summaries, as required by the NICHD data use agreement for nuMoM2b.

## Links

- [Interactive explorer](https://martinfrasch.github.io/postpartum-readmission-economics/)
- [Archived on Zenodo (doi:10.5281/zenodo.23749950)](https://doi.org/10.5281/zenodo.23749950)
- [Preprint on medRxiv (doi:10.1101/2025.12.16.25342440)](https://doi.org/10.1101/2025.12.16.25342440)
- [Analysis code on GitHub](https://github.com/martinfrasch/numom2b-postpartum-risk-prediction-health-economics)
