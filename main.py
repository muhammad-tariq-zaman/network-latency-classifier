"""Classify ping samples (ms, one per line) into bands and summarise them.

Usage: python3 main.py samples.txt
Bands: <50 excellent, <150 good, <300 fair, otherwise poor.
"""
import argparse
import statistics
import sys


def band(ms):
    if ms < 50:
        return "excellent"
    if ms < 150:
        return "good"
    if ms < 300:
        return "fair"
    return "poor"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="File with one latency value (ms) per line")
    args = parser.parse_args(argv)
    with open(args.path, encoding="utf-8") as f:
        samples = [float(l) for l in f if l.strip()]
    counts = {b: 0 for b in ("excellent", "good", "fair", "poor")}
    for s in samples:
        counts[band(s)] += 1
    print(f"n={len(samples)} avg={statistics.mean(samples):.1f}ms min={min(samples):.0f} max={max(samples):.0f}")
    for b, c in counts.items():
        print(f"{b}: {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
