# RLE

Simple Python module for run-length encoding iteratables.

```python
from rle import *
orig = [1,1,1,1,2,3,4,4,3,3,3]
rle = [(1, 4), (2, 1), (3, 1), (4, 2), (3, 3)]
assert list(rle_encode(orig)) == rle
assert list(rle_decode(rle)) == orig
```

No Copyright, Public Domain
