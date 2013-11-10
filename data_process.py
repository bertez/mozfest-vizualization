# -*- coding: utf-8 -*-
#!/usr/bin/env python

""" This module process a bunch of twitter data scraped during the 2013
mozilla festival and calculate some totals """

import json
import re

class MozfestDataProcessor(object):
    """This class processes twitter data"""

    def __init__(self, data_file, export_file):
        #super(MozfestDataProcessor, self).__init__()

        self.data_file = open(data_file)
        self.export_file = open(export_file, 'w')

        self.initial_data = json.load(self.data_file)
        self.totals_data = {}

        self.cleaned_text_data = [x['text'].lower() for x in self.initial_data]

    def count_different_users(self):
        """ Count total users """

        users_list = [data['screen_name'] for data in self.initial_data]
        return len(set(users_list))

    def count_total_tweets(self):
        """ Count total tweets """

        return len(self.initial_data)

    def count_total_retweets(self):
        """ Count total retweets """

        return len([data for data in self.initial_data \
            if not data['is_retweet']])

    def awesome_count(self):
        """ Count number os "awesome" """

        awesome_counter = 0
        for text in self.cleaned_text_data:
            awesome_counter += text.count('awesome')

        return awesome_counter

    def count_geo_tweets(self):
        """ Count total geolocalized tweets """

        return len([x for x in self.initial_data if x['location'] is not None])

    def count_total_hashtags(self):
        """ Count total number of hashtags """
        hashtags = []
        for text in self.cleaned_text_data:
            tweet_hashtags = re.findall(r'#\w+', text)
            hashtags.extend(tweet_hashtags)

        return len(set(hashtags))

    def count_users_mentioned(self):
        """ Count total mentioned users """
        users = []
        for text in self.cleaned_text_data:
            tweet_users = re.findall(r'@\w+', text)
            users.extend(tweet_users)

        return len(set(users))

    def process_totals(self):
        """ Do the process """
        self.totals_data['different_users'] = self.count_different_users()
        self.totals_data['total_tweets'] = self.count_total_tweets()
        self.totals_data['total_retweets'] = self.count_total_retweets()
        self.totals_data['awesome_count'] = self.awesome_count()
        self.totals_data['geo_tweets'] = self.count_geo_tweets()
        self.totals_data['total_hashtags'] = self.count_total_hashtags()
        self.totals_data['users_mentioned'] = self.count_users_mentioned()

    def save_result(self):
        """ Save result to export file """
        json.dump(self.totals_data, self.export_file, indent=4,
                  separators=(',', ': '))
        self.export_file.close()

def main():
    """ Start process """
    data_processor = MozfestDataProcessor('original_data/data_mozfest.json',
        'processed_data/mozfest_totals.json')
    data_processor.process_totals()
    print data_processor.totals_data
    data_processor.save_result()

if __name__ == '__main__':
    main()
