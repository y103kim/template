import platform
from setuptools import setup, Extension

extArgs = {}
extArgs["name"] = "native"
extArgs["sources"] = []
extArgs["sources"].append("native.cpp")
if platform.system() == "Linux":
    extArgs["extra_compile_args"] = ["-std=c++2a", "-Wno-write-strings"]
    extArgs["extra_link_args"] = ["-static-libstdc++"]
    extArgs["define_macros"] = [("_GLIBCXX_USE_CXX11_ABI", 0)]
else:
    extArgs["extra_compile_args"] = ["/std:c++latest"]

native = Extension(**extArgs)

setup(
    name="native",
    version="1.0.0",
    python_requires=">=3.6",
    ext_modules=[native],
)
