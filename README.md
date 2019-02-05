# Notations

Statically estimate "Big-O" notations for a given Python function.

## Example

```python
from notations import notation

def my_example_function(arg1, arg2):
    f = 0
    for a in arg1:
        for i in a:
            f+=1
    for b in arg2:
        for j in b:
            f+=1

print(notation(my_example_function))
```

Will print `O(n^2)`

## TODO

This is a rough sketch of a concept at this stage.

- `while` operators
- Look at the relationship between input arguments in a function, just because a loop is nested, doesn't mean the `O(n_n)` is correct
- branches inside loops
