from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "Jared_auto_createfb",  # ← Ito na ang pangalan ng .so file: Jared_auto_createfb.so
        sources=["Jared_auto_create.pyx"],
        language="c",
        extra_compile_args=["-O0", "-g", "-Wno-unreachable-code", "-Wno-sign-compare"],
        extra_link_args=["-lpython3.13"]
    )
]

setup(
    name="MySharedLibrary",
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"})
)

