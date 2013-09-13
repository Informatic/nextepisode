# -*- coding: utf-8 -*-

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
        print u'Next episode of %s (%s) is scheduled on %s' % (series_name,
                nextep['episodename'], nextep['firstaired'])
    else:
        print u'No next episode of %s scheduled.' % series_name

api = tvdb_api.Tvdb()
for series_name in sys.argv[1:]:
    try:
        do_magic(series_name)
    except:
        print u'[!] Fetching failed for %s: %s' % (series_name, sys.exc_info()[1])
