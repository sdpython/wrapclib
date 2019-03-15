"""
Copyright (c) 2010, David Reiss and Facebook, Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name of Facebook nor the names of its contributors
  may be used to endorse or promote products derived from this software
  without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import sre_constants
import _re2

__all__ = [
    "error",
    "escape",
    "compile",
    "search",
    "match",
    "fullmatch",
    "Set",
    "UNANCHORED",
    "ANCHOR_START",
    "ANCHOR_BOTH",
]

# Module-private compilation function, for future caching, other enhancements
_compile = _re2._compile  # pylint: disable=E1101

error = sre_constants.error  # pylint: disable=E1101
escape = _re2.escape  # pylint: disable=E1101
Set = _re2.Set  # pylint: disable=E1101
UNANCHORED = _re2.UNANCHORED  # pylint: disable=E1101
ANCHOR_START = _re2.ANCHOR_START  # pylint: disable=E1101
ANCHOR_BOTH = _re2.ANCHOR_BOTH  # pylint: disable=E1101


def compile(pattern):  # pylint: disable=W0622
    "Compiles a regular expression pattern, returning a pattern object."
    return _compile(pattern, error)


def search(pattern, string, pos=0, endpos=-1):
    """Scans through string looking for a match to the pattern, returning
    a match object, or None if no match was found."""
    if endpos != -1:
        return _compile(pattern, error).search(string, pos, endpos)
    else:
        return _compile(pattern, error).search(string, pos)


def match(pattern, string):
    """Tries to apply the pattern at the start of the string, returning
    a match object, or None if no match was found."""
    return _compile(pattern, error).match(string)


def fullmatch(pattern, string):
    """Tries to apply the pattern to the entire string, returning
    a match object, or None if no match was found."""
    return _compile(pattern, error).fullmatch(string)


def findall(pattern, string, pos=0, endpos=-1):
    """
    Implements method :epkg:`*py:re:findall`
    for *re2* in :epkg:`Python`.

    @param      pattern     compiled regular expression
    @param      string      string to search
    @param      pos         first position to look into
    @param      endpos      last position to look into (-1 for the last one)
    @return                 list of results
    """
    if isinstance(pattern, str):
        pattern = _compile(pattern, error)
    results = []
    if endpos == -1:
        def fsearch(s, p):
            return pattern.search(s, p)
    else:
        def fsearch(s, p):
            return pattern.search(s, p, endpos)
    res = fsearch(string, pos)
    while res:
        results.append(res.groups())
        pos = res.span()[1]
        res = fsearch(string, pos)
    return results
