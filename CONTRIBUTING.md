# Contributing

This guide is meant for contributors to the workshop materials. If you are a participant, you can ignore this section.

## Development environment

The development environment is similar to the installation instructions for the workshop.

Additionally, you will need to install the development dependencies (see in `.github/workflows/ci.yml` for the newest dependencies).
These are `pytest` and more to run the tutorial notebooks for testing and `pre-commit` to run some cleanup before committing.

```bash
    uv pip install pytest pytest-xdist nbval pre-commit
```

### Pre-commit

To install the pre-commit hooks, run:

```bash
    pre-commit install
```

This will run a few tests and notebook cleanups before you commit. You can also manually run the checks with:

```bash
    pre-commit run -a  # -a means run on all files, not just the ones you are committing. Not needed switch
```


## Testing

To run the tests, you can use the following command:

```bash
    pytest --nbval-lax --dist loadscope -n auto --ignore=session1
```

where `--nbval-lax` will run the notebooks and check for errors, `--dist loadscope -n auto` will run the tests in parallel, and `--ignore=session1` will ignore the first session tests (as an example).

### Errors in the notebooks

If a notebook is *supposed* to have an exception, you can add a tag `raises-exception` to the cell that raises the exception. This will tell `nbval` to ignore that exception and treat the raise as a success.