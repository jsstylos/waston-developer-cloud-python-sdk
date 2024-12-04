# coding: utf-8
from unittest import TestCase
import os
import ibm_watson
import pytest
import json
import time
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class TestNaturalLanguageUnderstandingV1(TestCase):

    def setUp(self):
        
        with open('./auth.json') as f:
            data = json.load(f)
            nlu_auth = data.get("nlu")

            self.authenticator = IAMAuthenticator(nlu_auth.get("apikey"))
            self.natural_language_understanding = ibm_watson.NaturalLanguageUnderstandingV1(version='2018-03-16', authenticator=self.authenticator)
            self.natural_language_understanding.set_default_headers({
                'X-Watson-Learning-Opt-Out': '1',
                'X-Watson-Test': '1'
            })

    def test_analyze(self):
        response = self.natural_language_understanding.analyze(
            text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
            'Superman fears not Banner, but Wayne.',
            features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions())).get_result()
        assert response is not None
