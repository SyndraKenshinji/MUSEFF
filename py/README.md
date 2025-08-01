A more complex python project would require you to separate different modules in different files.

First of all, python is normally very bad at modularizing and separating dependencies for different
projects. For that reason, you should (almost) always use tools differentiate "environments"
for different projects.

The way python works, you need to install a module for it to be "importable".

For that reason, you need to run `pip install -e .` in the root of the python project.

For this command to recognize correctly which directories are modules,
and how exactly to install them, you need either a `setup.py` or a `project.toml`
that specify those things.
(Similar to how a C  project might use a specific Makefile when building for production)

You need a __init__.py in the root of the directory to specify it as the root of a module.

Since `setup.py` and `project.toml` specify how your package should be built for production,
it should contain runtime dependencies (e.g. numpy). Development dependencies should be on
a separate `requirements.txt`.

```
py/
├── mypackage/
│   ├── __init__.py
│   └── some_module.py
├── tests/
│   └── test_some_module.py
├── setup.py
└── requirements.txt
```

If you are a developer you should not only run `pip install -e .` to make your package(s) runnable,
but you should also install all development requirements with `pip install -r requirements.txt`

Some common dependencies are:
- For testing: pytest, unittest
