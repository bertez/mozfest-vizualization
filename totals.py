# -*- coding: utf-8 -*-
#!/usr/bin/env python

""" Calculate data totals """

import json

class MozfestDataProcessor(object):
    """Calculate mozfest tweets data totals"""
    def __init__(self, data_file, export_file):
        super(MozfestDataProcessor, self).__init__()

        self.data_file = open(data_file)
        self.export_file = open(export_file, 'w')

        self.initial_data = json.load(self.data_file)
        self.final_data = {}

    def count_different_users(self):
        """ Count total users """
        pass

    def count_total_tweets(self):
        """ Count total tweets """
        pass

    def count_total_retweets(self):
        """ Count total retweets """
        pass

    def awesome_count(self):
        """ Count number os "awesome" """
        pass

    def count_geo_tweets(self):
        """ Count total geolocalized tweets """
        pass

    def count_extra_hashtags(self):
        """ Count extra hashtags besides #mozfest_totals """
        pass

    def count_users_mentioned(self):
        """ Count total mentioned users """
        pass

    def process(self):
        """ Do the process """
        json.dump(self.final_data, self.export_file,
                  indent=4, separators=(',', ': '))
        self.export_file.close()

def main():
    """ Start process """
    data_processor = MozfestDataProcessor('original_data/data_mozfest.json',
        'processed_data/mozfest_totals.json')
    data_processor.process()

if __name__ == '__main__':
    main()
