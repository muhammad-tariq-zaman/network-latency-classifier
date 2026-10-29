# network-latency-classifier

Classify ping latency samples into excellent/good/fair/poor bands with average, min and max.

## How to run

```sh
python3 main.py samples.txt
```

## Example output

```
n=4 avg=192.5ms min=20 max=500
excellent: 1
good: 1
fair: 1
poor: 1
```

Standard library only. Run the tests with `python3 -m unittest discover`.
