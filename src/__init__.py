"""Hype Radar: detect emerging trends from social post streams.

Modules:
  stream     synthetic social post stream with injected hype events
  sentiment  fast lexicon-based sentiment scorer
  burst      sliding-window burst detector over per-minute volume
  topics     TF-IDF + MiniBatchKMeans topic discovery
  hype       hype scoring and alert engine
  evaluate   detection quality vs injected events (precision/recall, delay)
"""
