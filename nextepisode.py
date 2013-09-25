#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2013 Piotr 'inf' Dobrowolski

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
"""

import tvdb_api
import time
import sys

if len(sys.argv) < 2:
    print 'usage: nextepisode.py [series name] [series name] [series name]'
    exit(1)

now = time.strftime(r"%Y-%m-%d")
def do_magic(series_name):
    series = api[series_name]
    series_name = series['seriesname']
    nextep = None

    for season in series:
        for episode in series[season]:
            if series[season][episode]['firstaired'] >= now \
                and (nextep == None or nextep['firstaired'] > series[season][episode]['firstaired']):
                nextep = series[season][episode]
    if nextep:
        print u'Next episode of %s (%02dx%02d %s) is scheduled on %s' % (series_name,
                int(nextep['seasonnumber']), int(nextep['episodenumber']),
                nextep['episodename'], nextep['firstaired'])
    else:
        print u'No next episode of %s scheduled.' % series_name

api = tvdb_api.Tvdb()
for series_name in sys.argv[1:]:
    try:
        do_magic(series_name)
    except:
        print u'[!] Fetching failed for %s: %s' % (series_name, sys.exc_info()[1])
