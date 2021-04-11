# -*- coding: utf-8 -*-
import sys
import os
from setuptools import setup, Extension, find_packages
from pyquicksetup import read_version, read_readme, default_cmdclass

#########
# settings
#########

project_var_name = "wrapclib"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = project_var_name + ', Xavier Dupré'
DESCRIPTION = """Python Wrapper for some C libraries."""
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]


#######
# data
#######

# re2
sources_re2 = [
    'gitsrc/re2/bitstate.cc',
    'gitsrc/re2/compile.cc',
    'gitsrc/re2/dfa.cc',
    'gitsrc/re2/filtered_re2.cc',
    'gitsrc/re2/mimics_pcre.cc',
    'gitsrc/re2/nfa.cc',
    'gitsrc/re2/onepass.cc',
    'gitsrc/re2/parse.cc',
    'gitsrc/re2/perl_groups.cc',
    'gitsrc/re2/prefilter.cc',
    'gitsrc/re2/prefilter_tree.cc',
    'gitsrc/re2/prog.cc',
    'gitsrc/re2/re2.cc',
    'gitsrc/re2/regexp.cc',
    'gitsrc/re2/set.cc',
    'gitsrc/re2/simplify.cc',
    'gitsrc/re2/stringpiece.cc',
    'gitsrc/re2/tostring.cc',
    'gitsrc/re2/unicode_casefold.cc',
    'gitsrc/re2/unicode_groups.cc',
    'gitsrc/util/rune.cc',
    'gitsrc/util/strutil.cc',
    '_re2.cc',
]

header_re2 = [
    'gitsrc/re2/*.h',
    'gitsrc/util/*.h',
]


packages = find_packages(".")
package_dir = {k: k.replace(".", "/") for k in packages}
package_data = {
    project_var_name + ".js": ["*.js", "*.css"],
    project_var_name + ".re2": sources_re2 + header_re2,
}

if sys.platform.startswith("win"):
    libraries_re2 = ['kernel32', '-std=c++11']
    extra_compile_args_re2 = [
        '/wd4100', '/wd4201', '/wd4456', '/wd4457', '/wd4702', '/wd4815',
        '/utf-8', '/D', 'NOMINMAX']
elif sys.platform.startswith("darwin"):
    libraries_re2 = None
    extra_compile_args_re2 = ['-lpthread', '-stdlib=libc++', '-std=c++11',
                              '-mmacosx-version-min=10.7']
else:
    libraries_re2 = None
    extra_compile_args_re2 = ['-lpthread', '-std=c++11']

root = os.path.abspath(os.path.dirname(__file__))
ext_re2 = Extension('wrapclib.re2._re2',
                    [os.path.join(root, 'wrapclib/re2', name)
                     for name in sources_re2],
                    extra_compile_args=extra_compile_args_re2,
                    include_dirs=[os.path.join(
                        root, 'wrapclib/re2/gitsrc')],
                    libraries=libraries_re2)

setup(
    name=project_var_name,
    ext_modules=[ext_re2],
    version=read_version(__file__, project_var_name),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/wrapclib/helpsphinx/index.html",
    download_url="https://github.com/sdpython/wrapclib/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=default_cmdclass(),
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=["pyquickhelper", "pybind11", 'pyquicksetup>=0.2'],
    install_requires=["pybind11"],
)
