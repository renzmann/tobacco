# Tobacco: Your shiny new pipe `>>`!

Do you miss the `%>%` from R/dplyr? What about the `|>` from Julia? Now
you can use a `tobacco.pipe` to chain together function calls! The `@pipe`
decorator will take a function and repurpose the builtin right-bitshift
operator `>>` to be a function pipe. I've hardly ever seen anyone using 
`>>`, so it doesn't seem likely many people will miss the default behavior.

A pipeline takes the value of a function call on the left-hand side, and
passes it in as the first argument to the function on the right-hand side:

```python
0 >> f >> g  # evaluates to g(f(0))
```

You can even specify keyword closures within the pipeline

```python
# Evaluates to g(f(0, some_keyword=5), another="foo")
0 >> f(some_keyword=5) >> g(another="foo")
```


## Usage

```python
from tobacco import pipe


@pipe  # `pipe` overrides the builtin right-bitshift operator `>>`
def plus_one(a: int) -> int:
    return a + 1


@pipe
def minus_amount(b: int, amount: int = 2) -> int:
    return b - amount


@pipe
def plus_five(c: int) -> int:
    return c + 5


# 0 + 1 - 4 + 5 = 2
res = 0 >> plus_one >> minus_amount(amount=4) >> plus_five
print(res)  # 2
```

For very long data pipelines, this can clean up the readability a lot:

```python
result = (
    load_data
    >> clean_data
    >> add_columns
    >> do_analysis
    >> upload_to_database
)
```

In this short example, `result` is the output of `upload_to_database` after
all the prior steps completed.


## Installation

We're not on PyPi yet; there's a hundred versions of something similar on there
already. This is a bare-minimum version of function pipelines. Just clone
the repository and pip-install it locally.

```shell
git clone https://github.com/renzmann/tobacco
pip install ./tobacco
```
