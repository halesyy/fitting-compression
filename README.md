# Fitting Compression

Fitting compression is yet to be named compression ideology. It's attempting to merge two fields: curve fitting, and compression.

## Background

I've held this idea in the back of my head for 2-3 years, after realizing that something as simple as the linear curve `y=x` compresses infinite amounts of data, given iterative compute. This is a clear "best case", but the idea struck me as interesting to say the least.

## The Idea

If we can find a curve which fits a given dataset, then we can compress that dataset by storing the curve.

## The Problem

- Fitting of curves.
- Time-to-compress.
- Standardization.
- Brute forcey.

## Solution Ideas

- Standardization: use the alphabet only (to begin), and map them to numbers.
- Standardization: use a dictionary of words, and map them to numbers or differentials.
- Standardization: convert all data to bytes. Potentially use binary as the curve.

- Fitting: use a genetic algorithm to find the best curve.
- Fitting: use a neural network to find the best curve.
- Fitting: use a linear regression model to find the best curve.
- Fitting: brute-force an equation which fits closest to the data.

## Repo Solutions

To cut to the chase, this repo is attempting to do something different.

The idea came to use bytes, and forward-and-back noise injectors to try to shuffle the data in ways that represent randomness. We can then use the shuffles as the data, and look for data which is predictable.

I'll explain this if it ends up working (not great at getting the ideas out in words).

I'll be working from `/attempts/byte-fb-noise` (byte forard-back noise) for now.
