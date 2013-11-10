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

    @classmethod
    def count_different_users(cls):
        """ Count total users """
        return 20

    @classmethod
    def count_total_tweets(cls):
        """ Count total tweets """
        pass

    @classmethod
    def count_total_retweets(cls):
        """ Count total retweets """
        pass
    @classmethod
    def awesome_count(cls):
        """ Count number os "awesome" """
        pass

    @classmethod
    def count_geo_tweets(cls):
        """ Count total geolocalized tweets """
        pass

    @classmethod
    def count_extra_hashtags(cls):
        """ Count extra hashtags besides #mozfest_totals """
        pass

    @classmethod
    def count_users_mentioned(cls):
        """ Count total mentioned users """
        pass

    def process(self):
        """ Do the process """
        self.final_data['different_users'] = self.count_different_users()

    def save_result(self):
        """ Save result to export file """
        json.dump(self.final_data, self.export_file,
                  indent=4, separators=(',', ': '))
        self.export_file.close()

def main():
    """ Start process """
    data_processor = MozfestDataProcessor('original_data/data_mozfest.json',
        'processed_data/mozfest_totals.json')
    data_processor.process()
    data_processor.save_result()

if __name__ == '__main__':
    main()
