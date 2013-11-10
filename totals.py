# -*- coding: utf-8 -*-
#!/usr/bin/env python

""" Calculate data totals """

import json

DATA_FILE = open('original_data/data_mozfest.json')

INITIAL_DATA = json.load(DATA_FILE)

def count_different_users():
    """ Count total users """
    pass

def count_total_tweets():
    """ Count total tweets """
    pass

def count_total_retweets():
    """ Count total retweets """
    pass

def awesome_count():
    """ Count number os "awesome" """
    pass

def count_geo_tweets():
    """ Count total geolocalized tweets """
    pass

def count_extra_hashtags():
    """ Count extra hashtags besides #mozfest_totals """
    pass

def count_users_mentioned():
    """ Count total mentioned users """
    pass

FINAL_DATA = {}

EXPORT_FILE = open('processed_data/mozfest_totals.json', 'w')

json.dump(FINAL_DATA, EXPORT_FILE, indent=4, separators=(',', ': '))

EXPORT_FILE.close()
