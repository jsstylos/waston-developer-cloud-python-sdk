# Copyright 2015 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The v3 Visual Recognition service
(http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/visual-recognition/)
"""
import json
import mimetypes
from .watson_developer_cloud_service import WatsonDeveloperCloudService


class VisualRecognitionV3(WatsonDeveloperCloudService):

    """Client for the Visual Recognition service"""

    default_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api'
    latest_version = '2016-05-20'

    def __init__(self, version, url=default_url, use_vcap_services=True, api_key=None):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        :param version: specifies the specific version-date of the service to use
        """

        WatsonDeveloperCloudService.__init__(
            self, 'visual_recognition', url, None, None, use_vcap_services, api_key)
        self.version = version

    def get_classifier(self, classifier_id):
        """
        Retrieves information about a specific classifier.
        :param classifier_id: The classifier id
        """

        params = {'version': self.version}
        return self.request(method='GET', url='/v3/classifiers/{0}'.format(classifier_id), params=params,
                            accept_json=True)

    def delete_classifier(self, classifier_id):
        """
        Deletes a custom classifier with the specified classifier id.
        :param classifier_id: The classifier id
        """

        params = {'version': self.version}
        return self.request(method='DELETE', url='/v3/classifiers/{0}'.format(classifier_id), params=params,
                            accept_json=True)

    def list_classifiers(self, verbose=False):
        """
        Returns a list of user-created and built-in classifiers. (May change in the future to only user-created.)
        :param verbose: Specifies whether to return more information about each classifier, such as the author
        """

        params = {'verbose': verbose, 'version': self.version}
        return self.request(method='GET', url='/v3/classifiers', params=params, accept_json=True)

    def create_classifier(self, name, **kwargs):
        """
        Train a new classifier from example images which are uploaded.
        :param name: The desired short name of the new classifier.
        :param <NAME>_positive_examples: Up to 5 zip files of images that depict the subject of the new classifier.
        :param negative_examples: A zip file of images that do not depict the subject of the new classifier.
        :return:
        """

        params = {'version': self.version}
        data = {'name': name}
        # Params sent as url parameters here
        return self.request(method='POST', url='/v3/classifiers', files=kwargs,
                            data=data, params=params, accept_json=True)

    def classify(self, images_file=None, images_url=None, classifier_ids=None):
        """
        Returns a list of classification scores for one or more input images.
        :param images_file: An image file or zip file of image files to analyze.
        :param classifier_ids: The ids of classifiers to consider. When absent, considers all classifiers.
        :return:
        """

        if isinstance(classifier_ids, list):
            classifier_ids = json.dumps(classifier_ids)
        if classifier_ids:
            classifier_ids = '{"classifier_ids": ' + classifier_ids + '}'

        if images_file is None and images_url is None:
            raise AssertionError('You must specify either a file or a url')

        params = {'version': self.version}
        data = {'classifier_ids': classifier_ids}
        # Params sent as url parameters here
        if images_url:
            params['url'] = images_url
            return self.request(method='POST', url='/v3/classify', data=data, params=params, accept_json=True)
        else:
            guessed_mime_type = self.guess_mime_type(images_file)
            file_hash = {'images_file': (images_file.name, images_file, guessed_mime_type[0])}
            return self.request(method='POST', url='/v3/classify', files=file_hash, data=data, params=params, accept_json=True)

    def guess_mime_type(self, images_file):
        guessed_mime_type = mimetypes.guess_type(images_file.name)
        if guessed_mime_type[0] not in ['image/gif', 'image/jpeg', 'image/png']:
            raise AssertionError('You must specify a jpeg, png, or gif image')
        return guessed_mime_type

    def detect_faces(self, images_file=None, images_url=None):
        """
        Returns a list of faces detected.  This includes identities for famous people.
        :param images_file: An image file or zip file of image files to analyze.
        :return:
        """

        params = {'version': self.version}
        # Params sent as url parameters here
        if images_url:
            params['url'] = images_url
            return self.request(method='POST', url='/v3/detect_faces', params=params, accept_json=True)
        else:
            guessed_mime_type = self.guess_mime_type(images_file)
            file_hash = {'images_file': (images_file.name, images_file, guessed_mime_type[0])}
            return self.request(method='POST', url='/v3/detect_faces', files=file_hash,
                                params=params, accept_json=True)

    def recognize_text(self, images_file=None, images_url=None):
        """
        Returns a list of recognized text
        :param images_file: An image file or zip file of image files to analyze.
        :return:
        """

        params = {'version': self.version}
        # Params sent as url parameters here
        if images_url:
            params['url'] = images_url
            return self.request(method='POST', url='/v3/recognize_text', params=params, accept_json=True)
        else:
            guessed_mime_type = self.guess_mime_type(images_file)
            file_hash = {'images_file': (images_file.name, images_file, guessed_mime_type[0])}
            return self.request(method='POST', url='/v3/recognize_text',
                                files=file_hash, params=params, accept_json=True)
