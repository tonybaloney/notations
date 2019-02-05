# Notations

Statically estimate "Big-O" notations for a given Python function.

**this is an early prototype**

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
- test comprehensions

## FAQ

* **Why not use the AST?** The AST cannot be built at runtime (easily) from a code object, this library is intended to be used to evaluate the execution-order of a compiled function. 
* **How could you possibly calculate the order without running the code?** This function equates the order by looking at the level of loop-nesting in a function, the use of comprehensions and the relationships between arguments. Dynamic runtime benchmarks are susceptible to environmental conditions (noisy neighbours) and there are already plenty of tools out there that do this

## Research notes

* [Paper on asymptotic heirarchy](https://www.d.umn.edu/~ddunham/cs3512s10/notes/l12.pdf)
