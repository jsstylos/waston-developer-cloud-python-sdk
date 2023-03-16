# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2019, 2023.
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
Unit Tests for DiscoveryV2
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_watson.discovery_v2 import *

version = 'testString'

_service = DiscoveryV2(
    authenticator=NoAuthAuthenticator(),
    version=version,
)

_base_url = 'https://api.us-south.discovery.watson.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Projects
##############################################################################
# region

class TestListProjects():
    """
    Test Class for list_projects
    """

    @responses.activate
    def test_list_projects_all_params(self):
        """
        list_projects()
        """
        # Set up mock
        url = preprocess_url('/v2/projects')
        mock_response = '{"projects": [{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_projects()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_projects_all_params_with_retries(self):
        # Enable retries and run test_list_projects_all_params.
        _service.enable_retries()
        self.test_list_projects_all_params()

        # Disable retries and run test_list_projects_all_params.
        _service.disable_retries()
        self.test_list_projects_all_params()

    @responses.activate
    def test_list_projects_value_error(self):
        """
        test_list_projects_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects')
        mock_response = '{"projects": [{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_projects(**req_copy)

    def test_list_projects_value_error_with_retries(self):
        # Enable retries and run test_list_projects_value_error.
        _service.enable_retries()
        self.test_list_projects_value_error()

        # Disable retries and run test_list_projects_value_error.
        _service.disable_retries()
        self.test_list_projects_value_error()

class TestCreateProject():
    """
    Test Class for create_project
    """

    @responses.activate
    def test_create_project_all_params(self):
        """
        create_project()
        """
        # Set up mock
        url = preprocess_url('/v2/projects')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DefaultQueryParamsPassages model
        default_query_params_passages_model = {}
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsTableResults model
        default_query_params_table_results_model = {}
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsSuggestedRefinements model
        default_query_params_suggested_refinements_model = {}
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        # Construct a dict representation of a DefaultQueryParams model
        default_query_params_model = {}
        default_query_params_model['collection_ids'] = ['testString']
        default_query_params_model['passages'] = default_query_params_passages_model
        default_query_params_model['table_results'] = default_query_params_table_results_model
        default_query_params_model['aggregation'] = 'testString'
        default_query_params_model['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model['spelling_suggestions'] = True
        default_query_params_model['highlight'] = True
        default_query_params_model['count'] = 38
        default_query_params_model['sort'] = 'testString'
        default_query_params_model['return'] = ['testString']

        # Set up parameter values
        name = 'testString'
        type = 'document_retrieval'
        default_query_parameters = default_query_params_model

        # Invoke method
        response = _service.create_project(
            name,
            type,
            default_query_parameters=default_query_parameters,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'document_retrieval'
        assert req_body['default_query_parameters'] == default_query_params_model

    def test_create_project_all_params_with_retries(self):
        # Enable retries and run test_create_project_all_params.
        _service.enable_retries()
        self.test_create_project_all_params()

        # Disable retries and run test_create_project_all_params.
        _service.disable_retries()
        self.test_create_project_all_params()

    @responses.activate
    def test_create_project_value_error(self):
        """
        test_create_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DefaultQueryParamsPassages model
        default_query_params_passages_model = {}
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsTableResults model
        default_query_params_table_results_model = {}
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        # Construct a dict representation of a DefaultQueryParamsSuggestedRefinements model
        default_query_params_suggested_refinements_model = {}
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        # Construct a dict representation of a DefaultQueryParams model
        default_query_params_model = {}
        default_query_params_model['collection_ids'] = ['testString']
        default_query_params_model['passages'] = default_query_params_passages_model
        default_query_params_model['table_results'] = default_query_params_table_results_model
        default_query_params_model['aggregation'] = 'testString'
        default_query_params_model['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model['spelling_suggestions'] = True
        default_query_params_model['highlight'] = True
        default_query_params_model['count'] = 38
        default_query_params_model['sort'] = 'testString'
        default_query_params_model['return'] = ['testString']

        # Set up parameter values
        name = 'testString'
        type = 'document_retrieval'
        default_query_parameters = default_query_params_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_project(**req_copy)

    def test_create_project_value_error_with_retries(self):
        # Enable retries and run test_create_project_value_error.
        _service.enable_retries()
        self.test_create_project_value_error()

        # Disable retries and run test_create_project_value_error.
        _service.disable_retries()
        self.test_create_project_value_error()

class TestGetProject():
    """
    Test Class for get_project
    """

    @responses.activate
    def test_get_project_all_params(self):
        """
        get_project()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.get_project(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_project_all_params_with_retries(self):
        # Enable retries and run test_get_project_all_params.
        _service.enable_retries()
        self.test_get_project_all_params()

        # Disable retries and run test_get_project_all_params.
        _service.disable_retries()
        self.test_get_project_all_params()

    @responses.activate
    def test_get_project_value_error(self):
        """
        test_get_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_project(**req_copy)

    def test_get_project_value_error_with_retries(self):
        # Enable retries and run test_get_project_value_error.
        _service.enable_retries()
        self.test_get_project_value_error()

        # Disable retries and run test_get_project_value_error.
        _service.disable_retries()
        self.test_get_project_value_error()

class TestUpdateProject():
    """
    Test Class for update_project
    """

    @responses.activate
    def test_update_project_all_params(self):
        """
        update_project()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        name = 'testString'

        # Invoke method
        response = _service.update_project(
            project_id,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'

    def test_update_project_all_params_with_retries(self):
        # Enable retries and run test_update_project_all_params.
        _service.enable_retries()
        self.test_update_project_all_params()

        # Disable retries and run test_update_project_all_params.
        _service.disable_retries()
        self.test_update_project_all_params()

    @responses.activate
    def test_update_project_required_params(self):
        """
        test_update_project_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.update_project(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_project_required_params_with_retries(self):
        # Enable retries and run test_update_project_required_params.
        _service.enable_retries()
        self.test_update_project_required_params()

        # Disable retries and run test_update_project_required_params.
        _service.disable_retries()
        self.test_update_project_required_params()

    @responses.activate
    def test_update_project_value_error(self):
        """
        test_update_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString')
        mock_response = '{"project_id": "project_id", "name": "name", "type": "document_retrieval", "relevancy_training_status": {"data_updated": "data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": ["collection_ids"], "passages": {"enabled": false, "count": 5, "fields": ["fields"], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "sort", "return": ["return_"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_project(**req_copy)

    def test_update_project_value_error_with_retries(self):
        # Enable retries and run test_update_project_value_error.
        _service.enable_retries()
        self.test_update_project_value_error()

        # Disable retries and run test_update_project_value_error.
        _service.disable_retries()
        self.test_update_project_value_error()

class TestDeleteProject():
    """
    Test Class for delete_project
    """

    @responses.activate
    def test_delete_project_all_params(self):
        """
        delete_project()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.delete_project(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_project_all_params_with_retries(self):
        # Enable retries and run test_delete_project_all_params.
        _service.enable_retries()
        self.test_delete_project_all_params()

        # Disable retries and run test_delete_project_all_params.
        _service.disable_retries()
        self.test_delete_project_all_params()

    @responses.activate
    def test_delete_project_value_error(self):
        """
        test_delete_project_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_project(**req_copy)

    def test_delete_project_value_error_with_retries(self):
        # Enable retries and run test_delete_project_value_error.
        _service.enable_retries()
        self.test_delete_project_value_error()

        # Disable retries and run test_delete_project_value_error.
        _service.disable_retries()
        self.test_delete_project_value_error()

class TestListFields():
    """
    Test Class for list_fields
    """

    @responses.activate
    def test_list_fields_all_params(self):
        """
        list_fields()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested", "collection_id": "collection_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_ids = ['testString']

        # Invoke method
        response = _service.list_fields(
            project_id,
            collection_ids=collection_ids,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'collection_ids={}'.format(','.join(collection_ids)) in query_string

    def test_list_fields_all_params_with_retries(self):
        # Enable retries and run test_list_fields_all_params.
        _service.enable_retries()
        self.test_list_fields_all_params()

        # Disable retries and run test_list_fields_all_params.
        _service.disable_retries()
        self.test_list_fields_all_params()

    @responses.activate
    def test_list_fields_required_params(self):
        """
        test_list_fields_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested", "collection_id": "collection_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_fields(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_fields_required_params_with_retries(self):
        # Enable retries and run test_list_fields_required_params.
        _service.enable_retries()
        self.test_list_fields_required_params()

        # Disable retries and run test_list_fields_required_params.
        _service.disable_retries()
        self.test_list_fields_required_params()

    @responses.activate
    def test_list_fields_value_error(self):
        """
        test_list_fields_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested", "collection_id": "collection_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_fields(**req_copy)

    def test_list_fields_value_error_with_retries(self):
        # Enable retries and run test_list_fields_value_error.
        _service.enable_retries()
        self.test_list_fields_value_error()

        # Disable retries and run test_list_fields_value_error.
        _service.disable_retries()
        self.test_list_fields_value_error()

# endregion
##############################################################################
# End of Service: Projects
##############################################################################

##############################################################################
# Start of Service: Collections
##############################################################################
# region

class TestListCollections():
    """
    Test Class for list_collections
    """

    @responses.activate
    def test_list_collections_all_params(self):
        """
        list_collections()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_collections(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_collections_all_params_with_retries(self):
        # Enable retries and run test_list_collections_all_params.
        _service.enable_retries()
        self.test_list_collections_all_params()

        # Disable retries and run test_list_collections_all_params.
        _service.disable_retries()
        self.test_list_collections_all_params()

    @responses.activate
    def test_list_collections_value_error(self):
        """
        test_list_collections_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_collections(**req_copy)

    def test_list_collections_value_error_with_retries(self):
        # Enable retries and run test_list_collections_value_error.
        _service.enable_retries()
        self.test_list_collections_value_error()

        # Disable retries and run test_list_collections_value_error.
        _service.disable_retries()
        self.test_list_collections_value_error()

class TestCreateCollection():
    """
    Test Class for create_collection
    """

    @responses.activate
    def test_create_collection_all_params(self):
        """
        create_collection()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "smart_document_understanding": {"enabled": false, "model": "custom"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        name = 'testString'
        description = 'testString'
        language = 'en'
        enrichments = [collection_enrichment_model]

        # Invoke method
        response = _service.create_collection(
            project_id,
            name,
            description=description,
            language=language,
            enrichments=enrichments,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['language'] == 'en'
        assert req_body['enrichments'] == [collection_enrichment_model]

    def test_create_collection_all_params_with_retries(self):
        # Enable retries and run test_create_collection_all_params.
        _service.enable_retries()
        self.test_create_collection_all_params()

        # Disable retries and run test_create_collection_all_params.
        _service.disable_retries()
        self.test_create_collection_all_params()

    @responses.activate
    def test_create_collection_value_error(self):
        """
        test_create_collection_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "smart_document_understanding": {"enabled": false, "model": "custom"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        name = 'testString'
        description = 'testString'
        language = 'en'
        enrichments = [collection_enrichment_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_collection(**req_copy)

    def test_create_collection_value_error_with_retries(self):
        # Enable retries and run test_create_collection_value_error.
        _service.enable_retries()
        self.test_create_collection_value_error()

        # Disable retries and run test_create_collection_value_error.
        _service.disable_retries()
        self.test_create_collection_value_error()

class TestGetCollection():
    """
    Test Class for get_collection
    """

    @responses.activate
    def test_get_collection_all_params(self):
        """
        get_collection()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "smart_document_understanding": {"enabled": false, "model": "custom"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.get_collection(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_collection_all_params_with_retries(self):
        # Enable retries and run test_get_collection_all_params.
        _service.enable_retries()
        self.test_get_collection_all_params()

        # Disable retries and run test_get_collection_all_params.
        _service.disable_retries()
        self.test_get_collection_all_params()

    @responses.activate
    def test_get_collection_value_error(self):
        """
        test_get_collection_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "smart_document_understanding": {"enabled": false, "model": "custom"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_collection(**req_copy)

    def test_get_collection_value_error_with_retries(self):
        # Enable retries and run test_get_collection_value_error.
        _service.enable_retries()
        self.test_get_collection_value_error()

        # Disable retries and run test_get_collection_value_error.
        _service.disable_retries()
        self.test_get_collection_value_error()

class TestUpdateCollection():
    """
    Test Class for update_collection
    """

    @responses.activate
    def test_update_collection_all_params(self):
        """
        update_collection()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "smart_document_understanding": {"enabled": false, "model": "custom"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        name = 'testString'
        description = 'testString'
        enrichments = [collection_enrichment_model]

        # Invoke method
        response = _service.update_collection(
            project_id,
            collection_id,
            name=name,
            description=description,
            enrichments=enrichments,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['enrichments'] == [collection_enrichment_model]

    def test_update_collection_all_params_with_retries(self):
        # Enable retries and run test_update_collection_all_params.
        _service.enable_retries()
        self.test_update_collection_all_params()

        # Disable retries and run test_update_collection_all_params.
        _service.disable_retries()
        self.test_update_collection_all_params()

    @responses.activate
    def test_update_collection_value_error(self):
        """
        test_update_collection_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "smart_document_understanding": {"enabled": false, "model": "custom"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CollectionEnrichment model
        collection_enrichment_model = {}
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        name = 'testString'
        description = 'testString'
        enrichments = [collection_enrichment_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_collection(**req_copy)

    def test_update_collection_value_error_with_retries(self):
        # Enable retries and run test_update_collection_value_error.
        _service.enable_retries()
        self.test_update_collection_value_error()

        # Disable retries and run test_update_collection_value_error.
        _service.disable_retries()
        self.test_update_collection_value_error()

class TestDeleteCollection():
    """
    Test Class for delete_collection
    """

    @responses.activate
    def test_delete_collection_all_params(self):
        """
        delete_collection()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_collection(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_collection_all_params_with_retries(self):
        # Enable retries and run test_delete_collection_all_params.
        _service.enable_retries()
        self.test_delete_collection_all_params()

        # Disable retries and run test_delete_collection_all_params.
        _service.disable_retries()
        self.test_delete_collection_all_params()

    @responses.activate
    def test_delete_collection_value_error(self):
        """
        test_delete_collection_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_collection(**req_copy)

    def test_delete_collection_value_error_with_retries(self):
        # Enable retries and run test_delete_collection_value_error.
        _service.enable_retries()
        self.test_delete_collection_value_error()

        # Disable retries and run test_delete_collection_value_error.
        _service.disable_retries()
        self.test_delete_collection_value_error()

# endregion
##############################################################################
# End of Service: Collections
##############################################################################

##############################################################################
# Start of Service: Documents
##############################################################################
# region

class TestListDocuments():
    """
    Test Class for list_documents
    """

    @responses.activate
    def test_list_documents_all_params(self):
        """
        list_documents()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents')
        mock_response = '{"matching_results": 16, "documents": [{"document_id": "document_id", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "available", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "children": {"have_notices": true, "count": 5}, "filename": "filename", "file_type": "file_type", "sha256": "sha256"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        count = 38
        status = 'testString'
        has_notices = True
        is_parent = True
        parent_document_id = 'testString'
        sha256 = 'testString'

        # Invoke method
        response = _service.list_documents(
            project_id,
            collection_id,
            count=count,
            status=status,
            has_notices=has_notices,
            is_parent=is_parent,
            parent_document_id=parent_document_id,
            sha256=sha256,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'count={}'.format(count) in query_string
        assert 'status={}'.format(status) in query_string
        assert 'has_notices={}'.format('true' if has_notices else 'false') in query_string
        assert 'is_parent={}'.format('true' if is_parent else 'false') in query_string
        assert 'parent_document_id={}'.format(parent_document_id) in query_string
        assert 'sha256={}'.format(sha256) in query_string

    def test_list_documents_all_params_with_retries(self):
        # Enable retries and run test_list_documents_all_params.
        _service.enable_retries()
        self.test_list_documents_all_params()

        # Disable retries and run test_list_documents_all_params.
        _service.disable_retries()
        self.test_list_documents_all_params()

    @responses.activate
    def test_list_documents_required_params(self):
        """
        test_list_documents_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents')
        mock_response = '{"matching_results": 16, "documents": [{"document_id": "document_id", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "available", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "children": {"have_notices": true, "count": 5}, "filename": "filename", "file_type": "file_type", "sha256": "sha256"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.list_documents(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_documents_required_params_with_retries(self):
        # Enable retries and run test_list_documents_required_params.
        _service.enable_retries()
        self.test_list_documents_required_params()

        # Disable retries and run test_list_documents_required_params.
        _service.disable_retries()
        self.test_list_documents_required_params()

    @responses.activate
    def test_list_documents_value_error(self):
        """
        test_list_documents_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents')
        mock_response = '{"matching_results": 16, "documents": [{"document_id": "document_id", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "available", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "children": {"have_notices": true, "count": 5}, "filename": "filename", "file_type": "file_type", "sha256": "sha256"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_documents(**req_copy)

    def test_list_documents_value_error_with_retries(self):
        # Enable retries and run test_list_documents_value_error.
        _service.enable_retries()
        self.test_list_documents_value_error()

        # Disable retries and run test_list_documents_value_error.
        _service.disable_retries()
        self.test_list_documents_value_error()

class TestAddDocument():
    """
    Test Class for add_document
    """

    @responses.activate
    def test_add_document_all_params(self):
        """
        add_document()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'
        x_watson_discovery_force = False

        # Invoke method
        response = _service.add_document(
            project_id,
            collection_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            x_watson_discovery_force=x_watson_discovery_force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_add_document_all_params_with_retries(self):
        # Enable retries and run test_add_document_all_params.
        _service.enable_retries()
        self.test_add_document_all_params()

        # Disable retries and run test_add_document_all_params.
        _service.disable_retries()
        self.test_add_document_all_params()

    @responses.activate
    def test_add_document_required_params(self):
        """
        test_add_document_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.add_document(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_add_document_required_params_with_retries(self):
        # Enable retries and run test_add_document_required_params.
        _service.enable_retries()
        self.test_add_document_required_params()

        # Disable retries and run test_add_document_required_params.
        _service.disable_retries()
        self.test_add_document_required_params()

    @responses.activate
    def test_add_document_value_error(self):
        """
        test_add_document_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_document(**req_copy)

    def test_add_document_value_error_with_retries(self):
        # Enable retries and run test_add_document_value_error.
        _service.enable_retries()
        self.test_add_document_value_error()

        # Disable retries and run test_add_document_value_error.
        _service.disable_retries()
        self.test_add_document_value_error()

class TestGetDocument():
    """
    Test Class for get_document
    """

    @responses.activate
    def test_get_document_all_params(self):
        """
        get_document()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "available", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "children": {"have_notices": true, "count": 5}, "filename": "filename", "file_type": "file_type", "sha256": "sha256"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.get_document(
            project_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_document_all_params_with_retries(self):
        # Enable retries and run test_get_document_all_params.
        _service.enable_retries()
        self.test_get_document_all_params()

        # Disable retries and run test_get_document_all_params.
        _service.disable_retries()
        self.test_get_document_all_params()

    @responses.activate
    def test_get_document_value_error(self):
        """
        test_get_document_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "available", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "children": {"have_notices": true, "count": 5}, "filename": "filename", "file_type": "file_type", "sha256": "sha256"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_document(**req_copy)

    def test_get_document_value_error_with_retries(self):
        # Enable retries and run test_get_document_value_error.
        _service.enable_retries()
        self.test_get_document_value_error()

        # Disable retries and run test_get_document_value_error.
        _service.disable_retries()
        self.test_get_document_value_error()

class TestUpdateDocument():
    """
    Test Class for update_document
    """

    @responses.activate
    def test_update_document_all_params(self):
        """
        update_document()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'
        x_watson_discovery_force = False

        # Invoke method
        response = _service.update_document(
            project_id,
            collection_id,
            document_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            x_watson_discovery_force=x_watson_discovery_force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_update_document_all_params_with_retries(self):
        # Enable retries and run test_update_document_all_params.
        _service.enable_retries()
        self.test_update_document_all_params()

        # Disable retries and run test_update_document_all_params.
        _service.disable_retries()
        self.test_update_document_all_params()

    @responses.activate
    def test_update_document_required_params(self):
        """
        test_update_document_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.update_document(
            project_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_update_document_required_params_with_retries(self):
        # Enable retries and run test_update_document_required_params.
        _service.enable_retries()
        self.test_update_document_required_params()

        # Disable retries and run test_update_document_required_params.
        _service.disable_retries()
        self.test_update_document_required_params()

    @responses.activate
    def test_update_document_value_error(self):
        """
        test_update_document_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_document(**req_copy)

    def test_update_document_value_error_with_retries(self):
        # Enable retries and run test_update_document_value_error.
        _service.enable_retries()
        self.test_update_document_value_error()

        # Disable retries and run test_update_document_value_error.
        _service.disable_retries()
        self.test_update_document_value_error()

class TestDeleteDocument():
    """
    Test Class for delete_document
    """

    @responses.activate
    def test_delete_document_all_params(self):
        """
        delete_document()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'
        x_watson_discovery_force = False

        # Invoke method
        response = _service.delete_document(
            project_id,
            collection_id,
            document_id,
            x_watson_discovery_force=x_watson_discovery_force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_document_all_params_with_retries(self):
        # Enable retries and run test_delete_document_all_params.
        _service.enable_retries()
        self.test_delete_document_all_params()

        # Disable retries and run test_delete_document_all_params.
        _service.disable_retries()
        self.test_delete_document_all_params()

    @responses.activate
    def test_delete_document_required_params(self):
        """
        test_delete_document_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.delete_document(
            project_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_document_required_params_with_retries(self):
        # Enable retries and run test_delete_document_required_params.
        _service.enable_retries()
        self.test_delete_document_required_params()

        # Disable retries and run test_delete_document_required_params.
        _service.disable_retries()
        self.test_delete_document_required_params()

    @responses.activate
    def test_delete_document_value_error(self):
        """
        test_delete_document_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_document(**req_copy)

    def test_delete_document_value_error_with_retries(self):
        # Enable retries and run test_delete_document_value_error.
        _service.enable_retries()
        self.test_delete_document_value_error()

        # Disable retries and run test_delete_document_value_error.
        _service.disable_retries()
        self.test_delete_document_value_error()

# endregion
##############################################################################
# End of Service: Documents
##############################################################################

##############################################################################
# Start of Service: Queries
##############################################################################
# region

class TestQuery():
    """
    Test Class for query
    """

    @responses.activate
    def test_query_all_params(self):
        """
        query()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"document_id": "document_id", "metadata": {"anyKey": "anyValue"}, "result_metadata": {"document_retrieval_source": "search", "collection_id": "collection_id", "confidence": 0}, "document_passages": [{"passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field", "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}], "aggregations": [{"type": "term", "field": "field", "count": 5, "name": "name", "results": [{"key": "key", "matching_results": 16, "relevancy": 9, "total_matching_documents": 24, "estimated_matching_results": 26, "aggregations": [{"anyKey": "anyValue"}]}]}], "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query", "suggested_refinements": [{"text": "text"}], "table_results": [{"table_id": "table_id", "source_document_id": "source_document_id", "collection_id": "collection_id", "table_html": "table_html", "table_html_offset": 17, "table": {"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"text": "text", "location": {"begin": 5, "end": 3}}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": [{"id": "id"}], "row_header_texts": [{"text": "text"}], "row_header_texts_normalized": [{"text_normalized": "text_normalized"}], "column_header_ids": [{"id": "id"}], "column_header_texts": [{"text": "text"}], "column_header_texts_normalized": [{"text_normalized": "text_normalized"}], "attributes": [{"type": "type", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}]}}], "passages": [{"passage_text": "passage_text", "passage_score": 13, "document_id": "document_id", "collection_id": "collection_id", "start_offset": 12, "end_offset": 10, "field": "field", "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a QueryLargeTableResults model
        query_large_table_results_model = {}
        query_large_table_results_model['enabled'] = True
        query_large_table_results_model['count'] = 38

        # Construct a dict representation of a QueryLargeSuggestedRefinements model
        query_large_suggested_refinements_model = {}
        query_large_suggested_refinements_model['enabled'] = True
        query_large_suggested_refinements_model['count'] = 1

        # Construct a dict representation of a QueryLargePassages model
        query_large_passages_model = {}
        query_large_passages_model['enabled'] = True
        query_large_passages_model['per_document'] = True
        query_large_passages_model['max_per_document'] = 38
        query_large_passages_model['fields'] = ['testString']
        query_large_passages_model['count'] = 400
        query_large_passages_model['characters'] = 50
        query_large_passages_model['find_answers'] = False
        query_large_passages_model['max_answers_per_passage'] = 38

        # Construct a dict representation of a QueryLargeSimilar model
        query_large_similar_model = {}
        query_large_similar_model['enabled'] = False
        query_large_similar_model['document_ids'] = ['testString']
        query_large_similar_model['fields'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        collection_ids = ['testString']
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        aggregation = 'testString'
        count = 38
        return_ = ['testString']
        offset = 38
        sort = 'testString'
        highlight = True
        spelling_suggestions = True
        table_results = query_large_table_results_model
        suggested_refinements = query_large_suggested_refinements_model
        passages = query_large_passages_model
        similar = query_large_similar_model

        # Invoke method
        response = _service.query(
            project_id,
            collection_ids=collection_ids,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            aggregation=aggregation,
            count=count,
            return_=return_,
            offset=offset,
            sort=sort,
            highlight=highlight,
            spelling_suggestions=spelling_suggestions,
            table_results=table_results,
            suggested_refinements=suggested_refinements,
            passages=passages,
            similar=similar,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['collection_ids'] == ['testString']
        assert req_body['filter'] == 'testString'
        assert req_body['query'] == 'testString'
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['aggregation'] == 'testString'
        assert req_body['count'] == 38
        assert req_body['return'] == ['testString']
        assert req_body['offset'] == 38
        assert req_body['sort'] == 'testString'
        assert req_body['highlight'] == True
        assert req_body['spelling_suggestions'] == True
        assert req_body['table_results'] == query_large_table_results_model
        assert req_body['suggested_refinements'] == query_large_suggested_refinements_model
        assert req_body['passages'] == query_large_passages_model
        assert req_body['similar'] == query_large_similar_model

    def test_query_all_params_with_retries(self):
        # Enable retries and run test_query_all_params.
        _service.enable_retries()
        self.test_query_all_params()

        # Disable retries and run test_query_all_params.
        _service.disable_retries()
        self.test_query_all_params()

    @responses.activate
    def test_query_required_params(self):
        """
        test_query_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"document_id": "document_id", "metadata": {"anyKey": "anyValue"}, "result_metadata": {"document_retrieval_source": "search", "collection_id": "collection_id", "confidence": 0}, "document_passages": [{"passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field", "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}], "aggregations": [{"type": "term", "field": "field", "count": 5, "name": "name", "results": [{"key": "key", "matching_results": 16, "relevancy": 9, "total_matching_documents": 24, "estimated_matching_results": 26, "aggregations": [{"anyKey": "anyValue"}]}]}], "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query", "suggested_refinements": [{"text": "text"}], "table_results": [{"table_id": "table_id", "source_document_id": "source_document_id", "collection_id": "collection_id", "table_html": "table_html", "table_html_offset": 17, "table": {"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"text": "text", "location": {"begin": 5, "end": 3}}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": [{"id": "id"}], "row_header_texts": [{"text": "text"}], "row_header_texts_normalized": [{"text_normalized": "text_normalized"}], "column_header_ids": [{"id": "id"}], "column_header_texts": [{"text": "text"}], "column_header_texts_normalized": [{"text_normalized": "text_normalized"}], "attributes": [{"type": "type", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}]}}], "passages": [{"passage_text": "passage_text", "passage_score": 13, "document_id": "document_id", "collection_id": "collection_id", "start_offset": 12, "end_offset": 10, "field": "field", "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.query(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_query_required_params_with_retries(self):
        # Enable retries and run test_query_required_params.
        _service.enable_retries()
        self.test_query_required_params()

        # Disable retries and run test_query_required_params.
        _service.disable_retries()
        self.test_query_required_params()

    @responses.activate
    def test_query_value_error(self):
        """
        test_query_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"document_id": "document_id", "metadata": {"anyKey": "anyValue"}, "result_metadata": {"document_retrieval_source": "search", "collection_id": "collection_id", "confidence": 0}, "document_passages": [{"passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field", "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}], "aggregations": [{"type": "term", "field": "field", "count": 5, "name": "name", "results": [{"key": "key", "matching_results": 16, "relevancy": 9, "total_matching_documents": 24, "estimated_matching_results": 26, "aggregations": [{"anyKey": "anyValue"}]}]}], "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query", "suggested_refinements": [{"text": "text"}], "table_results": [{"table_id": "table_id", "source_document_id": "source_document_id", "collection_id": "collection_id", "table_html": "table_html", "table_html_offset": 17, "table": {"location": {"begin": 5, "end": 3}, "text": "text", "section_title": {"text": "text", "location": {"begin": 5, "end": 3}}, "title": {"text": "text", "location": {"begin": 5, "end": 3}}, "table_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "row_headers": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "column_headers": [{"cell_id": "cell_id", "location": {"anyKey": "anyValue"}, "text": "text", "text_normalized": "text_normalized", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16}], "key_value_pairs": [{"key": {"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}, "value": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text"}]}], "body_cells": [{"cell_id": "cell_id", "location": {"begin": 5, "end": 3}, "text": "text", "row_index_begin": 15, "row_index_end": 13, "column_index_begin": 18, "column_index_end": 16, "row_header_ids": [{"id": "id"}], "row_header_texts": [{"text": "text"}], "row_header_texts_normalized": [{"text_normalized": "text_normalized"}], "column_header_ids": [{"id": "id"}], "column_header_texts": [{"text": "text"}], "column_header_texts_normalized": [{"text_normalized": "text_normalized"}], "attributes": [{"type": "type", "text": "text", "location": {"begin": 5, "end": 3}}]}], "contexts": [{"text": "text", "location": {"begin": 5, "end": 3}}]}}], "passages": [{"passage_text": "passage_text", "passage_score": 13, "document_id": "document_id", "collection_id": "collection_id", "start_offset": 12, "end_offset": 10, "field": "field", "answers": [{"answer_text": "answer_text", "start_offset": 12, "end_offset": 10, "confidence": 0}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query(**req_copy)

    def test_query_value_error_with_retries(self):
        # Enable retries and run test_query_value_error.
        _service.enable_retries()
        self.test_query_value_error()

        # Disable retries and run test_query_value_error.
        _service.disable_retries()
        self.test_query_value_error()

class TestGetAutocompletion():
    """
    Test Class for get_autocompletion
    """

    @responses.activate
    def test_get_autocompletion_all_params(self):
        """
        get_autocompletion()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        prefix = 'testString'
        collection_ids = ['testString']
        field = 'testString'
        count = 38

        # Invoke method
        response = _service.get_autocompletion(
            project_id,
            prefix,
            collection_ids=collection_ids,
            field=field,
            count=count,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'prefix={}'.format(prefix) in query_string
        assert 'collection_ids={}'.format(','.join(collection_ids)) in query_string
        assert 'field={}'.format(field) in query_string
        assert 'count={}'.format(count) in query_string

    def test_get_autocompletion_all_params_with_retries(self):
        # Enable retries and run test_get_autocompletion_all_params.
        _service.enable_retries()
        self.test_get_autocompletion_all_params()

        # Disable retries and run test_get_autocompletion_all_params.
        _service.disable_retries()
        self.test_get_autocompletion_all_params()

    @responses.activate
    def test_get_autocompletion_required_params(self):
        """
        test_get_autocompletion_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        prefix = 'testString'

        # Invoke method
        response = _service.get_autocompletion(
            project_id,
            prefix,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'prefix={}'.format(prefix) in query_string

    def test_get_autocompletion_required_params_with_retries(self):
        # Enable retries and run test_get_autocompletion_required_params.
        _service.enable_retries()
        self.test_get_autocompletion_required_params()

        # Disable retries and run test_get_autocompletion_required_params.
        _service.disable_retries()
        self.test_get_autocompletion_required_params()

    @responses.activate
    def test_get_autocompletion_value_error(self):
        """
        test_get_autocompletion_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        prefix = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "prefix": prefix,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_autocompletion(**req_copy)

    def test_get_autocompletion_value_error_with_retries(self):
        # Enable retries and run test_get_autocompletion_value_error.
        _service.enable_retries()
        self.test_get_autocompletion_value_error()

        # Disable retries and run test_get_autocompletion_value_error.
        _service.disable_retries()
        self.test_get_autocompletion_value_error()

class TestQueryCollectionNotices():
    """
    Test Class for query_collection_notices
    """

    @responses.activate
    def test_query_collection_notices_all_params(self):
        """
        query_collection_notices()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        count = 38
        offset = 38

        # Invoke method
        response = _service.query_collection_notices(
            project_id,
            collection_id,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            count=count,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string
        assert 'query={}'.format(query) in query_string
        assert 'natural_language_query={}'.format(natural_language_query) in query_string
        assert 'count={}'.format(count) in query_string
        assert 'offset={}'.format(offset) in query_string

    def test_query_collection_notices_all_params_with_retries(self):
        # Enable retries and run test_query_collection_notices_all_params.
        _service.enable_retries()
        self.test_query_collection_notices_all_params()

        # Disable retries and run test_query_collection_notices_all_params.
        _service.disable_retries()
        self.test_query_collection_notices_all_params()

    @responses.activate
    def test_query_collection_notices_required_params(self):
        """
        test_query_collection_notices_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.query_collection_notices(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_query_collection_notices_required_params_with_retries(self):
        # Enable retries and run test_query_collection_notices_required_params.
        _service.enable_retries()
        self.test_query_collection_notices_required_params()

        # Disable retries and run test_query_collection_notices_required_params.
        _service.disable_retries()
        self.test_query_collection_notices_required_params()

    @responses.activate
    def test_query_collection_notices_value_error(self):
        """
        test_query_collection_notices_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query_collection_notices(**req_copy)

    def test_query_collection_notices_value_error_with_retries(self):
        # Enable retries and run test_query_collection_notices_value_error.
        _service.enable_retries()
        self.test_query_collection_notices_value_error()

        # Disable retries and run test_query_collection_notices_value_error.
        _service.disable_retries()
        self.test_query_collection_notices_value_error()

class TestQueryNotices():
    """
    Test Class for query_notices
    """

    @responses.activate
    def test_query_notices_all_params(self):
        """
        query_notices()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        count = 38
        offset = 38

        # Invoke method
        response = _service.query_notices(
            project_id,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            count=count,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string
        assert 'query={}'.format(query) in query_string
        assert 'natural_language_query={}'.format(natural_language_query) in query_string
        assert 'count={}'.format(count) in query_string
        assert 'offset={}'.format(offset) in query_string

    def test_query_notices_all_params_with_retries(self):
        # Enable retries and run test_query_notices_all_params.
        _service.enable_retries()
        self.test_query_notices_all_params()

        # Disable retries and run test_query_notices_all_params.
        _service.disable_retries()
        self.test_query_notices_all_params()

    @responses.activate
    def test_query_notices_required_params(self):
        """
        test_query_notices_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.query_notices(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_query_notices_required_params_with_retries(self):
        # Enable retries and run test_query_notices_required_params.
        _service.enable_retries()
        self.test_query_notices_required_params()

        # Disable retries and run test_query_notices_required_params.
        _service.disable_retries()
        self.test_query_notices_required_params()

    @responses.activate
    def test_query_notices_value_error(self):
        """
        test_query_notices_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/notices')
        mock_response = '{"matching_results": 16, "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query_notices(**req_copy)

    def test_query_notices_value_error_with_retries(self):
        # Enable retries and run test_query_notices_value_error.
        _service.enable_retries()
        self.test_query_notices_value_error()

        # Disable retries and run test_query_notices_value_error.
        _service.disable_retries()
        self.test_query_notices_value_error()

# endregion
##############################################################################
# End of Service: Queries
##############################################################################

##############################################################################
# Start of Service: QueryModifications
##############################################################################
# region

class TestGetStopwordList():
    """
    Test Class for get_stopword_list
    """

    @responses.activate
    def test_get_stopword_list_all_params(self):
        """
        get_stopword_list()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/stopwords')
        mock_response = '{"stopwords": ["stopwords"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.get_stopword_list(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_stopword_list_all_params_with_retries(self):
        # Enable retries and run test_get_stopword_list_all_params.
        _service.enable_retries()
        self.test_get_stopword_list_all_params()

        # Disable retries and run test_get_stopword_list_all_params.
        _service.disable_retries()
        self.test_get_stopword_list_all_params()

    @responses.activate
    def test_get_stopword_list_value_error(self):
        """
        test_get_stopword_list_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/stopwords')
        mock_response = '{"stopwords": ["stopwords"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_stopword_list(**req_copy)

    def test_get_stopword_list_value_error_with_retries(self):
        # Enable retries and run test_get_stopword_list_value_error.
        _service.enable_retries()
        self.test_get_stopword_list_value_error()

        # Disable retries and run test_get_stopword_list_value_error.
        _service.disable_retries()
        self.test_get_stopword_list_value_error()

class TestCreateStopwordList():
    """
    Test Class for create_stopword_list
    """

    @responses.activate
    def test_create_stopword_list_all_params(self):
        """
        create_stopword_list()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/stopwords')
        mock_response = '{"stopwords": ["stopwords"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        stopwords = ['testString']

        # Invoke method
        response = _service.create_stopword_list(
            project_id,
            collection_id,
            stopwords=stopwords,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['stopwords'] == ['testString']

    def test_create_stopword_list_all_params_with_retries(self):
        # Enable retries and run test_create_stopword_list_all_params.
        _service.enable_retries()
        self.test_create_stopword_list_all_params()

        # Disable retries and run test_create_stopword_list_all_params.
        _service.disable_retries()
        self.test_create_stopword_list_all_params()

    @responses.activate
    def test_create_stopword_list_required_params(self):
        """
        test_create_stopword_list_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/stopwords')
        mock_response = '{"stopwords": ["stopwords"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.create_stopword_list(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_stopword_list_required_params_with_retries(self):
        # Enable retries and run test_create_stopword_list_required_params.
        _service.enable_retries()
        self.test_create_stopword_list_required_params()

        # Disable retries and run test_create_stopword_list_required_params.
        _service.disable_retries()
        self.test_create_stopword_list_required_params()

    @responses.activate
    def test_create_stopword_list_value_error(self):
        """
        test_create_stopword_list_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/stopwords')
        mock_response = '{"stopwords": ["stopwords"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_stopword_list(**req_copy)

    def test_create_stopword_list_value_error_with_retries(self):
        # Enable retries and run test_create_stopword_list_value_error.
        _service.enable_retries()
        self.test_create_stopword_list_value_error()

        # Disable retries and run test_create_stopword_list_value_error.
        _service.disable_retries()
        self.test_create_stopword_list_value_error()

class TestDeleteStopwordList():
    """
    Test Class for delete_stopword_list
    """

    @responses.activate
    def test_delete_stopword_list_all_params(self):
        """
        delete_stopword_list()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/stopwords')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_stopword_list(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_stopword_list_all_params_with_retries(self):
        # Enable retries and run test_delete_stopword_list_all_params.
        _service.enable_retries()
        self.test_delete_stopword_list_all_params()

        # Disable retries and run test_delete_stopword_list_all_params.
        _service.disable_retries()
        self.test_delete_stopword_list_all_params()

    @responses.activate
    def test_delete_stopword_list_value_error(self):
        """
        test_delete_stopword_list_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/stopwords')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_stopword_list(**req_copy)

    def test_delete_stopword_list_value_error_with_retries(self):
        # Enable retries and run test_delete_stopword_list_value_error.
        _service.enable_retries()
        self.test_delete_stopword_list_value_error()

        # Disable retries and run test_delete_stopword_list_value_error.
        _service.disable_retries()
        self.test_delete_stopword_list_value_error()

class TestListExpansions():
    """
    Test Class for list_expansions
    """

    @responses.activate
    def test_list_expansions_all_params(self):
        """
        list_expansions()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.list_expansions(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_expansions_all_params_with_retries(self):
        # Enable retries and run test_list_expansions_all_params.
        _service.enable_retries()
        self.test_list_expansions_all_params()

        # Disable retries and run test_list_expansions_all_params.
        _service.disable_retries()
        self.test_list_expansions_all_params()

    @responses.activate
    def test_list_expansions_value_error(self):
        """
        test_list_expansions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_expansions(**req_copy)

    def test_list_expansions_value_error_with_retries(self):
        # Enable retries and run test_list_expansions_value_error.
        _service.enable_retries()
        self.test_list_expansions_value_error()

        # Disable retries and run test_list_expansions_value_error.
        _service.disable_retries()
        self.test_list_expansions_value_error()

class TestCreateExpansions():
    """
    Test Class for create_expansions
    """

    @responses.activate
    def test_create_expansions_all_params(self):
        """
        create_expansions()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Expansion model
        expansion_model = {}
        expansion_model['input_terms'] = ['testString']
        expansion_model['expanded_terms'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        expansions = [expansion_model]

        # Invoke method
        response = _service.create_expansions(
            project_id,
            collection_id,
            expansions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expansions'] == [expansion_model]

    def test_create_expansions_all_params_with_retries(self):
        # Enable retries and run test_create_expansions_all_params.
        _service.enable_retries()
        self.test_create_expansions_all_params()

        # Disable retries and run test_create_expansions_all_params.
        _service.disable_retries()
        self.test_create_expansions_all_params()

    @responses.activate
    def test_create_expansions_value_error(self):
        """
        test_create_expansions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Expansion model
        expansion_model = {}
        expansion_model['input_terms'] = ['testString']
        expansion_model['expanded_terms'] = ['testString']

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        expansions = [expansion_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
            "expansions": expansions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_expansions(**req_copy)

    def test_create_expansions_value_error_with_retries(self):
        # Enable retries and run test_create_expansions_value_error.
        _service.enable_retries()
        self.test_create_expansions_value_error()

        # Disable retries and run test_create_expansions_value_error.
        _service.disable_retries()
        self.test_create_expansions_value_error()

class TestDeleteExpansions():
    """
    Test Class for delete_expansions
    """

    @responses.activate
    def test_delete_expansions_all_params(self):
        """
        delete_expansions()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/expansions')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_expansions(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_expansions_all_params_with_retries(self):
        # Enable retries and run test_delete_expansions_all_params.
        _service.enable_retries()
        self.test_delete_expansions_all_params()

        # Disable retries and run test_delete_expansions_all_params.
        _service.disable_retries()
        self.test_delete_expansions_all_params()

    @responses.activate
    def test_delete_expansions_value_error(self):
        """
        test_delete_expansions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/expansions')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_expansions(**req_copy)

    def test_delete_expansions_value_error_with_retries(self):
        # Enable retries and run test_delete_expansions_value_error.
        _service.enable_retries()
        self.test_delete_expansions_value_error()

        # Disable retries and run test_delete_expansions_value_error.
        _service.disable_retries()
        self.test_delete_expansions_value_error()

# endregion
##############################################################################
# End of Service: QueryModifications
##############################################################################

##############################################################################
# Start of Service: ComponentSettings
##############################################################################
# region

class TestGetComponentSettings():
    """
    Test Class for get_component_settings
    """

    @responses.activate
    def test_get_component_settings_all_params(self):
        """
        get_component_settings()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/component_settings')
        mock_response = '{"fields_shown": {"body": {"use_passage": false, "field": "field"}, "title": {"field": "field"}}, "autocomplete": true, "structured_search": false, "results_per_page": 16, "aggregations": [{"name": "name", "label": "label", "multiple_selections_allowed": false, "visualization_type": "auto"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.get_component_settings(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_component_settings_all_params_with_retries(self):
        # Enable retries and run test_get_component_settings_all_params.
        _service.enable_retries()
        self.test_get_component_settings_all_params()

        # Disable retries and run test_get_component_settings_all_params.
        _service.disable_retries()
        self.test_get_component_settings_all_params()

    @responses.activate
    def test_get_component_settings_value_error(self):
        """
        test_get_component_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/component_settings')
        mock_response = '{"fields_shown": {"body": {"use_passage": false, "field": "field"}, "title": {"field": "field"}}, "autocomplete": true, "structured_search": false, "results_per_page": 16, "aggregations": [{"name": "name", "label": "label", "multiple_selections_allowed": false, "visualization_type": "auto"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_component_settings(**req_copy)

    def test_get_component_settings_value_error_with_retries(self):
        # Enable retries and run test_get_component_settings_value_error.
        _service.enable_retries()
        self.test_get_component_settings_value_error()

        # Disable retries and run test_get_component_settings_value_error.
        _service.disable_retries()
        self.test_get_component_settings_value_error()

# endregion
##############################################################################
# End of Service: ComponentSettings
##############################################################################

##############################################################################
# Start of Service: TrainingData
##############################################################################
# region

class TestListTrainingQueries():
    """
    Test Class for list_training_queries
    """

    @responses.activate
    def test_list_training_queries_all_params(self):
        """
        list_training_queries()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries')
        mock_response = '{"queries": [{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_training_queries(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_training_queries_all_params_with_retries(self):
        # Enable retries and run test_list_training_queries_all_params.
        _service.enable_retries()
        self.test_list_training_queries_all_params()

        # Disable retries and run test_list_training_queries_all_params.
        _service.disable_retries()
        self.test_list_training_queries_all_params()

    @responses.activate
    def test_list_training_queries_value_error(self):
        """
        test_list_training_queries_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries')
        mock_response = '{"queries": [{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_training_queries(**req_copy)

    def test_list_training_queries_value_error_with_retries(self):
        # Enable retries and run test_list_training_queries_value_error.
        _service.enable_retries()
        self.test_list_training_queries_value_error()

        # Disable retries and run test_list_training_queries_value_error.
        _service.disable_retries()
        self.test_list_training_queries_value_error()

class TestDeleteTrainingQueries():
    """
    Test Class for delete_training_queries
    """

    @responses.activate
    def test_delete_training_queries_all_params(self):
        """
        delete_training_queries()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.delete_training_queries(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_training_queries_all_params_with_retries(self):
        # Enable retries and run test_delete_training_queries_all_params.
        _service.enable_retries()
        self.test_delete_training_queries_all_params()

        # Disable retries and run test_delete_training_queries_all_params.
        _service.disable_retries()
        self.test_delete_training_queries_all_params()

    @responses.activate
    def test_delete_training_queries_value_error(self):
        """
        test_delete_training_queries_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_training_queries(**req_copy)

    def test_delete_training_queries_value_error_with_retries(self):
        # Enable retries and run test_delete_training_queries_value_error.
        _service.enable_retries()
        self.test_delete_training_queries_value_error()

        # Disable retries and run test_delete_training_queries_value_error.
        _service.disable_retries()
        self.test_delete_training_queries_value_error()

class TestCreateTrainingQuery():
    """
    Test Class for create_training_query
    """

    @responses.activate
    def test_create_training_query_all_params(self):
        """
        create_training_query()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Invoke method
        response = _service.create_training_query(
            project_id,
            natural_language_query,
            examples,
            filter=filter,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['examples'] == [training_example_model]
        assert req_body['filter'] == 'testString'

    def test_create_training_query_all_params_with_retries(self):
        # Enable retries and run test_create_training_query_all_params.
        _service.enable_retries()
        self.test_create_training_query_all_params()

        # Disable retries and run test_create_training_query_all_params.
        _service.disable_retries()
        self.test_create_training_query_all_params()

    @responses.activate
    def test_create_training_query_value_error(self):
        """
        test_create_training_query_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "natural_language_query": natural_language_query,
            "examples": examples,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_training_query(**req_copy)

    def test_create_training_query_value_error_with_retries(self):
        # Enable retries and run test_create_training_query_value_error.
        _service.enable_retries()
        self.test_create_training_query_value_error()

        # Disable retries and run test_create_training_query_value_error.
        _service.disable_retries()
        self.test_create_training_query_value_error()

class TestGetTrainingQuery():
    """
    Test Class for get_training_query
    """

    @responses.activate
    def test_get_training_query_all_params(self):
        """
        get_training_query()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Invoke method
        response = _service.get_training_query(
            project_id,
            query_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_training_query_all_params_with_retries(self):
        # Enable retries and run test_get_training_query_all_params.
        _service.enable_retries()
        self.test_get_training_query_all_params()

        # Disable retries and run test_get_training_query_all_params.
        _service.disable_retries()
        self.test_get_training_query_all_params()

    @responses.activate
    def test_get_training_query_value_error(self):
        """
        test_get_training_query_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_training_query(**req_copy)

    def test_get_training_query_value_error_with_retries(self):
        # Enable retries and run test_get_training_query_value_error.
        _service.enable_retries()
        self.test_get_training_query_value_error()

        # Disable retries and run test_get_training_query_value_error.
        _service.disable_retries()
        self.test_get_training_query_value_error()

class TestUpdateTrainingQuery():
    """
    Test Class for update_training_query
    """

    @responses.activate
    def test_update_training_query_all_params(self):
        """
        update_training_query()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Invoke method
        response = _service.update_training_query(
            project_id,
            query_id,
            natural_language_query,
            examples,
            filter=filter,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['examples'] == [training_example_model]
        assert req_body['filter'] == 'testString'

    def test_update_training_query_all_params_with_retries(self):
        # Enable retries and run test_update_training_query_all_params.
        _service.enable_retries()
        self.test_update_training_query_all_params()

        # Disable retries and run test_update_training_query_all_params.
        _service.disable_retries()
        self.test_update_training_query_all_params()

    @responses.activate
    def test_update_training_query_value_error(self):
        """
        test_update_training_query_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"document_id": "document_id", "collection_id": "collection_id", "relevance": 9, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'
        natural_language_query = 'testString'
        examples = [training_example_model]
        filter = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "query_id": query_id,
            "natural_language_query": natural_language_query,
            "examples": examples,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_training_query(**req_copy)

    def test_update_training_query_value_error_with_retries(self):
        # Enable retries and run test_update_training_query_value_error.
        _service.enable_retries()
        self.test_update_training_query_value_error()

        # Disable retries and run test_update_training_query_value_error.
        _service.disable_retries()
        self.test_update_training_query_value_error()

class TestDeleteTrainingQuery():
    """
    Test Class for delete_training_query
    """

    @responses.activate
    def test_delete_training_query_all_params(self):
        """
        delete_training_query()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Invoke method
        response = _service.delete_training_query(
            project_id,
            query_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_training_query_all_params_with_retries(self):
        # Enable retries and run test_delete_training_query_all_params.
        _service.enable_retries()
        self.test_delete_training_query_all_params()

        # Disable retries and run test_delete_training_query_all_params.
        _service.disable_retries()
        self.test_delete_training_query_all_params()

    @responses.activate
    def test_delete_training_query_value_error(self):
        """
        test_delete_training_query_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/training_data/queries/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        query_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_training_query(**req_copy)

    def test_delete_training_query_value_error_with_retries(self):
        # Enable retries and run test_delete_training_query_value_error.
        _service.enable_retries()
        self.test_delete_training_query_value_error()

        # Disable retries and run test_delete_training_query_value_error.
        _service.disable_retries()
        self.test_delete_training_query_value_error()

# endregion
##############################################################################
# End of Service: TrainingData
##############################################################################

##############################################################################
# Start of Service: Enrichments
##############################################################################
# region

class TestListEnrichments():
    """
    Test Class for list_enrichments
    """

    @responses.activate
    def test_list_enrichments_all_params(self):
        """
        list_enrichments()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments')
        mock_response = '{"enrichments": [{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_enrichments(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_enrichments_all_params_with_retries(self):
        # Enable retries and run test_list_enrichments_all_params.
        _service.enable_retries()
        self.test_list_enrichments_all_params()

        # Disable retries and run test_list_enrichments_all_params.
        _service.disable_retries()
        self.test_list_enrichments_all_params()

    @responses.activate
    def test_list_enrichments_value_error(self):
        """
        test_list_enrichments_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments')
        mock_response = '{"enrichments": [{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_enrichments(**req_copy)

    def test_list_enrichments_value_error_with_retries(self):
        # Enable retries and run test_list_enrichments_value_error.
        _service.enable_retries()
        self.test_list_enrichments_value_error()

        # Disable retries and run test_list_enrichments_value_error.
        _service.disable_retries()
        self.test_list_enrichments_value_error()

class TestCreateEnrichment():
    """
    Test Class for create_enrichment
    """

    @responses.activate
    def test_create_enrichment_all_params(self):
        """
        create_enrichment()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'
        enrichment_options_model['classifier_id'] = 'testString'
        enrichment_options_model['model_id'] = 'testString'
        enrichment_options_model['confidence_threshold'] = 0
        enrichment_options_model['top_k'] = 38

        # Construct a dict representation of a CreateEnrichment model
        create_enrichment_model = {}
        create_enrichment_model['name'] = 'testString'
        create_enrichment_model['description'] = 'testString'
        create_enrichment_model['type'] = 'classifier'
        create_enrichment_model['options'] = enrichment_options_model

        # Set up parameter values
        project_id = 'testString'
        enrichment = create_enrichment_model
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_enrichment(
            project_id,
            enrichment,
            file=file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_enrichment_all_params_with_retries(self):
        # Enable retries and run test_create_enrichment_all_params.
        _service.enable_retries()
        self.test_create_enrichment_all_params()

        # Disable retries and run test_create_enrichment_all_params.
        _service.disable_retries()
        self.test_create_enrichment_all_params()

    @responses.activate
    def test_create_enrichment_required_params(self):
        """
        test_create_enrichment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'
        enrichment_options_model['classifier_id'] = 'testString'
        enrichment_options_model['model_id'] = 'testString'
        enrichment_options_model['confidence_threshold'] = 0
        enrichment_options_model['top_k'] = 38

        # Construct a dict representation of a CreateEnrichment model
        create_enrichment_model = {}
        create_enrichment_model['name'] = 'testString'
        create_enrichment_model['description'] = 'testString'
        create_enrichment_model['type'] = 'classifier'
        create_enrichment_model['options'] = enrichment_options_model

        # Set up parameter values
        project_id = 'testString'
        enrichment = create_enrichment_model

        # Invoke method
        response = _service.create_enrichment(
            project_id,
            enrichment,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_enrichment_required_params_with_retries(self):
        # Enable retries and run test_create_enrichment_required_params.
        _service.enable_retries()
        self.test_create_enrichment_required_params()

        # Disable retries and run test_create_enrichment_required_params.
        _service.disable_retries()
        self.test_create_enrichment_required_params()

    @responses.activate
    def test_create_enrichment_value_error(self):
        """
        test_create_enrichment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'
        enrichment_options_model['classifier_id'] = 'testString'
        enrichment_options_model['model_id'] = 'testString'
        enrichment_options_model['confidence_threshold'] = 0
        enrichment_options_model['top_k'] = 38

        # Construct a dict representation of a CreateEnrichment model
        create_enrichment_model = {}
        create_enrichment_model['name'] = 'testString'
        create_enrichment_model['description'] = 'testString'
        create_enrichment_model['type'] = 'classifier'
        create_enrichment_model['options'] = enrichment_options_model

        # Set up parameter values
        project_id = 'testString'
        enrichment = create_enrichment_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment": enrichment,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_enrichment(**req_copy)

    def test_create_enrichment_value_error_with_retries(self):
        # Enable retries and run test_create_enrichment_value_error.
        _service.enable_retries()
        self.test_create_enrichment_value_error()

        # Disable retries and run test_create_enrichment_value_error.
        _service.disable_retries()
        self.test_create_enrichment_value_error()

class TestGetEnrichment():
    """
    Test Class for get_enrichment
    """

    @responses.activate
    def test_get_enrichment_all_params(self):
        """
        get_enrichment()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Invoke method
        response = _service.get_enrichment(
            project_id,
            enrichment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_enrichment_all_params_with_retries(self):
        # Enable retries and run test_get_enrichment_all_params.
        _service.enable_retries()
        self.test_get_enrichment_all_params()

        # Disable retries and run test_get_enrichment_all_params.
        _service.disable_retries()
        self.test_get_enrichment_all_params()

    @responses.activate
    def test_get_enrichment_value_error(self):
        """
        test_get_enrichment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment_id": enrichment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_enrichment(**req_copy)

    def test_get_enrichment_value_error_with_retries(self):
        # Enable retries and run test_get_enrichment_value_error.
        _service.enable_retries()
        self.test_get_enrichment_value_error()

        # Disable retries and run test_get_enrichment_value_error.
        _service.disable_retries()
        self.test_get_enrichment_value_error()

class TestUpdateEnrichment():
    """
    Test Class for update_enrichment
    """

    @responses.activate
    def test_update_enrichment_all_params(self):
        """
        update_enrichment()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.update_enrichment(
            project_id,
            enrichment_id,
            name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'

    def test_update_enrichment_all_params_with_retries(self):
        # Enable retries and run test_update_enrichment_all_params.
        _service.enable_retries()
        self.test_update_enrichment_all_params()

        # Disable retries and run test_update_enrichment_all_params.
        _service.disable_retries()
        self.test_update_enrichment_all_params()

    @responses.activate
    def test_update_enrichment_value_error(self):
        """
        test_update_enrichment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments/testString')
        mock_response = '{"enrichment_id": "enrichment_id", "name": "name", "description": "description", "type": "part_of_speech", "options": {"languages": ["languages"], "entity_type": "entity_type", "regular_expression": "regular_expression", "result_field": "result_field", "classifier_id": "classifier_id", "model_id": "model_id", "confidence_threshold": 0, "top_k": 5}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment_id": enrichment_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_enrichment(**req_copy)

    def test_update_enrichment_value_error_with_retries(self):
        # Enable retries and run test_update_enrichment_value_error.
        _service.enable_retries()
        self.test_update_enrichment_value_error()

        # Disable retries and run test_update_enrichment_value_error.
        _service.disable_retries()
        self.test_update_enrichment_value_error()

class TestDeleteEnrichment():
    """
    Test Class for delete_enrichment
    """

    @responses.activate
    def test_delete_enrichment_all_params(self):
        """
        delete_enrichment()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Invoke method
        response = _service.delete_enrichment(
            project_id,
            enrichment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_enrichment_all_params_with_retries(self):
        # Enable retries and run test_delete_enrichment_all_params.
        _service.enable_retries()
        self.test_delete_enrichment_all_params()

        # Disable retries and run test_delete_enrichment_all_params.
        _service.disable_retries()
        self.test_delete_enrichment_all_params()

    @responses.activate
    def test_delete_enrichment_value_error(self):
        """
        test_delete_enrichment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/enrichments/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        enrichment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "enrichment_id": enrichment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_enrichment(**req_copy)

    def test_delete_enrichment_value_error_with_retries(self):
        # Enable retries and run test_delete_enrichment_value_error.
        _service.enable_retries()
        self.test_delete_enrichment_value_error()

        # Disable retries and run test_delete_enrichment_value_error.
        _service.disable_retries()
        self.test_delete_enrichment_value_error()

# endregion
##############################################################################
# End of Service: Enrichments
##############################################################################

##############################################################################
# Start of Service: DocumentClassifiers
##############################################################################
# region

class TestListDocumentClassifiers():
    """
    Test Class for list_document_classifiers
    """

    @responses.activate
    def test_list_document_classifiers_all_params(self):
        """
        list_document_classifiers()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers')
        mock_response = '{"classifiers": [{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Invoke method
        response = _service.list_document_classifiers(
            project_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_document_classifiers_all_params_with_retries(self):
        # Enable retries and run test_list_document_classifiers_all_params.
        _service.enable_retries()
        self.test_list_document_classifiers_all_params()

        # Disable retries and run test_list_document_classifiers_all_params.
        _service.disable_retries()
        self.test_list_document_classifiers_all_params()

    @responses.activate
    def test_list_document_classifiers_value_error(self):
        """
        test_list_document_classifiers_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers')
        mock_response = '{"classifiers": [{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_document_classifiers(**req_copy)

    def test_list_document_classifiers_value_error_with_retries(self):
        # Enable retries and run test_list_document_classifiers_value_error.
        _service.enable_retries()
        self.test_list_document_classifiers_value_error()

        # Disable retries and run test_list_document_classifiers_value_error.
        _service.disable_retries()
        self.test_list_document_classifiers_value_error()

class TestCreateDocumentClassifier():
    """
    Test Class for create_document_classifier
    """

    @responses.activate
    def test_create_document_classifier_all_params(self):
        """
        create_document_classifier()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DocumentClassifierEnrichment model
        document_classifier_enrichment_model = {}
        document_classifier_enrichment_model['enrichment_id'] = 'testString'
        document_classifier_enrichment_model['fields'] = ['testString']

        # Construct a dict representation of a ClassifierFederatedModel model
        classifier_federated_model_model = {}
        classifier_federated_model_model['field'] = 'testString'

        # Construct a dict representation of a CreateDocumentClassifier model
        create_document_classifier_model = {}
        create_document_classifier_model['name'] = 'testString'
        create_document_classifier_model['description'] = 'testString'
        create_document_classifier_model['language'] = 'en'
        create_document_classifier_model['answer_field'] = 'testString'
        create_document_classifier_model['enrichments'] = [document_classifier_enrichment_model]
        create_document_classifier_model['federated_classification'] = classifier_federated_model_model

        # Set up parameter values
        project_id = 'testString'
        training_data = io.BytesIO(b'This is a mock file.').getvalue()
        classifier = create_document_classifier_model
        test_data = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_document_classifier(
            project_id,
            training_data,
            classifier,
            test_data=test_data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_document_classifier_all_params_with_retries(self):
        # Enable retries and run test_create_document_classifier_all_params.
        _service.enable_retries()
        self.test_create_document_classifier_all_params()

        # Disable retries and run test_create_document_classifier_all_params.
        _service.disable_retries()
        self.test_create_document_classifier_all_params()

    @responses.activate
    def test_create_document_classifier_required_params(self):
        """
        test_create_document_classifier_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DocumentClassifierEnrichment model
        document_classifier_enrichment_model = {}
        document_classifier_enrichment_model['enrichment_id'] = 'testString'
        document_classifier_enrichment_model['fields'] = ['testString']

        # Construct a dict representation of a ClassifierFederatedModel model
        classifier_federated_model_model = {}
        classifier_federated_model_model['field'] = 'testString'

        # Construct a dict representation of a CreateDocumentClassifier model
        create_document_classifier_model = {}
        create_document_classifier_model['name'] = 'testString'
        create_document_classifier_model['description'] = 'testString'
        create_document_classifier_model['language'] = 'en'
        create_document_classifier_model['answer_field'] = 'testString'
        create_document_classifier_model['enrichments'] = [document_classifier_enrichment_model]
        create_document_classifier_model['federated_classification'] = classifier_federated_model_model

        # Set up parameter values
        project_id = 'testString'
        training_data = io.BytesIO(b'This is a mock file.').getvalue()
        classifier = create_document_classifier_model

        # Invoke method
        response = _service.create_document_classifier(
            project_id,
            training_data,
            classifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_document_classifier_required_params_with_retries(self):
        # Enable retries and run test_create_document_classifier_required_params.
        _service.enable_retries()
        self.test_create_document_classifier_required_params()

        # Disable retries and run test_create_document_classifier_required_params.
        _service.disable_retries()
        self.test_create_document_classifier_required_params()

    @responses.activate
    def test_create_document_classifier_value_error(self):
        """
        test_create_document_classifier_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DocumentClassifierEnrichment model
        document_classifier_enrichment_model = {}
        document_classifier_enrichment_model['enrichment_id'] = 'testString'
        document_classifier_enrichment_model['fields'] = ['testString']

        # Construct a dict representation of a ClassifierFederatedModel model
        classifier_federated_model_model = {}
        classifier_federated_model_model['field'] = 'testString'

        # Construct a dict representation of a CreateDocumentClassifier model
        create_document_classifier_model = {}
        create_document_classifier_model['name'] = 'testString'
        create_document_classifier_model['description'] = 'testString'
        create_document_classifier_model['language'] = 'en'
        create_document_classifier_model['answer_field'] = 'testString'
        create_document_classifier_model['enrichments'] = [document_classifier_enrichment_model]
        create_document_classifier_model['federated_classification'] = classifier_federated_model_model

        # Set up parameter values
        project_id = 'testString'
        training_data = io.BytesIO(b'This is a mock file.').getvalue()
        classifier = create_document_classifier_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "training_data": training_data,
            "classifier": classifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_document_classifier(**req_copy)

    def test_create_document_classifier_value_error_with_retries(self):
        # Enable retries and run test_create_document_classifier_value_error.
        _service.enable_retries()
        self.test_create_document_classifier_value_error()

        # Disable retries and run test_create_document_classifier_value_error.
        _service.disable_retries()
        self.test_create_document_classifier_value_error()

class TestGetDocumentClassifier():
    """
    Test Class for get_document_classifier
    """

    @responses.activate
    def test_get_document_classifier_all_params(self):
        """
        get_document_classifier()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'

        # Invoke method
        response = _service.get_document_classifier(
            project_id,
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_document_classifier_all_params_with_retries(self):
        # Enable retries and run test_get_document_classifier_all_params.
        _service.enable_retries()
        self.test_get_document_classifier_all_params()

        # Disable retries and run test_get_document_classifier_all_params.
        _service.disable_retries()
        self.test_get_document_classifier_all_params()

    @responses.activate
    def test_get_document_classifier_value_error(self):
        """
        test_get_document_classifier_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_document_classifier(**req_copy)

    def test_get_document_classifier_value_error_with_retries(self):
        # Enable retries and run test_get_document_classifier_value_error.
        _service.enable_retries()
        self.test_get_document_classifier_value_error()

        # Disable retries and run test_get_document_classifier_value_error.
        _service.disable_retries()
        self.test_get_document_classifier_value_error()

class TestUpdateDocumentClassifier():
    """
    Test Class for update_document_classifier
    """

    @responses.activate
    def test_update_document_classifier_all_params(self):
        """
        update_document_classifier()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a UpdateDocumentClassifier model
        update_document_classifier_model = {}
        update_document_classifier_model['name'] = 'testString'
        update_document_classifier_model['description'] = 'testString'

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        classifier = update_document_classifier_model
        training_data = io.BytesIO(b'This is a mock file.').getvalue()
        test_data = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.update_document_classifier(
            project_id,
            classifier_id,
            classifier,
            training_data=training_data,
            test_data=test_data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_update_document_classifier_all_params_with_retries(self):
        # Enable retries and run test_update_document_classifier_all_params.
        _service.enable_retries()
        self.test_update_document_classifier_all_params()

        # Disable retries and run test_update_document_classifier_all_params.
        _service.disable_retries()
        self.test_update_document_classifier_all_params()

    @responses.activate
    def test_update_document_classifier_required_params(self):
        """
        test_update_document_classifier_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a UpdateDocumentClassifier model
        update_document_classifier_model = {}
        update_document_classifier_model['name'] = 'testString'
        update_document_classifier_model['description'] = 'testString'

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        classifier = update_document_classifier_model

        # Invoke method
        response = _service.update_document_classifier(
            project_id,
            classifier_id,
            classifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_update_document_classifier_required_params_with_retries(self):
        # Enable retries and run test_update_document_classifier_required_params.
        _service.enable_retries()
        self.test_update_document_classifier_required_params()

        # Disable retries and run test_update_document_classifier_required_params.
        _service.disable_retries()
        self.test_update_document_classifier_required_params()

    @responses.activate
    def test_update_document_classifier_value_error(self):
        """
        test_update_document_classifier_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "language": "en", "enrichments": [{"enrichment_id": "enrichment_id", "fields": ["fields"]}], "recognized_fields": ["recognized_fields"], "answer_field": "answer_field", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "federated_classification": {"field": "field"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a UpdateDocumentClassifier model
        update_document_classifier_model = {}
        update_document_classifier_model['name'] = 'testString'
        update_document_classifier_model['description'] = 'testString'

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        classifier = update_document_classifier_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
            "classifier": classifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_document_classifier(**req_copy)

    def test_update_document_classifier_value_error_with_retries(self):
        # Enable retries and run test_update_document_classifier_value_error.
        _service.enable_retries()
        self.test_update_document_classifier_value_error()

        # Disable retries and run test_update_document_classifier_value_error.
        _service.disable_retries()
        self.test_update_document_classifier_value_error()

class TestDeleteDocumentClassifier():
    """
    Test Class for delete_document_classifier
    """

    @responses.activate
    def test_delete_document_classifier_all_params(self):
        """
        delete_document_classifier()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'

        # Invoke method
        response = _service.delete_document_classifier(
            project_id,
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_document_classifier_all_params_with_retries(self):
        # Enable retries and run test_delete_document_classifier_all_params.
        _service.enable_retries()
        self.test_delete_document_classifier_all_params()

        # Disable retries and run test_delete_document_classifier_all_params.
        _service.disable_retries()
        self.test_delete_document_classifier_all_params()

    @responses.activate
    def test_delete_document_classifier_value_error(self):
        """
        test_delete_document_classifier_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_document_classifier(**req_copy)

    def test_delete_document_classifier_value_error_with_retries(self):
        # Enable retries and run test_delete_document_classifier_value_error.
        _service.enable_retries()
        self.test_delete_document_classifier_value_error()

        # Disable retries and run test_delete_document_classifier_value_error.
        _service.disable_retries()
        self.test_delete_document_classifier_value_error()

# endregion
##############################################################################
# End of Service: DocumentClassifiers
##############################################################################

##############################################################################
# Start of Service: DocumentClassifierModels
##############################################################################
# region

class TestListDocumentClassifierModels():
    """
    Test Class for list_document_classifier_models
    """

    @responses.activate
    def test_list_document_classifier_models_all_params(self):
        """
        list_document_classifier_models()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models')
        mock_response = '{"models": [{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'

        # Invoke method
        response = _service.list_document_classifier_models(
            project_id,
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_document_classifier_models_all_params_with_retries(self):
        # Enable retries and run test_list_document_classifier_models_all_params.
        _service.enable_retries()
        self.test_list_document_classifier_models_all_params()

        # Disable retries and run test_list_document_classifier_models_all_params.
        _service.disable_retries()
        self.test_list_document_classifier_models_all_params()

    @responses.activate
    def test_list_document_classifier_models_value_error(self):
        """
        test_list_document_classifier_models_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models')
        mock_response = '{"models": [{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_document_classifier_models(**req_copy)

    def test_list_document_classifier_models_value_error_with_retries(self):
        # Enable retries and run test_list_document_classifier_models_value_error.
        _service.enable_retries()
        self.test_list_document_classifier_models_value_error()

        # Disable retries and run test_list_document_classifier_models_value_error.
        _service.disable_retries()
        self.test_list_document_classifier_models_value_error()

class TestCreateDocumentClassifierModel():
    """
    Test Class for create_document_classifier_model
    """

    @responses.activate
    def test_create_document_classifier_model_all_params(self):
        """
        create_document_classifier_model()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models')
        mock_response = '{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        name = 'testString'
        description = 'testString'
        learning_rate = 0
        l1_regularization_strengths = [1.0E-6]
        l2_regularization_strengths = [1.0E-6]
        training_max_steps = 0
        improvement_ratio = 0

        # Invoke method
        response = _service.create_document_classifier_model(
            project_id,
            classifier_id,
            name,
            description=description,
            learning_rate=learning_rate,
            l1_regularization_strengths=l1_regularization_strengths,
            l2_regularization_strengths=l2_regularization_strengths,
            training_max_steps=training_max_steps,
            improvement_ratio=improvement_ratio,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['learning_rate'] == 0
        assert req_body['l1_regularization_strengths'] == [1.0E-6]
        assert req_body['l2_regularization_strengths'] == [1.0E-6]
        assert req_body['training_max_steps'] == 0
        assert req_body['improvement_ratio'] == 0

    def test_create_document_classifier_model_all_params_with_retries(self):
        # Enable retries and run test_create_document_classifier_model_all_params.
        _service.enable_retries()
        self.test_create_document_classifier_model_all_params()

        # Disable retries and run test_create_document_classifier_model_all_params.
        _service.disable_retries()
        self.test_create_document_classifier_model_all_params()

    @responses.activate
    def test_create_document_classifier_model_value_error(self):
        """
        test_create_document_classifier_model_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models')
        mock_response = '{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        name = 'testString'
        description = 'testString'
        learning_rate = 0
        l1_regularization_strengths = [1.0E-6]
        l2_regularization_strengths = [1.0E-6]
        training_max_steps = 0
        improvement_ratio = 0

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_document_classifier_model(**req_copy)

    def test_create_document_classifier_model_value_error_with_retries(self):
        # Enable retries and run test_create_document_classifier_model_value_error.
        _service.enable_retries()
        self.test_create_document_classifier_model_value_error()

        # Disable retries and run test_create_document_classifier_model_value_error.
        _service.disable_retries()
        self.test_create_document_classifier_model_value_error()

class TestGetDocumentClassifierModel():
    """
    Test Class for get_document_classifier_model
    """

    @responses.activate
    def test_get_document_classifier_model_all_params(self):
        """
        get_document_classifier_model()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models/testString')
        mock_response = '{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        model_id = 'testString'

        # Invoke method
        response = _service.get_document_classifier_model(
            project_id,
            classifier_id,
            model_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_document_classifier_model_all_params_with_retries(self):
        # Enable retries and run test_get_document_classifier_model_all_params.
        _service.enable_retries()
        self.test_get_document_classifier_model_all_params()

        # Disable retries and run test_get_document_classifier_model_all_params.
        _service.disable_retries()
        self.test_get_document_classifier_model_all_params()

    @responses.activate
    def test_get_document_classifier_model_value_error(self):
        """
        test_get_document_classifier_model_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models/testString')
        mock_response = '{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        model_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
            "model_id": model_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_document_classifier_model(**req_copy)

    def test_get_document_classifier_model_value_error_with_retries(self):
        # Enable retries and run test_get_document_classifier_model_value_error.
        _service.enable_retries()
        self.test_get_document_classifier_model_value_error()

        # Disable retries and run test_get_document_classifier_model_value_error.
        _service.disable_retries()
        self.test_get_document_classifier_model_value_error()

class TestUpdateDocumentClassifierModel():
    """
    Test Class for update_document_classifier_model
    """

    @responses.activate
    def test_update_document_classifier_model_all_params(self):
        """
        update_document_classifier_model()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models/testString')
        mock_response = '{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        model_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.update_document_classifier_model(
            project_id,
            classifier_id,
            model_id,
            name=name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'

    def test_update_document_classifier_model_all_params_with_retries(self):
        # Enable retries and run test_update_document_classifier_model_all_params.
        _service.enable_retries()
        self.test_update_document_classifier_model_all_params()

        # Disable retries and run test_update_document_classifier_model_all_params.
        _service.disable_retries()
        self.test_update_document_classifier_model_all_params()

    @responses.activate
    def test_update_document_classifier_model_value_error(self):
        """
        test_update_document_classifier_model_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models/testString')
        mock_response = '{"model_id": "model_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "training_data_file": "training_data_file", "test_data_file": "test_data_file", "status": "training", "evaluation": {"micro_average": {"precision": 0, "recall": 0, "f1": 0}, "macro_average": {"precision": 0, "recall": 0, "f1": 0}, "per_class": [{"name": "name", "precision": 0, "recall": 0, "f1": 0}]}, "enrichment_id": "enrichment_id", "deployed_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        model_id = 'testString'
        name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
            "model_id": model_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_document_classifier_model(**req_copy)

    def test_update_document_classifier_model_value_error_with_retries(self):
        # Enable retries and run test_update_document_classifier_model_value_error.
        _service.enable_retries()
        self.test_update_document_classifier_model_value_error()

        # Disable retries and run test_update_document_classifier_model_value_error.
        _service.disable_retries()
        self.test_update_document_classifier_model_value_error()

class TestDeleteDocumentClassifierModel():
    """
    Test Class for delete_document_classifier_model
    """

    @responses.activate
    def test_delete_document_classifier_model_all_params(self):
        """
        delete_document_classifier_model()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        model_id = 'testString'

        # Invoke method
        response = _service.delete_document_classifier_model(
            project_id,
            classifier_id,
            model_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_document_classifier_model_all_params_with_retries(self):
        # Enable retries and run test_delete_document_classifier_model_all_params.
        _service.enable_retries()
        self.test_delete_document_classifier_model_all_params()

        # Disable retries and run test_delete_document_classifier_model_all_params.
        _service.disable_retries()
        self.test_delete_document_classifier_model_all_params()

    @responses.activate
    def test_delete_document_classifier_model_value_error(self):
        """
        test_delete_document_classifier_model_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/document_classifiers/testString/models/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        project_id = 'testString'
        classifier_id = 'testString'
        model_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "classifier_id": classifier_id,
            "model_id": model_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_document_classifier_model(**req_copy)

    def test_delete_document_classifier_model_value_error_with_retries(self):
        # Enable retries and run test_delete_document_classifier_model_value_error.
        _service.enable_retries()
        self.test_delete_document_classifier_model_value_error()

        # Disable retries and run test_delete_document_classifier_model_value_error.
        _service.disable_retries()
        self.test_delete_document_classifier_model_value_error()

# endregion
##############################################################################
# End of Service: DocumentClassifierModels
##############################################################################

##############################################################################
# Start of Service: Analyze
##############################################################################
# region

class TestAnalyzeDocument():
    """
    Test Class for analyze_document
    """

    @responses.activate
    def test_analyze_document_all_params(self):
        """
        analyze_document()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/analyze')
        mock_response = '{"notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "result": {"metadata": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'

        # Invoke method
        response = _service.analyze_document(
            project_id,
            collection_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_analyze_document_all_params_with_retries(self):
        # Enable retries and run test_analyze_document_all_params.
        _service.enable_retries()
        self.test_analyze_document_all_params()

        # Disable retries and run test_analyze_document_all_params.
        _service.disable_retries()
        self.test_analyze_document_all_params()

    @responses.activate
    def test_analyze_document_required_params(self):
        """
        test_analyze_document_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/analyze')
        mock_response = '{"notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "result": {"metadata": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.analyze_document(
            project_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_analyze_document_required_params_with_retries(self):
        # Enable retries and run test_analyze_document_required_params.
        _service.enable_retries()
        self.test_analyze_document_required_params()

        # Disable retries and run test_analyze_document_required_params.
        _service.disable_retries()
        self.test_analyze_document_required_params()

    @responses.activate
    def test_analyze_document_value_error(self):
        """
        test_analyze_document_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/projects/testString/collections/testString/analyze')
        mock_response = '{"notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "collection_id": "collection_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}], "result": {"metadata": {"anyKey": "anyValue"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        project_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "project_id": project_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.analyze_document(**req_copy)

    def test_analyze_document_value_error_with_retries(self):
        # Enable retries and run test_analyze_document_value_error.
        _service.enable_retries()
        self.test_analyze_document_value_error()

        # Disable retries and run test_analyze_document_value_error.
        _service.disable_retries()
        self.test_analyze_document_value_error()

# endregion
##############################################################################
# End of Service: Analyze
##############################################################################

##############################################################################
# Start of Service: UserData
##############################################################################
# region

class TestDeleteUserData():
    """
    Test Class for delete_user_data
    """

    @responses.activate
    def test_delete_user_data_all_params(self):
        """
        delete_user_data()
        """
        # Set up mock
        url = preprocess_url('/v2/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customer_id = 'testString'

        # Invoke method
        response = _service.delete_user_data(
            customer_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'customer_id={}'.format(customer_id) in query_string

    def test_delete_user_data_all_params_with_retries(self):
        # Enable retries and run test_delete_user_data_all_params.
        _service.enable_retries()
        self.test_delete_user_data_all_params()

        # Disable retries and run test_delete_user_data_all_params.
        _service.disable_retries()
        self.test_delete_user_data_all_params()

    @responses.activate
    def test_delete_user_data_value_error(self):
        """
        test_delete_user_data_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customer_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customer_id": customer_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_user_data(**req_copy)

    def test_delete_user_data_value_error_with_retries(self):
        # Enable retries and run test_delete_user_data_value_error.
        _service.enable_retries()
        self.test_delete_user_data_value_error()

        # Disable retries and run test_delete_user_data_value_error.
        _service.disable_retries()
        self.test_delete_user_data_value_error()

# endregion
##############################################################################
# End of Service: UserData
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AnalyzedDocument():
    """
    Test Class for AnalyzedDocument
    """

    def test_analyzed_document_serialization(self):
        """
        Test serialization/deserialization for AnalyzedDocument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice

        analyzed_result_model = {} # AnalyzedResult
        analyzed_result_model['metadata'] = {'foo': 'bar'}
        analyzed_result_model['foo'] = 'testString'

        # Construct a json representation of a AnalyzedDocument model
        analyzed_document_model_json = {}
        analyzed_document_model_json['notices'] = [notice_model]
        analyzed_document_model_json['result'] = analyzed_result_model

        # Construct a model instance of AnalyzedDocument by calling from_dict on the json representation
        analyzed_document_model = AnalyzedDocument.from_dict(analyzed_document_model_json)
        assert analyzed_document_model != False

        # Construct a model instance of AnalyzedDocument by calling from_dict on the json representation
        analyzed_document_model_dict = AnalyzedDocument.from_dict(analyzed_document_model_json).__dict__
        analyzed_document_model2 = AnalyzedDocument(**analyzed_document_model_dict)

        # Verify the model instances are equivalent
        assert analyzed_document_model == analyzed_document_model2

        # Convert model instance back to dict and verify no loss of data
        analyzed_document_model_json2 = analyzed_document_model.to_dict()
        assert analyzed_document_model_json2 == analyzed_document_model_json

class TestModel_AnalyzedResult():
    """
    Test Class for AnalyzedResult
    """

    def test_analyzed_result_serialization(self):
        """
        Test serialization/deserialization for AnalyzedResult
        """

        # Construct a json representation of a AnalyzedResult model
        analyzed_result_model_json = {}
        analyzed_result_model_json['metadata'] = {'foo': 'bar'}
        analyzed_result_model_json['foo'] = 'testString'

        # Construct a model instance of AnalyzedResult by calling from_dict on the json representation
        analyzed_result_model = AnalyzedResult.from_dict(analyzed_result_model_json)
        assert analyzed_result_model != False

        # Construct a model instance of AnalyzedResult by calling from_dict on the json representation
        analyzed_result_model_dict = AnalyzedResult.from_dict(analyzed_result_model_json).__dict__
        analyzed_result_model2 = AnalyzedResult(**analyzed_result_model_dict)

        # Verify the model instances are equivalent
        assert analyzed_result_model == analyzed_result_model2

        # Convert model instance back to dict and verify no loss of data
        analyzed_result_model_json2 = analyzed_result_model.to_dict()
        assert analyzed_result_model_json2 == analyzed_result_model_json

        # Test get_properties and set_properties methods.
        analyzed_result_model.set_properties({})
        actual_dict = analyzed_result_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        analyzed_result_model.set_properties(expected_dict)
        actual_dict = analyzed_result_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_ClassifierFederatedModel():
    """
    Test Class for ClassifierFederatedModel
    """

    def test_classifier_federated_model_serialization(self):
        """
        Test serialization/deserialization for ClassifierFederatedModel
        """

        # Construct a json representation of a ClassifierFederatedModel model
        classifier_federated_model_model_json = {}
        classifier_federated_model_model_json['field'] = 'testString'

        # Construct a model instance of ClassifierFederatedModel by calling from_dict on the json representation
        classifier_federated_model_model = ClassifierFederatedModel.from_dict(classifier_federated_model_model_json)
        assert classifier_federated_model_model != False

        # Construct a model instance of ClassifierFederatedModel by calling from_dict on the json representation
        classifier_federated_model_model_dict = ClassifierFederatedModel.from_dict(classifier_federated_model_model_json).__dict__
        classifier_federated_model_model2 = ClassifierFederatedModel(**classifier_federated_model_model_dict)

        # Verify the model instances are equivalent
        assert classifier_federated_model_model == classifier_federated_model_model2

        # Convert model instance back to dict and verify no loss of data
        classifier_federated_model_model_json2 = classifier_federated_model_model.to_dict()
        assert classifier_federated_model_model_json2 == classifier_federated_model_model_json

class TestModel_ClassifierModelEvaluation():
    """
    Test Class for ClassifierModelEvaluation
    """

    def test_classifier_model_evaluation_serialization(self):
        """
        Test serialization/deserialization for ClassifierModelEvaluation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        model_evaluation_micro_average_model = {} # ModelEvaluationMicroAverage
        model_evaluation_micro_average_model['precision'] = 0
        model_evaluation_micro_average_model['recall'] = 0
        model_evaluation_micro_average_model['f1'] = 0

        model_evaluation_macro_average_model = {} # ModelEvaluationMacroAverage
        model_evaluation_macro_average_model['precision'] = 0
        model_evaluation_macro_average_model['recall'] = 0
        model_evaluation_macro_average_model['f1'] = 0

        per_class_model_evaluation_model = {} # PerClassModelEvaluation
        per_class_model_evaluation_model['name'] = 'testString'
        per_class_model_evaluation_model['precision'] = 0
        per_class_model_evaluation_model['recall'] = 0
        per_class_model_evaluation_model['f1'] = 0

        # Construct a json representation of a ClassifierModelEvaluation model
        classifier_model_evaluation_model_json = {}
        classifier_model_evaluation_model_json['micro_average'] = model_evaluation_micro_average_model
        classifier_model_evaluation_model_json['macro_average'] = model_evaluation_macro_average_model
        classifier_model_evaluation_model_json['per_class'] = [per_class_model_evaluation_model]

        # Construct a model instance of ClassifierModelEvaluation by calling from_dict on the json representation
        classifier_model_evaluation_model = ClassifierModelEvaluation.from_dict(classifier_model_evaluation_model_json)
        assert classifier_model_evaluation_model != False

        # Construct a model instance of ClassifierModelEvaluation by calling from_dict on the json representation
        classifier_model_evaluation_model_dict = ClassifierModelEvaluation.from_dict(classifier_model_evaluation_model_json).__dict__
        classifier_model_evaluation_model2 = ClassifierModelEvaluation(**classifier_model_evaluation_model_dict)

        # Verify the model instances are equivalent
        assert classifier_model_evaluation_model == classifier_model_evaluation_model2

        # Convert model instance back to dict and verify no loss of data
        classifier_model_evaluation_model_json2 = classifier_model_evaluation_model.to_dict()
        assert classifier_model_evaluation_model_json2 == classifier_model_evaluation_model_json

class TestModel_Collection():
    """
    Test Class for Collection
    """

    def test_collection_serialization(self):
        """
        Test serialization/deserialization for Collection
        """

        # Construct a json representation of a Collection model
        collection_model_json = {}
        collection_model_json['name'] = 'testString'

        # Construct a model instance of Collection by calling from_dict on the json representation
        collection_model = Collection.from_dict(collection_model_json)
        assert collection_model != False

        # Construct a model instance of Collection by calling from_dict on the json representation
        collection_model_dict = Collection.from_dict(collection_model_json).__dict__
        collection_model2 = Collection(**collection_model_dict)

        # Verify the model instances are equivalent
        assert collection_model == collection_model2

        # Convert model instance back to dict and verify no loss of data
        collection_model_json2 = collection_model.to_dict()
        assert collection_model_json2 == collection_model_json

class TestModel_CollectionDetails():
    """
    Test Class for CollectionDetails
    """

    def test_collection_details_serialization(self):
        """
        Test serialization/deserialization for CollectionDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        collection_enrichment_model = {} # CollectionEnrichment
        collection_enrichment_model['enrichment_id'] = 'testString'
        collection_enrichment_model['fields'] = ['testString']

        # Construct a json representation of a CollectionDetails model
        collection_details_model_json = {}
        collection_details_model_json['name'] = 'testString'
        collection_details_model_json['description'] = 'testString'
        collection_details_model_json['language'] = 'en'
        collection_details_model_json['enrichments'] = [collection_enrichment_model]

        # Construct a model instance of CollectionDetails by calling from_dict on the json representation
        collection_details_model = CollectionDetails.from_dict(collection_details_model_json)
        assert collection_details_model != False

        # Construct a model instance of CollectionDetails by calling from_dict on the json representation
        collection_details_model_dict = CollectionDetails.from_dict(collection_details_model_json).__dict__
        collection_details_model2 = CollectionDetails(**collection_details_model_dict)

        # Verify the model instances are equivalent
        assert collection_details_model == collection_details_model2

        # Convert model instance back to dict and verify no loss of data
        collection_details_model_json2 = collection_details_model.to_dict()
        assert collection_details_model_json2 == collection_details_model_json

class TestModel_CollectionDetailsSmartDocumentUnderstanding():
    """
    Test Class for CollectionDetailsSmartDocumentUnderstanding
    """

    def test_collection_details_smart_document_understanding_serialization(self):
        """
        Test serialization/deserialization for CollectionDetailsSmartDocumentUnderstanding
        """

        # Construct a json representation of a CollectionDetailsSmartDocumentUnderstanding model
        collection_details_smart_document_understanding_model_json = {}
        collection_details_smart_document_understanding_model_json['enabled'] = True
        collection_details_smart_document_understanding_model_json['model'] = 'custom'

        # Construct a model instance of CollectionDetailsSmartDocumentUnderstanding by calling from_dict on the json representation
        collection_details_smart_document_understanding_model = CollectionDetailsSmartDocumentUnderstanding.from_dict(collection_details_smart_document_understanding_model_json)
        assert collection_details_smart_document_understanding_model != False

        # Construct a model instance of CollectionDetailsSmartDocumentUnderstanding by calling from_dict on the json representation
        collection_details_smart_document_understanding_model_dict = CollectionDetailsSmartDocumentUnderstanding.from_dict(collection_details_smart_document_understanding_model_json).__dict__
        collection_details_smart_document_understanding_model2 = CollectionDetailsSmartDocumentUnderstanding(**collection_details_smart_document_understanding_model_dict)

        # Verify the model instances are equivalent
        assert collection_details_smart_document_understanding_model == collection_details_smart_document_understanding_model2

        # Convert model instance back to dict and verify no loss of data
        collection_details_smart_document_understanding_model_json2 = collection_details_smart_document_understanding_model.to_dict()
        assert collection_details_smart_document_understanding_model_json2 == collection_details_smart_document_understanding_model_json

class TestModel_CollectionEnrichment():
    """
    Test Class for CollectionEnrichment
    """

    def test_collection_enrichment_serialization(self):
        """
        Test serialization/deserialization for CollectionEnrichment
        """

        # Construct a json representation of a CollectionEnrichment model
        collection_enrichment_model_json = {}
        collection_enrichment_model_json['enrichment_id'] = 'testString'
        collection_enrichment_model_json['fields'] = ['testString']

        # Construct a model instance of CollectionEnrichment by calling from_dict on the json representation
        collection_enrichment_model = CollectionEnrichment.from_dict(collection_enrichment_model_json)
        assert collection_enrichment_model != False

        # Construct a model instance of CollectionEnrichment by calling from_dict on the json representation
        collection_enrichment_model_dict = CollectionEnrichment.from_dict(collection_enrichment_model_json).__dict__
        collection_enrichment_model2 = CollectionEnrichment(**collection_enrichment_model_dict)

        # Verify the model instances are equivalent
        assert collection_enrichment_model == collection_enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        collection_enrichment_model_json2 = collection_enrichment_model.to_dict()
        assert collection_enrichment_model_json2 == collection_enrichment_model_json

class TestModel_Completions():
    """
    Test Class for Completions
    """

    def test_completions_serialization(self):
        """
        Test serialization/deserialization for Completions
        """

        # Construct a json representation of a Completions model
        completions_model_json = {}
        completions_model_json['completions'] = ['testString']

        # Construct a model instance of Completions by calling from_dict on the json representation
        completions_model = Completions.from_dict(completions_model_json)
        assert completions_model != False

        # Construct a model instance of Completions by calling from_dict on the json representation
        completions_model_dict = Completions.from_dict(completions_model_json).__dict__
        completions_model2 = Completions(**completions_model_dict)

        # Verify the model instances are equivalent
        assert completions_model == completions_model2

        # Convert model instance back to dict and verify no loss of data
        completions_model_json2 = completions_model.to_dict()
        assert completions_model_json2 == completions_model_json

class TestModel_ComponentSettingsAggregation():
    """
    Test Class for ComponentSettingsAggregation
    """

    def test_component_settings_aggregation_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsAggregation
        """

        # Construct a json representation of a ComponentSettingsAggregation model
        component_settings_aggregation_model_json = {}
        component_settings_aggregation_model_json['name'] = 'testString'
        component_settings_aggregation_model_json['label'] = 'testString'
        component_settings_aggregation_model_json['multiple_selections_allowed'] = True
        component_settings_aggregation_model_json['visualization_type'] = 'auto'

        # Construct a model instance of ComponentSettingsAggregation by calling from_dict on the json representation
        component_settings_aggregation_model = ComponentSettingsAggregation.from_dict(component_settings_aggregation_model_json)
        assert component_settings_aggregation_model != False

        # Construct a model instance of ComponentSettingsAggregation by calling from_dict on the json representation
        component_settings_aggregation_model_dict = ComponentSettingsAggregation.from_dict(component_settings_aggregation_model_json).__dict__
        component_settings_aggregation_model2 = ComponentSettingsAggregation(**component_settings_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_aggregation_model == component_settings_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_aggregation_model_json2 = component_settings_aggregation_model.to_dict()
        assert component_settings_aggregation_model_json2 == component_settings_aggregation_model_json

class TestModel_ComponentSettingsFieldsShown():
    """
    Test Class for ComponentSettingsFieldsShown
    """

    def test_component_settings_fields_shown_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsFieldsShown
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_settings_fields_shown_body_model = {} # ComponentSettingsFieldsShownBody
        component_settings_fields_shown_body_model['use_passage'] = True
        component_settings_fields_shown_body_model['field'] = 'testString'

        component_settings_fields_shown_title_model = {} # ComponentSettingsFieldsShownTitle
        component_settings_fields_shown_title_model['field'] = 'testString'

        # Construct a json representation of a ComponentSettingsFieldsShown model
        component_settings_fields_shown_model_json = {}
        component_settings_fields_shown_model_json['body'] = component_settings_fields_shown_body_model
        component_settings_fields_shown_model_json['title'] = component_settings_fields_shown_title_model

        # Construct a model instance of ComponentSettingsFieldsShown by calling from_dict on the json representation
        component_settings_fields_shown_model = ComponentSettingsFieldsShown.from_dict(component_settings_fields_shown_model_json)
        assert component_settings_fields_shown_model != False

        # Construct a model instance of ComponentSettingsFieldsShown by calling from_dict on the json representation
        component_settings_fields_shown_model_dict = ComponentSettingsFieldsShown.from_dict(component_settings_fields_shown_model_json).__dict__
        component_settings_fields_shown_model2 = ComponentSettingsFieldsShown(**component_settings_fields_shown_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_fields_shown_model == component_settings_fields_shown_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_fields_shown_model_json2 = component_settings_fields_shown_model.to_dict()
        assert component_settings_fields_shown_model_json2 == component_settings_fields_shown_model_json

class TestModel_ComponentSettingsFieldsShownBody():
    """
    Test Class for ComponentSettingsFieldsShownBody
    """

    def test_component_settings_fields_shown_body_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsFieldsShownBody
        """

        # Construct a json representation of a ComponentSettingsFieldsShownBody model
        component_settings_fields_shown_body_model_json = {}
        component_settings_fields_shown_body_model_json['use_passage'] = True
        component_settings_fields_shown_body_model_json['field'] = 'testString'

        # Construct a model instance of ComponentSettingsFieldsShownBody by calling from_dict on the json representation
        component_settings_fields_shown_body_model = ComponentSettingsFieldsShownBody.from_dict(component_settings_fields_shown_body_model_json)
        assert component_settings_fields_shown_body_model != False

        # Construct a model instance of ComponentSettingsFieldsShownBody by calling from_dict on the json representation
        component_settings_fields_shown_body_model_dict = ComponentSettingsFieldsShownBody.from_dict(component_settings_fields_shown_body_model_json).__dict__
        component_settings_fields_shown_body_model2 = ComponentSettingsFieldsShownBody(**component_settings_fields_shown_body_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_fields_shown_body_model == component_settings_fields_shown_body_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_fields_shown_body_model_json2 = component_settings_fields_shown_body_model.to_dict()
        assert component_settings_fields_shown_body_model_json2 == component_settings_fields_shown_body_model_json

class TestModel_ComponentSettingsFieldsShownTitle():
    """
    Test Class for ComponentSettingsFieldsShownTitle
    """

    def test_component_settings_fields_shown_title_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsFieldsShownTitle
        """

        # Construct a json representation of a ComponentSettingsFieldsShownTitle model
        component_settings_fields_shown_title_model_json = {}
        component_settings_fields_shown_title_model_json['field'] = 'testString'

        # Construct a model instance of ComponentSettingsFieldsShownTitle by calling from_dict on the json representation
        component_settings_fields_shown_title_model = ComponentSettingsFieldsShownTitle.from_dict(component_settings_fields_shown_title_model_json)
        assert component_settings_fields_shown_title_model != False

        # Construct a model instance of ComponentSettingsFieldsShownTitle by calling from_dict on the json representation
        component_settings_fields_shown_title_model_dict = ComponentSettingsFieldsShownTitle.from_dict(component_settings_fields_shown_title_model_json).__dict__
        component_settings_fields_shown_title_model2 = ComponentSettingsFieldsShownTitle(**component_settings_fields_shown_title_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_fields_shown_title_model == component_settings_fields_shown_title_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_fields_shown_title_model_json2 = component_settings_fields_shown_title_model.to_dict()
        assert component_settings_fields_shown_title_model_json2 == component_settings_fields_shown_title_model_json

class TestModel_ComponentSettingsResponse():
    """
    Test Class for ComponentSettingsResponse
    """

    def test_component_settings_response_serialization(self):
        """
        Test serialization/deserialization for ComponentSettingsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        component_settings_fields_shown_body_model = {} # ComponentSettingsFieldsShownBody
        component_settings_fields_shown_body_model['use_passage'] = True
        component_settings_fields_shown_body_model['field'] = 'testString'

        component_settings_fields_shown_title_model = {} # ComponentSettingsFieldsShownTitle
        component_settings_fields_shown_title_model['field'] = 'testString'

        component_settings_fields_shown_model = {} # ComponentSettingsFieldsShown
        component_settings_fields_shown_model['body'] = component_settings_fields_shown_body_model
        component_settings_fields_shown_model['title'] = component_settings_fields_shown_title_model

        component_settings_aggregation_model = {} # ComponentSettingsAggregation
        component_settings_aggregation_model['name'] = 'testString'
        component_settings_aggregation_model['label'] = 'testString'
        component_settings_aggregation_model['multiple_selections_allowed'] = True
        component_settings_aggregation_model['visualization_type'] = 'auto'

        # Construct a json representation of a ComponentSettingsResponse model
        component_settings_response_model_json = {}
        component_settings_response_model_json['fields_shown'] = component_settings_fields_shown_model
        component_settings_response_model_json['autocomplete'] = True
        component_settings_response_model_json['structured_search'] = True
        component_settings_response_model_json['results_per_page'] = 38
        component_settings_response_model_json['aggregations'] = [component_settings_aggregation_model]

        # Construct a model instance of ComponentSettingsResponse by calling from_dict on the json representation
        component_settings_response_model = ComponentSettingsResponse.from_dict(component_settings_response_model_json)
        assert component_settings_response_model != False

        # Construct a model instance of ComponentSettingsResponse by calling from_dict on the json representation
        component_settings_response_model_dict = ComponentSettingsResponse.from_dict(component_settings_response_model_json).__dict__
        component_settings_response_model2 = ComponentSettingsResponse(**component_settings_response_model_dict)

        # Verify the model instances are equivalent
        assert component_settings_response_model == component_settings_response_model2

        # Convert model instance back to dict and verify no loss of data
        component_settings_response_model_json2 = component_settings_response_model.to_dict()
        assert component_settings_response_model_json2 == component_settings_response_model_json

class TestModel_CreateDocumentClassifier():
    """
    Test Class for CreateDocumentClassifier
    """

    def test_create_document_classifier_serialization(self):
        """
        Test serialization/deserialization for CreateDocumentClassifier
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_classifier_enrichment_model = {} # DocumentClassifierEnrichment
        document_classifier_enrichment_model['enrichment_id'] = 'testString'
        document_classifier_enrichment_model['fields'] = ['testString']

        classifier_federated_model_model = {} # ClassifierFederatedModel
        classifier_federated_model_model['field'] = 'testString'

        # Construct a json representation of a CreateDocumentClassifier model
        create_document_classifier_model_json = {}
        create_document_classifier_model_json['name'] = 'testString'
        create_document_classifier_model_json['description'] = 'testString'
        create_document_classifier_model_json['language'] = 'en'
        create_document_classifier_model_json['answer_field'] = 'testString'
        create_document_classifier_model_json['enrichments'] = [document_classifier_enrichment_model]
        create_document_classifier_model_json['federated_classification'] = classifier_federated_model_model

        # Construct a model instance of CreateDocumentClassifier by calling from_dict on the json representation
        create_document_classifier_model = CreateDocumentClassifier.from_dict(create_document_classifier_model_json)
        assert create_document_classifier_model != False

        # Construct a model instance of CreateDocumentClassifier by calling from_dict on the json representation
        create_document_classifier_model_dict = CreateDocumentClassifier.from_dict(create_document_classifier_model_json).__dict__
        create_document_classifier_model2 = CreateDocumentClassifier(**create_document_classifier_model_dict)

        # Verify the model instances are equivalent
        assert create_document_classifier_model == create_document_classifier_model2

        # Convert model instance back to dict and verify no loss of data
        create_document_classifier_model_json2 = create_document_classifier_model.to_dict()
        assert create_document_classifier_model_json2 == create_document_classifier_model_json

class TestModel_CreateEnrichment():
    """
    Test Class for CreateEnrichment
    """

    def test_create_enrichment_serialization(self):
        """
        Test serialization/deserialization for CreateEnrichment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'
        enrichment_options_model['classifier_id'] = 'testString'
        enrichment_options_model['model_id'] = 'testString'
        enrichment_options_model['confidence_threshold'] = 0
        enrichment_options_model['top_k'] = 38

        # Construct a json representation of a CreateEnrichment model
        create_enrichment_model_json = {}
        create_enrichment_model_json['name'] = 'testString'
        create_enrichment_model_json['description'] = 'testString'
        create_enrichment_model_json['type'] = 'classifier'
        create_enrichment_model_json['options'] = enrichment_options_model

        # Construct a model instance of CreateEnrichment by calling from_dict on the json representation
        create_enrichment_model = CreateEnrichment.from_dict(create_enrichment_model_json)
        assert create_enrichment_model != False

        # Construct a model instance of CreateEnrichment by calling from_dict on the json representation
        create_enrichment_model_dict = CreateEnrichment.from_dict(create_enrichment_model_json).__dict__
        create_enrichment_model2 = CreateEnrichment(**create_enrichment_model_dict)

        # Verify the model instances are equivalent
        assert create_enrichment_model == create_enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        create_enrichment_model_json2 = create_enrichment_model.to_dict()
        assert create_enrichment_model_json2 == create_enrichment_model_json

class TestModel_DefaultQueryParams():
    """
    Test Class for DefaultQueryParams
    """

    def test_default_query_params_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParams
        """

        # Construct dict forms of any model objects needed in order to build this model.

        default_query_params_passages_model = {} # DefaultQueryParamsPassages
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        default_query_params_table_results_model = {} # DefaultQueryParamsTableResults
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        default_query_params_suggested_refinements_model = {} # DefaultQueryParamsSuggestedRefinements
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        # Construct a json representation of a DefaultQueryParams model
        default_query_params_model_json = {}
        default_query_params_model_json['collection_ids'] = ['testString']
        default_query_params_model_json['passages'] = default_query_params_passages_model
        default_query_params_model_json['table_results'] = default_query_params_table_results_model
        default_query_params_model_json['aggregation'] = 'testString'
        default_query_params_model_json['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model_json['spelling_suggestions'] = True
        default_query_params_model_json['highlight'] = True
        default_query_params_model_json['count'] = 38
        default_query_params_model_json['sort'] = 'testString'
        default_query_params_model_json['return'] = ['testString']

        # Construct a model instance of DefaultQueryParams by calling from_dict on the json representation
        default_query_params_model = DefaultQueryParams.from_dict(default_query_params_model_json)
        assert default_query_params_model != False

        # Construct a model instance of DefaultQueryParams by calling from_dict on the json representation
        default_query_params_model_dict = DefaultQueryParams.from_dict(default_query_params_model_json).__dict__
        default_query_params_model2 = DefaultQueryParams(**default_query_params_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_model == default_query_params_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_model_json2 = default_query_params_model.to_dict()
        assert default_query_params_model_json2 == default_query_params_model_json

class TestModel_DefaultQueryParamsPassages():
    """
    Test Class for DefaultQueryParamsPassages
    """

    def test_default_query_params_passages_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParamsPassages
        """

        # Construct a json representation of a DefaultQueryParamsPassages model
        default_query_params_passages_model_json = {}
        default_query_params_passages_model_json['enabled'] = True
        default_query_params_passages_model_json['count'] = 38
        default_query_params_passages_model_json['fields'] = ['testString']
        default_query_params_passages_model_json['characters'] = 38
        default_query_params_passages_model_json['per_document'] = True
        default_query_params_passages_model_json['max_per_document'] = 38

        # Construct a model instance of DefaultQueryParamsPassages by calling from_dict on the json representation
        default_query_params_passages_model = DefaultQueryParamsPassages.from_dict(default_query_params_passages_model_json)
        assert default_query_params_passages_model != False

        # Construct a model instance of DefaultQueryParamsPassages by calling from_dict on the json representation
        default_query_params_passages_model_dict = DefaultQueryParamsPassages.from_dict(default_query_params_passages_model_json).__dict__
        default_query_params_passages_model2 = DefaultQueryParamsPassages(**default_query_params_passages_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_passages_model == default_query_params_passages_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_passages_model_json2 = default_query_params_passages_model.to_dict()
        assert default_query_params_passages_model_json2 == default_query_params_passages_model_json

class TestModel_DefaultQueryParamsSuggestedRefinements():
    """
    Test Class for DefaultQueryParamsSuggestedRefinements
    """

    def test_default_query_params_suggested_refinements_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParamsSuggestedRefinements
        """

        # Construct a json representation of a DefaultQueryParamsSuggestedRefinements model
        default_query_params_suggested_refinements_model_json = {}
        default_query_params_suggested_refinements_model_json['enabled'] = True
        default_query_params_suggested_refinements_model_json['count'] = 38

        # Construct a model instance of DefaultQueryParamsSuggestedRefinements by calling from_dict on the json representation
        default_query_params_suggested_refinements_model = DefaultQueryParamsSuggestedRefinements.from_dict(default_query_params_suggested_refinements_model_json)
        assert default_query_params_suggested_refinements_model != False

        # Construct a model instance of DefaultQueryParamsSuggestedRefinements by calling from_dict on the json representation
        default_query_params_suggested_refinements_model_dict = DefaultQueryParamsSuggestedRefinements.from_dict(default_query_params_suggested_refinements_model_json).__dict__
        default_query_params_suggested_refinements_model2 = DefaultQueryParamsSuggestedRefinements(**default_query_params_suggested_refinements_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_suggested_refinements_model == default_query_params_suggested_refinements_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_suggested_refinements_model_json2 = default_query_params_suggested_refinements_model.to_dict()
        assert default_query_params_suggested_refinements_model_json2 == default_query_params_suggested_refinements_model_json

class TestModel_DefaultQueryParamsTableResults():
    """
    Test Class for DefaultQueryParamsTableResults
    """

    def test_default_query_params_table_results_serialization(self):
        """
        Test serialization/deserialization for DefaultQueryParamsTableResults
        """

        # Construct a json representation of a DefaultQueryParamsTableResults model
        default_query_params_table_results_model_json = {}
        default_query_params_table_results_model_json['enabled'] = True
        default_query_params_table_results_model_json['count'] = 38
        default_query_params_table_results_model_json['per_document'] = 38

        # Construct a model instance of DefaultQueryParamsTableResults by calling from_dict on the json representation
        default_query_params_table_results_model = DefaultQueryParamsTableResults.from_dict(default_query_params_table_results_model_json)
        assert default_query_params_table_results_model != False

        # Construct a model instance of DefaultQueryParamsTableResults by calling from_dict on the json representation
        default_query_params_table_results_model_dict = DefaultQueryParamsTableResults.from_dict(default_query_params_table_results_model_json).__dict__
        default_query_params_table_results_model2 = DefaultQueryParamsTableResults(**default_query_params_table_results_model_dict)

        # Verify the model instances are equivalent
        assert default_query_params_table_results_model == default_query_params_table_results_model2

        # Convert model instance back to dict and verify no loss of data
        default_query_params_table_results_model_json2 = default_query_params_table_results_model.to_dict()
        assert default_query_params_table_results_model_json2 == default_query_params_table_results_model_json

class TestModel_DeleteDocumentResponse():
    """
    Test Class for DeleteDocumentResponse
    """

    def test_delete_document_response_serialization(self):
        """
        Test serialization/deserialization for DeleteDocumentResponse
        """

        # Construct a json representation of a DeleteDocumentResponse model
        delete_document_response_model_json = {}
        delete_document_response_model_json['document_id'] = 'testString'
        delete_document_response_model_json['status'] = 'deleted'

        # Construct a model instance of DeleteDocumentResponse by calling from_dict on the json representation
        delete_document_response_model = DeleteDocumentResponse.from_dict(delete_document_response_model_json)
        assert delete_document_response_model != False

        # Construct a model instance of DeleteDocumentResponse by calling from_dict on the json representation
        delete_document_response_model_dict = DeleteDocumentResponse.from_dict(delete_document_response_model_json).__dict__
        delete_document_response_model2 = DeleteDocumentResponse(**delete_document_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_document_response_model == delete_document_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_document_response_model_json2 = delete_document_response_model.to_dict()
        assert delete_document_response_model_json2 == delete_document_response_model_json

class TestModel_DocumentAccepted():
    """
    Test Class for DocumentAccepted
    """

    def test_document_accepted_serialization(self):
        """
        Test serialization/deserialization for DocumentAccepted
        """

        # Construct a json representation of a DocumentAccepted model
        document_accepted_model_json = {}
        document_accepted_model_json['document_id'] = 'testString'
        document_accepted_model_json['status'] = 'processing'

        # Construct a model instance of DocumentAccepted by calling from_dict on the json representation
        document_accepted_model = DocumentAccepted.from_dict(document_accepted_model_json)
        assert document_accepted_model != False

        # Construct a model instance of DocumentAccepted by calling from_dict on the json representation
        document_accepted_model_dict = DocumentAccepted.from_dict(document_accepted_model_json).__dict__
        document_accepted_model2 = DocumentAccepted(**document_accepted_model_dict)

        # Verify the model instances are equivalent
        assert document_accepted_model == document_accepted_model2

        # Convert model instance back to dict and verify no loss of data
        document_accepted_model_json2 = document_accepted_model.to_dict()
        assert document_accepted_model_json2 == document_accepted_model_json

class TestModel_DocumentAttribute():
    """
    Test Class for DocumentAttribute
    """

    def test_document_attribute_serialization(self):
        """
        Test serialization/deserialization for DocumentAttribute
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a DocumentAttribute model
        document_attribute_model_json = {}
        document_attribute_model_json['type'] = 'testString'
        document_attribute_model_json['text'] = 'testString'
        document_attribute_model_json['location'] = table_element_location_model

        # Construct a model instance of DocumentAttribute by calling from_dict on the json representation
        document_attribute_model = DocumentAttribute.from_dict(document_attribute_model_json)
        assert document_attribute_model != False

        # Construct a model instance of DocumentAttribute by calling from_dict on the json representation
        document_attribute_model_dict = DocumentAttribute.from_dict(document_attribute_model_json).__dict__
        document_attribute_model2 = DocumentAttribute(**document_attribute_model_dict)

        # Verify the model instances are equivalent
        assert document_attribute_model == document_attribute_model2

        # Convert model instance back to dict and verify no loss of data
        document_attribute_model_json2 = document_attribute_model.to_dict()
        assert document_attribute_model_json2 == document_attribute_model_json

class TestModel_DocumentClassifier():
    """
    Test Class for DocumentClassifier
    """

    def test_document_classifier_serialization(self):
        """
        Test serialization/deserialization for DocumentClassifier
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_classifier_enrichment_model = {} # DocumentClassifierEnrichment
        document_classifier_enrichment_model['enrichment_id'] = 'testString'
        document_classifier_enrichment_model['fields'] = ['testString']

        classifier_federated_model_model = {} # ClassifierFederatedModel
        classifier_federated_model_model['field'] = 'testString'

        # Construct a json representation of a DocumentClassifier model
        document_classifier_model_json = {}
        document_classifier_model_json['name'] = 'testString'
        document_classifier_model_json['description'] = 'testString'
        document_classifier_model_json['language'] = 'en'
        document_classifier_model_json['enrichments'] = [document_classifier_enrichment_model]
        document_classifier_model_json['recognized_fields'] = ['testString']
        document_classifier_model_json['answer_field'] = 'testString'
        document_classifier_model_json['training_data_file'] = 'testString'
        document_classifier_model_json['test_data_file'] = 'testString'
        document_classifier_model_json['federated_classification'] = classifier_federated_model_model

        # Construct a model instance of DocumentClassifier by calling from_dict on the json representation
        document_classifier_model = DocumentClassifier.from_dict(document_classifier_model_json)
        assert document_classifier_model != False

        # Construct a model instance of DocumentClassifier by calling from_dict on the json representation
        document_classifier_model_dict = DocumentClassifier.from_dict(document_classifier_model_json).__dict__
        document_classifier_model2 = DocumentClassifier(**document_classifier_model_dict)

        # Verify the model instances are equivalent
        assert document_classifier_model == document_classifier_model2

        # Convert model instance back to dict and verify no loss of data
        document_classifier_model_json2 = document_classifier_model.to_dict()
        assert document_classifier_model_json2 == document_classifier_model_json

class TestModel_DocumentClassifierEnrichment():
    """
    Test Class for DocumentClassifierEnrichment
    """

    def test_document_classifier_enrichment_serialization(self):
        """
        Test serialization/deserialization for DocumentClassifierEnrichment
        """

        # Construct a json representation of a DocumentClassifierEnrichment model
        document_classifier_enrichment_model_json = {}
        document_classifier_enrichment_model_json['enrichment_id'] = 'testString'
        document_classifier_enrichment_model_json['fields'] = ['testString']

        # Construct a model instance of DocumentClassifierEnrichment by calling from_dict on the json representation
        document_classifier_enrichment_model = DocumentClassifierEnrichment.from_dict(document_classifier_enrichment_model_json)
        assert document_classifier_enrichment_model != False

        # Construct a model instance of DocumentClassifierEnrichment by calling from_dict on the json representation
        document_classifier_enrichment_model_dict = DocumentClassifierEnrichment.from_dict(document_classifier_enrichment_model_json).__dict__
        document_classifier_enrichment_model2 = DocumentClassifierEnrichment(**document_classifier_enrichment_model_dict)

        # Verify the model instances are equivalent
        assert document_classifier_enrichment_model == document_classifier_enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        document_classifier_enrichment_model_json2 = document_classifier_enrichment_model.to_dict()
        assert document_classifier_enrichment_model_json2 == document_classifier_enrichment_model_json

class TestModel_DocumentClassifierModel():
    """
    Test Class for DocumentClassifierModel
    """

    def test_document_classifier_model_serialization(self):
        """
        Test serialization/deserialization for DocumentClassifierModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        model_evaluation_micro_average_model = {} # ModelEvaluationMicroAverage
        model_evaluation_micro_average_model['precision'] = 0
        model_evaluation_micro_average_model['recall'] = 0
        model_evaluation_micro_average_model['f1'] = 0

        model_evaluation_macro_average_model = {} # ModelEvaluationMacroAverage
        model_evaluation_macro_average_model['precision'] = 0
        model_evaluation_macro_average_model['recall'] = 0
        model_evaluation_macro_average_model['f1'] = 0

        per_class_model_evaluation_model = {} # PerClassModelEvaluation
        per_class_model_evaluation_model['name'] = 'testString'
        per_class_model_evaluation_model['precision'] = 0
        per_class_model_evaluation_model['recall'] = 0
        per_class_model_evaluation_model['f1'] = 0

        classifier_model_evaluation_model = {} # ClassifierModelEvaluation
        classifier_model_evaluation_model['micro_average'] = model_evaluation_micro_average_model
        classifier_model_evaluation_model['macro_average'] = model_evaluation_macro_average_model
        classifier_model_evaluation_model['per_class'] = [per_class_model_evaluation_model]

        # Construct a json representation of a DocumentClassifierModel model
        document_classifier_model_model_json = {}
        document_classifier_model_model_json['name'] = 'testString'
        document_classifier_model_model_json['description'] = 'testString'
        document_classifier_model_model_json['training_data_file'] = 'testString'
        document_classifier_model_model_json['test_data_file'] = 'testString'
        document_classifier_model_model_json['status'] = 'training'
        document_classifier_model_model_json['evaluation'] = classifier_model_evaluation_model
        document_classifier_model_model_json['enrichment_id'] = 'testString'

        # Construct a model instance of DocumentClassifierModel by calling from_dict on the json representation
        document_classifier_model_model = DocumentClassifierModel.from_dict(document_classifier_model_model_json)
        assert document_classifier_model_model != False

        # Construct a model instance of DocumentClassifierModel by calling from_dict on the json representation
        document_classifier_model_model_dict = DocumentClassifierModel.from_dict(document_classifier_model_model_json).__dict__
        document_classifier_model_model2 = DocumentClassifierModel(**document_classifier_model_model_dict)

        # Verify the model instances are equivalent
        assert document_classifier_model_model == document_classifier_model_model2

        # Convert model instance back to dict and verify no loss of data
        document_classifier_model_model_json2 = document_classifier_model_model.to_dict()
        assert document_classifier_model_model_json2 == document_classifier_model_model_json

class TestModel_DocumentClassifierModels():
    """
    Test Class for DocumentClassifierModels
    """

    def test_document_classifier_models_serialization(self):
        """
        Test serialization/deserialization for DocumentClassifierModels
        """

        # Construct dict forms of any model objects needed in order to build this model.

        model_evaluation_micro_average_model = {} # ModelEvaluationMicroAverage
        model_evaluation_micro_average_model['precision'] = 0
        model_evaluation_micro_average_model['recall'] = 0
        model_evaluation_micro_average_model['f1'] = 0

        model_evaluation_macro_average_model = {} # ModelEvaluationMacroAverage
        model_evaluation_macro_average_model['precision'] = 0
        model_evaluation_macro_average_model['recall'] = 0
        model_evaluation_macro_average_model['f1'] = 0

        per_class_model_evaluation_model = {} # PerClassModelEvaluation
        per_class_model_evaluation_model['name'] = 'testString'
        per_class_model_evaluation_model['precision'] = 0
        per_class_model_evaluation_model['recall'] = 0
        per_class_model_evaluation_model['f1'] = 0

        classifier_model_evaluation_model = {} # ClassifierModelEvaluation
        classifier_model_evaluation_model['micro_average'] = model_evaluation_micro_average_model
        classifier_model_evaluation_model['macro_average'] = model_evaluation_macro_average_model
        classifier_model_evaluation_model['per_class'] = [per_class_model_evaluation_model]

        document_classifier_model_model = {} # DocumentClassifierModel
        document_classifier_model_model['name'] = 'testString'
        document_classifier_model_model['description'] = 'testString'
        document_classifier_model_model['training_data_file'] = 'testString'
        document_classifier_model_model['test_data_file'] = 'testString'
        document_classifier_model_model['status'] = 'training'
        document_classifier_model_model['evaluation'] = classifier_model_evaluation_model
        document_classifier_model_model['enrichment_id'] = 'testString'

        # Construct a json representation of a DocumentClassifierModels model
        document_classifier_models_model_json = {}
        document_classifier_models_model_json['models'] = [document_classifier_model_model]

        # Construct a model instance of DocumentClassifierModels by calling from_dict on the json representation
        document_classifier_models_model = DocumentClassifierModels.from_dict(document_classifier_models_model_json)
        assert document_classifier_models_model != False

        # Construct a model instance of DocumentClassifierModels by calling from_dict on the json representation
        document_classifier_models_model_dict = DocumentClassifierModels.from_dict(document_classifier_models_model_json).__dict__
        document_classifier_models_model2 = DocumentClassifierModels(**document_classifier_models_model_dict)

        # Verify the model instances are equivalent
        assert document_classifier_models_model == document_classifier_models_model2

        # Convert model instance back to dict and verify no loss of data
        document_classifier_models_model_json2 = document_classifier_models_model.to_dict()
        assert document_classifier_models_model_json2 == document_classifier_models_model_json

class TestModel_DocumentClassifiers():
    """
    Test Class for DocumentClassifiers
    """

    def test_document_classifiers_serialization(self):
        """
        Test serialization/deserialization for DocumentClassifiers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_classifier_enrichment_model = {} # DocumentClassifierEnrichment
        document_classifier_enrichment_model['enrichment_id'] = 'testString'
        document_classifier_enrichment_model['fields'] = ['testString']

        classifier_federated_model_model = {} # ClassifierFederatedModel
        classifier_federated_model_model['field'] = 'testString'

        document_classifier_model = {} # DocumentClassifier
        document_classifier_model['name'] = 'testString'
        document_classifier_model['description'] = 'testString'
        document_classifier_model['language'] = 'en'
        document_classifier_model['enrichments'] = [document_classifier_enrichment_model]
        document_classifier_model['recognized_fields'] = ['testString']
        document_classifier_model['answer_field'] = 'testString'
        document_classifier_model['training_data_file'] = 'testString'
        document_classifier_model['test_data_file'] = 'testString'
        document_classifier_model['federated_classification'] = classifier_federated_model_model

        # Construct a json representation of a DocumentClassifiers model
        document_classifiers_model_json = {}
        document_classifiers_model_json['classifiers'] = [document_classifier_model]

        # Construct a model instance of DocumentClassifiers by calling from_dict on the json representation
        document_classifiers_model = DocumentClassifiers.from_dict(document_classifiers_model_json)
        assert document_classifiers_model != False

        # Construct a model instance of DocumentClassifiers by calling from_dict on the json representation
        document_classifiers_model_dict = DocumentClassifiers.from_dict(document_classifiers_model_json).__dict__
        document_classifiers_model2 = DocumentClassifiers(**document_classifiers_model_dict)

        # Verify the model instances are equivalent
        assert document_classifiers_model == document_classifiers_model2

        # Convert model instance back to dict and verify no loss of data
        document_classifiers_model_json2 = document_classifiers_model.to_dict()
        assert document_classifiers_model_json2 == document_classifiers_model_json

class TestModel_DocumentDetails():
    """
    Test Class for DocumentDetails
    """

    def test_document_details_serialization(self):
        """
        Test serialization/deserialization for DocumentDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice

        document_details_children_model = {} # DocumentDetailsChildren
        document_details_children_model['have_notices'] = True
        document_details_children_model['count'] = 38

        # Construct a json representation of a DocumentDetails model
        document_details_model_json = {}
        document_details_model_json['status'] = 'available'
        document_details_model_json['notices'] = [notice_model]
        document_details_model_json['children'] = document_details_children_model
        document_details_model_json['filename'] = 'testString'
        document_details_model_json['file_type'] = 'testString'
        document_details_model_json['sha256'] = 'testString'

        # Construct a model instance of DocumentDetails by calling from_dict on the json representation
        document_details_model = DocumentDetails.from_dict(document_details_model_json)
        assert document_details_model != False

        # Construct a model instance of DocumentDetails by calling from_dict on the json representation
        document_details_model_dict = DocumentDetails.from_dict(document_details_model_json).__dict__
        document_details_model2 = DocumentDetails(**document_details_model_dict)

        # Verify the model instances are equivalent
        assert document_details_model == document_details_model2

        # Convert model instance back to dict and verify no loss of data
        document_details_model_json2 = document_details_model.to_dict()
        assert document_details_model_json2 == document_details_model_json

class TestModel_DocumentDetailsChildren():
    """
    Test Class for DocumentDetailsChildren
    """

    def test_document_details_children_serialization(self):
        """
        Test serialization/deserialization for DocumentDetailsChildren
        """

        # Construct a json representation of a DocumentDetailsChildren model
        document_details_children_model_json = {}
        document_details_children_model_json['have_notices'] = True
        document_details_children_model_json['count'] = 38

        # Construct a model instance of DocumentDetailsChildren by calling from_dict on the json representation
        document_details_children_model = DocumentDetailsChildren.from_dict(document_details_children_model_json)
        assert document_details_children_model != False

        # Construct a model instance of DocumentDetailsChildren by calling from_dict on the json representation
        document_details_children_model_dict = DocumentDetailsChildren.from_dict(document_details_children_model_json).__dict__
        document_details_children_model2 = DocumentDetailsChildren(**document_details_children_model_dict)

        # Verify the model instances are equivalent
        assert document_details_children_model == document_details_children_model2

        # Convert model instance back to dict and verify no loss of data
        document_details_children_model_json2 = document_details_children_model.to_dict()
        assert document_details_children_model_json2 == document_details_children_model_json

class TestModel_Enrichment():
    """
    Test Class for Enrichment
    """

    def test_enrichment_serialization(self):
        """
        Test serialization/deserialization for Enrichment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'
        enrichment_options_model['classifier_id'] = 'testString'
        enrichment_options_model['model_id'] = 'testString'
        enrichment_options_model['confidence_threshold'] = 0
        enrichment_options_model['top_k'] = 38

        # Construct a json representation of a Enrichment model
        enrichment_model_json = {}
        enrichment_model_json['name'] = 'testString'
        enrichment_model_json['description'] = 'testString'
        enrichment_model_json['type'] = 'part_of_speech'
        enrichment_model_json['options'] = enrichment_options_model

        # Construct a model instance of Enrichment by calling from_dict on the json representation
        enrichment_model = Enrichment.from_dict(enrichment_model_json)
        assert enrichment_model != False

        # Construct a model instance of Enrichment by calling from_dict on the json representation
        enrichment_model_dict = Enrichment.from_dict(enrichment_model_json).__dict__
        enrichment_model2 = Enrichment(**enrichment_model_dict)

        # Verify the model instances are equivalent
        assert enrichment_model == enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        enrichment_model_json2 = enrichment_model.to_dict()
        assert enrichment_model_json2 == enrichment_model_json

class TestModel_EnrichmentOptions():
    """
    Test Class for EnrichmentOptions
    """

    def test_enrichment_options_serialization(self):
        """
        Test serialization/deserialization for EnrichmentOptions
        """

        # Construct a json representation of a EnrichmentOptions model
        enrichment_options_model_json = {}
        enrichment_options_model_json['languages'] = ['testString']
        enrichment_options_model_json['entity_type'] = 'testString'
        enrichment_options_model_json['regular_expression'] = 'testString'
        enrichment_options_model_json['result_field'] = 'testString'
        enrichment_options_model_json['classifier_id'] = 'testString'
        enrichment_options_model_json['model_id'] = 'testString'
        enrichment_options_model_json['confidence_threshold'] = 0
        enrichment_options_model_json['top_k'] = 38

        # Construct a model instance of EnrichmentOptions by calling from_dict on the json representation
        enrichment_options_model = EnrichmentOptions.from_dict(enrichment_options_model_json)
        assert enrichment_options_model != False

        # Construct a model instance of EnrichmentOptions by calling from_dict on the json representation
        enrichment_options_model_dict = EnrichmentOptions.from_dict(enrichment_options_model_json).__dict__
        enrichment_options_model2 = EnrichmentOptions(**enrichment_options_model_dict)

        # Verify the model instances are equivalent
        assert enrichment_options_model == enrichment_options_model2

        # Convert model instance back to dict and verify no loss of data
        enrichment_options_model_json2 = enrichment_options_model.to_dict()
        assert enrichment_options_model_json2 == enrichment_options_model_json

class TestModel_Enrichments():
    """
    Test Class for Enrichments
    """

    def test_enrichments_serialization(self):
        """
        Test serialization/deserialization for Enrichments
        """

        # Construct dict forms of any model objects needed in order to build this model.

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['languages'] = ['testString']
        enrichment_options_model['entity_type'] = 'testString'
        enrichment_options_model['regular_expression'] = 'testString'
        enrichment_options_model['result_field'] = 'testString'
        enrichment_options_model['classifier_id'] = 'testString'
        enrichment_options_model['model_id'] = 'testString'
        enrichment_options_model['confidence_threshold'] = 0
        enrichment_options_model['top_k'] = 38

        enrichment_model = {} # Enrichment
        enrichment_model['name'] = 'testString'
        enrichment_model['description'] = 'testString'
        enrichment_model['type'] = 'part_of_speech'
        enrichment_model['options'] = enrichment_options_model

        # Construct a json representation of a Enrichments model
        enrichments_model_json = {}
        enrichments_model_json['enrichments'] = [enrichment_model]

        # Construct a model instance of Enrichments by calling from_dict on the json representation
        enrichments_model = Enrichments.from_dict(enrichments_model_json)
        assert enrichments_model != False

        # Construct a model instance of Enrichments by calling from_dict on the json representation
        enrichments_model_dict = Enrichments.from_dict(enrichments_model_json).__dict__
        enrichments_model2 = Enrichments(**enrichments_model_dict)

        # Verify the model instances are equivalent
        assert enrichments_model == enrichments_model2

        # Convert model instance back to dict and verify no loss of data
        enrichments_model_json2 = enrichments_model.to_dict()
        assert enrichments_model_json2 == enrichments_model_json

class TestModel_Expansion():
    """
    Test Class for Expansion
    """

    def test_expansion_serialization(self):
        """
        Test serialization/deserialization for Expansion
        """

        # Construct a json representation of a Expansion model
        expansion_model_json = {}
        expansion_model_json['input_terms'] = ['testString']
        expansion_model_json['expanded_terms'] = ['testString']

        # Construct a model instance of Expansion by calling from_dict on the json representation
        expansion_model = Expansion.from_dict(expansion_model_json)
        assert expansion_model != False

        # Construct a model instance of Expansion by calling from_dict on the json representation
        expansion_model_dict = Expansion.from_dict(expansion_model_json).__dict__
        expansion_model2 = Expansion(**expansion_model_dict)

        # Verify the model instances are equivalent
        assert expansion_model == expansion_model2

        # Convert model instance back to dict and verify no loss of data
        expansion_model_json2 = expansion_model.to_dict()
        assert expansion_model_json2 == expansion_model_json

class TestModel_Expansions():
    """
    Test Class for Expansions
    """

    def test_expansions_serialization(self):
        """
        Test serialization/deserialization for Expansions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        expansion_model = {} # Expansion
        expansion_model['input_terms'] = ['testString']
        expansion_model['expanded_terms'] = ['testString']

        # Construct a json representation of a Expansions model
        expansions_model_json = {}
        expansions_model_json['expansions'] = [expansion_model]

        # Construct a model instance of Expansions by calling from_dict on the json representation
        expansions_model = Expansions.from_dict(expansions_model_json)
        assert expansions_model != False

        # Construct a model instance of Expansions by calling from_dict on the json representation
        expansions_model_dict = Expansions.from_dict(expansions_model_json).__dict__
        expansions_model2 = Expansions(**expansions_model_dict)

        # Verify the model instances are equivalent
        assert expansions_model == expansions_model2

        # Convert model instance back to dict and verify no loss of data
        expansions_model_json2 = expansions_model.to_dict()
        assert expansions_model_json2 == expansions_model_json

class TestModel_Field():
    """
    Test Class for Field
    """

    def test_field_serialization(self):
        """
        Test serialization/deserialization for Field
        """

        # Construct a json representation of a Field model
        field_model_json = {}

        # Construct a model instance of Field by calling from_dict on the json representation
        field_model = Field.from_dict(field_model_json)
        assert field_model != False

        # Construct a model instance of Field by calling from_dict on the json representation
        field_model_dict = Field.from_dict(field_model_json).__dict__
        field_model2 = Field(**field_model_dict)

        # Verify the model instances are equivalent
        assert field_model == field_model2

        # Convert model instance back to dict and verify no loss of data
        field_model_json2 = field_model.to_dict()
        assert field_model_json2 == field_model_json

class TestModel_ListCollectionsResponse():
    """
    Test Class for ListCollectionsResponse
    """

    def test_list_collections_response_serialization(self):
        """
        Test serialization/deserialization for ListCollectionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        collection_model = {} # Collection
        collection_model['name'] = 'example'

        # Construct a json representation of a ListCollectionsResponse model
        list_collections_response_model_json = {}
        list_collections_response_model_json['collections'] = [collection_model]

        # Construct a model instance of ListCollectionsResponse by calling from_dict on the json representation
        list_collections_response_model = ListCollectionsResponse.from_dict(list_collections_response_model_json)
        assert list_collections_response_model != False

        # Construct a model instance of ListCollectionsResponse by calling from_dict on the json representation
        list_collections_response_model_dict = ListCollectionsResponse.from_dict(list_collections_response_model_json).__dict__
        list_collections_response_model2 = ListCollectionsResponse(**list_collections_response_model_dict)

        # Verify the model instances are equivalent
        assert list_collections_response_model == list_collections_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_collections_response_model_json2 = list_collections_response_model.to_dict()
        assert list_collections_response_model_json2 == list_collections_response_model_json

class TestModel_ListDocumentsResponse():
    """
    Test Class for ListDocumentsResponse
    """

    def test_list_documents_response_serialization(self):
        """
        Test serialization/deserialization for ListDocumentsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice

        document_details_children_model = {} # DocumentDetailsChildren
        document_details_children_model['have_notices'] = True
        document_details_children_model['count'] = 38

        document_details_model = {} # DocumentDetails
        document_details_model['status'] = 'available'
        document_details_model['notices'] = [notice_model]
        document_details_model['children'] = document_details_children_model
        document_details_model['filename'] = 'testString'
        document_details_model['file_type'] = 'testString'
        document_details_model['sha256'] = 'testString'

        # Construct a json representation of a ListDocumentsResponse model
        list_documents_response_model_json = {}
        list_documents_response_model_json['matching_results'] = 38
        list_documents_response_model_json['documents'] = [document_details_model]

        # Construct a model instance of ListDocumentsResponse by calling from_dict on the json representation
        list_documents_response_model = ListDocumentsResponse.from_dict(list_documents_response_model_json)
        assert list_documents_response_model != False

        # Construct a model instance of ListDocumentsResponse by calling from_dict on the json representation
        list_documents_response_model_dict = ListDocumentsResponse.from_dict(list_documents_response_model_json).__dict__
        list_documents_response_model2 = ListDocumentsResponse(**list_documents_response_model_dict)

        # Verify the model instances are equivalent
        assert list_documents_response_model == list_documents_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_documents_response_model_json2 = list_documents_response_model.to_dict()
        assert list_documents_response_model_json2 == list_documents_response_model_json

class TestModel_ListFieldsResponse():
    """
    Test Class for ListFieldsResponse
    """

    def test_list_fields_response_serialization(self):
        """
        Test serialization/deserialization for ListFieldsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        field_model = {} # Field

        # Construct a json representation of a ListFieldsResponse model
        list_fields_response_model_json = {}
        list_fields_response_model_json['fields'] = [field_model]

        # Construct a model instance of ListFieldsResponse by calling from_dict on the json representation
        list_fields_response_model = ListFieldsResponse.from_dict(list_fields_response_model_json)
        assert list_fields_response_model != False

        # Construct a model instance of ListFieldsResponse by calling from_dict on the json representation
        list_fields_response_model_dict = ListFieldsResponse.from_dict(list_fields_response_model_json).__dict__
        list_fields_response_model2 = ListFieldsResponse(**list_fields_response_model_dict)

        # Verify the model instances are equivalent
        assert list_fields_response_model == list_fields_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_fields_response_model_json2 = list_fields_response_model.to_dict()
        assert list_fields_response_model_json2 == list_fields_response_model_json

class TestModel_ListProjectsResponse():
    """
    Test Class for ListProjectsResponse
    """

    def test_list_projects_response_serialization(self):
        """
        Test serialization/deserialization for ListProjectsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        project_list_details_model = {} # ProjectListDetails
        project_list_details_model['name'] = 'testString'
        project_list_details_model['type'] = 'document_retrieval'

        # Construct a json representation of a ListProjectsResponse model
        list_projects_response_model_json = {}
        list_projects_response_model_json['projects'] = [project_list_details_model]

        # Construct a model instance of ListProjectsResponse by calling from_dict on the json representation
        list_projects_response_model = ListProjectsResponse.from_dict(list_projects_response_model_json)
        assert list_projects_response_model != False

        # Construct a model instance of ListProjectsResponse by calling from_dict on the json representation
        list_projects_response_model_dict = ListProjectsResponse.from_dict(list_projects_response_model_json).__dict__
        list_projects_response_model2 = ListProjectsResponse(**list_projects_response_model_dict)

        # Verify the model instances are equivalent
        assert list_projects_response_model == list_projects_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_projects_response_model_json2 = list_projects_response_model.to_dict()
        assert list_projects_response_model_json2 == list_projects_response_model_json

class TestModel_ModelEvaluationMacroAverage():
    """
    Test Class for ModelEvaluationMacroAverage
    """

    def test_model_evaluation_macro_average_serialization(self):
        """
        Test serialization/deserialization for ModelEvaluationMacroAverage
        """

        # Construct a json representation of a ModelEvaluationMacroAverage model
        model_evaluation_macro_average_model_json = {}
        model_evaluation_macro_average_model_json['precision'] = 0
        model_evaluation_macro_average_model_json['recall'] = 0
        model_evaluation_macro_average_model_json['f1'] = 0

        # Construct a model instance of ModelEvaluationMacroAverage by calling from_dict on the json representation
        model_evaluation_macro_average_model = ModelEvaluationMacroAverage.from_dict(model_evaluation_macro_average_model_json)
        assert model_evaluation_macro_average_model != False

        # Construct a model instance of ModelEvaluationMacroAverage by calling from_dict on the json representation
        model_evaluation_macro_average_model_dict = ModelEvaluationMacroAverage.from_dict(model_evaluation_macro_average_model_json).__dict__
        model_evaluation_macro_average_model2 = ModelEvaluationMacroAverage(**model_evaluation_macro_average_model_dict)

        # Verify the model instances are equivalent
        assert model_evaluation_macro_average_model == model_evaluation_macro_average_model2

        # Convert model instance back to dict and verify no loss of data
        model_evaluation_macro_average_model_json2 = model_evaluation_macro_average_model.to_dict()
        assert model_evaluation_macro_average_model_json2 == model_evaluation_macro_average_model_json

class TestModel_ModelEvaluationMicroAverage():
    """
    Test Class for ModelEvaluationMicroAverage
    """

    def test_model_evaluation_micro_average_serialization(self):
        """
        Test serialization/deserialization for ModelEvaluationMicroAverage
        """

        # Construct a json representation of a ModelEvaluationMicroAverage model
        model_evaluation_micro_average_model_json = {}
        model_evaluation_micro_average_model_json['precision'] = 0
        model_evaluation_micro_average_model_json['recall'] = 0
        model_evaluation_micro_average_model_json['f1'] = 0

        # Construct a model instance of ModelEvaluationMicroAverage by calling from_dict on the json representation
        model_evaluation_micro_average_model = ModelEvaluationMicroAverage.from_dict(model_evaluation_micro_average_model_json)
        assert model_evaluation_micro_average_model != False

        # Construct a model instance of ModelEvaluationMicroAverage by calling from_dict on the json representation
        model_evaluation_micro_average_model_dict = ModelEvaluationMicroAverage.from_dict(model_evaluation_micro_average_model_json).__dict__
        model_evaluation_micro_average_model2 = ModelEvaluationMicroAverage(**model_evaluation_micro_average_model_dict)

        # Verify the model instances are equivalent
        assert model_evaluation_micro_average_model == model_evaluation_micro_average_model2

        # Convert model instance back to dict and verify no loss of data
        model_evaluation_micro_average_model_json2 = model_evaluation_micro_average_model.to_dict()
        assert model_evaluation_micro_average_model_json2 == model_evaluation_micro_average_model_json

class TestModel_Notice():
    """
    Test Class for Notice
    """

    def test_notice_serialization(self):
        """
        Test serialization/deserialization for Notice
        """

        # Construct a json representation of a Notice model
        notice_model_json = {}

        # Construct a model instance of Notice by calling from_dict on the json representation
        notice_model = Notice.from_dict(notice_model_json)
        assert notice_model != False

        # Construct a model instance of Notice by calling from_dict on the json representation
        notice_model_dict = Notice.from_dict(notice_model_json).__dict__
        notice_model2 = Notice(**notice_model_dict)

        # Verify the model instances are equivalent
        assert notice_model == notice_model2

        # Convert model instance back to dict and verify no loss of data
        notice_model_json2 = notice_model.to_dict()
        assert notice_model_json2 == notice_model_json

class TestModel_PerClassModelEvaluation():
    """
    Test Class for PerClassModelEvaluation
    """

    def test_per_class_model_evaluation_serialization(self):
        """
        Test serialization/deserialization for PerClassModelEvaluation
        """

        # Construct a json representation of a PerClassModelEvaluation model
        per_class_model_evaluation_model_json = {}
        per_class_model_evaluation_model_json['name'] = 'testString'
        per_class_model_evaluation_model_json['precision'] = 0
        per_class_model_evaluation_model_json['recall'] = 0
        per_class_model_evaluation_model_json['f1'] = 0

        # Construct a model instance of PerClassModelEvaluation by calling from_dict on the json representation
        per_class_model_evaluation_model = PerClassModelEvaluation.from_dict(per_class_model_evaluation_model_json)
        assert per_class_model_evaluation_model != False

        # Construct a model instance of PerClassModelEvaluation by calling from_dict on the json representation
        per_class_model_evaluation_model_dict = PerClassModelEvaluation.from_dict(per_class_model_evaluation_model_json).__dict__
        per_class_model_evaluation_model2 = PerClassModelEvaluation(**per_class_model_evaluation_model_dict)

        # Verify the model instances are equivalent
        assert per_class_model_evaluation_model == per_class_model_evaluation_model2

        # Convert model instance back to dict and verify no loss of data
        per_class_model_evaluation_model_json2 = per_class_model_evaluation_model.to_dict()
        assert per_class_model_evaluation_model_json2 == per_class_model_evaluation_model_json

class TestModel_ProjectDetails():
    """
    Test Class for ProjectDetails
    """

    def test_project_details_serialization(self):
        """
        Test serialization/deserialization for ProjectDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        default_query_params_passages_model = {} # DefaultQueryParamsPassages
        default_query_params_passages_model['enabled'] = True
        default_query_params_passages_model['count'] = 38
        default_query_params_passages_model['fields'] = ['testString']
        default_query_params_passages_model['characters'] = 38
        default_query_params_passages_model['per_document'] = True
        default_query_params_passages_model['max_per_document'] = 38

        default_query_params_table_results_model = {} # DefaultQueryParamsTableResults
        default_query_params_table_results_model['enabled'] = True
        default_query_params_table_results_model['count'] = 38
        default_query_params_table_results_model['per_document'] = 38

        default_query_params_suggested_refinements_model = {} # DefaultQueryParamsSuggestedRefinements
        default_query_params_suggested_refinements_model['enabled'] = True
        default_query_params_suggested_refinements_model['count'] = 38

        default_query_params_model = {} # DefaultQueryParams
        default_query_params_model['collection_ids'] = ['testString']
        default_query_params_model['passages'] = default_query_params_passages_model
        default_query_params_model['table_results'] = default_query_params_table_results_model
        default_query_params_model['aggregation'] = 'testString'
        default_query_params_model['suggested_refinements'] = default_query_params_suggested_refinements_model
        default_query_params_model['spelling_suggestions'] = True
        default_query_params_model['highlight'] = True
        default_query_params_model['count'] = 38
        default_query_params_model['sort'] = 'testString'
        default_query_params_model['return'] = ['testString']

        # Construct a json representation of a ProjectDetails model
        project_details_model_json = {}
        project_details_model_json['name'] = 'testString'
        project_details_model_json['type'] = 'document_retrieval'
        project_details_model_json['default_query_parameters'] = default_query_params_model

        # Construct a model instance of ProjectDetails by calling from_dict on the json representation
        project_details_model = ProjectDetails.from_dict(project_details_model_json)
        assert project_details_model != False

        # Construct a model instance of ProjectDetails by calling from_dict on the json representation
        project_details_model_dict = ProjectDetails.from_dict(project_details_model_json).__dict__
        project_details_model2 = ProjectDetails(**project_details_model_dict)

        # Verify the model instances are equivalent
        assert project_details_model == project_details_model2

        # Convert model instance back to dict and verify no loss of data
        project_details_model_json2 = project_details_model.to_dict()
        assert project_details_model_json2 == project_details_model_json

class TestModel_ProjectListDetails():
    """
    Test Class for ProjectListDetails
    """

    def test_project_list_details_serialization(self):
        """
        Test serialization/deserialization for ProjectListDetails
        """

        # Construct a json representation of a ProjectListDetails model
        project_list_details_model_json = {}
        project_list_details_model_json['name'] = 'testString'
        project_list_details_model_json['type'] = 'document_retrieval'

        # Construct a model instance of ProjectListDetails by calling from_dict on the json representation
        project_list_details_model = ProjectListDetails.from_dict(project_list_details_model_json)
        assert project_list_details_model != False

        # Construct a model instance of ProjectListDetails by calling from_dict on the json representation
        project_list_details_model_dict = ProjectListDetails.from_dict(project_list_details_model_json).__dict__
        project_list_details_model2 = ProjectListDetails(**project_list_details_model_dict)

        # Verify the model instances are equivalent
        assert project_list_details_model == project_list_details_model2

        # Convert model instance back to dict and verify no loss of data
        project_list_details_model_json2 = project_list_details_model.to_dict()
        assert project_list_details_model_json2 == project_list_details_model_json

class TestModel_ProjectListDetailsRelevancyTrainingStatus():
    """
    Test Class for ProjectListDetailsRelevancyTrainingStatus
    """

    def test_project_list_details_relevancy_training_status_serialization(self):
        """
        Test serialization/deserialization for ProjectListDetailsRelevancyTrainingStatus
        """

        # Construct a json representation of a ProjectListDetailsRelevancyTrainingStatus model
        project_list_details_relevancy_training_status_model_json = {}
        project_list_details_relevancy_training_status_model_json['data_updated'] = 'testString'
        project_list_details_relevancy_training_status_model_json['total_examples'] = 38
        project_list_details_relevancy_training_status_model_json['sufficient_label_diversity'] = True
        project_list_details_relevancy_training_status_model_json['processing'] = True
        project_list_details_relevancy_training_status_model_json['minimum_examples_added'] = True
        project_list_details_relevancy_training_status_model_json['successfully_trained'] = 'testString'
        project_list_details_relevancy_training_status_model_json['available'] = True
        project_list_details_relevancy_training_status_model_json['notices'] = 38
        project_list_details_relevancy_training_status_model_json['minimum_queries_added'] = True

        # Construct a model instance of ProjectListDetailsRelevancyTrainingStatus by calling from_dict on the json representation
        project_list_details_relevancy_training_status_model = ProjectListDetailsRelevancyTrainingStatus.from_dict(project_list_details_relevancy_training_status_model_json)
        assert project_list_details_relevancy_training_status_model != False

        # Construct a model instance of ProjectListDetailsRelevancyTrainingStatus by calling from_dict on the json representation
        project_list_details_relevancy_training_status_model_dict = ProjectListDetailsRelevancyTrainingStatus.from_dict(project_list_details_relevancy_training_status_model_json).__dict__
        project_list_details_relevancy_training_status_model2 = ProjectListDetailsRelevancyTrainingStatus(**project_list_details_relevancy_training_status_model_dict)

        # Verify the model instances are equivalent
        assert project_list_details_relevancy_training_status_model == project_list_details_relevancy_training_status_model2

        # Convert model instance back to dict and verify no loss of data
        project_list_details_relevancy_training_status_model_json2 = project_list_details_relevancy_training_status_model.to_dict()
        assert project_list_details_relevancy_training_status_model_json2 == project_list_details_relevancy_training_status_model_json

class TestModel_QueryGroupByAggregationResult():
    """
    Test Class for QueryGroupByAggregationResult
    """

    def test_query_group_by_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryGroupByAggregationResult
        """

        # Construct a json representation of a QueryGroupByAggregationResult model
        query_group_by_aggregation_result_model_json = {}
        query_group_by_aggregation_result_model_json['key'] = 'testString'
        query_group_by_aggregation_result_model_json['matching_results'] = 38
        query_group_by_aggregation_result_model_json['relevancy'] = 72.5
        query_group_by_aggregation_result_model_json['total_matching_documents'] = 38
        query_group_by_aggregation_result_model_json['estimated_matching_results'] = 72.5
        query_group_by_aggregation_result_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryGroupByAggregationResult by calling from_dict on the json representation
        query_group_by_aggregation_result_model = QueryGroupByAggregationResult.from_dict(query_group_by_aggregation_result_model_json)
        assert query_group_by_aggregation_result_model != False

        # Construct a model instance of QueryGroupByAggregationResult by calling from_dict on the json representation
        query_group_by_aggregation_result_model_dict = QueryGroupByAggregationResult.from_dict(query_group_by_aggregation_result_model_json).__dict__
        query_group_by_aggregation_result_model2 = QueryGroupByAggregationResult(**query_group_by_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_group_by_aggregation_result_model == query_group_by_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_group_by_aggregation_result_model_json2 = query_group_by_aggregation_result_model.to_dict()
        assert query_group_by_aggregation_result_model_json2 == query_group_by_aggregation_result_model_json

class TestModel_QueryHistogramAggregationResult():
    """
    Test Class for QueryHistogramAggregationResult
    """

    def test_query_histogram_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryHistogramAggregationResult
        """

        # Construct a json representation of a QueryHistogramAggregationResult model
        query_histogram_aggregation_result_model_json = {}
        query_histogram_aggregation_result_model_json['key'] = 26
        query_histogram_aggregation_result_model_json['matching_results'] = 38
        query_histogram_aggregation_result_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryHistogramAggregationResult by calling from_dict on the json representation
        query_histogram_aggregation_result_model = QueryHistogramAggregationResult.from_dict(query_histogram_aggregation_result_model_json)
        assert query_histogram_aggregation_result_model != False

        # Construct a model instance of QueryHistogramAggregationResult by calling from_dict on the json representation
        query_histogram_aggregation_result_model_dict = QueryHistogramAggregationResult.from_dict(query_histogram_aggregation_result_model_json).__dict__
        query_histogram_aggregation_result_model2 = QueryHistogramAggregationResult(**query_histogram_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_histogram_aggregation_result_model == query_histogram_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_histogram_aggregation_result_model_json2 = query_histogram_aggregation_result_model.to_dict()
        assert query_histogram_aggregation_result_model_json2 == query_histogram_aggregation_result_model_json

class TestModel_QueryLargePassages():
    """
    Test Class for QueryLargePassages
    """

    def test_query_large_passages_serialization(self):
        """
        Test serialization/deserialization for QueryLargePassages
        """

        # Construct a json representation of a QueryLargePassages model
        query_large_passages_model_json = {}
        query_large_passages_model_json['enabled'] = True
        query_large_passages_model_json['per_document'] = True
        query_large_passages_model_json['max_per_document'] = 38
        query_large_passages_model_json['fields'] = ['testString']
        query_large_passages_model_json['count'] = 400
        query_large_passages_model_json['characters'] = 50
        query_large_passages_model_json['find_answers'] = False
        query_large_passages_model_json['max_answers_per_passage'] = 38

        # Construct a model instance of QueryLargePassages by calling from_dict on the json representation
        query_large_passages_model = QueryLargePassages.from_dict(query_large_passages_model_json)
        assert query_large_passages_model != False

        # Construct a model instance of QueryLargePassages by calling from_dict on the json representation
        query_large_passages_model_dict = QueryLargePassages.from_dict(query_large_passages_model_json).__dict__
        query_large_passages_model2 = QueryLargePassages(**query_large_passages_model_dict)

        # Verify the model instances are equivalent
        assert query_large_passages_model == query_large_passages_model2

        # Convert model instance back to dict and verify no loss of data
        query_large_passages_model_json2 = query_large_passages_model.to_dict()
        assert query_large_passages_model_json2 == query_large_passages_model_json

class TestModel_QueryLargeSimilar():
    """
    Test Class for QueryLargeSimilar
    """

    def test_query_large_similar_serialization(self):
        """
        Test serialization/deserialization for QueryLargeSimilar
        """

        # Construct a json representation of a QueryLargeSimilar model
        query_large_similar_model_json = {}
        query_large_similar_model_json['enabled'] = False
        query_large_similar_model_json['document_ids'] = ['testString']
        query_large_similar_model_json['fields'] = ['testString']

        # Construct a model instance of QueryLargeSimilar by calling from_dict on the json representation
        query_large_similar_model = QueryLargeSimilar.from_dict(query_large_similar_model_json)
        assert query_large_similar_model != False

        # Construct a model instance of QueryLargeSimilar by calling from_dict on the json representation
        query_large_similar_model_dict = QueryLargeSimilar.from_dict(query_large_similar_model_json).__dict__
        query_large_similar_model2 = QueryLargeSimilar(**query_large_similar_model_dict)

        # Verify the model instances are equivalent
        assert query_large_similar_model == query_large_similar_model2

        # Convert model instance back to dict and verify no loss of data
        query_large_similar_model_json2 = query_large_similar_model.to_dict()
        assert query_large_similar_model_json2 == query_large_similar_model_json

class TestModel_QueryLargeSuggestedRefinements():
    """
    Test Class for QueryLargeSuggestedRefinements
    """

    def test_query_large_suggested_refinements_serialization(self):
        """
        Test serialization/deserialization for QueryLargeSuggestedRefinements
        """

        # Construct a json representation of a QueryLargeSuggestedRefinements model
        query_large_suggested_refinements_model_json = {}
        query_large_suggested_refinements_model_json['enabled'] = True
        query_large_suggested_refinements_model_json['count'] = 1

        # Construct a model instance of QueryLargeSuggestedRefinements by calling from_dict on the json representation
        query_large_suggested_refinements_model = QueryLargeSuggestedRefinements.from_dict(query_large_suggested_refinements_model_json)
        assert query_large_suggested_refinements_model != False

        # Construct a model instance of QueryLargeSuggestedRefinements by calling from_dict on the json representation
        query_large_suggested_refinements_model_dict = QueryLargeSuggestedRefinements.from_dict(query_large_suggested_refinements_model_json).__dict__
        query_large_suggested_refinements_model2 = QueryLargeSuggestedRefinements(**query_large_suggested_refinements_model_dict)

        # Verify the model instances are equivalent
        assert query_large_suggested_refinements_model == query_large_suggested_refinements_model2

        # Convert model instance back to dict and verify no loss of data
        query_large_suggested_refinements_model_json2 = query_large_suggested_refinements_model.to_dict()
        assert query_large_suggested_refinements_model_json2 == query_large_suggested_refinements_model_json

class TestModel_QueryLargeTableResults():
    """
    Test Class for QueryLargeTableResults
    """

    def test_query_large_table_results_serialization(self):
        """
        Test serialization/deserialization for QueryLargeTableResults
        """

        # Construct a json representation of a QueryLargeTableResults model
        query_large_table_results_model_json = {}
        query_large_table_results_model_json['enabled'] = True
        query_large_table_results_model_json['count'] = 38

        # Construct a model instance of QueryLargeTableResults by calling from_dict on the json representation
        query_large_table_results_model = QueryLargeTableResults.from_dict(query_large_table_results_model_json)
        assert query_large_table_results_model != False

        # Construct a model instance of QueryLargeTableResults by calling from_dict on the json representation
        query_large_table_results_model_dict = QueryLargeTableResults.from_dict(query_large_table_results_model_json).__dict__
        query_large_table_results_model2 = QueryLargeTableResults(**query_large_table_results_model_dict)

        # Verify the model instances are equivalent
        assert query_large_table_results_model == query_large_table_results_model2

        # Convert model instance back to dict and verify no loss of data
        query_large_table_results_model_json2 = query_large_table_results_model.to_dict()
        assert query_large_table_results_model_json2 == query_large_table_results_model_json

class TestModel_QueryNoticesResponse():
    """
    Test Class for QueryNoticesResponse
    """

    def test_query_notices_response_serialization(self):
        """
        Test serialization/deserialization for QueryNoticesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice

        # Construct a json representation of a QueryNoticesResponse model
        query_notices_response_model_json = {}
        query_notices_response_model_json['matching_results'] = 38
        query_notices_response_model_json['notices'] = [notice_model]

        # Construct a model instance of QueryNoticesResponse by calling from_dict on the json representation
        query_notices_response_model = QueryNoticesResponse.from_dict(query_notices_response_model_json)
        assert query_notices_response_model != False

        # Construct a model instance of QueryNoticesResponse by calling from_dict on the json representation
        query_notices_response_model_dict = QueryNoticesResponse.from_dict(query_notices_response_model_json).__dict__
        query_notices_response_model2 = QueryNoticesResponse(**query_notices_response_model_dict)

        # Verify the model instances are equivalent
        assert query_notices_response_model == query_notices_response_model2

        # Convert model instance back to dict and verify no loss of data
        query_notices_response_model_json2 = query_notices_response_model.to_dict()
        assert query_notices_response_model_json2 == query_notices_response_model_json

class TestModel_QueryPairAggregationResult():
    """
    Test Class for QueryPairAggregationResult
    """

    def test_query_pair_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryPairAggregationResult
        """

        # Construct a json representation of a QueryPairAggregationResult model
        query_pair_aggregation_result_model_json = {}
        query_pair_aggregation_result_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryPairAggregationResult by calling from_dict on the json representation
        query_pair_aggregation_result_model = QueryPairAggregationResult.from_dict(query_pair_aggregation_result_model_json)
        assert query_pair_aggregation_result_model != False

        # Construct a model instance of QueryPairAggregationResult by calling from_dict on the json representation
        query_pair_aggregation_result_model_dict = QueryPairAggregationResult.from_dict(query_pair_aggregation_result_model_json).__dict__
        query_pair_aggregation_result_model2 = QueryPairAggregationResult(**query_pair_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_pair_aggregation_result_model == query_pair_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_pair_aggregation_result_model_json2 = query_pair_aggregation_result_model.to_dict()
        assert query_pair_aggregation_result_model_json2 == query_pair_aggregation_result_model_json

class TestModel_QueryResponse():
    """
    Test Class for QueryResponse
    """

    def test_query_response_serialization(self):
        """
        Test serialization/deserialization for QueryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['document_retrieval_source'] = 'search'
        query_result_metadata_model['collection_id'] = 'testString'
        query_result_metadata_model['confidence'] = 0

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        query_result_passage_model = {} # QueryResultPassage
        query_result_passage_model['passage_text'] = 'testString'
        query_result_passage_model['start_offset'] = 38
        query_result_passage_model['end_offset'] = 38
        query_result_passage_model['field'] = 'testString'
        query_result_passage_model['answers'] = [result_passage_answer_model]

        query_result_model = {} # QueryResult
        query_result_model['document_id'] = 'testString'
        query_result_model['metadata'] = {'foo': 'bar'}
        query_result_model['result_metadata'] = query_result_metadata_model
        query_result_model['document_passages'] = [query_result_passage_model]
        query_result_model['id'] = 'watson-generated ID'

        query_term_aggregation_result_model = {} # QueryTermAggregationResult
        query_term_aggregation_result_model['key'] = 'active'
        query_term_aggregation_result_model['matching_results'] = 34
        query_term_aggregation_result_model['relevancy'] = 72.5
        query_term_aggregation_result_model['total_matching_documents'] = 38
        query_term_aggregation_result_model['estimated_matching_results'] = 72.5
        query_term_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        query_aggregation_model = {} # QueryAggregationQueryTermAggregation
        query_aggregation_model['type'] = 'term'
        query_aggregation_model['field'] = 'field'
        query_aggregation_model['count'] = 1
        query_aggregation_model['name'] = 'testString'
        query_aggregation_model['results'] = [query_term_aggregation_result_model]

        retrieval_details_model = {} # RetrievalDetails
        retrieval_details_model['document_retrieval_strategy'] = 'untrained'

        query_suggested_refinement_model = {} # QuerySuggestedRefinement
        query_suggested_refinement_model['text'] = 'testString'

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_text_location_model = {} # TableTextLocation
        table_text_location_model['text'] = 'testString'
        table_text_location_model['location'] = table_element_location_model

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = {'foo': 'bar'}
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        table_row_headers_model = {} # TableRowHeaders
        table_row_headers_model['cell_id'] = 'testString'
        table_row_headers_model['location'] = table_element_location_model
        table_row_headers_model['text'] = 'testString'
        table_row_headers_model['text_normalized'] = 'testString'
        table_row_headers_model['row_index_begin'] = 26
        table_row_headers_model['row_index_end'] = 26
        table_row_headers_model['column_index_begin'] = 26
        table_row_headers_model['column_index_end'] = 26

        table_column_headers_model = {} # TableColumnHeaders
        table_column_headers_model['cell_id'] = 'testString'
        table_column_headers_model['location'] = {'foo': 'bar'}
        table_column_headers_model['text'] = 'testString'
        table_column_headers_model['text_normalized'] = 'testString'
        table_column_headers_model['row_index_begin'] = 26
        table_column_headers_model['row_index_end'] = 26
        table_column_headers_model['column_index_begin'] = 26
        table_column_headers_model['column_index_end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        table_key_value_pairs_model = {} # TableKeyValuePairs
        table_key_value_pairs_model['key'] = table_cell_key_model
        table_key_value_pairs_model['value'] = [table_cell_values_model]

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        table_body_cells_model = {} # TableBodyCells
        table_body_cells_model['cell_id'] = 'testString'
        table_body_cells_model['location'] = table_element_location_model
        table_body_cells_model['text'] = 'testString'
        table_body_cells_model['row_index_begin'] = 26
        table_body_cells_model['row_index_end'] = 26
        table_body_cells_model['column_index_begin'] = 26
        table_body_cells_model['column_index_end'] = 26
        table_body_cells_model['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model['attributes'] = [document_attribute_model]

        table_result_table_model = {} # TableResultTable
        table_result_table_model['location'] = table_element_location_model
        table_result_table_model['text'] = 'testString'
        table_result_table_model['section_title'] = table_text_location_model
        table_result_table_model['title'] = table_text_location_model
        table_result_table_model['table_headers'] = [table_headers_model]
        table_result_table_model['row_headers'] = [table_row_headers_model]
        table_result_table_model['column_headers'] = [table_column_headers_model]
        table_result_table_model['key_value_pairs'] = [table_key_value_pairs_model]
        table_result_table_model['body_cells'] = [table_body_cells_model]
        table_result_table_model['contexts'] = [table_text_location_model]

        query_table_result_model = {} # QueryTableResult
        query_table_result_model['table_id'] = 'testString'
        query_table_result_model['source_document_id'] = 'testString'
        query_table_result_model['collection_id'] = 'testString'
        query_table_result_model['table_html'] = 'testString'
        query_table_result_model['table_html_offset'] = 38
        query_table_result_model['table'] = table_result_table_model

        query_response_passage_model = {} # QueryResponsePassage
        query_response_passage_model['passage_text'] = 'testString'
        query_response_passage_model['passage_score'] = 72.5
        query_response_passage_model['document_id'] = 'testString'
        query_response_passage_model['collection_id'] = 'testString'
        query_response_passage_model['start_offset'] = 38
        query_response_passage_model['end_offset'] = 38
        query_response_passage_model['field'] = 'testString'
        query_response_passage_model['answers'] = [result_passage_answer_model]

        # Construct a json representation of a QueryResponse model
        query_response_model_json = {}
        query_response_model_json['matching_results'] = 38
        query_response_model_json['results'] = [query_result_model]
        query_response_model_json['aggregations'] = [query_aggregation_model]
        query_response_model_json['retrieval_details'] = retrieval_details_model
        query_response_model_json['suggested_query'] = 'testString'
        query_response_model_json['suggested_refinements'] = [query_suggested_refinement_model]
        query_response_model_json['table_results'] = [query_table_result_model]
        query_response_model_json['passages'] = [query_response_passage_model]

        # Construct a model instance of QueryResponse by calling from_dict on the json representation
        query_response_model = QueryResponse.from_dict(query_response_model_json)
        assert query_response_model != False

        # Construct a model instance of QueryResponse by calling from_dict on the json representation
        query_response_model_dict = QueryResponse.from_dict(query_response_model_json).__dict__
        query_response_model2 = QueryResponse(**query_response_model_dict)

        # Verify the model instances are equivalent
        assert query_response_model == query_response_model2

        # Convert model instance back to dict and verify no loss of data
        query_response_model_json2 = query_response_model.to_dict()
        assert query_response_model_json2 == query_response_model_json

class TestModel_QueryResponsePassage():
    """
    Test Class for QueryResponsePassage
    """

    def test_query_response_passage_serialization(self):
        """
        Test serialization/deserialization for QueryResponsePassage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        # Construct a json representation of a QueryResponsePassage model
        query_response_passage_model_json = {}
        query_response_passage_model_json['passage_text'] = 'testString'
        query_response_passage_model_json['passage_score'] = 72.5
        query_response_passage_model_json['document_id'] = 'testString'
        query_response_passage_model_json['collection_id'] = 'testString'
        query_response_passage_model_json['start_offset'] = 38
        query_response_passage_model_json['end_offset'] = 38
        query_response_passage_model_json['field'] = 'testString'
        query_response_passage_model_json['answers'] = [result_passage_answer_model]

        # Construct a model instance of QueryResponsePassage by calling from_dict on the json representation
        query_response_passage_model = QueryResponsePassage.from_dict(query_response_passage_model_json)
        assert query_response_passage_model != False

        # Construct a model instance of QueryResponsePassage by calling from_dict on the json representation
        query_response_passage_model_dict = QueryResponsePassage.from_dict(query_response_passage_model_json).__dict__
        query_response_passage_model2 = QueryResponsePassage(**query_response_passage_model_dict)

        # Verify the model instances are equivalent
        assert query_response_passage_model == query_response_passage_model2

        # Convert model instance back to dict and verify no loss of data
        query_response_passage_model_json2 = query_response_passage_model.to_dict()
        assert query_response_passage_model_json2 == query_response_passage_model_json

class TestModel_QueryResult():
    """
    Test Class for QueryResult
    """

    def test_query_result_serialization(self):
        """
        Test serialization/deserialization for QueryResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['document_retrieval_source'] = 'search'
        query_result_metadata_model['collection_id'] = 'testString'
        query_result_metadata_model['confidence'] = 0

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        query_result_passage_model = {} # QueryResultPassage
        query_result_passage_model['passage_text'] = 'testString'
        query_result_passage_model['start_offset'] = 38
        query_result_passage_model['end_offset'] = 38
        query_result_passage_model['field'] = 'testString'
        query_result_passage_model['answers'] = [result_passage_answer_model]

        # Construct a json representation of a QueryResult model
        query_result_model_json = {}
        query_result_model_json['document_id'] = 'testString'
        query_result_model_json['metadata'] = {'foo': 'bar'}
        query_result_model_json['result_metadata'] = query_result_metadata_model
        query_result_model_json['document_passages'] = [query_result_passage_model]
        query_result_model_json['foo'] = 'testString'

        # Construct a model instance of QueryResult by calling from_dict on the json representation
        query_result_model = QueryResult.from_dict(query_result_model_json)
        assert query_result_model != False

        # Construct a model instance of QueryResult by calling from_dict on the json representation
        query_result_model_dict = QueryResult.from_dict(query_result_model_json).__dict__
        query_result_model2 = QueryResult(**query_result_model_dict)

        # Verify the model instances are equivalent
        assert query_result_model == query_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_model_json2 = query_result_model.to_dict()
        assert query_result_model_json2 == query_result_model_json

        # Test get_properties and set_properties methods.
        query_result_model.set_properties({})
        actual_dict = query_result_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        query_result_model.set_properties(expected_dict)
        actual_dict = query_result_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_QueryResultMetadata():
    """
    Test Class for QueryResultMetadata
    """

    def test_query_result_metadata_serialization(self):
        """
        Test serialization/deserialization for QueryResultMetadata
        """

        # Construct a json representation of a QueryResultMetadata model
        query_result_metadata_model_json = {}
        query_result_metadata_model_json['document_retrieval_source'] = 'search'
        query_result_metadata_model_json['collection_id'] = 'testString'
        query_result_metadata_model_json['confidence'] = 0

        # Construct a model instance of QueryResultMetadata by calling from_dict on the json representation
        query_result_metadata_model = QueryResultMetadata.from_dict(query_result_metadata_model_json)
        assert query_result_metadata_model != False

        # Construct a model instance of QueryResultMetadata by calling from_dict on the json representation
        query_result_metadata_model_dict = QueryResultMetadata.from_dict(query_result_metadata_model_json).__dict__
        query_result_metadata_model2 = QueryResultMetadata(**query_result_metadata_model_dict)

        # Verify the model instances are equivalent
        assert query_result_metadata_model == query_result_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_metadata_model_json2 = query_result_metadata_model.to_dict()
        assert query_result_metadata_model_json2 == query_result_metadata_model_json

class TestModel_QueryResultPassage():
    """
    Test Class for QueryResultPassage
    """

    def test_query_result_passage_serialization(self):
        """
        Test serialization/deserialization for QueryResultPassage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        result_passage_answer_model = {} # ResultPassageAnswer
        result_passage_answer_model['answer_text'] = 'testString'
        result_passage_answer_model['start_offset'] = 38
        result_passage_answer_model['end_offset'] = 38
        result_passage_answer_model['confidence'] = 0

        # Construct a json representation of a QueryResultPassage model
        query_result_passage_model_json = {}
        query_result_passage_model_json['passage_text'] = 'testString'
        query_result_passage_model_json['start_offset'] = 38
        query_result_passage_model_json['end_offset'] = 38
        query_result_passage_model_json['field'] = 'testString'
        query_result_passage_model_json['answers'] = [result_passage_answer_model]

        # Construct a model instance of QueryResultPassage by calling from_dict on the json representation
        query_result_passage_model = QueryResultPassage.from_dict(query_result_passage_model_json)
        assert query_result_passage_model != False

        # Construct a model instance of QueryResultPassage by calling from_dict on the json representation
        query_result_passage_model_dict = QueryResultPassage.from_dict(query_result_passage_model_json).__dict__
        query_result_passage_model2 = QueryResultPassage(**query_result_passage_model_dict)

        # Verify the model instances are equivalent
        assert query_result_passage_model == query_result_passage_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_passage_model_json2 = query_result_passage_model.to_dict()
        assert query_result_passage_model_json2 == query_result_passage_model_json

class TestModel_QuerySuggestedRefinement():
    """
    Test Class for QuerySuggestedRefinement
    """

    def test_query_suggested_refinement_serialization(self):
        """
        Test serialization/deserialization for QuerySuggestedRefinement
        """

        # Construct a json representation of a QuerySuggestedRefinement model
        query_suggested_refinement_model_json = {}
        query_suggested_refinement_model_json['text'] = 'testString'

        # Construct a model instance of QuerySuggestedRefinement by calling from_dict on the json representation
        query_suggested_refinement_model = QuerySuggestedRefinement.from_dict(query_suggested_refinement_model_json)
        assert query_suggested_refinement_model != False

        # Construct a model instance of QuerySuggestedRefinement by calling from_dict on the json representation
        query_suggested_refinement_model_dict = QuerySuggestedRefinement.from_dict(query_suggested_refinement_model_json).__dict__
        query_suggested_refinement_model2 = QuerySuggestedRefinement(**query_suggested_refinement_model_dict)

        # Verify the model instances are equivalent
        assert query_suggested_refinement_model == query_suggested_refinement_model2

        # Convert model instance back to dict and verify no loss of data
        query_suggested_refinement_model_json2 = query_suggested_refinement_model.to_dict()
        assert query_suggested_refinement_model_json2 == query_suggested_refinement_model_json

class TestModel_QueryTableResult():
    """
    Test Class for QueryTableResult
    """

    def test_query_table_result_serialization(self):
        """
        Test serialization/deserialization for QueryTableResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_text_location_model = {} # TableTextLocation
        table_text_location_model['text'] = 'testString'
        table_text_location_model['location'] = table_element_location_model

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = {'foo': 'bar'}
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        table_row_headers_model = {} # TableRowHeaders
        table_row_headers_model['cell_id'] = 'testString'
        table_row_headers_model['location'] = table_element_location_model
        table_row_headers_model['text'] = 'testString'
        table_row_headers_model['text_normalized'] = 'testString'
        table_row_headers_model['row_index_begin'] = 26
        table_row_headers_model['row_index_end'] = 26
        table_row_headers_model['column_index_begin'] = 26
        table_row_headers_model['column_index_end'] = 26

        table_column_headers_model = {} # TableColumnHeaders
        table_column_headers_model['cell_id'] = 'testString'
        table_column_headers_model['location'] = {'foo': 'bar'}
        table_column_headers_model['text'] = 'testString'
        table_column_headers_model['text_normalized'] = 'testString'
        table_column_headers_model['row_index_begin'] = 26
        table_column_headers_model['row_index_end'] = 26
        table_column_headers_model['column_index_begin'] = 26
        table_column_headers_model['column_index_end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        table_key_value_pairs_model = {} # TableKeyValuePairs
        table_key_value_pairs_model['key'] = table_cell_key_model
        table_key_value_pairs_model['value'] = [table_cell_values_model]

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        table_body_cells_model = {} # TableBodyCells
        table_body_cells_model['cell_id'] = 'testString'
        table_body_cells_model['location'] = table_element_location_model
        table_body_cells_model['text'] = 'testString'
        table_body_cells_model['row_index_begin'] = 26
        table_body_cells_model['row_index_end'] = 26
        table_body_cells_model['column_index_begin'] = 26
        table_body_cells_model['column_index_end'] = 26
        table_body_cells_model['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model['attributes'] = [document_attribute_model]

        table_result_table_model = {} # TableResultTable
        table_result_table_model['location'] = table_element_location_model
        table_result_table_model['text'] = 'testString'
        table_result_table_model['section_title'] = table_text_location_model
        table_result_table_model['title'] = table_text_location_model
        table_result_table_model['table_headers'] = [table_headers_model]
        table_result_table_model['row_headers'] = [table_row_headers_model]
        table_result_table_model['column_headers'] = [table_column_headers_model]
        table_result_table_model['key_value_pairs'] = [table_key_value_pairs_model]
        table_result_table_model['body_cells'] = [table_body_cells_model]
        table_result_table_model['contexts'] = [table_text_location_model]

        # Construct a json representation of a QueryTableResult model
        query_table_result_model_json = {}
        query_table_result_model_json['table_id'] = 'testString'
        query_table_result_model_json['source_document_id'] = 'testString'
        query_table_result_model_json['collection_id'] = 'testString'
        query_table_result_model_json['table_html'] = 'testString'
        query_table_result_model_json['table_html_offset'] = 38
        query_table_result_model_json['table'] = table_result_table_model

        # Construct a model instance of QueryTableResult by calling from_dict on the json representation
        query_table_result_model = QueryTableResult.from_dict(query_table_result_model_json)
        assert query_table_result_model != False

        # Construct a model instance of QueryTableResult by calling from_dict on the json representation
        query_table_result_model_dict = QueryTableResult.from_dict(query_table_result_model_json).__dict__
        query_table_result_model2 = QueryTableResult(**query_table_result_model_dict)

        # Verify the model instances are equivalent
        assert query_table_result_model == query_table_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_table_result_model_json2 = query_table_result_model.to_dict()
        assert query_table_result_model_json2 == query_table_result_model_json

class TestModel_QueryTermAggregationResult():
    """
    Test Class for QueryTermAggregationResult
    """

    def test_query_term_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTermAggregationResult
        """

        # Construct a json representation of a QueryTermAggregationResult model
        query_term_aggregation_result_model_json = {}
        query_term_aggregation_result_model_json['key'] = 'testString'
        query_term_aggregation_result_model_json['matching_results'] = 38
        query_term_aggregation_result_model_json['relevancy'] = 72.5
        query_term_aggregation_result_model_json['total_matching_documents'] = 38
        query_term_aggregation_result_model_json['estimated_matching_results'] = 72.5
        query_term_aggregation_result_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryTermAggregationResult by calling from_dict on the json representation
        query_term_aggregation_result_model = QueryTermAggregationResult.from_dict(query_term_aggregation_result_model_json)
        assert query_term_aggregation_result_model != False

        # Construct a model instance of QueryTermAggregationResult by calling from_dict on the json representation
        query_term_aggregation_result_model_dict = QueryTermAggregationResult.from_dict(query_term_aggregation_result_model_json).__dict__
        query_term_aggregation_result_model2 = QueryTermAggregationResult(**query_term_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_term_aggregation_result_model == query_term_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_term_aggregation_result_model_json2 = query_term_aggregation_result_model.to_dict()
        assert query_term_aggregation_result_model_json2 == query_term_aggregation_result_model_json

class TestModel_QueryTimesliceAggregationResult():
    """
    Test Class for QueryTimesliceAggregationResult
    """

    def test_query_timeslice_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTimesliceAggregationResult
        """

        # Construct a json representation of a QueryTimesliceAggregationResult model
        query_timeslice_aggregation_result_model_json = {}
        query_timeslice_aggregation_result_model_json['key_as_string'] = 'testString'
        query_timeslice_aggregation_result_model_json['key'] = 26
        query_timeslice_aggregation_result_model_json['matching_results'] = 26
        query_timeslice_aggregation_result_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryTimesliceAggregationResult by calling from_dict on the json representation
        query_timeslice_aggregation_result_model = QueryTimesliceAggregationResult.from_dict(query_timeslice_aggregation_result_model_json)
        assert query_timeslice_aggregation_result_model != False

        # Construct a model instance of QueryTimesliceAggregationResult by calling from_dict on the json representation
        query_timeslice_aggregation_result_model_dict = QueryTimesliceAggregationResult.from_dict(query_timeslice_aggregation_result_model_json).__dict__
        query_timeslice_aggregation_result_model2 = QueryTimesliceAggregationResult(**query_timeslice_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_timeslice_aggregation_result_model == query_timeslice_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_timeslice_aggregation_result_model_json2 = query_timeslice_aggregation_result_model.to_dict()
        assert query_timeslice_aggregation_result_model_json2 == query_timeslice_aggregation_result_model_json

class TestModel_QueryTopHitsAggregationResult():
    """
    Test Class for QueryTopHitsAggregationResult
    """

    def test_query_top_hits_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTopHitsAggregationResult
        """

        # Construct a json representation of a QueryTopHitsAggregationResult model
        query_top_hits_aggregation_result_model_json = {}
        query_top_hits_aggregation_result_model_json['matching_results'] = 38
        query_top_hits_aggregation_result_model_json['hits'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryTopHitsAggregationResult by calling from_dict on the json representation
        query_top_hits_aggregation_result_model = QueryTopHitsAggregationResult.from_dict(query_top_hits_aggregation_result_model_json)
        assert query_top_hits_aggregation_result_model != False

        # Construct a model instance of QueryTopHitsAggregationResult by calling from_dict on the json representation
        query_top_hits_aggregation_result_model_dict = QueryTopHitsAggregationResult.from_dict(query_top_hits_aggregation_result_model_json).__dict__
        query_top_hits_aggregation_result_model2 = QueryTopHitsAggregationResult(**query_top_hits_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_top_hits_aggregation_result_model == query_top_hits_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_top_hits_aggregation_result_model_json2 = query_top_hits_aggregation_result_model.to_dict()
        assert query_top_hits_aggregation_result_model_json2 == query_top_hits_aggregation_result_model_json

class TestModel_QueryTopicAggregationResult():
    """
    Test Class for QueryTopicAggregationResult
    """

    def test_query_topic_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTopicAggregationResult
        """

        # Construct a json representation of a QueryTopicAggregationResult model
        query_topic_aggregation_result_model_json = {}
        query_topic_aggregation_result_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryTopicAggregationResult by calling from_dict on the json representation
        query_topic_aggregation_result_model = QueryTopicAggregationResult.from_dict(query_topic_aggregation_result_model_json)
        assert query_topic_aggregation_result_model != False

        # Construct a model instance of QueryTopicAggregationResult by calling from_dict on the json representation
        query_topic_aggregation_result_model_dict = QueryTopicAggregationResult.from_dict(query_topic_aggregation_result_model_json).__dict__
        query_topic_aggregation_result_model2 = QueryTopicAggregationResult(**query_topic_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_topic_aggregation_result_model == query_topic_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_topic_aggregation_result_model_json2 = query_topic_aggregation_result_model.to_dict()
        assert query_topic_aggregation_result_model_json2 == query_topic_aggregation_result_model_json

class TestModel_QueryTrendAggregationResult():
    """
    Test Class for QueryTrendAggregationResult
    """

    def test_query_trend_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for QueryTrendAggregationResult
        """

        # Construct a json representation of a QueryTrendAggregationResult model
        query_trend_aggregation_result_model_json = {}
        query_trend_aggregation_result_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryTrendAggregationResult by calling from_dict on the json representation
        query_trend_aggregation_result_model = QueryTrendAggregationResult.from_dict(query_trend_aggregation_result_model_json)
        assert query_trend_aggregation_result_model != False

        # Construct a model instance of QueryTrendAggregationResult by calling from_dict on the json representation
        query_trend_aggregation_result_model_dict = QueryTrendAggregationResult.from_dict(query_trend_aggregation_result_model_json).__dict__
        query_trend_aggregation_result_model2 = QueryTrendAggregationResult(**query_trend_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert query_trend_aggregation_result_model == query_trend_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_trend_aggregation_result_model_json2 = query_trend_aggregation_result_model.to_dict()
        assert query_trend_aggregation_result_model_json2 == query_trend_aggregation_result_model_json

class TestModel_ResultPassageAnswer():
    """
    Test Class for ResultPassageAnswer
    """

    def test_result_passage_answer_serialization(self):
        """
        Test serialization/deserialization for ResultPassageAnswer
        """

        # Construct a json representation of a ResultPassageAnswer model
        result_passage_answer_model_json = {}
        result_passage_answer_model_json['answer_text'] = 'testString'
        result_passage_answer_model_json['start_offset'] = 38
        result_passage_answer_model_json['end_offset'] = 38
        result_passage_answer_model_json['confidence'] = 0

        # Construct a model instance of ResultPassageAnswer by calling from_dict on the json representation
        result_passage_answer_model = ResultPassageAnswer.from_dict(result_passage_answer_model_json)
        assert result_passage_answer_model != False

        # Construct a model instance of ResultPassageAnswer by calling from_dict on the json representation
        result_passage_answer_model_dict = ResultPassageAnswer.from_dict(result_passage_answer_model_json).__dict__
        result_passage_answer_model2 = ResultPassageAnswer(**result_passage_answer_model_dict)

        # Verify the model instances are equivalent
        assert result_passage_answer_model == result_passage_answer_model2

        # Convert model instance back to dict and verify no loss of data
        result_passage_answer_model_json2 = result_passage_answer_model.to_dict()
        assert result_passage_answer_model_json2 == result_passage_answer_model_json

class TestModel_RetrievalDetails():
    """
    Test Class for RetrievalDetails
    """

    def test_retrieval_details_serialization(self):
        """
        Test serialization/deserialization for RetrievalDetails
        """

        # Construct a json representation of a RetrievalDetails model
        retrieval_details_model_json = {}
        retrieval_details_model_json['document_retrieval_strategy'] = 'untrained'

        # Construct a model instance of RetrievalDetails by calling from_dict on the json representation
        retrieval_details_model = RetrievalDetails.from_dict(retrieval_details_model_json)
        assert retrieval_details_model != False

        # Construct a model instance of RetrievalDetails by calling from_dict on the json representation
        retrieval_details_model_dict = RetrievalDetails.from_dict(retrieval_details_model_json).__dict__
        retrieval_details_model2 = RetrievalDetails(**retrieval_details_model_dict)

        # Verify the model instances are equivalent
        assert retrieval_details_model == retrieval_details_model2

        # Convert model instance back to dict and verify no loss of data
        retrieval_details_model_json2 = retrieval_details_model.to_dict()
        assert retrieval_details_model_json2 == retrieval_details_model_json

class TestModel_StopWordList():
    """
    Test Class for StopWordList
    """

    def test_stop_word_list_serialization(self):
        """
        Test serialization/deserialization for StopWordList
        """

        # Construct a json representation of a StopWordList model
        stop_word_list_model_json = {}
        stop_word_list_model_json['stopwords'] = ['testString']

        # Construct a model instance of StopWordList by calling from_dict on the json representation
        stop_word_list_model = StopWordList.from_dict(stop_word_list_model_json)
        assert stop_word_list_model != False

        # Construct a model instance of StopWordList by calling from_dict on the json representation
        stop_word_list_model_dict = StopWordList.from_dict(stop_word_list_model_json).__dict__
        stop_word_list_model2 = StopWordList(**stop_word_list_model_dict)

        # Verify the model instances are equivalent
        assert stop_word_list_model == stop_word_list_model2

        # Convert model instance back to dict and verify no loss of data
        stop_word_list_model_json2 = stop_word_list_model.to_dict()
        assert stop_word_list_model_json2 == stop_word_list_model_json

class TestModel_TableBodyCells():
    """
    Test Class for TableBodyCells
    """

    def test_table_body_cells_serialization(self):
        """
        Test serialization/deserialization for TableBodyCells
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        # Construct a json representation of a TableBodyCells model
        table_body_cells_model_json = {}
        table_body_cells_model_json['cell_id'] = 'testString'
        table_body_cells_model_json['location'] = table_element_location_model
        table_body_cells_model_json['text'] = 'testString'
        table_body_cells_model_json['row_index_begin'] = 26
        table_body_cells_model_json['row_index_end'] = 26
        table_body_cells_model_json['column_index_begin'] = 26
        table_body_cells_model_json['column_index_end'] = 26
        table_body_cells_model_json['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model_json['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model_json['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model_json['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model_json['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model_json['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model_json['attributes'] = [document_attribute_model]

        # Construct a model instance of TableBodyCells by calling from_dict on the json representation
        table_body_cells_model = TableBodyCells.from_dict(table_body_cells_model_json)
        assert table_body_cells_model != False

        # Construct a model instance of TableBodyCells by calling from_dict on the json representation
        table_body_cells_model_dict = TableBodyCells.from_dict(table_body_cells_model_json).__dict__
        table_body_cells_model2 = TableBodyCells(**table_body_cells_model_dict)

        # Verify the model instances are equivalent
        assert table_body_cells_model == table_body_cells_model2

        # Convert model instance back to dict and verify no loss of data
        table_body_cells_model_json2 = table_body_cells_model.to_dict()
        assert table_body_cells_model_json2 == table_body_cells_model_json

class TestModel_TableCellKey():
    """
    Test Class for TableCellKey
    """

    def test_table_cell_key_serialization(self):
        """
        Test serialization/deserialization for TableCellKey
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableCellKey model
        table_cell_key_model_json = {}
        table_cell_key_model_json['cell_id'] = 'testString'
        table_cell_key_model_json['location'] = table_element_location_model
        table_cell_key_model_json['text'] = 'testString'

        # Construct a model instance of TableCellKey by calling from_dict on the json representation
        table_cell_key_model = TableCellKey.from_dict(table_cell_key_model_json)
        assert table_cell_key_model != False

        # Construct a model instance of TableCellKey by calling from_dict on the json representation
        table_cell_key_model_dict = TableCellKey.from_dict(table_cell_key_model_json).__dict__
        table_cell_key_model2 = TableCellKey(**table_cell_key_model_dict)

        # Verify the model instances are equivalent
        assert table_cell_key_model == table_cell_key_model2

        # Convert model instance back to dict and verify no loss of data
        table_cell_key_model_json2 = table_cell_key_model.to_dict()
        assert table_cell_key_model_json2 == table_cell_key_model_json

class TestModel_TableCellValues():
    """
    Test Class for TableCellValues
    """

    def test_table_cell_values_serialization(self):
        """
        Test serialization/deserialization for TableCellValues
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableCellValues model
        table_cell_values_model_json = {}
        table_cell_values_model_json['cell_id'] = 'testString'
        table_cell_values_model_json['location'] = table_element_location_model
        table_cell_values_model_json['text'] = 'testString'

        # Construct a model instance of TableCellValues by calling from_dict on the json representation
        table_cell_values_model = TableCellValues.from_dict(table_cell_values_model_json)
        assert table_cell_values_model != False

        # Construct a model instance of TableCellValues by calling from_dict on the json representation
        table_cell_values_model_dict = TableCellValues.from_dict(table_cell_values_model_json).__dict__
        table_cell_values_model2 = TableCellValues(**table_cell_values_model_dict)

        # Verify the model instances are equivalent
        assert table_cell_values_model == table_cell_values_model2

        # Convert model instance back to dict and verify no loss of data
        table_cell_values_model_json2 = table_cell_values_model.to_dict()
        assert table_cell_values_model_json2 == table_cell_values_model_json

class TestModel_TableColumnHeaderIds():
    """
    Test Class for TableColumnHeaderIds
    """

    def test_table_column_header_ids_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaderIds
        """

        # Construct a json representation of a TableColumnHeaderIds model
        table_column_header_ids_model_json = {}
        table_column_header_ids_model_json['id'] = 'testString'

        # Construct a model instance of TableColumnHeaderIds by calling from_dict on the json representation
        table_column_header_ids_model = TableColumnHeaderIds.from_dict(table_column_header_ids_model_json)
        assert table_column_header_ids_model != False

        # Construct a model instance of TableColumnHeaderIds by calling from_dict on the json representation
        table_column_header_ids_model_dict = TableColumnHeaderIds.from_dict(table_column_header_ids_model_json).__dict__
        table_column_header_ids_model2 = TableColumnHeaderIds(**table_column_header_ids_model_dict)

        # Verify the model instances are equivalent
        assert table_column_header_ids_model == table_column_header_ids_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_header_ids_model_json2 = table_column_header_ids_model.to_dict()
        assert table_column_header_ids_model_json2 == table_column_header_ids_model_json

class TestModel_TableColumnHeaderTexts():
    """
    Test Class for TableColumnHeaderTexts
    """

    def test_table_column_header_texts_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaderTexts
        """

        # Construct a json representation of a TableColumnHeaderTexts model
        table_column_header_texts_model_json = {}
        table_column_header_texts_model_json['text'] = 'testString'

        # Construct a model instance of TableColumnHeaderTexts by calling from_dict on the json representation
        table_column_header_texts_model = TableColumnHeaderTexts.from_dict(table_column_header_texts_model_json)
        assert table_column_header_texts_model != False

        # Construct a model instance of TableColumnHeaderTexts by calling from_dict on the json representation
        table_column_header_texts_model_dict = TableColumnHeaderTexts.from_dict(table_column_header_texts_model_json).__dict__
        table_column_header_texts_model2 = TableColumnHeaderTexts(**table_column_header_texts_model_dict)

        # Verify the model instances are equivalent
        assert table_column_header_texts_model == table_column_header_texts_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_header_texts_model_json2 = table_column_header_texts_model.to_dict()
        assert table_column_header_texts_model_json2 == table_column_header_texts_model_json

class TestModel_TableColumnHeaderTextsNormalized():
    """
    Test Class for TableColumnHeaderTextsNormalized
    """

    def test_table_column_header_texts_normalized_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaderTextsNormalized
        """

        # Construct a json representation of a TableColumnHeaderTextsNormalized model
        table_column_header_texts_normalized_model_json = {}
        table_column_header_texts_normalized_model_json['text_normalized'] = 'testString'

        # Construct a model instance of TableColumnHeaderTextsNormalized by calling from_dict on the json representation
        table_column_header_texts_normalized_model = TableColumnHeaderTextsNormalized.from_dict(table_column_header_texts_normalized_model_json)
        assert table_column_header_texts_normalized_model != False

        # Construct a model instance of TableColumnHeaderTextsNormalized by calling from_dict on the json representation
        table_column_header_texts_normalized_model_dict = TableColumnHeaderTextsNormalized.from_dict(table_column_header_texts_normalized_model_json).__dict__
        table_column_header_texts_normalized_model2 = TableColumnHeaderTextsNormalized(**table_column_header_texts_normalized_model_dict)

        # Verify the model instances are equivalent
        assert table_column_header_texts_normalized_model == table_column_header_texts_normalized_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_header_texts_normalized_model_json2 = table_column_header_texts_normalized_model.to_dict()
        assert table_column_header_texts_normalized_model_json2 == table_column_header_texts_normalized_model_json

class TestModel_TableColumnHeaders():
    """
    Test Class for TableColumnHeaders
    """

    def test_table_column_headers_serialization(self):
        """
        Test serialization/deserialization for TableColumnHeaders
        """

        # Construct a json representation of a TableColumnHeaders model
        table_column_headers_model_json = {}
        table_column_headers_model_json['cell_id'] = 'testString'
        table_column_headers_model_json['location'] = {'foo': 'bar'}
        table_column_headers_model_json['text'] = 'testString'
        table_column_headers_model_json['text_normalized'] = 'testString'
        table_column_headers_model_json['row_index_begin'] = 26
        table_column_headers_model_json['row_index_end'] = 26
        table_column_headers_model_json['column_index_begin'] = 26
        table_column_headers_model_json['column_index_end'] = 26

        # Construct a model instance of TableColumnHeaders by calling from_dict on the json representation
        table_column_headers_model = TableColumnHeaders.from_dict(table_column_headers_model_json)
        assert table_column_headers_model != False

        # Construct a model instance of TableColumnHeaders by calling from_dict on the json representation
        table_column_headers_model_dict = TableColumnHeaders.from_dict(table_column_headers_model_json).__dict__
        table_column_headers_model2 = TableColumnHeaders(**table_column_headers_model_dict)

        # Verify the model instances are equivalent
        assert table_column_headers_model == table_column_headers_model2

        # Convert model instance back to dict and verify no loss of data
        table_column_headers_model_json2 = table_column_headers_model.to_dict()
        assert table_column_headers_model_json2 == table_column_headers_model_json

class TestModel_TableElementLocation():
    """
    Test Class for TableElementLocation
    """

    def test_table_element_location_serialization(self):
        """
        Test serialization/deserialization for TableElementLocation
        """

        # Construct a json representation of a TableElementLocation model
        table_element_location_model_json = {}
        table_element_location_model_json['begin'] = 26
        table_element_location_model_json['end'] = 26

        # Construct a model instance of TableElementLocation by calling from_dict on the json representation
        table_element_location_model = TableElementLocation.from_dict(table_element_location_model_json)
        assert table_element_location_model != False

        # Construct a model instance of TableElementLocation by calling from_dict on the json representation
        table_element_location_model_dict = TableElementLocation.from_dict(table_element_location_model_json).__dict__
        table_element_location_model2 = TableElementLocation(**table_element_location_model_dict)

        # Verify the model instances are equivalent
        assert table_element_location_model == table_element_location_model2

        # Convert model instance back to dict and verify no loss of data
        table_element_location_model_json2 = table_element_location_model.to_dict()
        assert table_element_location_model_json2 == table_element_location_model_json

class TestModel_TableHeaders():
    """
    Test Class for TableHeaders
    """

    def test_table_headers_serialization(self):
        """
        Test serialization/deserialization for TableHeaders
        """

        # Construct a json representation of a TableHeaders model
        table_headers_model_json = {}
        table_headers_model_json['cell_id'] = 'testString'
        table_headers_model_json['location'] = {'foo': 'bar'}
        table_headers_model_json['text'] = 'testString'
        table_headers_model_json['row_index_begin'] = 26
        table_headers_model_json['row_index_end'] = 26
        table_headers_model_json['column_index_begin'] = 26
        table_headers_model_json['column_index_end'] = 26

        # Construct a model instance of TableHeaders by calling from_dict on the json representation
        table_headers_model = TableHeaders.from_dict(table_headers_model_json)
        assert table_headers_model != False

        # Construct a model instance of TableHeaders by calling from_dict on the json representation
        table_headers_model_dict = TableHeaders.from_dict(table_headers_model_json).__dict__
        table_headers_model2 = TableHeaders(**table_headers_model_dict)

        # Verify the model instances are equivalent
        assert table_headers_model == table_headers_model2

        # Convert model instance back to dict and verify no loss of data
        table_headers_model_json2 = table_headers_model.to_dict()
        assert table_headers_model_json2 == table_headers_model_json

class TestModel_TableKeyValuePairs():
    """
    Test Class for TableKeyValuePairs
    """

    def test_table_key_value_pairs_serialization(self):
        """
        Test serialization/deserialization for TableKeyValuePairs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        # Construct a json representation of a TableKeyValuePairs model
        table_key_value_pairs_model_json = {}
        table_key_value_pairs_model_json['key'] = table_cell_key_model
        table_key_value_pairs_model_json['value'] = [table_cell_values_model]

        # Construct a model instance of TableKeyValuePairs by calling from_dict on the json representation
        table_key_value_pairs_model = TableKeyValuePairs.from_dict(table_key_value_pairs_model_json)
        assert table_key_value_pairs_model != False

        # Construct a model instance of TableKeyValuePairs by calling from_dict on the json representation
        table_key_value_pairs_model_dict = TableKeyValuePairs.from_dict(table_key_value_pairs_model_json).__dict__
        table_key_value_pairs_model2 = TableKeyValuePairs(**table_key_value_pairs_model_dict)

        # Verify the model instances are equivalent
        assert table_key_value_pairs_model == table_key_value_pairs_model2

        # Convert model instance back to dict and verify no loss of data
        table_key_value_pairs_model_json2 = table_key_value_pairs_model.to_dict()
        assert table_key_value_pairs_model_json2 == table_key_value_pairs_model_json

class TestModel_TableResultTable():
    """
    Test Class for TableResultTable
    """

    def test_table_result_table_serialization(self):
        """
        Test serialization/deserialization for TableResultTable
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        table_text_location_model = {} # TableTextLocation
        table_text_location_model['text'] = 'testString'
        table_text_location_model['location'] = table_element_location_model

        table_headers_model = {} # TableHeaders
        table_headers_model['cell_id'] = 'testString'
        table_headers_model['location'] = {'foo': 'bar'}
        table_headers_model['text'] = 'testString'
        table_headers_model['row_index_begin'] = 26
        table_headers_model['row_index_end'] = 26
        table_headers_model['column_index_begin'] = 26
        table_headers_model['column_index_end'] = 26

        table_row_headers_model = {} # TableRowHeaders
        table_row_headers_model['cell_id'] = 'testString'
        table_row_headers_model['location'] = table_element_location_model
        table_row_headers_model['text'] = 'testString'
        table_row_headers_model['text_normalized'] = 'testString'
        table_row_headers_model['row_index_begin'] = 26
        table_row_headers_model['row_index_end'] = 26
        table_row_headers_model['column_index_begin'] = 26
        table_row_headers_model['column_index_end'] = 26

        table_column_headers_model = {} # TableColumnHeaders
        table_column_headers_model['cell_id'] = 'testString'
        table_column_headers_model['location'] = {'foo': 'bar'}
        table_column_headers_model['text'] = 'testString'
        table_column_headers_model['text_normalized'] = 'testString'
        table_column_headers_model['row_index_begin'] = 26
        table_column_headers_model['row_index_end'] = 26
        table_column_headers_model['column_index_begin'] = 26
        table_column_headers_model['column_index_end'] = 26

        table_cell_key_model = {} # TableCellKey
        table_cell_key_model['cell_id'] = 'testString'
        table_cell_key_model['location'] = table_element_location_model
        table_cell_key_model['text'] = 'testString'

        table_cell_values_model = {} # TableCellValues
        table_cell_values_model['cell_id'] = 'testString'
        table_cell_values_model['location'] = table_element_location_model
        table_cell_values_model['text'] = 'testString'

        table_key_value_pairs_model = {} # TableKeyValuePairs
        table_key_value_pairs_model['key'] = table_cell_key_model
        table_key_value_pairs_model['value'] = [table_cell_values_model]

        table_row_header_ids_model = {} # TableRowHeaderIds
        table_row_header_ids_model['id'] = 'testString'

        table_row_header_texts_model = {} # TableRowHeaderTexts
        table_row_header_texts_model['text'] = 'testString'

        table_row_header_texts_normalized_model = {} # TableRowHeaderTextsNormalized
        table_row_header_texts_normalized_model['text_normalized'] = 'testString'

        table_column_header_ids_model = {} # TableColumnHeaderIds
        table_column_header_ids_model['id'] = 'testString'

        table_column_header_texts_model = {} # TableColumnHeaderTexts
        table_column_header_texts_model['text'] = 'testString'

        table_column_header_texts_normalized_model = {} # TableColumnHeaderTextsNormalized
        table_column_header_texts_normalized_model['text_normalized'] = 'testString'

        document_attribute_model = {} # DocumentAttribute
        document_attribute_model['type'] = 'testString'
        document_attribute_model['text'] = 'testString'
        document_attribute_model['location'] = table_element_location_model

        table_body_cells_model = {} # TableBodyCells
        table_body_cells_model['cell_id'] = 'testString'
        table_body_cells_model['location'] = table_element_location_model
        table_body_cells_model['text'] = 'testString'
        table_body_cells_model['row_index_begin'] = 26
        table_body_cells_model['row_index_end'] = 26
        table_body_cells_model['column_index_begin'] = 26
        table_body_cells_model['column_index_end'] = 26
        table_body_cells_model['row_header_ids'] = [table_row_header_ids_model]
        table_body_cells_model['row_header_texts'] = [table_row_header_texts_model]
        table_body_cells_model['row_header_texts_normalized'] = [table_row_header_texts_normalized_model]
        table_body_cells_model['column_header_ids'] = [table_column_header_ids_model]
        table_body_cells_model['column_header_texts'] = [table_column_header_texts_model]
        table_body_cells_model['column_header_texts_normalized'] = [table_column_header_texts_normalized_model]
        table_body_cells_model['attributes'] = [document_attribute_model]

        # Construct a json representation of a TableResultTable model
        table_result_table_model_json = {}
        table_result_table_model_json['location'] = table_element_location_model
        table_result_table_model_json['text'] = 'testString'
        table_result_table_model_json['section_title'] = table_text_location_model
        table_result_table_model_json['title'] = table_text_location_model
        table_result_table_model_json['table_headers'] = [table_headers_model]
        table_result_table_model_json['row_headers'] = [table_row_headers_model]
        table_result_table_model_json['column_headers'] = [table_column_headers_model]
        table_result_table_model_json['key_value_pairs'] = [table_key_value_pairs_model]
        table_result_table_model_json['body_cells'] = [table_body_cells_model]
        table_result_table_model_json['contexts'] = [table_text_location_model]

        # Construct a model instance of TableResultTable by calling from_dict on the json representation
        table_result_table_model = TableResultTable.from_dict(table_result_table_model_json)
        assert table_result_table_model != False

        # Construct a model instance of TableResultTable by calling from_dict on the json representation
        table_result_table_model_dict = TableResultTable.from_dict(table_result_table_model_json).__dict__
        table_result_table_model2 = TableResultTable(**table_result_table_model_dict)

        # Verify the model instances are equivalent
        assert table_result_table_model == table_result_table_model2

        # Convert model instance back to dict and verify no loss of data
        table_result_table_model_json2 = table_result_table_model.to_dict()
        assert table_result_table_model_json2 == table_result_table_model_json

class TestModel_TableRowHeaderIds():
    """
    Test Class for TableRowHeaderIds
    """

    def test_table_row_header_ids_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaderIds
        """

        # Construct a json representation of a TableRowHeaderIds model
        table_row_header_ids_model_json = {}
        table_row_header_ids_model_json['id'] = 'testString'

        # Construct a model instance of TableRowHeaderIds by calling from_dict on the json representation
        table_row_header_ids_model = TableRowHeaderIds.from_dict(table_row_header_ids_model_json)
        assert table_row_header_ids_model != False

        # Construct a model instance of TableRowHeaderIds by calling from_dict on the json representation
        table_row_header_ids_model_dict = TableRowHeaderIds.from_dict(table_row_header_ids_model_json).__dict__
        table_row_header_ids_model2 = TableRowHeaderIds(**table_row_header_ids_model_dict)

        # Verify the model instances are equivalent
        assert table_row_header_ids_model == table_row_header_ids_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_header_ids_model_json2 = table_row_header_ids_model.to_dict()
        assert table_row_header_ids_model_json2 == table_row_header_ids_model_json

class TestModel_TableRowHeaderTexts():
    """
    Test Class for TableRowHeaderTexts
    """

    def test_table_row_header_texts_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaderTexts
        """

        # Construct a json representation of a TableRowHeaderTexts model
        table_row_header_texts_model_json = {}
        table_row_header_texts_model_json['text'] = 'testString'

        # Construct a model instance of TableRowHeaderTexts by calling from_dict on the json representation
        table_row_header_texts_model = TableRowHeaderTexts.from_dict(table_row_header_texts_model_json)
        assert table_row_header_texts_model != False

        # Construct a model instance of TableRowHeaderTexts by calling from_dict on the json representation
        table_row_header_texts_model_dict = TableRowHeaderTexts.from_dict(table_row_header_texts_model_json).__dict__
        table_row_header_texts_model2 = TableRowHeaderTexts(**table_row_header_texts_model_dict)

        # Verify the model instances are equivalent
        assert table_row_header_texts_model == table_row_header_texts_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_header_texts_model_json2 = table_row_header_texts_model.to_dict()
        assert table_row_header_texts_model_json2 == table_row_header_texts_model_json

class TestModel_TableRowHeaderTextsNormalized():
    """
    Test Class for TableRowHeaderTextsNormalized
    """

    def test_table_row_header_texts_normalized_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaderTextsNormalized
        """

        # Construct a json representation of a TableRowHeaderTextsNormalized model
        table_row_header_texts_normalized_model_json = {}
        table_row_header_texts_normalized_model_json['text_normalized'] = 'testString'

        # Construct a model instance of TableRowHeaderTextsNormalized by calling from_dict on the json representation
        table_row_header_texts_normalized_model = TableRowHeaderTextsNormalized.from_dict(table_row_header_texts_normalized_model_json)
        assert table_row_header_texts_normalized_model != False

        # Construct a model instance of TableRowHeaderTextsNormalized by calling from_dict on the json representation
        table_row_header_texts_normalized_model_dict = TableRowHeaderTextsNormalized.from_dict(table_row_header_texts_normalized_model_json).__dict__
        table_row_header_texts_normalized_model2 = TableRowHeaderTextsNormalized(**table_row_header_texts_normalized_model_dict)

        # Verify the model instances are equivalent
        assert table_row_header_texts_normalized_model == table_row_header_texts_normalized_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_header_texts_normalized_model_json2 = table_row_header_texts_normalized_model.to_dict()
        assert table_row_header_texts_normalized_model_json2 == table_row_header_texts_normalized_model_json

class TestModel_TableRowHeaders():
    """
    Test Class for TableRowHeaders
    """

    def test_table_row_headers_serialization(self):
        """
        Test serialization/deserialization for TableRowHeaders
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableRowHeaders model
        table_row_headers_model_json = {}
        table_row_headers_model_json['cell_id'] = 'testString'
        table_row_headers_model_json['location'] = table_element_location_model
        table_row_headers_model_json['text'] = 'testString'
        table_row_headers_model_json['text_normalized'] = 'testString'
        table_row_headers_model_json['row_index_begin'] = 26
        table_row_headers_model_json['row_index_end'] = 26
        table_row_headers_model_json['column_index_begin'] = 26
        table_row_headers_model_json['column_index_end'] = 26

        # Construct a model instance of TableRowHeaders by calling from_dict on the json representation
        table_row_headers_model = TableRowHeaders.from_dict(table_row_headers_model_json)
        assert table_row_headers_model != False

        # Construct a model instance of TableRowHeaders by calling from_dict on the json representation
        table_row_headers_model_dict = TableRowHeaders.from_dict(table_row_headers_model_json).__dict__
        table_row_headers_model2 = TableRowHeaders(**table_row_headers_model_dict)

        # Verify the model instances are equivalent
        assert table_row_headers_model == table_row_headers_model2

        # Convert model instance back to dict and verify no loss of data
        table_row_headers_model_json2 = table_row_headers_model.to_dict()
        assert table_row_headers_model_json2 == table_row_headers_model_json

class TestModel_TableTextLocation():
    """
    Test Class for TableTextLocation
    """

    def test_table_text_location_serialization(self):
        """
        Test serialization/deserialization for TableTextLocation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        table_element_location_model = {} # TableElementLocation
        table_element_location_model['begin'] = 26
        table_element_location_model['end'] = 26

        # Construct a json representation of a TableTextLocation model
        table_text_location_model_json = {}
        table_text_location_model_json['text'] = 'testString'
        table_text_location_model_json['location'] = table_element_location_model

        # Construct a model instance of TableTextLocation by calling from_dict on the json representation
        table_text_location_model = TableTextLocation.from_dict(table_text_location_model_json)
        assert table_text_location_model != False

        # Construct a model instance of TableTextLocation by calling from_dict on the json representation
        table_text_location_model_dict = TableTextLocation.from_dict(table_text_location_model_json).__dict__
        table_text_location_model2 = TableTextLocation(**table_text_location_model_dict)

        # Verify the model instances are equivalent
        assert table_text_location_model == table_text_location_model2

        # Convert model instance back to dict and verify no loss of data
        table_text_location_model_json2 = table_text_location_model.to_dict()
        assert table_text_location_model_json2 == table_text_location_model_json

class TestModel_TrainingExample():
    """
    Test Class for TrainingExample
    """

    def test_training_example_serialization(self):
        """
        Test serialization/deserialization for TrainingExample
        """

        # Construct a json representation of a TrainingExample model
        training_example_model_json = {}
        training_example_model_json['document_id'] = 'testString'
        training_example_model_json['collection_id'] = 'testString'
        training_example_model_json['relevance'] = 38

        # Construct a model instance of TrainingExample by calling from_dict on the json representation
        training_example_model = TrainingExample.from_dict(training_example_model_json)
        assert training_example_model != False

        # Construct a model instance of TrainingExample by calling from_dict on the json representation
        training_example_model_dict = TrainingExample.from_dict(training_example_model_json).__dict__
        training_example_model2 = TrainingExample(**training_example_model_dict)

        # Verify the model instances are equivalent
        assert training_example_model == training_example_model2

        # Convert model instance back to dict and verify no loss of data
        training_example_model_json2 = training_example_model.to_dict()
        assert training_example_model_json2 == training_example_model_json

class TestModel_TrainingQuery():
    """
    Test Class for TrainingQuery
    """

    def test_training_query_serialization(self):
        """
        Test serialization/deserialization for TrainingQuery
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_example_model = {} # TrainingExample
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        # Construct a json representation of a TrainingQuery model
        training_query_model_json = {}
        training_query_model_json['natural_language_query'] = 'testString'
        training_query_model_json['filter'] = 'testString'
        training_query_model_json['examples'] = [training_example_model]

        # Construct a model instance of TrainingQuery by calling from_dict on the json representation
        training_query_model = TrainingQuery.from_dict(training_query_model_json)
        assert training_query_model != False

        # Construct a model instance of TrainingQuery by calling from_dict on the json representation
        training_query_model_dict = TrainingQuery.from_dict(training_query_model_json).__dict__
        training_query_model2 = TrainingQuery(**training_query_model_dict)

        # Verify the model instances are equivalent
        assert training_query_model == training_query_model2

        # Convert model instance back to dict and verify no loss of data
        training_query_model_json2 = training_query_model.to_dict()
        assert training_query_model_json2 == training_query_model_json

class TestModel_TrainingQuerySet():
    """
    Test Class for TrainingQuerySet
    """

    def test_training_query_set_serialization(self):
        """
        Test serialization/deserialization for TrainingQuerySet
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_example_model = {} # TrainingExample
        training_example_model['document_id'] = 'testString'
        training_example_model['collection_id'] = 'testString'
        training_example_model['relevance'] = 38

        training_query_model = {} # TrainingQuery
        training_query_model['natural_language_query'] = 'testString'
        training_query_model['filter'] = 'testString'
        training_query_model['examples'] = [training_example_model]

        # Construct a json representation of a TrainingQuerySet model
        training_query_set_model_json = {}
        training_query_set_model_json['queries'] = [training_query_model]

        # Construct a model instance of TrainingQuerySet by calling from_dict on the json representation
        training_query_set_model = TrainingQuerySet.from_dict(training_query_set_model_json)
        assert training_query_set_model != False

        # Construct a model instance of TrainingQuerySet by calling from_dict on the json representation
        training_query_set_model_dict = TrainingQuerySet.from_dict(training_query_set_model_json).__dict__
        training_query_set_model2 = TrainingQuerySet(**training_query_set_model_dict)

        # Verify the model instances are equivalent
        assert training_query_set_model == training_query_set_model2

        # Convert model instance back to dict and verify no loss of data
        training_query_set_model_json2 = training_query_set_model.to_dict()
        assert training_query_set_model_json2 == training_query_set_model_json

class TestModel_UpdateDocumentClassifier():
    """
    Test Class for UpdateDocumentClassifier
    """

    def test_update_document_classifier_serialization(self):
        """
        Test serialization/deserialization for UpdateDocumentClassifier
        """

        # Construct a json representation of a UpdateDocumentClassifier model
        update_document_classifier_model_json = {}
        update_document_classifier_model_json['name'] = 'testString'
        update_document_classifier_model_json['description'] = 'testString'

        # Construct a model instance of UpdateDocumentClassifier by calling from_dict on the json representation
        update_document_classifier_model = UpdateDocumentClassifier.from_dict(update_document_classifier_model_json)
        assert update_document_classifier_model != False

        # Construct a model instance of UpdateDocumentClassifier by calling from_dict on the json representation
        update_document_classifier_model_dict = UpdateDocumentClassifier.from_dict(update_document_classifier_model_json).__dict__
        update_document_classifier_model2 = UpdateDocumentClassifier(**update_document_classifier_model_dict)

        # Verify the model instances are equivalent
        assert update_document_classifier_model == update_document_classifier_model2

        # Convert model instance back to dict and verify no loss of data
        update_document_classifier_model_json2 = update_document_classifier_model.to_dict()
        assert update_document_classifier_model_json2 == update_document_classifier_model_json

class TestModel_QueryAggregationQueryCalculationAggregation():
    """
    Test Class for QueryAggregationQueryCalculationAggregation
    """

    def test_query_aggregation_query_calculation_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryCalculationAggregation
        """

        # Construct a json representation of a QueryAggregationQueryCalculationAggregation model
        query_aggregation_query_calculation_aggregation_model_json = {}
        query_aggregation_query_calculation_aggregation_model_json['type'] = 'unique_count'
        query_aggregation_query_calculation_aggregation_model_json['field'] = 'testString'
        query_aggregation_query_calculation_aggregation_model_json['value'] = 72.5

        # Construct a model instance of QueryAggregationQueryCalculationAggregation by calling from_dict on the json representation
        query_aggregation_query_calculation_aggregation_model = QueryAggregationQueryCalculationAggregation.from_dict(query_aggregation_query_calculation_aggregation_model_json)
        assert query_aggregation_query_calculation_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryCalculationAggregation by calling from_dict on the json representation
        query_aggregation_query_calculation_aggregation_model_dict = QueryAggregationQueryCalculationAggregation.from_dict(query_aggregation_query_calculation_aggregation_model_json).__dict__
        query_aggregation_query_calculation_aggregation_model2 = QueryAggregationQueryCalculationAggregation(**query_aggregation_query_calculation_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_calculation_aggregation_model == query_aggregation_query_calculation_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_calculation_aggregation_model_json2 = query_aggregation_query_calculation_aggregation_model.to_dict()
        assert query_aggregation_query_calculation_aggregation_model_json2 == query_aggregation_query_calculation_aggregation_model_json

class TestModel_QueryAggregationQueryFilterAggregation():
    """
    Test Class for QueryAggregationQueryFilterAggregation
    """

    def test_query_aggregation_query_filter_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryFilterAggregation
        """

        # Construct a json representation of a QueryAggregationQueryFilterAggregation model
        query_aggregation_query_filter_aggregation_model_json = {}
        query_aggregation_query_filter_aggregation_model_json['type'] = 'filter'
        query_aggregation_query_filter_aggregation_model_json['match'] = 'testString'
        query_aggregation_query_filter_aggregation_model_json['matching_results'] = 26
        query_aggregation_query_filter_aggregation_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryAggregationQueryFilterAggregation by calling from_dict on the json representation
        query_aggregation_query_filter_aggregation_model = QueryAggregationQueryFilterAggregation.from_dict(query_aggregation_query_filter_aggregation_model_json)
        assert query_aggregation_query_filter_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryFilterAggregation by calling from_dict on the json representation
        query_aggregation_query_filter_aggregation_model_dict = QueryAggregationQueryFilterAggregation.from_dict(query_aggregation_query_filter_aggregation_model_json).__dict__
        query_aggregation_query_filter_aggregation_model2 = QueryAggregationQueryFilterAggregation(**query_aggregation_query_filter_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_filter_aggregation_model == query_aggregation_query_filter_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_filter_aggregation_model_json2 = query_aggregation_query_filter_aggregation_model.to_dict()
        assert query_aggregation_query_filter_aggregation_model_json2 == query_aggregation_query_filter_aggregation_model_json

class TestModel_QueryAggregationQueryGroupByAggregation():
    """
    Test Class for QueryAggregationQueryGroupByAggregation
    """

    def test_query_aggregation_query_group_by_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryGroupByAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_group_by_aggregation_result_model = {} # QueryGroupByAggregationResult
        query_group_by_aggregation_result_model['key'] = 'testString'
        query_group_by_aggregation_result_model['matching_results'] = 38
        query_group_by_aggregation_result_model['relevancy'] = 72.5
        query_group_by_aggregation_result_model['total_matching_documents'] = 38
        query_group_by_aggregation_result_model['estimated_matching_results'] = 72.5
        query_group_by_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryGroupByAggregation model
        query_aggregation_query_group_by_aggregation_model_json = {}
        query_aggregation_query_group_by_aggregation_model_json['type'] = 'group_by'
        query_aggregation_query_group_by_aggregation_model_json['results'] = [query_group_by_aggregation_result_model]

        # Construct a model instance of QueryAggregationQueryGroupByAggregation by calling from_dict on the json representation
        query_aggregation_query_group_by_aggregation_model = QueryAggregationQueryGroupByAggregation.from_dict(query_aggregation_query_group_by_aggregation_model_json)
        assert query_aggregation_query_group_by_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryGroupByAggregation by calling from_dict on the json representation
        query_aggregation_query_group_by_aggregation_model_dict = QueryAggregationQueryGroupByAggregation.from_dict(query_aggregation_query_group_by_aggregation_model_json).__dict__
        query_aggregation_query_group_by_aggregation_model2 = QueryAggregationQueryGroupByAggregation(**query_aggregation_query_group_by_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_group_by_aggregation_model == query_aggregation_query_group_by_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_group_by_aggregation_model_json2 = query_aggregation_query_group_by_aggregation_model.to_dict()
        assert query_aggregation_query_group_by_aggregation_model_json2 == query_aggregation_query_group_by_aggregation_model_json

class TestModel_QueryAggregationQueryHistogramAggregation():
    """
    Test Class for QueryAggregationQueryHistogramAggregation
    """

    def test_query_aggregation_query_histogram_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryHistogramAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_histogram_aggregation_result_model = {} # QueryHistogramAggregationResult
        query_histogram_aggregation_result_model['key'] = 26
        query_histogram_aggregation_result_model['matching_results'] = 38
        query_histogram_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryHistogramAggregation model
        query_aggregation_query_histogram_aggregation_model_json = {}
        query_aggregation_query_histogram_aggregation_model_json['type'] = 'histogram'
        query_aggregation_query_histogram_aggregation_model_json['field'] = 'testString'
        query_aggregation_query_histogram_aggregation_model_json['interval'] = 38
        query_aggregation_query_histogram_aggregation_model_json['name'] = 'testString'
        query_aggregation_query_histogram_aggregation_model_json['results'] = [query_histogram_aggregation_result_model]

        # Construct a model instance of QueryAggregationQueryHistogramAggregation by calling from_dict on the json representation
        query_aggregation_query_histogram_aggregation_model = QueryAggregationQueryHistogramAggregation.from_dict(query_aggregation_query_histogram_aggregation_model_json)
        assert query_aggregation_query_histogram_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryHistogramAggregation by calling from_dict on the json representation
        query_aggregation_query_histogram_aggregation_model_dict = QueryAggregationQueryHistogramAggregation.from_dict(query_aggregation_query_histogram_aggregation_model_json).__dict__
        query_aggregation_query_histogram_aggregation_model2 = QueryAggregationQueryHistogramAggregation(**query_aggregation_query_histogram_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_histogram_aggregation_model == query_aggregation_query_histogram_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_histogram_aggregation_model_json2 = query_aggregation_query_histogram_aggregation_model.to_dict()
        assert query_aggregation_query_histogram_aggregation_model_json2 == query_aggregation_query_histogram_aggregation_model_json

class TestModel_QueryAggregationQueryNestedAggregation():
    """
    Test Class for QueryAggregationQueryNestedAggregation
    """

    def test_query_aggregation_query_nested_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryNestedAggregation
        """

        # Construct a json representation of a QueryAggregationQueryNestedAggregation model
        query_aggregation_query_nested_aggregation_model_json = {}
        query_aggregation_query_nested_aggregation_model_json['type'] = 'nested'
        query_aggregation_query_nested_aggregation_model_json['path'] = 'testString'
        query_aggregation_query_nested_aggregation_model_json['matching_results'] = 26
        query_aggregation_query_nested_aggregation_model_json['aggregations'] = [{'foo': 'bar'}]

        # Construct a model instance of QueryAggregationQueryNestedAggregation by calling from_dict on the json representation
        query_aggregation_query_nested_aggregation_model = QueryAggregationQueryNestedAggregation.from_dict(query_aggregation_query_nested_aggregation_model_json)
        assert query_aggregation_query_nested_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryNestedAggregation by calling from_dict on the json representation
        query_aggregation_query_nested_aggregation_model_dict = QueryAggregationQueryNestedAggregation.from_dict(query_aggregation_query_nested_aggregation_model_json).__dict__
        query_aggregation_query_nested_aggregation_model2 = QueryAggregationQueryNestedAggregation(**query_aggregation_query_nested_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_nested_aggregation_model == query_aggregation_query_nested_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_nested_aggregation_model_json2 = query_aggregation_query_nested_aggregation_model.to_dict()
        assert query_aggregation_query_nested_aggregation_model_json2 == query_aggregation_query_nested_aggregation_model_json

class TestModel_QueryAggregationQueryPairAggregation():
    """
    Test Class for QueryAggregationQueryPairAggregation
    """

    def test_query_aggregation_query_pair_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryPairAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_pair_aggregation_result_model = {} # QueryPairAggregationResult
        query_pair_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryPairAggregation model
        query_aggregation_query_pair_aggregation_model_json = {}
        query_aggregation_query_pair_aggregation_model_json['type'] = 'pair'
        query_aggregation_query_pair_aggregation_model_json['first'] = 'testString'
        query_aggregation_query_pair_aggregation_model_json['second'] = 'testString'
        query_aggregation_query_pair_aggregation_model_json['show_estimated_matching_results'] = False
        query_aggregation_query_pair_aggregation_model_json['show_total_matching_documents'] = False
        query_aggregation_query_pair_aggregation_model_json['results'] = [query_pair_aggregation_result_model]

        # Construct a model instance of QueryAggregationQueryPairAggregation by calling from_dict on the json representation
        query_aggregation_query_pair_aggregation_model = QueryAggregationQueryPairAggregation.from_dict(query_aggregation_query_pair_aggregation_model_json)
        assert query_aggregation_query_pair_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryPairAggregation by calling from_dict on the json representation
        query_aggregation_query_pair_aggregation_model_dict = QueryAggregationQueryPairAggregation.from_dict(query_aggregation_query_pair_aggregation_model_json).__dict__
        query_aggregation_query_pair_aggregation_model2 = QueryAggregationQueryPairAggregation(**query_aggregation_query_pair_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_pair_aggregation_model == query_aggregation_query_pair_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_pair_aggregation_model_json2 = query_aggregation_query_pair_aggregation_model.to_dict()
        assert query_aggregation_query_pair_aggregation_model_json2 == query_aggregation_query_pair_aggregation_model_json

class TestModel_QueryAggregationQueryTermAggregation():
    """
    Test Class for QueryAggregationQueryTermAggregation
    """

    def test_query_aggregation_query_term_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryTermAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_term_aggregation_result_model = {} # QueryTermAggregationResult
        query_term_aggregation_result_model['key'] = 'testString'
        query_term_aggregation_result_model['matching_results'] = 38
        query_term_aggregation_result_model['relevancy'] = 72.5
        query_term_aggregation_result_model['total_matching_documents'] = 38
        query_term_aggregation_result_model['estimated_matching_results'] = 72.5
        query_term_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryTermAggregation model
        query_aggregation_query_term_aggregation_model_json = {}
        query_aggregation_query_term_aggregation_model_json['type'] = 'term'
        query_aggregation_query_term_aggregation_model_json['field'] = 'testString'
        query_aggregation_query_term_aggregation_model_json['count'] = 38
        query_aggregation_query_term_aggregation_model_json['name'] = 'testString'
        query_aggregation_query_term_aggregation_model_json['results'] = [query_term_aggregation_result_model]

        # Construct a model instance of QueryAggregationQueryTermAggregation by calling from_dict on the json representation
        query_aggregation_query_term_aggregation_model = QueryAggregationQueryTermAggregation.from_dict(query_aggregation_query_term_aggregation_model_json)
        assert query_aggregation_query_term_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryTermAggregation by calling from_dict on the json representation
        query_aggregation_query_term_aggregation_model_dict = QueryAggregationQueryTermAggregation.from_dict(query_aggregation_query_term_aggregation_model_json).__dict__
        query_aggregation_query_term_aggregation_model2 = QueryAggregationQueryTermAggregation(**query_aggregation_query_term_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_term_aggregation_model == query_aggregation_query_term_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_term_aggregation_model_json2 = query_aggregation_query_term_aggregation_model.to_dict()
        assert query_aggregation_query_term_aggregation_model_json2 == query_aggregation_query_term_aggregation_model_json

class TestModel_QueryAggregationQueryTimesliceAggregation():
    """
    Test Class for QueryAggregationQueryTimesliceAggregation
    """

    def test_query_aggregation_query_timeslice_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryTimesliceAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_timeslice_aggregation_result_model = {} # QueryTimesliceAggregationResult
        query_timeslice_aggregation_result_model['key_as_string'] = 'testString'
        query_timeslice_aggregation_result_model['key'] = 26
        query_timeslice_aggregation_result_model['matching_results'] = 26
        query_timeslice_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryTimesliceAggregation model
        query_aggregation_query_timeslice_aggregation_model_json = {}
        query_aggregation_query_timeslice_aggregation_model_json['type'] = 'timeslice'
        query_aggregation_query_timeslice_aggregation_model_json['field'] = 'testString'
        query_aggregation_query_timeslice_aggregation_model_json['interval'] = 'testString'
        query_aggregation_query_timeslice_aggregation_model_json['name'] = 'testString'
        query_aggregation_query_timeslice_aggregation_model_json['results'] = [query_timeslice_aggregation_result_model]

        # Construct a model instance of QueryAggregationQueryTimesliceAggregation by calling from_dict on the json representation
        query_aggregation_query_timeslice_aggregation_model = QueryAggregationQueryTimesliceAggregation.from_dict(query_aggregation_query_timeslice_aggregation_model_json)
        assert query_aggregation_query_timeslice_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryTimesliceAggregation by calling from_dict on the json representation
        query_aggregation_query_timeslice_aggregation_model_dict = QueryAggregationQueryTimesliceAggregation.from_dict(query_aggregation_query_timeslice_aggregation_model_json).__dict__
        query_aggregation_query_timeslice_aggregation_model2 = QueryAggregationQueryTimesliceAggregation(**query_aggregation_query_timeslice_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_timeslice_aggregation_model == query_aggregation_query_timeslice_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_timeslice_aggregation_model_json2 = query_aggregation_query_timeslice_aggregation_model.to_dict()
        assert query_aggregation_query_timeslice_aggregation_model_json2 == query_aggregation_query_timeslice_aggregation_model_json

class TestModel_QueryAggregationQueryTopHitsAggregation():
    """
    Test Class for QueryAggregationQueryTopHitsAggregation
    """

    def test_query_aggregation_query_top_hits_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryTopHitsAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_top_hits_aggregation_result_model = {} # QueryTopHitsAggregationResult
        query_top_hits_aggregation_result_model['matching_results'] = 38
        query_top_hits_aggregation_result_model['hits'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryTopHitsAggregation model
        query_aggregation_query_top_hits_aggregation_model_json = {}
        query_aggregation_query_top_hits_aggregation_model_json['type'] = 'top_hits'
        query_aggregation_query_top_hits_aggregation_model_json['size'] = 38
        query_aggregation_query_top_hits_aggregation_model_json['name'] = 'testString'
        query_aggregation_query_top_hits_aggregation_model_json['hits'] = query_top_hits_aggregation_result_model

        # Construct a model instance of QueryAggregationQueryTopHitsAggregation by calling from_dict on the json representation
        query_aggregation_query_top_hits_aggregation_model = QueryAggregationQueryTopHitsAggregation.from_dict(query_aggregation_query_top_hits_aggregation_model_json)
        assert query_aggregation_query_top_hits_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryTopHitsAggregation by calling from_dict on the json representation
        query_aggregation_query_top_hits_aggregation_model_dict = QueryAggregationQueryTopHitsAggregation.from_dict(query_aggregation_query_top_hits_aggregation_model_json).__dict__
        query_aggregation_query_top_hits_aggregation_model2 = QueryAggregationQueryTopHitsAggregation(**query_aggregation_query_top_hits_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_top_hits_aggregation_model == query_aggregation_query_top_hits_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_top_hits_aggregation_model_json2 = query_aggregation_query_top_hits_aggregation_model.to_dict()
        assert query_aggregation_query_top_hits_aggregation_model_json2 == query_aggregation_query_top_hits_aggregation_model_json

class TestModel_QueryAggregationQueryTopicAggregation():
    """
    Test Class for QueryAggregationQueryTopicAggregation
    """

    def test_query_aggregation_query_topic_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryTopicAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_topic_aggregation_result_model = {} # QueryTopicAggregationResult
        query_topic_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryTopicAggregation model
        query_aggregation_query_topic_aggregation_model_json = {}
        query_aggregation_query_topic_aggregation_model_json['type'] = 'topic'
        query_aggregation_query_topic_aggregation_model_json['facet'] = 'testString'
        query_aggregation_query_topic_aggregation_model_json['time_segments'] = 'testString'
        query_aggregation_query_topic_aggregation_model_json['show_estimated_matching_results'] = False
        query_aggregation_query_topic_aggregation_model_json['show_total_matching_documents'] = False
        query_aggregation_query_topic_aggregation_model_json['results'] = [query_topic_aggregation_result_model]

        # Construct a model instance of QueryAggregationQueryTopicAggregation by calling from_dict on the json representation
        query_aggregation_query_topic_aggregation_model = QueryAggregationQueryTopicAggregation.from_dict(query_aggregation_query_topic_aggregation_model_json)
        assert query_aggregation_query_topic_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryTopicAggregation by calling from_dict on the json representation
        query_aggregation_query_topic_aggregation_model_dict = QueryAggregationQueryTopicAggregation.from_dict(query_aggregation_query_topic_aggregation_model_json).__dict__
        query_aggregation_query_topic_aggregation_model2 = QueryAggregationQueryTopicAggregation(**query_aggregation_query_topic_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_topic_aggregation_model == query_aggregation_query_topic_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_topic_aggregation_model_json2 = query_aggregation_query_topic_aggregation_model.to_dict()
        assert query_aggregation_query_topic_aggregation_model_json2 == query_aggregation_query_topic_aggregation_model_json

class TestModel_QueryAggregationQueryTrendAggregation():
    """
    Test Class for QueryAggregationQueryTrendAggregation
    """

    def test_query_aggregation_query_trend_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregationQueryTrendAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_trend_aggregation_result_model = {} # QueryTrendAggregationResult
        query_trend_aggregation_result_model['aggregations'] = [{'foo': 'bar'}]

        # Construct a json representation of a QueryAggregationQueryTrendAggregation model
        query_aggregation_query_trend_aggregation_model_json = {}
        query_aggregation_query_trend_aggregation_model_json['type'] = 'trend'
        query_aggregation_query_trend_aggregation_model_json['facet'] = 'testString'
        query_aggregation_query_trend_aggregation_model_json['time_segments'] = 'testString'
        query_aggregation_query_trend_aggregation_model_json['show_estimated_matching_results'] = False
        query_aggregation_query_trend_aggregation_model_json['show_total_matching_documents'] = False
        query_aggregation_query_trend_aggregation_model_json['results'] = [query_trend_aggregation_result_model]

        # Construct a model instance of QueryAggregationQueryTrendAggregation by calling from_dict on the json representation
        query_aggregation_query_trend_aggregation_model = QueryAggregationQueryTrendAggregation.from_dict(query_aggregation_query_trend_aggregation_model_json)
        assert query_aggregation_query_trend_aggregation_model != False

        # Construct a model instance of QueryAggregationQueryTrendAggregation by calling from_dict on the json representation
        query_aggregation_query_trend_aggregation_model_dict = QueryAggregationQueryTrendAggregation.from_dict(query_aggregation_query_trend_aggregation_model_json).__dict__
        query_aggregation_query_trend_aggregation_model2 = QueryAggregationQueryTrendAggregation(**query_aggregation_query_trend_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert query_aggregation_query_trend_aggregation_model == query_aggregation_query_trend_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_query_trend_aggregation_model_json2 = query_aggregation_query_trend_aggregation_model.to_dict()
        assert query_aggregation_query_trend_aggregation_model_json2 == query_aggregation_query_trend_aggregation_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
