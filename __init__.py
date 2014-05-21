#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright notice
# ----------------
#
# Copyright (C) 2013 Daniel Jung
# Contact: d.jung@jacobs-university.de
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
#
"""Implement a function "columnize" that formats a list of strings in a
compact set of columns of variable width, comparable to what the "ls" command
of many unix shells does.

The code is based on cmd.Cmd.columnize from the Python(R) standard library.
It is modified and redistributed conforming to the Python Software Foundation
License (PSF license).

"Python" is a registered trademark of the Python Software Foundation."""


def columnize(slist, displaywidth=80):
    """Format a list of strings in a compact set of columns of variable
    width.

    Based on cmd.Cmd.columnize from the Python(R) standard library."""
    # 2013-07-12 - 2013-07-12
    if not slist:
        return ''
    out = ''
    size = len(slist)
    if size == 1:
        return '%s' % str(slist[0])

    # try every row count from 1 upwards
    for nrows in range(1, len(slist)):
        ncols = (size+nrows-1) // nrows
        colwidths = []
        totwidth = -2
        for col in range(ncols):
            colwidth = 0
            for row in range(nrows):
                i = row+nrows*col
                if i >= size:
                    break
                x = slist[i]
                colwidth = max(colwidth, len(x))
            colwidths.append(colwidth)
            totwidth += colwidth+2
            if totwidth > displaywidth:
                break
        if totwidth <= displaywidth:
            break
    else:
        nrows = len(slist)
        ncols = 1
        colwidths = [0]
    for row in range(nrows):
        texts = []
        for col in range(ncols):
            i = row+nrows*col
            x = '' if i >= size else slist[i]
            texts.append(x)
        while texts and not texts[-1]:
            del texts[-1]
        for col in range(len(texts)):
            texts[col] = texts[col].ljust(colwidths[col])
        out += '%s\n' % str('  '.join(texts))
    #if out[-1] == '\n': out = out[:-1]
    return out.strip()
