# RPython Raylib Example

RPython is a subset of Python2 that is compilable to C. Created specifically to implement [PyPy](https://pypy.org/). To learn more about it read https://rpython.readthedocs.io/en/latest/

Here is a simple demo on how to write Native Raylib App in RPython.

## Quick Start

Download and unpack the dependencies. Over time the version in the links may get outdates. Update them accordingly: https://pypy.org/download.html

```console
$ wget https://github.com/raysan5/raylib/releases/download/5.0/raylib-5.0_linux_amd64.tar.gz
$ tar fvx raylib-5.0_linux_amd64.tar.gz
$ wget https://downloads.python.org/pypy/pypy2.7-v7.3.17-linux64.tar.bz2
$ tar fvx pypy2.7-v7.3.17-linux64.tar.bz2
$ wget https://downloads.python.org/pypy/pypy3.10-v7.3.17-src.tar.bz2
$ tar fvx pypy3.10-v7.3.17-src.tar.bz2
```

Build and run the example:

```console
$ ./pypy2.7-v7.3.17-linux64/bin/pypy ./pypy3.10-v7.3.17-src/rpython main.py
$ ./urmom
```
