# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2019, 2024.
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
Unit Tests for AssistantV2
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
from ibm_watson.assistant_v2 import *

version = 'testString'

_service = AssistantV2(
    authenticator=NoAuthAuthenticator(),
    version=version,
)

_base_url = 'https://api.us-south.assistant.watson.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: ConversationalSkillProviders
##############################################################################
# region


class TestCreateProvider:
    """
    Test Class for create_provider
    """

    @responses.activate
    def test_create_provider_all_params(self):
        """
        create_provider()
        """
        # Set up mock
        url = preprocess_url('/v2/providers')
        mock_response = '{"provider_id": "provider_id", "specification": {"servers": [{"url": "url"}], "components": {"securitySchemes": {"authentication_method": "basic", "basic": {"username": {"type": "value", "value": "value"}}, "oauth2": {"preferred_flow": "password", "flows": {"token_url": "token_url", "refresh_url": "refresh_url", "client_auth_type": "Body", "content_type": "content_type", "header_prefix": "header_prefix", "username": {"type": "value", "value": "value"}}}}}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProviderSpecificationServersItem model
        provider_specification_servers_item_model = {}
        provider_specification_servers_item_model['url'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationTypeAndValue model
        provider_authentication_type_and_value_model = {}
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemesBasic model
        provider_specification_components_security_schemes_basic_model = {}
        provider_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2PasswordUsername model
        provider_authentication_o_auth2_password_username_model = {}
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password model
        provider_authentication_o_auth2_flows_model = {}
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2 model
        provider_authentication_o_auth2_model = {}
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemes model
        provider_specification_components_security_schemes_model = {}
        provider_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_specification_components_security_schemes_model['basic'] = provider_specification_components_security_schemes_basic_model
        provider_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        # Construct a dict representation of a ProviderSpecificationComponents model
        provider_specification_components_model = {}
        provider_specification_components_model['securitySchemes'] = provider_specification_components_security_schemes_model

        # Construct a dict representation of a ProviderSpecification model
        provider_specification_model = {}
        provider_specification_model['servers'] = [provider_specification_servers_item_model]
        provider_specification_model['components'] = provider_specification_components_model

        # Construct a dict representation of a ProviderPrivateAuthenticationBearerFlow model
        provider_private_authentication_model = {}
        provider_private_authentication_model['token'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderPrivate model
        provider_private_model = {}
        provider_private_model['authentication'] = provider_private_authentication_model

        # Set up parameter values
        provider_id = 'testString'
        specification = provider_specification_model
        private = provider_private_model

        # Invoke method
        response = _service.create_provider(
            provider_id,
            specification,
            private,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['provider_id'] == 'testString'
        assert req_body['specification'] == provider_specification_model
        assert req_body['private'] == provider_private_model

    def test_create_provider_all_params_with_retries(self):
        # Enable retries and run test_create_provider_all_params.
        _service.enable_retries()
        self.test_create_provider_all_params()

        # Disable retries and run test_create_provider_all_params.
        _service.disable_retries()
        self.test_create_provider_all_params()

    @responses.activate
    def test_create_provider_value_error(self):
        """
        test_create_provider_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/providers')
        mock_response = '{"provider_id": "provider_id", "specification": {"servers": [{"url": "url"}], "components": {"securitySchemes": {"authentication_method": "basic", "basic": {"username": {"type": "value", "value": "value"}}, "oauth2": {"preferred_flow": "password", "flows": {"token_url": "token_url", "refresh_url": "refresh_url", "client_auth_type": "Body", "content_type": "content_type", "header_prefix": "header_prefix", "username": {"type": "value", "value": "value"}}}}}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProviderSpecificationServersItem model
        provider_specification_servers_item_model = {}
        provider_specification_servers_item_model['url'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationTypeAndValue model
        provider_authentication_type_and_value_model = {}
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemesBasic model
        provider_specification_components_security_schemes_basic_model = {}
        provider_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2PasswordUsername model
        provider_authentication_o_auth2_password_username_model = {}
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password model
        provider_authentication_o_auth2_flows_model = {}
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2 model
        provider_authentication_o_auth2_model = {}
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemes model
        provider_specification_components_security_schemes_model = {}
        provider_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_specification_components_security_schemes_model['basic'] = provider_specification_components_security_schemes_basic_model
        provider_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        # Construct a dict representation of a ProviderSpecificationComponents model
        provider_specification_components_model = {}
        provider_specification_components_model['securitySchemes'] = provider_specification_components_security_schemes_model

        # Construct a dict representation of a ProviderSpecification model
        provider_specification_model = {}
        provider_specification_model['servers'] = [provider_specification_servers_item_model]
        provider_specification_model['components'] = provider_specification_components_model

        # Construct a dict representation of a ProviderPrivateAuthenticationBearerFlow model
        provider_private_authentication_model = {}
        provider_private_authentication_model['token'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderPrivate model
        provider_private_model = {}
        provider_private_model['authentication'] = provider_private_authentication_model

        # Set up parameter values
        provider_id = 'testString'
        specification = provider_specification_model
        private = provider_private_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "specification": specification,
            "private": private,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_provider(**req_copy)

    def test_create_provider_value_error_with_retries(self):
        # Enable retries and run test_create_provider_value_error.
        _service.enable_retries()
        self.test_create_provider_value_error()

        # Disable retries and run test_create_provider_value_error.
        _service.disable_retries()
        self.test_create_provider_value_error()


class TestListProviders:
    """
    Test Class for list_providers
    """

    @responses.activate
    def test_list_providers_all_params(self):
        """
        list_providers()
        """
        # Set up mock
        url = preprocess_url('/v2/providers')
        mock_response = '{"conversational_skill_providers": [{"provider_id": "provider_id", "specification": {"servers": [{"url": "url"}], "components": {"securitySchemes": {"authentication_method": "basic", "basic": {"username": {"type": "value", "value": "value"}}, "oauth2": {"preferred_flow": "password", "flows": {"token_url": "token_url", "refresh_url": "refresh_url", "client_auth_type": "Body", "content_type": "content_type", "header_prefix": "header_prefix", "username": {"type": "value", "value": "value"}}}}}}}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_limit = 100
        include_count = False
        sort = 'name'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_providers(
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_list_providers_all_params_with_retries(self):
        # Enable retries and run test_list_providers_all_params.
        _service.enable_retries()
        self.test_list_providers_all_params()

        # Disable retries and run test_list_providers_all_params.
        _service.disable_retries()
        self.test_list_providers_all_params()

    @responses.activate
    def test_list_providers_required_params(self):
        """
        test_list_providers_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/providers')
        mock_response = '{"conversational_skill_providers": [{"provider_id": "provider_id", "specification": {"servers": [{"url": "url"}], "components": {"securitySchemes": {"authentication_method": "basic", "basic": {"username": {"type": "value", "value": "value"}}, "oauth2": {"preferred_flow": "password", "flows": {"token_url": "token_url", "refresh_url": "refresh_url", "client_auth_type": "Body", "content_type": "content_type", "header_prefix": "header_prefix", "username": {"type": "value", "value": "value"}}}}}}}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_providers()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_providers_required_params_with_retries(self):
        # Enable retries and run test_list_providers_required_params.
        _service.enable_retries()
        self.test_list_providers_required_params()

        # Disable retries and run test_list_providers_required_params.
        _service.disable_retries()
        self.test_list_providers_required_params()

    @responses.activate
    def test_list_providers_value_error(self):
        """
        test_list_providers_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/providers')
        mock_response = '{"conversational_skill_providers": [{"provider_id": "provider_id", "specification": {"servers": [{"url": "url"}], "components": {"securitySchemes": {"authentication_method": "basic", "basic": {"username": {"type": "value", "value": "value"}}, "oauth2": {"preferred_flow": "password", "flows": {"token_url": "token_url", "refresh_url": "refresh_url", "client_auth_type": "Body", "content_type": "content_type", "header_prefix": "header_prefix", "username": {"type": "value", "value": "value"}}}}}}}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_providers(**req_copy)

    def test_list_providers_value_error_with_retries(self):
        # Enable retries and run test_list_providers_value_error.
        _service.enable_retries()
        self.test_list_providers_value_error()

        # Disable retries and run test_list_providers_value_error.
        _service.disable_retries()
        self.test_list_providers_value_error()


class TestUpdateProvider:
    """
    Test Class for update_provider
    """

    @responses.activate
    def test_update_provider_all_params(self):
        """
        update_provider()
        """
        # Set up mock
        url = preprocess_url('/v2/providers/testString')
        mock_response = '{"provider_id": "provider_id", "specification": {"servers": [{"url": "url"}], "components": {"securitySchemes": {"authentication_method": "basic", "basic": {"username": {"type": "value", "value": "value"}}, "oauth2": {"preferred_flow": "password", "flows": {"token_url": "token_url", "refresh_url": "refresh_url", "client_auth_type": "Body", "content_type": "content_type", "header_prefix": "header_prefix", "username": {"type": "value", "value": "value"}}}}}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProviderSpecificationServersItem model
        provider_specification_servers_item_model = {}
        provider_specification_servers_item_model['url'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationTypeAndValue model
        provider_authentication_type_and_value_model = {}
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemesBasic model
        provider_specification_components_security_schemes_basic_model = {}
        provider_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2PasswordUsername model
        provider_authentication_o_auth2_password_username_model = {}
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password model
        provider_authentication_o_auth2_flows_model = {}
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2 model
        provider_authentication_o_auth2_model = {}
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemes model
        provider_specification_components_security_schemes_model = {}
        provider_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_specification_components_security_schemes_model['basic'] = provider_specification_components_security_schemes_basic_model
        provider_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        # Construct a dict representation of a ProviderSpecificationComponents model
        provider_specification_components_model = {}
        provider_specification_components_model['securitySchemes'] = provider_specification_components_security_schemes_model

        # Construct a dict representation of a ProviderSpecification model
        provider_specification_model = {}
        provider_specification_model['servers'] = [provider_specification_servers_item_model]
        provider_specification_model['components'] = provider_specification_components_model

        # Construct a dict representation of a ProviderPrivateAuthenticationBearerFlow model
        provider_private_authentication_model = {}
        provider_private_authentication_model['token'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderPrivate model
        provider_private_model = {}
        provider_private_model['authentication'] = provider_private_authentication_model

        # Set up parameter values
        provider_id = 'testString'
        specification = provider_specification_model
        private = provider_private_model

        # Invoke method
        response = _service.update_provider(
            provider_id,
            specification,
            private,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['specification'] == provider_specification_model
        assert req_body['private'] == provider_private_model

    def test_update_provider_all_params_with_retries(self):
        # Enable retries and run test_update_provider_all_params.
        _service.enable_retries()
        self.test_update_provider_all_params()

        # Disable retries and run test_update_provider_all_params.
        _service.disable_retries()
        self.test_update_provider_all_params()

    @responses.activate
    def test_update_provider_value_error(self):
        """
        test_update_provider_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/providers/testString')
        mock_response = '{"provider_id": "provider_id", "specification": {"servers": [{"url": "url"}], "components": {"securitySchemes": {"authentication_method": "basic", "basic": {"username": {"type": "value", "value": "value"}}, "oauth2": {"preferred_flow": "password", "flows": {"token_url": "token_url", "refresh_url": "refresh_url", "client_auth_type": "Body", "content_type": "content_type", "header_prefix": "header_prefix", "username": {"type": "value", "value": "value"}}}}}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ProviderSpecificationServersItem model
        provider_specification_servers_item_model = {}
        provider_specification_servers_item_model['url'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationTypeAndValue model
        provider_authentication_type_and_value_model = {}
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemesBasic model
        provider_specification_components_security_schemes_basic_model = {}
        provider_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2PasswordUsername model
        provider_authentication_o_auth2_password_username_model = {}
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        # Construct a dict representation of a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password model
        provider_authentication_o_auth2_flows_model = {}
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        # Construct a dict representation of a ProviderAuthenticationOAuth2 model
        provider_authentication_o_auth2_model = {}
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        # Construct a dict representation of a ProviderSpecificationComponentsSecuritySchemes model
        provider_specification_components_security_schemes_model = {}
        provider_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_specification_components_security_schemes_model['basic'] = provider_specification_components_security_schemes_basic_model
        provider_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        # Construct a dict representation of a ProviderSpecificationComponents model
        provider_specification_components_model = {}
        provider_specification_components_model['securitySchemes'] = provider_specification_components_security_schemes_model

        # Construct a dict representation of a ProviderSpecification model
        provider_specification_model = {}
        provider_specification_model['servers'] = [provider_specification_servers_item_model]
        provider_specification_model['components'] = provider_specification_components_model

        # Construct a dict representation of a ProviderPrivateAuthenticationBearerFlow model
        provider_private_authentication_model = {}
        provider_private_authentication_model['token'] = provider_authentication_type_and_value_model

        # Construct a dict representation of a ProviderPrivate model
        provider_private_model = {}
        provider_private_model['authentication'] = provider_private_authentication_model

        # Set up parameter values
        provider_id = 'testString'
        specification = provider_specification_model
        private = provider_private_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "provider_id": provider_id,
            "specification": specification,
            "private": private,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_provider(**req_copy)

    def test_update_provider_value_error_with_retries(self):
        # Enable retries and run test_update_provider_value_error.
        _service.enable_retries()
        self.test_update_provider_value_error()

        # Disable retries and run test_update_provider_value_error.
        _service.disable_retries()
        self.test_update_provider_value_error()


# endregion
##############################################################################
# End of Service: ConversationalSkillProviders
##############################################################################

##############################################################################
# Start of Service: Assistants
##############################################################################
# region


class TestCreateAssistant:
    """
    Test Class for create_assistant
    """

    @responses.activate
    def test_create_assistant_all_params(self):
        """
        create_assistant()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants')
        mock_response = '{"assistant_id": "assistant_id", "name": "name", "description": "description", "language": "language", "assistant_skills": [{"skill_id": "skill_id", "type": "dialog"}], "assistant_environments": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        language = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_assistant(
            language=language,
            name=name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['language'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'

    def test_create_assistant_all_params_with_retries(self):
        # Enable retries and run test_create_assistant_all_params.
        _service.enable_retries()
        self.test_create_assistant_all_params()

        # Disable retries and run test_create_assistant_all_params.
        _service.disable_retries()
        self.test_create_assistant_all_params()

    @responses.activate
    def test_create_assistant_required_params(self):
        """
        test_create_assistant_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants')
        mock_response = '{"assistant_id": "assistant_id", "name": "name", "description": "description", "language": "language", "assistant_skills": [{"skill_id": "skill_id", "type": "dialog"}], "assistant_environments": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_assistant()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_assistant_required_params_with_retries(self):
        # Enable retries and run test_create_assistant_required_params.
        _service.enable_retries()
        self.test_create_assistant_required_params()

        # Disable retries and run test_create_assistant_required_params.
        _service.disable_retries()
        self.test_create_assistant_required_params()

    @responses.activate
    def test_create_assistant_value_error(self):
        """
        test_create_assistant_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants')
        mock_response = '{"assistant_id": "assistant_id", "name": "name", "description": "description", "language": "language", "assistant_skills": [{"skill_id": "skill_id", "type": "dialog"}], "assistant_environments": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_assistant(**req_copy)

    def test_create_assistant_value_error_with_retries(self):
        # Enable retries and run test_create_assistant_value_error.
        _service.enable_retries()
        self.test_create_assistant_value_error()

        # Disable retries and run test_create_assistant_value_error.
        _service.disable_retries()
        self.test_create_assistant_value_error()


class TestListAssistants:
    """
    Test Class for list_assistants
    """

    @responses.activate
    def test_list_assistants_all_params(self):
        """
        list_assistants()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants')
        mock_response = '{"assistants": [{"assistant_id": "assistant_id", "name": "name", "description": "description", "language": "language", "assistant_skills": [{"skill_id": "skill_id", "type": "dialog"}], "assistant_environments": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page_limit = 100
        include_count = False
        sort = 'name'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_assistants(
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_list_assistants_all_params_with_retries(self):
        # Enable retries and run test_list_assistants_all_params.
        _service.enable_retries()
        self.test_list_assistants_all_params()

        # Disable retries and run test_list_assistants_all_params.
        _service.disable_retries()
        self.test_list_assistants_all_params()

    @responses.activate
    def test_list_assistants_required_params(self):
        """
        test_list_assistants_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants')
        mock_response = '{"assistants": [{"assistant_id": "assistant_id", "name": "name", "description": "description", "language": "language", "assistant_skills": [{"skill_id": "skill_id", "type": "dialog"}], "assistant_environments": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_assistants()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_assistants_required_params_with_retries(self):
        # Enable retries and run test_list_assistants_required_params.
        _service.enable_retries()
        self.test_list_assistants_required_params()

        # Disable retries and run test_list_assistants_required_params.
        _service.disable_retries()
        self.test_list_assistants_required_params()

    @responses.activate
    def test_list_assistants_value_error(self):
        """
        test_list_assistants_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants')
        mock_response = '{"assistants": [{"assistant_id": "assistant_id", "name": "name", "description": "description", "language": "language", "assistant_skills": [{"skill_id": "skill_id", "type": "dialog"}], "assistant_environments": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_assistants(**req_copy)

    def test_list_assistants_value_error_with_retries(self):
        # Enable retries and run test_list_assistants_value_error.
        _service.enable_retries()
        self.test_list_assistants_value_error()

        # Disable retries and run test_list_assistants_value_error.
        _service.disable_retries()
        self.test_list_assistants_value_error()


class TestDeleteAssistant:
    """
    Test Class for delete_assistant
    """

    @responses.activate
    def test_delete_assistant_all_params(self):
        """
        delete_assistant()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString')
        responses.add(
            responses.DELETE,
            url,
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.delete_assistant(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_assistant_all_params_with_retries(self):
        # Enable retries and run test_delete_assistant_all_params.
        _service.enable_retries()
        self.test_delete_assistant_all_params()

        # Disable retries and run test_delete_assistant_all_params.
        _service.disable_retries()
        self.test_delete_assistant_all_params()

    @responses.activate
    def test_delete_assistant_value_error(self):
        """
        test_delete_assistant_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString')
        responses.add(
            responses.DELETE,
            url,
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_assistant(**req_copy)

    def test_delete_assistant_value_error_with_retries(self):
        # Enable retries and run test_delete_assistant_value_error.
        _service.enable_retries()
        self.test_delete_assistant_value_error()

        # Disable retries and run test_delete_assistant_value_error.
        _service.disable_retries()
        self.test_delete_assistant_value_error()


# endregion
##############################################################################
# End of Service: Assistants
##############################################################################

##############################################################################
# Start of Service: Sessions
##############################################################################
# region


class TestCreateSession:
    """
    Test Class for create_session
    """

    @responses.activate
    def test_create_session_all_params(self):
        """
        create_session()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions')
        mock_response = '{"session_id": "session_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a RequestAnalytics model
        request_analytics_model = {}
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        # Set up parameter values
        assistant_id = 'testString'
        analytics = request_analytics_model

        # Invoke method
        response = _service.create_session(
            assistant_id,
            analytics=analytics,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['analytics'] == request_analytics_model

    def test_create_session_all_params_with_retries(self):
        # Enable retries and run test_create_session_all_params.
        _service.enable_retries()
        self.test_create_session_all_params()

        # Disable retries and run test_create_session_all_params.
        _service.disable_retries()
        self.test_create_session_all_params()

    @responses.activate
    def test_create_session_required_params(self):
        """
        test_create_session_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions')
        mock_response = '{"session_id": "session_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.create_session(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_session_required_params_with_retries(self):
        # Enable retries and run test_create_session_required_params.
        _service.enable_retries()
        self.test_create_session_required_params()

        # Disable retries and run test_create_session_required_params.
        _service.disable_retries()
        self.test_create_session_required_params()

    @responses.activate
    def test_create_session_value_error(self):
        """
        test_create_session_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions')
        mock_response = '{"session_id": "session_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_session(**req_copy)

    def test_create_session_value_error_with_retries(self):
        # Enable retries and run test_create_session_value_error.
        _service.enable_retries()
        self.test_create_session_value_error()

        # Disable retries and run test_create_session_value_error.
        _service.disable_retries()
        self.test_create_session_value_error()


class TestDeleteSession:
    """
    Test Class for delete_session
    """

    @responses.activate
    def test_delete_session_all_params(self):
        """
        delete_session()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        session_id = 'testString'

        # Invoke method
        response = _service.delete_session(
            assistant_id,
            session_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_session_all_params_with_retries(self):
        # Enable retries and run test_delete_session_all_params.
        _service.enable_retries()
        self.test_delete_session_all_params()

        # Disable retries and run test_delete_session_all_params.
        _service.disable_retries()
        self.test_delete_session_all_params()

    @responses.activate
    def test_delete_session_value_error(self):
        """
        test_delete_session_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions/testString')
        responses.add(
            responses.DELETE,
            url,
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        session_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_session(**req_copy)

    def test_delete_session_value_error_with_retries(self):
        # Enable retries and run test_delete_session_value_error.
        _service.enable_retries()
        self.test_delete_session_value_error()

        # Disable retries and run test_delete_session_value_error.
        _service.disable_retries()
        self.test_delete_session_value_error()


# endregion
##############################################################################
# End of Service: Sessions
##############################################################################

##############################################################################
# Start of Service: Message
##############################################################################
# region


class TestMessage:
    """
    Test Class for message
    """

    @responses.activate
    def test_message_all_params(self):
        """
        message()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id", "masked_output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "masked_input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RuntimeIntent model
        runtime_intent_model = {}
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        # Construct a dict representation of a CaptureGroup model
        capture_group_model = {}
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        # Construct a dict representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model = {}
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        # Construct a dict representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model = {}
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        # Construct a dict representation of a RuntimeEntityRole model
        runtime_entity_role_model = {}
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a dict representation of a RuntimeEntity model
        runtime_entity_model = {}
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        # Construct a dict representation of a MessageInputAttachment model
        message_input_attachment_model = {}
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        # Construct a dict representation of a RequestAnalytics model
        request_analytics_model = {}
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        # Construct a dict representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model = {}
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a dict representation of a MessageInputOptions model
        message_input_options_model = {}
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        # Construct a dict representation of a MessageInput model
        message_input_model = {}
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        # Construct a dict representation of a MessageContextGlobalSystem model
        message_context_global_system_model = {}
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        # Construct a dict representation of a MessageContextGlobal model
        message_context_global_model = {}
        message_context_global_model['system'] = message_context_global_system_model

        # Construct a dict representation of a MessageContextSkillSystem model
        message_context_skill_system_model = {}
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a dict representation of a MessageContextDialogSkill model
        message_context_dialog_skill_model = {}
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        # Construct a dict representation of a MessageContextActionSkill model
        message_context_action_skill_model = {}
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a MessageContextSkills model
        message_context_skills_model = {}
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        # Construct a dict representation of a MessageContext model
        message_context_model = {}
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        session_id = 'testString'
        input = message_input_model
        context = message_context_model
        user_id = 'testString'

        # Invoke method
        response = _service.message(
            assistant_id,
            environment_id,
            session_id,
            input=input,
            context=context,
            user_id=user_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == message_input_model
        assert req_body['context'] == message_context_model
        assert req_body['user_id'] == 'testString'

    def test_message_all_params_with_retries(self):
        # Enable retries and run test_message_all_params.
        _service.enable_retries()
        self.test_message_all_params()

        # Disable retries and run test_message_all_params.
        _service.disable_retries()
        self.test_message_all_params()

    @responses.activate
    def test_message_required_params(self):
        """
        test_message_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id", "masked_output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "masked_input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        session_id = 'testString'

        # Invoke method
        response = _service.message(
            assistant_id,
            environment_id,
            session_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_message_required_params_with_retries(self):
        # Enable retries and run test_message_required_params.
        _service.enable_retries()
        self.test_message_required_params()

        # Disable retries and run test_message_required_params.
        _service.disable_retries()
        self.test_message_required_params()

    @responses.activate
    def test_message_value_error(self):
        """
        test_message_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/sessions/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id", "masked_output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "masked_input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        session_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "environment_id": environment_id,
            "session_id": session_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.message(**req_copy)

    def test_message_value_error_with_retries(self):
        # Enable retries and run test_message_value_error.
        _service.enable_retries()
        self.test_message_value_error()

        # Disable retries and run test_message_value_error.
        _service.disable_retries()
        self.test_message_value_error()


class TestMessageStateless:
    """
    Test Class for message_stateless
    """

    @responses.activate
    def test_message_stateless_all_params(self):
        """
        message_stateless()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}, "private_action_variables": {"anyKey": "anyValue"}, "private_skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "masked_output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "masked_input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "user_id": "user_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RuntimeIntent model
        runtime_intent_model = {}
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        # Construct a dict representation of a CaptureGroup model
        capture_group_model = {}
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        # Construct a dict representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model = {}
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        # Construct a dict representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model = {}
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        # Construct a dict representation of a RuntimeEntityRole model
        runtime_entity_role_model = {}
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a dict representation of a RuntimeEntity model
        runtime_entity_model = {}
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        # Construct a dict representation of a MessageInputAttachment model
        message_input_attachment_model = {}
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        # Construct a dict representation of a RequestAnalytics model
        request_analytics_model = {}
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        # Construct a dict representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model = {}
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a dict representation of a StatelessMessageInputOptions model
        stateless_message_input_options_model = {}
        stateless_message_input_options_model['restart'] = False
        stateless_message_input_options_model['alternate_intents'] = False
        stateless_message_input_options_model['async_callout'] = False
        stateless_message_input_options_model['spelling'] = message_input_options_spelling_model
        stateless_message_input_options_model['debug'] = False

        # Construct a dict representation of a StatelessMessageInput model
        stateless_message_input_model = {}
        stateless_message_input_model['message_type'] = 'text'
        stateless_message_input_model['text'] = 'testString'
        stateless_message_input_model['intents'] = [runtime_intent_model]
        stateless_message_input_model['entities'] = [runtime_entity_model]
        stateless_message_input_model['suggestion_id'] = 'testString'
        stateless_message_input_model['attachments'] = [message_input_attachment_model]
        stateless_message_input_model['analytics'] = request_analytics_model
        stateless_message_input_model['options'] = stateless_message_input_options_model

        # Construct a dict representation of a MessageContextGlobalSystem model
        message_context_global_system_model = {}
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        # Construct a dict representation of a StatelessMessageContextGlobal model
        stateless_message_context_global_model = {}
        stateless_message_context_global_model['system'] = message_context_global_system_model
        stateless_message_context_global_model['session_id'] = 'testString'

        # Construct a dict representation of a MessageContextSkillSystem model
        message_context_skill_system_model = {}
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a dict representation of a MessageContextDialogSkill model
        message_context_dialog_skill_model = {}
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        # Construct a dict representation of a StatelessMessageContextSkillsActionsSkill model
        stateless_message_context_skills_actions_skill_model = {}
        stateless_message_context_skills_actions_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['system'] = message_context_skill_system_model
        stateless_message_context_skills_actions_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['skill_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a StatelessMessageContextSkills model
        stateless_message_context_skills_model = {}
        stateless_message_context_skills_model['main skill'] = message_context_dialog_skill_model
        stateless_message_context_skills_model['actions skill'] = stateless_message_context_skills_actions_skill_model

        # Construct a dict representation of a StatelessMessageContext model
        stateless_message_context_model = {}
        stateless_message_context_model['global'] = stateless_message_context_global_model
        stateless_message_context_model['skills'] = stateless_message_context_skills_model
        stateless_message_context_model['integrations'] = {'anyKey': 'anyValue'}

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        input = stateless_message_input_model
        context = stateless_message_context_model
        user_id = 'testString'

        # Invoke method
        response = _service.message_stateless(
            assistant_id,
            environment_id,
            input=input,
            context=context,
            user_id=user_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == stateless_message_input_model
        assert req_body['context'] == stateless_message_context_model
        assert req_body['user_id'] == 'testString'

    def test_message_stateless_all_params_with_retries(self):
        # Enable retries and run test_message_stateless_all_params.
        _service.enable_retries()
        self.test_message_stateless_all_params()

        # Disable retries and run test_message_stateless_all_params.
        _service.disable_retries()
        self.test_message_stateless_all_params()

    @responses.activate
    def test_message_stateless_required_params(self):
        """
        test_message_stateless_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}, "private_action_variables": {"anyKey": "anyValue"}, "private_skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "masked_output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "masked_input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "user_id": "user_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Invoke method
        response = _service.message_stateless(
            assistant_id,
            environment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_message_stateless_required_params_with_retries(self):
        # Enable retries and run test_message_stateless_required_params.
        _service.enable_retries()
        self.test_message_stateless_required_params()

        # Disable retries and run test_message_stateless_required_params.
        _service.disable_retries()
        self.test_message_stateless_required_params()

    @responses.activate
    def test_message_stateless_value_error(self):
        """
        test_message_stateless_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}, "private_action_variables": {"anyKey": "anyValue"}, "private_skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "masked_output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "masked_input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "user_id": "user_id"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.message_stateless(**req_copy)

    def test_message_stateless_value_error_with_retries(self):
        # Enable retries and run test_message_stateless_value_error.
        _service.enable_retries()
        self.test_message_stateless_value_error()

        # Disable retries and run test_message_stateless_value_error.
        _service.disable_retries()
        self.test_message_stateless_value_error()


# endregion
##############################################################################
# End of Service: Message
##############################################################################

##############################################################################
# Start of Service: MessageStream
##############################################################################
# region


class TestMessageStream:
    """
    Test Class for message_stream
    """

    @responses.activate
    def test_message_stream_all_params(self):
        """
        message_stream()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString/sessions/testString/message_stream')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='text/event-stream',
            status=200,
        )

        # Construct a dict representation of a RuntimeIntent model
        runtime_intent_model = {}
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        # Construct a dict representation of a CaptureGroup model
        capture_group_model = {}
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        # Construct a dict representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model = {}
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        # Construct a dict representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model = {}
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        # Construct a dict representation of a RuntimeEntityRole model
        runtime_entity_role_model = {}
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a dict representation of a RuntimeEntity model
        runtime_entity_model = {}
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        # Construct a dict representation of a MessageInputAttachment model
        message_input_attachment_model = {}
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        # Construct a dict representation of a RequestAnalytics model
        request_analytics_model = {}
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        # Construct a dict representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model = {}
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a dict representation of a MessageInputOptions model
        message_input_options_model = {}
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        # Construct a dict representation of a MessageInput model
        message_input_model = {}
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        # Construct a dict representation of a MessageContextGlobalSystem model
        message_context_global_system_model = {}
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        # Construct a dict representation of a MessageContextGlobal model
        message_context_global_model = {}
        message_context_global_model['system'] = message_context_global_system_model

        # Construct a dict representation of a MessageContextSkillSystem model
        message_context_skill_system_model = {}
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a dict representation of a MessageContextDialogSkill model
        message_context_dialog_skill_model = {}
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        # Construct a dict representation of a MessageContextActionSkill model
        message_context_action_skill_model = {}
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a MessageContextSkills model
        message_context_skills_model = {}
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        # Construct a dict representation of a MessageContext model
        message_context_model = {}
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        session_id = 'testString'
        input = message_input_model
        context = message_context_model
        user_id = 'testString'

        # Invoke method
        response = _service.message_stream(
            assistant_id,
            environment_id,
            session_id,
            input=input,
            context=context,
            user_id=user_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == message_input_model
        assert req_body['context'] == message_context_model
        assert req_body['user_id'] == 'testString'

    def test_message_stream_all_params_with_retries(self):
        # Enable retries and run test_message_stream_all_params.
        _service.enable_retries()
        self.test_message_stream_all_params()

        # Disable retries and run test_message_stream_all_params.
        _service.disable_retries()
        self.test_message_stream_all_params()

    @responses.activate
    def test_message_stream_required_params(self):
        """
        test_message_stream_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString/sessions/testString/message_stream')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='text/event-stream',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        session_id = 'testString'

        # Invoke method
        response = _service.message_stream(
            assistant_id,
            environment_id,
            session_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_message_stream_required_params_with_retries(self):
        # Enable retries and run test_message_stream_required_params.
        _service.enable_retries()
        self.test_message_stream_required_params()

        # Disable retries and run test_message_stream_required_params.
        _service.disable_retries()
        self.test_message_stream_required_params()

    @responses.activate
    def test_message_stream_value_error(self):
        """
        test_message_stream_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString/sessions/testString/message_stream')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='text/event-stream',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        session_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "environment_id": environment_id,
            "session_id": session_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.message_stream(**req_copy)

    def test_message_stream_value_error_with_retries(self):
        # Enable retries and run test_message_stream_value_error.
        _service.enable_retries()
        self.test_message_stream_value_error()

        # Disable retries and run test_message_stream_value_error.
        _service.disable_retries()
        self.test_message_stream_value_error()


class TestMessageStreamStateless:
    """
    Test Class for message_stream_stateless
    """

    @responses.activate
    def test_message_stream_stateless_all_params(self):
        """
        message_stream_stateless()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString/message_stream')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='text/event-stream',
            status=200,
        )

        # Construct a dict representation of a RuntimeIntent model
        runtime_intent_model = {}
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        # Construct a dict representation of a CaptureGroup model
        capture_group_model = {}
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        # Construct a dict representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model = {}
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        # Construct a dict representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model = {}
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        # Construct a dict representation of a RuntimeEntityRole model
        runtime_entity_role_model = {}
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a dict representation of a RuntimeEntity model
        runtime_entity_model = {}
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        # Construct a dict representation of a MessageInputAttachment model
        message_input_attachment_model = {}
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        # Construct a dict representation of a RequestAnalytics model
        request_analytics_model = {}
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        # Construct a dict representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model = {}
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a dict representation of a MessageInputOptions model
        message_input_options_model = {}
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        # Construct a dict representation of a MessageInput model
        message_input_model = {}
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        # Construct a dict representation of a MessageContextGlobalSystem model
        message_context_global_system_model = {}
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        # Construct a dict representation of a MessageContextGlobal model
        message_context_global_model = {}
        message_context_global_model['system'] = message_context_global_system_model

        # Construct a dict representation of a MessageContextSkillSystem model
        message_context_skill_system_model = {}
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a dict representation of a MessageContextDialogSkill model
        message_context_dialog_skill_model = {}
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        # Construct a dict representation of a MessageContextActionSkill model
        message_context_action_skill_model = {}
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a MessageContextSkills model
        message_context_skills_model = {}
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        # Construct a dict representation of a MessageContext model
        message_context_model = {}
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        input = message_input_model
        context = message_context_model
        user_id = 'testString'

        # Invoke method
        response = _service.message_stream_stateless(
            assistant_id,
            environment_id,
            input=input,
            context=context,
            user_id=user_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == message_input_model
        assert req_body['context'] == message_context_model
        assert req_body['user_id'] == 'testString'

    def test_message_stream_stateless_all_params_with_retries(self):
        # Enable retries and run test_message_stream_stateless_all_params.
        _service.enable_retries()
        self.test_message_stream_stateless_all_params()

        # Disable retries and run test_message_stream_stateless_all_params.
        _service.disable_retries()
        self.test_message_stream_stateless_all_params()

    @responses.activate
    def test_message_stream_stateless_required_params(self):
        """
        test_message_stream_stateless_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString/message_stream')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='text/event-stream',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Invoke method
        response = _service.message_stream_stateless(
            assistant_id,
            environment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_message_stream_stateless_required_params_with_retries(self):
        # Enable retries and run test_message_stream_stateless_required_params.
        _service.enable_retries()
        self.test_message_stream_stateless_required_params()

        # Disable retries and run test_message_stream_stateless_required_params.
        _service.disable_retries()
        self.test_message_stream_stateless_required_params()

    @responses.activate
    def test_message_stream_stateless_value_error(self):
        """
        test_message_stream_stateless_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString/message_stream')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='text/event-stream',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.message_stream_stateless(**req_copy)

    def test_message_stream_stateless_value_error_with_retries(self):
        # Enable retries and run test_message_stream_stateless_value_error.
        _service.enable_retries()
        self.test_message_stream_stateless_value_error()

        # Disable retries and run test_message_stream_stateless_value_error.
        _service.disable_retries()
        self.test_message_stream_stateless_value_error()


# endregion
##############################################################################
# End of Service: MessageStream
##############################################################################

##############################################################################
# Start of Service: BulkClassify
##############################################################################
# region


class TestBulkClassify:
    """
    Test Class for bulk_classify
    """

    @responses.activate
    def test_bulk_classify_all_params(self):
        """
        bulk_classify()
        """
        # Set up mock
        url = preprocess_url('/v2/skills/testString/workspace/bulk_classify')
        mock_response = '{"output": [{"input": {"text": "text"}, "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a BulkClassifyUtterance model
        bulk_classify_utterance_model = {}
        bulk_classify_utterance_model['text'] = 'testString'

        # Set up parameter values
        skill_id = 'testString'
        input = [bulk_classify_utterance_model]

        # Invoke method
        response = _service.bulk_classify(
            skill_id,
            input,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == [bulk_classify_utterance_model]

    def test_bulk_classify_all_params_with_retries(self):
        # Enable retries and run test_bulk_classify_all_params.
        _service.enable_retries()
        self.test_bulk_classify_all_params()

        # Disable retries and run test_bulk_classify_all_params.
        _service.disable_retries()
        self.test_bulk_classify_all_params()

    @responses.activate
    def test_bulk_classify_value_error(self):
        """
        test_bulk_classify_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/skills/testString/workspace/bulk_classify')
        mock_response = '{"output": [{"input": {"text": "text"}, "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a BulkClassifyUtterance model
        bulk_classify_utterance_model = {}
        bulk_classify_utterance_model['text'] = 'testString'

        # Set up parameter values
        skill_id = 'testString'
        input = [bulk_classify_utterance_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "skill_id": skill_id,
            "input": input,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.bulk_classify(**req_copy)

    def test_bulk_classify_value_error_with_retries(self):
        # Enable retries and run test_bulk_classify_value_error.
        _service.enable_retries()
        self.test_bulk_classify_value_error()

        # Disable retries and run test_bulk_classify_value_error.
        _service.disable_retries()
        self.test_bulk_classify_value_error()


# endregion
##############################################################################
# End of Service: BulkClassify
##############################################################################

##############################################################################
# Start of Service: Logs
##############################################################################
# region


class TestListLogs:
    """
    Test Class for list_logs
    """

    @responses.activate
    def test_list_logs_all_params(self):
        """
        list_logs()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/logs')
        mock_response = '{"logs": [{"log_id": "log_id", "request": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id"}, "response": {"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id"}, "assistant_id": "assistant_id", "session_id": "session_id", "skill_id": "skill_id", "snapshot": "snapshot", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "language": "language", "customer_id": "customer_id"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        sort = 'testString'
        filter = 'testString'
        page_limit = 100
        cursor = 'testString'

        # Invoke method
        response = _service.list_logs(
            assistant_id,
            sort=sort,
            filter=filter,
            page_limit=page_limit,
            cursor=cursor,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'sort={}'.format(sort) in query_string
        assert 'filter={}'.format(filter) in query_string
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'cursor={}'.format(cursor) in query_string

    def test_list_logs_all_params_with_retries(self):
        # Enable retries and run test_list_logs_all_params.
        _service.enable_retries()
        self.test_list_logs_all_params()

        # Disable retries and run test_list_logs_all_params.
        _service.disable_retries()
        self.test_list_logs_all_params()

    @responses.activate
    def test_list_logs_required_params(self):
        """
        test_list_logs_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/logs')
        mock_response = '{"logs": [{"log_id": "log_id", "request": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id"}, "response": {"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id"}, "assistant_id": "assistant_id", "session_id": "session_id", "skill_id": "skill_id", "snapshot": "snapshot", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "language": "language", "customer_id": "customer_id"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.list_logs(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_logs_required_params_with_retries(self):
        # Enable retries and run test_list_logs_required_params.
        _service.enable_retries()
        self.test_list_logs_required_params()

        # Disable retries and run test_list_logs_required_params.
        _service.disable_retries()
        self.test_list_logs_required_params()

    @responses.activate
    def test_list_logs_value_error(self):
        """
        test_list_logs_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/logs')
        mock_response = '{"logs": [{"log_id": "log_id", "request": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "suggestion_id": "suggestion_id", "attachments": [{"url": "url", "media_type": "media_type"}], "analytics": {"browser": "browser", "device": "device", "pageUrl": "page_url"}, "options": {"restart": false, "alternate_intents": false, "async_callout": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id"}, "response": {"output": {"generic": [{"response_type": "text", "text": "text", "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10, "skill": "skill"}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}, "skill": "skill"}], "actions": [{"name": "name", "type": "client", "parameters": {"anyKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed", "turn_events": [{"event": "action_visited", "source": {"type": "action", "action": "action", "action_title": "action_title", "condition": "condition"}, "action_start_time": "action_start_time", "condition_type": "user_defined", "reason": "intent", "result_variable": "result_variable"}]}, "user_defined": {"anyKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state", "skip_user_input": false}, "session_id": "session_id"}, "skills": {"main skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}}, "actions skill": {"user_defined": {"anyKey": "anyValue"}, "system": {"state": "state"}, "action_variables": {"anyKey": "anyValue"}, "skill_variables": {"anyKey": "anyValue"}}}, "integrations": {"anyKey": "anyValue"}}, "user_id": "user_id"}, "assistant_id": "assistant_id", "session_id": "session_id", "skill_id": "skill_id", "snapshot": "snapshot", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "language": "language", "customer_id": "customer_id"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_logs(**req_copy)

    def test_list_logs_value_error_with_retries(self):
        # Enable retries and run test_list_logs_value_error.
        _service.enable_retries()
        self.test_list_logs_value_error()

        # Disable retries and run test_list_logs_value_error.
        _service.disable_retries()
        self.test_list_logs_value_error()


# endregion
##############################################################################
# End of Service: Logs
##############################################################################

##############################################################################
# Start of Service: UserData
##############################################################################
# region


class TestDeleteUserData:
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
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        customer_id = 'testString'

        # Invoke method
        response = _service.delete_user_data(
            customer_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        customer_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customer_id": customer_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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
# Start of Service: Environments
##############################################################################
# region


class TestListEnvironments:
    """
    Test Class for list_environments
    """

    @responses.activate
    def test_list_environments_all_params(self):
        """
        list_environments()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments')
        mock_response = '{"environments": [{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        page_limit = 100
        include_count = False
        sort = 'name'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_environments(
            assistant_id,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_list_environments_all_params_with_retries(self):
        # Enable retries and run test_list_environments_all_params.
        _service.enable_retries()
        self.test_list_environments_all_params()

        # Disable retries and run test_list_environments_all_params.
        _service.disable_retries()
        self.test_list_environments_all_params()

    @responses.activate
    def test_list_environments_required_params(self):
        """
        test_list_environments_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments')
        mock_response = '{"environments": [{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.list_environments(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_environments_required_params_with_retries(self):
        # Enable retries and run test_list_environments_required_params.
        _service.enable_retries()
        self.test_list_environments_required_params()

        # Disable retries and run test_list_environments_required_params.
        _service.disable_retries()
        self.test_list_environments_required_params()

    @responses.activate
    def test_list_environments_value_error(self):
        """
        test_list_environments_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments')
        mock_response = '{"environments": [{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_environments(**req_copy)

    def test_list_environments_value_error_with_retries(self):
        # Enable retries and run test_list_environments_value_error.
        _service.enable_retries()
        self.test_list_environments_value_error()

        # Disable retries and run test_list_environments_value_error.
        _service.disable_retries()
        self.test_list_environments_value_error()


class TestGetEnvironment:
    """
    Test Class for get_environment
    """

    @responses.activate
    def test_get_environment_all_params(self):
        """
        get_environment()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        include_audit = False

        # Invoke method
        response = _service.get_environment(
            assistant_id,
            environment_id,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_get_environment_all_params_with_retries(self):
        # Enable retries and run test_get_environment_all_params.
        _service.enable_retries()
        self.test_get_environment_all_params()

        # Disable retries and run test_get_environment_all_params.
        _service.disable_retries()
        self.test_get_environment_all_params()

    @responses.activate
    def test_get_environment_required_params(self):
        """
        test_get_environment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Invoke method
        response = _service.get_environment(
            assistant_id,
            environment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_environment_required_params_with_retries(self):
        # Enable retries and run test_get_environment_required_params.
        _service.enable_retries()
        self.test_get_environment_required_params()

        # Disable retries and run test_get_environment_required_params.
        _service.disable_retries()
        self.test_get_environment_required_params()

    @responses.activate
    def test_get_environment_value_error(self):
        """
        test_get_environment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_environment(**req_copy)

    def test_get_environment_value_error_with_retries(self):
        # Enable retries and run test_get_environment_value_error.
        _service.enable_retries()
        self.test_get_environment_value_error()

        # Disable retries and run test_get_environment_value_error.
        _service.disable_retries()
        self.test_get_environment_value_error()


class TestUpdateEnvironment:
    """
    Test Class for update_environment
    """

    @responses.activate
    def test_update_environment_all_params(self):
        """
        update_environment()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateEnvironmentOrchestration model
        update_environment_orchestration_model = {}
        update_environment_orchestration_model['search_skill_fallback'] = True

        # Construct a dict representation of a EnvironmentSkill model
        environment_skill_model = {}
        environment_skill_model['skill_id'] = 'testString'
        environment_skill_model['type'] = 'dialog'
        environment_skill_model['disabled'] = True
        environment_skill_model['snapshot'] = 'testString'
        environment_skill_model['skill_reference'] = 'testString'

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'
        name = 'testString'
        description = 'testString'
        orchestration = update_environment_orchestration_model
        session_timeout = 10
        skill_references = [environment_skill_model]

        # Invoke method
        response = _service.update_environment(
            assistant_id,
            environment_id,
            name=name,
            description=description,
            orchestration=orchestration,
            session_timeout=session_timeout,
            skill_references=skill_references,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['orchestration'] == update_environment_orchestration_model
        assert req_body['session_timeout'] == 10
        assert req_body['skill_references'] == [environment_skill_model]

    def test_update_environment_all_params_with_retries(self):
        # Enable retries and run test_update_environment_all_params.
        _service.enable_retries()
        self.test_update_environment_all_params()

        # Disable retries and run test_update_environment_all_params.
        _service.disable_retries()
        self.test_update_environment_all_params()

    @responses.activate
    def test_update_environment_required_params(self):
        """
        test_update_environment_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Invoke method
        response = _service.update_environment(
            assistant_id,
            environment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_environment_required_params_with_retries(self):
        # Enable retries and run test_update_environment_required_params.
        _service.enable_retries()
        self.test_update_environment_required_params()

        # Disable retries and run test_update_environment_required_params.
        _service.disable_retries()
        self.test_update_environment_required_params()

    @responses.activate
    def test_update_environment_value_error(self):
        """
        test_update_environment_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/environments/testString')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_environment(**req_copy)

    def test_update_environment_value_error_with_retries(self):
        # Enable retries and run test_update_environment_value_error.
        _service.enable_retries()
        self.test_update_environment_value_error()

        # Disable retries and run test_update_environment_value_error.
        _service.disable_retries()
        self.test_update_environment_value_error()


# endregion
##############################################################################
# End of Service: Environments
##############################################################################

##############################################################################
# Start of Service: Releases
##############################################################################
# region


class TestCreateRelease:
    """
    Test Class for create_release
    """

    @responses.activate
    def test_create_release_all_params(self):
        """
        create_release()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases')
        mock_response = '{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assistant_id = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_release(
            assistant_id,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'

    def test_create_release_all_params_with_retries(self):
        # Enable retries and run test_create_release_all_params.
        _service.enable_retries()
        self.test_create_release_all_params()

        # Disable retries and run test_create_release_all_params.
        _service.disable_retries()
        self.test_create_release_all_params()

    @responses.activate
    def test_create_release_required_params(self):
        """
        test_create_release_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases')
        mock_response = '{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.create_release(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_create_release_required_params_with_retries(self):
        # Enable retries and run test_create_release_required_params.
        _service.enable_retries()
        self.test_create_release_required_params()

        # Disable retries and run test_create_release_required_params.
        _service.disable_retries()
        self.test_create_release_required_params()

    @responses.activate
    def test_create_release_value_error(self):
        """
        test_create_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases')
        mock_response = '{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_release(**req_copy)

    def test_create_release_value_error_with_retries(self):
        # Enable retries and run test_create_release_value_error.
        _service.enable_retries()
        self.test_create_release_value_error()

        # Disable retries and run test_create_release_value_error.
        _service.disable_retries()
        self.test_create_release_value_error()


class TestListReleases:
    """
    Test Class for list_releases
    """

    @responses.activate
    def test_list_releases_all_params(self):
        """
        list_releases()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases')
        mock_response = '{"releases": [{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        page_limit = 100
        include_count = False
        sort = 'name'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_releases(
            assistant_id,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_list_releases_all_params_with_retries(self):
        # Enable retries and run test_list_releases_all_params.
        _service.enable_retries()
        self.test_list_releases_all_params()

        # Disable retries and run test_list_releases_all_params.
        _service.disable_retries()
        self.test_list_releases_all_params()

    @responses.activate
    def test_list_releases_required_params(self):
        """
        test_list_releases_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases')
        mock_response = '{"releases": [{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.list_releases(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_releases_required_params_with_retries(self):
        # Enable retries and run test_list_releases_required_params.
        _service.enable_retries()
        self.test_list_releases_required_params()

        # Disable retries and run test_list_releases_required_params.
        _service.disable_retries()
        self.test_list_releases_required_params()

    @responses.activate
    def test_list_releases_value_error(self):
        """
        test_list_releases_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases')
        mock_response = '{"releases": [{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_releases(**req_copy)

    def test_list_releases_value_error_with_retries(self):
        # Enable retries and run test_list_releases_value_error.
        _service.enable_retries()
        self.test_list_releases_value_error()

        # Disable retries and run test_list_releases_value_error.
        _service.disable_retries()
        self.test_list_releases_value_error()


class TestGetRelease:
    """
    Test Class for get_release
    """

    @responses.activate
    def test_get_release_all_params(self):
        """
        get_release()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString')
        mock_response = '{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'
        include_audit = False

        # Invoke method
        response = _service.get_release(
            assistant_id,
            release,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_get_release_all_params_with_retries(self):
        # Enable retries and run test_get_release_all_params.
        _service.enable_retries()
        self.test_get_release_all_params()

        # Disable retries and run test_get_release_all_params.
        _service.disable_retries()
        self.test_get_release_all_params()

    @responses.activate
    def test_get_release_required_params(self):
        """
        test_get_release_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString')
        mock_response = '{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Invoke method
        response = _service.get_release(
            assistant_id,
            release,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_release_required_params_with_retries(self):
        # Enable retries and run test_get_release_required_params.
        _service.enable_retries()
        self.test_get_release_required_params()

        # Disable retries and run test_get_release_required_params.
        _service.disable_retries()
        self.test_get_release_required_params()

    @responses.activate
    def test_get_release_value_error(self):
        """
        test_get_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString')
        mock_response = '{"release": "release", "description": "description", "environment_references": [{"name": "name", "environment_id": "environment_id", "environment": "draft"}], "content": {"skills": [{"skill_id": "skill_id", "type": "dialog", "snapshot": "snapshot"}]}, "status": "Available", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "release": release,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_release(**req_copy)

    def test_get_release_value_error_with_retries(self):
        # Enable retries and run test_get_release_value_error.
        _service.enable_retries()
        self.test_get_release_value_error()

        # Disable retries and run test_get_release_value_error.
        _service.disable_retries()
        self.test_get_release_value_error()


class TestDeleteRelease:
    """
    Test Class for delete_release
    """

    @responses.activate
    def test_delete_release_all_params(self):
        """
        delete_release()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString')
        responses.add(
            responses.DELETE,
            url,
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Invoke method
        response = _service.delete_release(
            assistant_id,
            release,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_release_all_params_with_retries(self):
        # Enable retries and run test_delete_release_all_params.
        _service.enable_retries()
        self.test_delete_release_all_params()

        # Disable retries and run test_delete_release_all_params.
        _service.disable_retries()
        self.test_delete_release_all_params()

    @responses.activate
    def test_delete_release_value_error(self):
        """
        test_delete_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString')
        responses.add(
            responses.DELETE,
            url,
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "release": release,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_release(**req_copy)

    def test_delete_release_value_error_with_retries(self):
        # Enable retries and run test_delete_release_value_error.
        _service.enable_retries()
        self.test_delete_release_value_error()

        # Disable retries and run test_delete_release_value_error.
        _service.disable_retries()
        self.test_delete_release_value_error()


class TestDeployRelease:
    """
    Test Class for deploy_release
    """

    @responses.activate
    def test_deploy_release_all_params(self):
        """
        deploy_release()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/deploy')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'
        environment_id = 'testString'
        include_audit = False

        # Invoke method
        response = _service.deploy_release(
            assistant_id,
            release,
            environment_id,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['environment_id'] == 'testString'

    def test_deploy_release_all_params_with_retries(self):
        # Enable retries and run test_deploy_release_all_params.
        _service.enable_retries()
        self.test_deploy_release_all_params()

        # Disable retries and run test_deploy_release_all_params.
        _service.disable_retries()
        self.test_deploy_release_all_params()

    @responses.activate
    def test_deploy_release_required_params(self):
        """
        test_deploy_release_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/deploy')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'
        environment_id = 'testString'

        # Invoke method
        response = _service.deploy_release(
            assistant_id,
            release,
            environment_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['environment_id'] == 'testString'

    def test_deploy_release_required_params_with_retries(self):
        # Enable retries and run test_deploy_release_required_params.
        _service.enable_retries()
        self.test_deploy_release_required_params()

        # Disable retries and run test_deploy_release_required_params.
        _service.disable_retries()
        self.test_deploy_release_required_params()

    @responses.activate
    def test_deploy_release_value_error(self):
        """
        test_deploy_release_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/deploy')
        mock_response = '{"name": "name", "description": "description", "assistant_id": "assistant_id", "environment_id": "environment_id", "environment": "environment", "release_reference": {"release": "release"}, "orchestration": {"search_skill_fallback": false}, "session_timeout": 10, "integration_references": [{"integration_id": "integration_id", "type": "type"}], "skill_references": [{"skill_id": "skill_id", "type": "dialog", "disabled": true, "snapshot": "snapshot", "skill_reference": "skill_reference"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "release": release,
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.deploy_release(**req_copy)

    def test_deploy_release_value_error_with_retries(self):
        # Enable retries and run test_deploy_release_value_error.
        _service.enable_retries()
        self.test_deploy_release_value_error()

        # Disable retries and run test_deploy_release_value_error.
        _service.disable_retries()
        self.test_deploy_release_value_error()


class TestCreateReleaseExport:
    """
    Test Class for create_release_export
    """

    @responses.activate
    def test_create_release_export_all_params(self):
        """
        create_release_export()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/export')
        mock_response = '{"status": "Available", "task_id": "task_id", "assistant_id": "assistant_id", "release": "release", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status_errors": [{"message": "message"}], "status_description": "status_description"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'
        include_audit = False

        # Invoke method
        response = _service.create_release_export(
            assistant_id,
            release,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_create_release_export_all_params_with_retries(self):
        # Enable retries and run test_create_release_export_all_params.
        _service.enable_retries()
        self.test_create_release_export_all_params()

        # Disable retries and run test_create_release_export_all_params.
        _service.disable_retries()
        self.test_create_release_export_all_params()

    @responses.activate
    def test_create_release_export_required_params(self):
        """
        test_create_release_export_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/export')
        mock_response = '{"status": "Available", "task_id": "task_id", "assistant_id": "assistant_id", "release": "release", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status_errors": [{"message": "message"}], "status_description": "status_description"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Invoke method
        response = _service.create_release_export(
            assistant_id,
            release,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_release_export_required_params_with_retries(self):
        # Enable retries and run test_create_release_export_required_params.
        _service.enable_retries()
        self.test_create_release_export_required_params()

        # Disable retries and run test_create_release_export_required_params.
        _service.disable_retries()
        self.test_create_release_export_required_params()

    @responses.activate
    def test_create_release_export_value_error(self):
        """
        test_create_release_export_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/export')
        mock_response = '{"status": "Available", "task_id": "task_id", "assistant_id": "assistant_id", "release": "release", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status_errors": [{"message": "message"}], "status_description": "status_description"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "release": release,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_release_export(**req_copy)

    def test_create_release_export_value_error_with_retries(self):
        # Enable retries and run test_create_release_export_value_error.
        _service.enable_retries()
        self.test_create_release_export_value_error()

        # Disable retries and run test_create_release_export_value_error.
        _service.disable_retries()
        self.test_create_release_export_value_error()


class TestDownloadReleaseExport:
    """
    Test Class for download_release_export
    """

    @responses.activate
    def test_download_release_export_all_params(self):
        """
        download_release_export()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/export')
        mock_response = '{"status": "Available", "task_id": "task_id", "assistant_id": "assistant_id", "release": "release", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status_errors": [{"message": "message"}], "status_description": "status_description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'
        accept = 'application/json'
        include_audit = False

        # Invoke method
        response = _service.download_release_export(
            assistant_id,
            release,
            accept=accept,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_download_release_export_all_params_with_retries(self):
        # Enable retries and run test_download_release_export_all_params.
        _service.enable_retries()
        self.test_download_release_export_all_params()

        # Disable retries and run test_download_release_export_all_params.
        _service.disable_retries()
        self.test_download_release_export_all_params()

    @responses.activate
    def test_download_release_export_required_params(self):
        """
        test_download_release_export_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/export')
        mock_response = '{"status": "Available", "task_id": "task_id", "assistant_id": "assistant_id", "release": "release", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status_errors": [{"message": "message"}], "status_description": "status_description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Invoke method
        response = _service.download_release_export(
            assistant_id,
            release,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_download_release_export_required_params_with_retries(self):
        # Enable retries and run test_download_release_export_required_params.
        _service.enable_retries()
        self.test_download_release_export_required_params()

        # Disable retries and run test_download_release_export_required_params.
        _service.disable_retries()
        self.test_download_release_export_required_params()

    @responses.activate
    def test_download_release_export_value_error(self):
        """
        test_download_release_export_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/releases/testString/export')
        mock_response = '{"status": "Available", "task_id": "task_id", "assistant_id": "assistant_id", "release": "release", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status_errors": [{"message": "message"}], "status_description": "status_description"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        release = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "release": release,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.download_release_export(**req_copy)

    def test_download_release_export_value_error_with_retries(self):
        # Enable retries and run test_download_release_export_value_error.
        _service.enable_retries()
        self.test_download_release_export_value_error()

        # Disable retries and run test_download_release_export_value_error.
        _service.disable_retries()
        self.test_download_release_export_value_error()


class TestCreateReleaseImport:
    """
    Test Class for create_release_import
    """

    @responses.activate
    def test_create_release_import_all_params(self):
        """
        create_release_import()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/import')
        mock_response = '{"status": "Failed", "task_id": "task_id", "assistant_id": "assistant_id", "skill_impact_in_draft": ["action"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assistant_id = 'testString'
        body = io.BytesIO(b'This is a mock file.').getvalue()
        include_audit = False

        # Invoke method
        response = _service.create_release_import(
            assistant_id,
            body,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        assert responses.calls[0].request.body == body

    def test_create_release_import_all_params_with_retries(self):
        # Enable retries and run test_create_release_import_all_params.
        _service.enable_retries()
        self.test_create_release_import_all_params()

        # Disable retries and run test_create_release_import_all_params.
        _service.disable_retries()
        self.test_create_release_import_all_params()

    @responses.activate
    def test_create_release_import_required_params(self):
        """
        test_create_release_import_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/import')
        mock_response = '{"status": "Failed", "task_id": "task_id", "assistant_id": "assistant_id", "skill_impact_in_draft": ["action"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assistant_id = 'testString'
        body = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_release_import(
            assistant_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        assert responses.calls[0].request.body == body

    def test_create_release_import_required_params_with_retries(self):
        # Enable retries and run test_create_release_import_required_params.
        _service.enable_retries()
        self.test_create_release_import_required_params()

        # Disable retries and run test_create_release_import_required_params.
        _service.disable_retries()
        self.test_create_release_import_required_params()

    @responses.activate
    def test_create_release_import_value_error(self):
        """
        test_create_release_import_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/import')
        mock_response = '{"status": "Failed", "task_id": "task_id", "assistant_id": "assistant_id", "skill_impact_in_draft": ["action"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        assistant_id = 'testString'
        body = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_release_import(**req_copy)

    def test_create_release_import_value_error_with_retries(self):
        # Enable retries and run test_create_release_import_value_error.
        _service.enable_retries()
        self.test_create_release_import_value_error()

        # Disable retries and run test_create_release_import_value_error.
        _service.disable_retries()
        self.test_create_release_import_value_error()


class TestGetReleaseImportStatus:
    """
    Test Class for get_release_import_status
    """

    @responses.activate
    def test_get_release_import_status_all_params(self):
        """
        get_release_import_status()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/import')
        mock_response = '{"status": "Completed", "task_id": "task_id", "assistant_id": "assistant_id", "status_errors": [{"message": "message"}], "status_description": "status_description", "skill_impact_in_draft": ["action"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        include_audit = False

        # Invoke method
        response = _service.get_release_import_status(
            assistant_id,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_get_release_import_status_all_params_with_retries(self):
        # Enable retries and run test_get_release_import_status_all_params.
        _service.enable_retries()
        self.test_get_release_import_status_all_params()

        # Disable retries and run test_get_release_import_status_all_params.
        _service.disable_retries()
        self.test_get_release_import_status_all_params()

    @responses.activate
    def test_get_release_import_status_required_params(self):
        """
        test_get_release_import_status_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/import')
        mock_response = '{"status": "Completed", "task_id": "task_id", "assistant_id": "assistant_id", "status_errors": [{"message": "message"}], "status_description": "status_description", "skill_impact_in_draft": ["action"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.get_release_import_status(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_release_import_status_required_params_with_retries(self):
        # Enable retries and run test_get_release_import_status_required_params.
        _service.enable_retries()
        self.test_get_release_import_status_required_params()

        # Disable retries and run test_get_release_import_status_required_params.
        _service.disable_retries()
        self.test_get_release_import_status_required_params()

    @responses.activate
    def test_get_release_import_status_value_error(self):
        """
        test_get_release_import_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/import')
        mock_response = '{"status": "Completed", "task_id": "task_id", "assistant_id": "assistant_id", "status_errors": [{"message": "message"}], "status_description": "status_description", "skill_impact_in_draft": ["action"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_release_import_status(**req_copy)

    def test_get_release_import_status_value_error_with_retries(self):
        # Enable retries and run test_get_release_import_status_value_error.
        _service.enable_retries()
        self.test_get_release_import_status_value_error()

        # Disable retries and run test_get_release_import_status_value_error.
        _service.disable_retries()
        self.test_get_release_import_status_value_error()


# endregion
##############################################################################
# End of Service: Releases
##############################################################################

##############################################################################
# Start of Service: Skills
##############################################################################
# region


class TestGetSkill:
    """
    Test Class for get_skill
    """

    @responses.activate
    def test_get_skill_all_params(self):
        """
        get_skill()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills/testString')
        mock_response = '{"name": "name", "description": "description", "workspace": {"anyKey": "anyValue"}, "skill_id": "skill_id", "status": "Available", "status_errors": [{"message": "message"}], "status_description": "status_description", "dialog_settings": {"anyKey": "anyValue"}, "assistant_id": "assistant_id", "workspace_id": "workspace_id", "environment_id": "environment_id", "valid": false, "next_snapshot_version": "next_snapshot_version", "search_settings": {"discovery": {"instance_id": "instance_id", "project_id": "project_id", "url": "url", "max_primary_results": 10000, "max_total_results": 10000, "confidence_threshold": 0.0, "highlight": false, "find_answers": true, "authentication": {"basic": "basic", "bearer": "bearer"}}, "messages": {"success": "success", "error": "error", "no_result": "no_result"}, "schema_mapping": {"url": "url", "body": "body", "title": "title"}, "elastic_search": {"url": "url", "port": "port", "username": "username", "password": "password", "index": "index", "filter": ["anyValue"], "query_body": {"anyKey": "anyValue"}, "managed_index": "managed_index", "apikey": "apikey"}, "conversational_search": {"enabled": true, "response_length": {"option": "moderate"}, "search_confidence": {"threshold": "less_often"}}, "server_side_search": {"url": "url", "port": "port", "username": "username", "password": "password", "filter": "filter", "metadata": {"anyKey": "anyValue"}, "apikey": "apikey", "no_auth": false, "auth_type": "basic"}, "client_side_search": {"filter": "filter", "metadata": {"anyKey": "anyValue"}}}, "warnings": [{"code": "code", "path": "path", "message": "message"}], "language": "language", "type": "action"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        skill_id = 'testString'

        # Invoke method
        response = _service.get_skill(
            assistant_id,
            skill_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_skill_all_params_with_retries(self):
        # Enable retries and run test_get_skill_all_params.
        _service.enable_retries()
        self.test_get_skill_all_params()

        # Disable retries and run test_get_skill_all_params.
        _service.disable_retries()
        self.test_get_skill_all_params()

    @responses.activate
    def test_get_skill_value_error(self):
        """
        test_get_skill_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills/testString')
        mock_response = '{"name": "name", "description": "description", "workspace": {"anyKey": "anyValue"}, "skill_id": "skill_id", "status": "Available", "status_errors": [{"message": "message"}], "status_description": "status_description", "dialog_settings": {"anyKey": "anyValue"}, "assistant_id": "assistant_id", "workspace_id": "workspace_id", "environment_id": "environment_id", "valid": false, "next_snapshot_version": "next_snapshot_version", "search_settings": {"discovery": {"instance_id": "instance_id", "project_id": "project_id", "url": "url", "max_primary_results": 10000, "max_total_results": 10000, "confidence_threshold": 0.0, "highlight": false, "find_answers": true, "authentication": {"basic": "basic", "bearer": "bearer"}}, "messages": {"success": "success", "error": "error", "no_result": "no_result"}, "schema_mapping": {"url": "url", "body": "body", "title": "title"}, "elastic_search": {"url": "url", "port": "port", "username": "username", "password": "password", "index": "index", "filter": ["anyValue"], "query_body": {"anyKey": "anyValue"}, "managed_index": "managed_index", "apikey": "apikey"}, "conversational_search": {"enabled": true, "response_length": {"option": "moderate"}, "search_confidence": {"threshold": "less_often"}}, "server_side_search": {"url": "url", "port": "port", "username": "username", "password": "password", "filter": "filter", "metadata": {"anyKey": "anyValue"}, "apikey": "apikey", "no_auth": false, "auth_type": "basic"}, "client_side_search": {"filter": "filter", "metadata": {"anyKey": "anyValue"}}}, "warnings": [{"code": "code", "path": "path", "message": "message"}], "language": "language", "type": "action"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        skill_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "skill_id": skill_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_skill(**req_copy)

    def test_get_skill_value_error_with_retries(self):
        # Enable retries and run test_get_skill_value_error.
        _service.enable_retries()
        self.test_get_skill_value_error()

        # Disable retries and run test_get_skill_value_error.
        _service.disable_retries()
        self.test_get_skill_value_error()


class TestUpdateSkill:
    """
    Test Class for update_skill
    """

    @responses.activate
    def test_update_skill_all_params(self):
        """
        update_skill()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills/testString')
        mock_response = '{"name": "name", "description": "description", "workspace": {"anyKey": "anyValue"}, "skill_id": "skill_id", "status": "Available", "status_errors": [{"message": "message"}], "status_description": "status_description", "dialog_settings": {"anyKey": "anyValue"}, "assistant_id": "assistant_id", "workspace_id": "workspace_id", "environment_id": "environment_id", "valid": false, "next_snapshot_version": "next_snapshot_version", "search_settings": {"discovery": {"instance_id": "instance_id", "project_id": "project_id", "url": "url", "max_primary_results": 10000, "max_total_results": 10000, "confidence_threshold": 0.0, "highlight": false, "find_answers": true, "authentication": {"basic": "basic", "bearer": "bearer"}}, "messages": {"success": "success", "error": "error", "no_result": "no_result"}, "schema_mapping": {"url": "url", "body": "body", "title": "title"}, "elastic_search": {"url": "url", "port": "port", "username": "username", "password": "password", "index": "index", "filter": ["anyValue"], "query_body": {"anyKey": "anyValue"}, "managed_index": "managed_index", "apikey": "apikey"}, "conversational_search": {"enabled": true, "response_length": {"option": "moderate"}, "search_confidence": {"threshold": "less_often"}}, "server_side_search": {"url": "url", "port": "port", "username": "username", "password": "password", "filter": "filter", "metadata": {"anyKey": "anyValue"}, "apikey": "apikey", "no_auth": false, "auth_type": "basic"}, "client_side_search": {"filter": "filter", "metadata": {"anyKey": "anyValue"}}}, "warnings": [{"code": "code", "path": "path", "message": "message"}], "language": "language", "type": "action"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a SearchSettingsDiscoveryAuthentication model
        search_settings_discovery_authentication_model = {}
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        # Construct a dict representation of a SearchSettingsDiscovery model
        search_settings_discovery_model = {}
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        # Construct a dict representation of a SearchSettingsMessages model
        search_settings_messages_model = {}
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        # Construct a dict representation of a SearchSettingsSchemaMapping model
        search_settings_schema_mapping_model = {}
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        # Construct a dict representation of a SearchSettingsElasticSearch model
        search_settings_elastic_search_model = {}
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        # Construct a dict representation of a SearchSettingsConversationalSearchResponseLength model
        search_settings_conversational_search_response_length_model = {}
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        # Construct a dict representation of a SearchSettingsConversationalSearchSearchConfidence model
        search_settings_conversational_search_search_confidence_model = {}
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        # Construct a dict representation of a SearchSettingsConversationalSearch model
        search_settings_conversational_search_model = {}
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        # Construct a dict representation of a SearchSettingsServerSideSearch model
        search_settings_server_side_search_model = {}
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        # Construct a dict representation of a SearchSettingsClientSideSearch model
        search_settings_client_side_search_model = {}
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SearchSettings model
        search_settings_model = {}
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        # Set up parameter values
        assistant_id = 'testString'
        skill_id = 'testString'
        name = 'testString'
        description = 'testString'
        workspace = {'anyKey': 'anyValue'}
        dialog_settings = {'anyKey': 'anyValue'}
        search_settings = search_settings_model

        # Invoke method
        response = _service.update_skill(
            assistant_id,
            skill_id,
            name=name,
            description=description,
            workspace=workspace,
            dialog_settings=dialog_settings,
            search_settings=search_settings,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['workspace'] == {'anyKey': 'anyValue'}
        assert req_body['dialog_settings'] == {'anyKey': 'anyValue'}
        assert req_body['search_settings'] == search_settings_model

    def test_update_skill_all_params_with_retries(self):
        # Enable retries and run test_update_skill_all_params.
        _service.enable_retries()
        self.test_update_skill_all_params()

        # Disable retries and run test_update_skill_all_params.
        _service.disable_retries()
        self.test_update_skill_all_params()

    @responses.activate
    def test_update_skill_value_error(self):
        """
        test_update_skill_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills/testString')
        mock_response = '{"name": "name", "description": "description", "workspace": {"anyKey": "anyValue"}, "skill_id": "skill_id", "status": "Available", "status_errors": [{"message": "message"}], "status_description": "status_description", "dialog_settings": {"anyKey": "anyValue"}, "assistant_id": "assistant_id", "workspace_id": "workspace_id", "environment_id": "environment_id", "valid": false, "next_snapshot_version": "next_snapshot_version", "search_settings": {"discovery": {"instance_id": "instance_id", "project_id": "project_id", "url": "url", "max_primary_results": 10000, "max_total_results": 10000, "confidence_threshold": 0.0, "highlight": false, "find_answers": true, "authentication": {"basic": "basic", "bearer": "bearer"}}, "messages": {"success": "success", "error": "error", "no_result": "no_result"}, "schema_mapping": {"url": "url", "body": "body", "title": "title"}, "elastic_search": {"url": "url", "port": "port", "username": "username", "password": "password", "index": "index", "filter": ["anyValue"], "query_body": {"anyKey": "anyValue"}, "managed_index": "managed_index", "apikey": "apikey"}, "conversational_search": {"enabled": true, "response_length": {"option": "moderate"}, "search_confidence": {"threshold": "less_often"}}, "server_side_search": {"url": "url", "port": "port", "username": "username", "password": "password", "filter": "filter", "metadata": {"anyKey": "anyValue"}, "apikey": "apikey", "no_auth": false, "auth_type": "basic"}, "client_side_search": {"filter": "filter", "metadata": {"anyKey": "anyValue"}}}, "warnings": [{"code": "code", "path": "path", "message": "message"}], "language": "language", "type": "action"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a SearchSettingsDiscoveryAuthentication model
        search_settings_discovery_authentication_model = {}
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        # Construct a dict representation of a SearchSettingsDiscovery model
        search_settings_discovery_model = {}
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        # Construct a dict representation of a SearchSettingsMessages model
        search_settings_messages_model = {}
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        # Construct a dict representation of a SearchSettingsSchemaMapping model
        search_settings_schema_mapping_model = {}
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        # Construct a dict representation of a SearchSettingsElasticSearch model
        search_settings_elastic_search_model = {}
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        # Construct a dict representation of a SearchSettingsConversationalSearchResponseLength model
        search_settings_conversational_search_response_length_model = {}
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        # Construct a dict representation of a SearchSettingsConversationalSearchSearchConfidence model
        search_settings_conversational_search_search_confidence_model = {}
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        # Construct a dict representation of a SearchSettingsConversationalSearch model
        search_settings_conversational_search_model = {}
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        # Construct a dict representation of a SearchSettingsServerSideSearch model
        search_settings_server_side_search_model = {}
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        # Construct a dict representation of a SearchSettingsClientSideSearch model
        search_settings_client_side_search_model = {}
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SearchSettings model
        search_settings_model = {}
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        # Set up parameter values
        assistant_id = 'testString'
        skill_id = 'testString'
        name = 'testString'
        description = 'testString'
        workspace = {'anyKey': 'anyValue'}
        dialog_settings = {'anyKey': 'anyValue'}
        search_settings = search_settings_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "skill_id": skill_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_skill(**req_copy)

    def test_update_skill_value_error_with_retries(self):
        # Enable retries and run test_update_skill_value_error.
        _service.enable_retries()
        self.test_update_skill_value_error()

        # Disable retries and run test_update_skill_value_error.
        _service.disable_retries()
        self.test_update_skill_value_error()


class TestExportSkills:
    """
    Test Class for export_skills
    """

    @responses.activate
    def test_export_skills_all_params(self):
        """
        export_skills()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_export')
        mock_response = '{"assistant_skills": [{"name": "name", "description": "description", "workspace": {"anyKey": "anyValue"}, "skill_id": "skill_id", "status": "Available", "status_errors": [{"message": "message"}], "status_description": "status_description", "dialog_settings": {"anyKey": "anyValue"}, "assistant_id": "assistant_id", "workspace_id": "workspace_id", "environment_id": "environment_id", "valid": false, "next_snapshot_version": "next_snapshot_version", "search_settings": {"discovery": {"instance_id": "instance_id", "project_id": "project_id", "url": "url", "max_primary_results": 10000, "max_total_results": 10000, "confidence_threshold": 0.0, "highlight": false, "find_answers": true, "authentication": {"basic": "basic", "bearer": "bearer"}}, "messages": {"success": "success", "error": "error", "no_result": "no_result"}, "schema_mapping": {"url": "url", "body": "body", "title": "title"}, "elastic_search": {"url": "url", "port": "port", "username": "username", "password": "password", "index": "index", "filter": ["anyValue"], "query_body": {"anyKey": "anyValue"}, "managed_index": "managed_index", "apikey": "apikey"}, "conversational_search": {"enabled": true, "response_length": {"option": "moderate"}, "search_confidence": {"threshold": "less_often"}}, "server_side_search": {"url": "url", "port": "port", "username": "username", "password": "password", "filter": "filter", "metadata": {"anyKey": "anyValue"}, "apikey": "apikey", "no_auth": false, "auth_type": "basic"}, "client_side_search": {"filter": "filter", "metadata": {"anyKey": "anyValue"}}}, "warnings": [{"code": "code", "path": "path", "message": "message"}], "language": "language", "type": "action"}], "assistant_state": {"action_disabled": false, "dialog_disabled": false}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'
        include_audit = False

        # Invoke method
        response = _service.export_skills(
            assistant_id,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string

    def test_export_skills_all_params_with_retries(self):
        # Enable retries and run test_export_skills_all_params.
        _service.enable_retries()
        self.test_export_skills_all_params()

        # Disable retries and run test_export_skills_all_params.
        _service.disable_retries()
        self.test_export_skills_all_params()

    @responses.activate
    def test_export_skills_required_params(self):
        """
        test_export_skills_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_export')
        mock_response = '{"assistant_skills": [{"name": "name", "description": "description", "workspace": {"anyKey": "anyValue"}, "skill_id": "skill_id", "status": "Available", "status_errors": [{"message": "message"}], "status_description": "status_description", "dialog_settings": {"anyKey": "anyValue"}, "assistant_id": "assistant_id", "workspace_id": "workspace_id", "environment_id": "environment_id", "valid": false, "next_snapshot_version": "next_snapshot_version", "search_settings": {"discovery": {"instance_id": "instance_id", "project_id": "project_id", "url": "url", "max_primary_results": 10000, "max_total_results": 10000, "confidence_threshold": 0.0, "highlight": false, "find_answers": true, "authentication": {"basic": "basic", "bearer": "bearer"}}, "messages": {"success": "success", "error": "error", "no_result": "no_result"}, "schema_mapping": {"url": "url", "body": "body", "title": "title"}, "elastic_search": {"url": "url", "port": "port", "username": "username", "password": "password", "index": "index", "filter": ["anyValue"], "query_body": {"anyKey": "anyValue"}, "managed_index": "managed_index", "apikey": "apikey"}, "conversational_search": {"enabled": true, "response_length": {"option": "moderate"}, "search_confidence": {"threshold": "less_often"}}, "server_side_search": {"url": "url", "port": "port", "username": "username", "password": "password", "filter": "filter", "metadata": {"anyKey": "anyValue"}, "apikey": "apikey", "no_auth": false, "auth_type": "basic"}, "client_side_search": {"filter": "filter", "metadata": {"anyKey": "anyValue"}}}, "warnings": [{"code": "code", "path": "path", "message": "message"}], "language": "language", "type": "action"}], "assistant_state": {"action_disabled": false, "dialog_disabled": false}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.export_skills(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_export_skills_required_params_with_retries(self):
        # Enable retries and run test_export_skills_required_params.
        _service.enable_retries()
        self.test_export_skills_required_params()

        # Disable retries and run test_export_skills_required_params.
        _service.disable_retries()
        self.test_export_skills_required_params()

    @responses.activate
    def test_export_skills_value_error(self):
        """
        test_export_skills_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_export')
        mock_response = '{"assistant_skills": [{"name": "name", "description": "description", "workspace": {"anyKey": "anyValue"}, "skill_id": "skill_id", "status": "Available", "status_errors": [{"message": "message"}], "status_description": "status_description", "dialog_settings": {"anyKey": "anyValue"}, "assistant_id": "assistant_id", "workspace_id": "workspace_id", "environment_id": "environment_id", "valid": false, "next_snapshot_version": "next_snapshot_version", "search_settings": {"discovery": {"instance_id": "instance_id", "project_id": "project_id", "url": "url", "max_primary_results": 10000, "max_total_results": 10000, "confidence_threshold": 0.0, "highlight": false, "find_answers": true, "authentication": {"basic": "basic", "bearer": "bearer"}}, "messages": {"success": "success", "error": "error", "no_result": "no_result"}, "schema_mapping": {"url": "url", "body": "body", "title": "title"}, "elastic_search": {"url": "url", "port": "port", "username": "username", "password": "password", "index": "index", "filter": ["anyValue"], "query_body": {"anyKey": "anyValue"}, "managed_index": "managed_index", "apikey": "apikey"}, "conversational_search": {"enabled": true, "response_length": {"option": "moderate"}, "search_confidence": {"threshold": "less_often"}}, "server_side_search": {"url": "url", "port": "port", "username": "username", "password": "password", "filter": "filter", "metadata": {"anyKey": "anyValue"}, "apikey": "apikey", "no_auth": false, "auth_type": "basic"}, "client_side_search": {"filter": "filter", "metadata": {"anyKey": "anyValue"}}}, "warnings": [{"code": "code", "path": "path", "message": "message"}], "language": "language", "type": "action"}], "assistant_state": {"action_disabled": false, "dialog_disabled": false}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.export_skills(**req_copy)

    def test_export_skills_value_error_with_retries(self):
        # Enable retries and run test_export_skills_value_error.
        _service.enable_retries()
        self.test_export_skills_value_error()

        # Disable retries and run test_export_skills_value_error.
        _service.disable_retries()
        self.test_export_skills_value_error()


class TestImportSkills:
    """
    Test Class for import_skills
    """

    @responses.activate
    def test_import_skills_all_params(self):
        """
        import_skills()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_import')
        mock_response = '{"assistant_id": "assistant_id", "status": "Available", "status_description": "status_description", "status_errors": [{"message": "message"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a SearchSettingsDiscoveryAuthentication model
        search_settings_discovery_authentication_model = {}
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        # Construct a dict representation of a SearchSettingsDiscovery model
        search_settings_discovery_model = {}
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        # Construct a dict representation of a SearchSettingsMessages model
        search_settings_messages_model = {}
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        # Construct a dict representation of a SearchSettingsSchemaMapping model
        search_settings_schema_mapping_model = {}
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        # Construct a dict representation of a SearchSettingsElasticSearch model
        search_settings_elastic_search_model = {}
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        # Construct a dict representation of a SearchSettingsConversationalSearchResponseLength model
        search_settings_conversational_search_response_length_model = {}
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        # Construct a dict representation of a SearchSettingsConversationalSearchSearchConfidence model
        search_settings_conversational_search_search_confidence_model = {}
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        # Construct a dict representation of a SearchSettingsConversationalSearch model
        search_settings_conversational_search_model = {}
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        # Construct a dict representation of a SearchSettingsServerSideSearch model
        search_settings_server_side_search_model = {}
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        # Construct a dict representation of a SearchSettingsClientSideSearch model
        search_settings_client_side_search_model = {}
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SearchSettings model
        search_settings_model = {}
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        # Construct a dict representation of a SkillImport model
        skill_import_model = {}
        skill_import_model['name'] = 'testString'
        skill_import_model['description'] = 'testString'
        skill_import_model['workspace'] = {'anyKey': 'anyValue'}
        skill_import_model['dialog_settings'] = {'anyKey': 'anyValue'}
        skill_import_model['search_settings'] = search_settings_model
        skill_import_model['language'] = 'testString'
        skill_import_model['type'] = 'action'

        # Construct a dict representation of a AssistantState model
        assistant_state_model = {}
        assistant_state_model['action_disabled'] = True
        assistant_state_model['dialog_disabled'] = True

        # Set up parameter values
        assistant_id = 'testString'
        assistant_skills = [skill_import_model]
        assistant_state = assistant_state_model
        include_audit = False

        # Invoke method
        response = _service.import_skills(
            assistant_id,
            assistant_skills,
            assistant_state,
            include_audit=include_audit,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['assistant_skills'] == [skill_import_model]
        assert req_body['assistant_state'] == assistant_state_model

    def test_import_skills_all_params_with_retries(self):
        # Enable retries and run test_import_skills_all_params.
        _service.enable_retries()
        self.test_import_skills_all_params()

        # Disable retries and run test_import_skills_all_params.
        _service.disable_retries()
        self.test_import_skills_all_params()

    @responses.activate
    def test_import_skills_required_params(self):
        """
        test_import_skills_required_params()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_import')
        mock_response = '{"assistant_id": "assistant_id", "status": "Available", "status_description": "status_description", "status_errors": [{"message": "message"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a SearchSettingsDiscoveryAuthentication model
        search_settings_discovery_authentication_model = {}
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        # Construct a dict representation of a SearchSettingsDiscovery model
        search_settings_discovery_model = {}
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        # Construct a dict representation of a SearchSettingsMessages model
        search_settings_messages_model = {}
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        # Construct a dict representation of a SearchSettingsSchemaMapping model
        search_settings_schema_mapping_model = {}
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        # Construct a dict representation of a SearchSettingsElasticSearch model
        search_settings_elastic_search_model = {}
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        # Construct a dict representation of a SearchSettingsConversationalSearchResponseLength model
        search_settings_conversational_search_response_length_model = {}
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        # Construct a dict representation of a SearchSettingsConversationalSearchSearchConfidence model
        search_settings_conversational_search_search_confidence_model = {}
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        # Construct a dict representation of a SearchSettingsConversationalSearch model
        search_settings_conversational_search_model = {}
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        # Construct a dict representation of a SearchSettingsServerSideSearch model
        search_settings_server_side_search_model = {}
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        # Construct a dict representation of a SearchSettingsClientSideSearch model
        search_settings_client_side_search_model = {}
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SearchSettings model
        search_settings_model = {}
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        # Construct a dict representation of a SkillImport model
        skill_import_model = {}
        skill_import_model['name'] = 'testString'
        skill_import_model['description'] = 'testString'
        skill_import_model['workspace'] = {'anyKey': 'anyValue'}
        skill_import_model['dialog_settings'] = {'anyKey': 'anyValue'}
        skill_import_model['search_settings'] = search_settings_model
        skill_import_model['language'] = 'testString'
        skill_import_model['type'] = 'action'

        # Construct a dict representation of a AssistantState model
        assistant_state_model = {}
        assistant_state_model['action_disabled'] = True
        assistant_state_model['dialog_disabled'] = True

        # Set up parameter values
        assistant_id = 'testString'
        assistant_skills = [skill_import_model]
        assistant_state = assistant_state_model

        # Invoke method
        response = _service.import_skills(
            assistant_id,
            assistant_skills,
            assistant_state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['assistant_skills'] == [skill_import_model]
        assert req_body['assistant_state'] == assistant_state_model

    def test_import_skills_required_params_with_retries(self):
        # Enable retries and run test_import_skills_required_params.
        _service.enable_retries()
        self.test_import_skills_required_params()

        # Disable retries and run test_import_skills_required_params.
        _service.disable_retries()
        self.test_import_skills_required_params()

    @responses.activate
    def test_import_skills_value_error(self):
        """
        test_import_skills_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_import')
        mock_response = '{"assistant_id": "assistant_id", "status": "Available", "status_description": "status_description", "status_errors": [{"message": "message"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a SearchSettingsDiscoveryAuthentication model
        search_settings_discovery_authentication_model = {}
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        # Construct a dict representation of a SearchSettingsDiscovery model
        search_settings_discovery_model = {}
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        # Construct a dict representation of a SearchSettingsMessages model
        search_settings_messages_model = {}
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        # Construct a dict representation of a SearchSettingsSchemaMapping model
        search_settings_schema_mapping_model = {}
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        # Construct a dict representation of a SearchSettingsElasticSearch model
        search_settings_elastic_search_model = {}
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        # Construct a dict representation of a SearchSettingsConversationalSearchResponseLength model
        search_settings_conversational_search_response_length_model = {}
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        # Construct a dict representation of a SearchSettingsConversationalSearchSearchConfidence model
        search_settings_conversational_search_search_confidence_model = {}
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        # Construct a dict representation of a SearchSettingsConversationalSearch model
        search_settings_conversational_search_model = {}
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        # Construct a dict representation of a SearchSettingsServerSideSearch model
        search_settings_server_side_search_model = {}
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        # Construct a dict representation of a SearchSettingsClientSideSearch model
        search_settings_client_side_search_model = {}
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a SearchSettings model
        search_settings_model = {}
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        # Construct a dict representation of a SkillImport model
        skill_import_model = {}
        skill_import_model['name'] = 'testString'
        skill_import_model['description'] = 'testString'
        skill_import_model['workspace'] = {'anyKey': 'anyValue'}
        skill_import_model['dialog_settings'] = {'anyKey': 'anyValue'}
        skill_import_model['search_settings'] = search_settings_model
        skill_import_model['language'] = 'testString'
        skill_import_model['type'] = 'action'

        # Construct a dict representation of a AssistantState model
        assistant_state_model = {}
        assistant_state_model['action_disabled'] = True
        assistant_state_model['dialog_disabled'] = True

        # Set up parameter values
        assistant_id = 'testString'
        assistant_skills = [skill_import_model]
        assistant_state = assistant_state_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "assistant_skills": assistant_skills,
            "assistant_state": assistant_state,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.import_skills(**req_copy)

    def test_import_skills_value_error_with_retries(self):
        # Enable retries and run test_import_skills_value_error.
        _service.enable_retries()
        self.test_import_skills_value_error()

        # Disable retries and run test_import_skills_value_error.
        _service.disable_retries()
        self.test_import_skills_value_error()


class TestImportSkillsStatus:
    """
    Test Class for import_skills_status
    """

    @responses.activate
    def test_import_skills_status_all_params(self):
        """
        import_skills_status()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_import/status')
        mock_response = '{"assistant_id": "assistant_id", "status": "Available", "status_description": "status_description", "status_errors": [{"message": "message"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.import_skills_status(
            assistant_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_import_skills_status_all_params_with_retries(self):
        # Enable retries and run test_import_skills_status_all_params.
        _service.enable_retries()
        self.test_import_skills_status_all_params()

        # Disable retries and run test_import_skills_status_all_params.
        _service.disable_retries()
        self.test_import_skills_status_all_params()

    @responses.activate
    def test_import_skills_status_value_error(self):
        """
        test_import_skills_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/assistants/testString/skills_import/status')
        mock_response = '{"assistant_id": "assistant_id", "status": "Available", "status_description": "status_description", "status_errors": [{"message": "message"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.import_skills_status(**req_copy)

    def test_import_skills_status_value_error_with_retries(self):
        # Enable retries and run test_import_skills_status_value_error.
        _service.enable_retries()
        self.test_import_skills_status_value_error()

        # Disable retries and run test_import_skills_status_value_error.
        _service.disable_retries()
        self.test_import_skills_status_value_error()


# endregion
##############################################################################
# End of Service: Skills
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AgentAvailabilityMessage:
    """
    Test Class for AgentAvailabilityMessage
    """

    def test_agent_availability_message_serialization(self):
        """
        Test serialization/deserialization for AgentAvailabilityMessage
        """

        # Construct a json representation of a AgentAvailabilityMessage model
        agent_availability_message_model_json = {}
        agent_availability_message_model_json['message'] = 'testString'

        # Construct a model instance of AgentAvailabilityMessage by calling from_dict on the json representation
        agent_availability_message_model = AgentAvailabilityMessage.from_dict(agent_availability_message_model_json)
        assert agent_availability_message_model != False

        # Construct a model instance of AgentAvailabilityMessage by calling from_dict on the json representation
        agent_availability_message_model_dict = AgentAvailabilityMessage.from_dict(agent_availability_message_model_json).__dict__
        agent_availability_message_model2 = AgentAvailabilityMessage(**agent_availability_message_model_dict)

        # Verify the model instances are equivalent
        assert agent_availability_message_model == agent_availability_message_model2

        # Convert model instance back to dict and verify no loss of data
        agent_availability_message_model_json2 = agent_availability_message_model.to_dict()
        assert agent_availability_message_model_json2 == agent_availability_message_model_json


class TestModel_AssistantCollection:
    """
    Test Class for AssistantCollection
    """

    def test_assistant_collection_serialization(self):
        """
        Test serialization/deserialization for AssistantCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        assistant_data_model = {}  # AssistantData
        assistant_data_model['name'] = 'testString'
        assistant_data_model['description'] = 'testString'
        assistant_data_model['language'] = 'testString'

        pagination_model = {}  # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a AssistantCollection model
        assistant_collection_model_json = {}
        assistant_collection_model_json['assistants'] = [assistant_data_model]
        assistant_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of AssistantCollection by calling from_dict on the json representation
        assistant_collection_model = AssistantCollection.from_dict(assistant_collection_model_json)
        assert assistant_collection_model != False

        # Construct a model instance of AssistantCollection by calling from_dict on the json representation
        assistant_collection_model_dict = AssistantCollection.from_dict(assistant_collection_model_json).__dict__
        assistant_collection_model2 = AssistantCollection(**assistant_collection_model_dict)

        # Verify the model instances are equivalent
        assert assistant_collection_model == assistant_collection_model2

        # Convert model instance back to dict and verify no loss of data
        assistant_collection_model_json2 = assistant_collection_model.to_dict()
        assert assistant_collection_model_json2 == assistant_collection_model_json


class TestModel_AssistantData:
    """
    Test Class for AssistantData
    """

    def test_assistant_data_serialization(self):
        """
        Test serialization/deserialization for AssistantData
        """

        # Construct a json representation of a AssistantData model
        assistant_data_model_json = {}
        assistant_data_model_json['name'] = 'testString'
        assistant_data_model_json['description'] = 'testString'
        assistant_data_model_json['language'] = 'testString'

        # Construct a model instance of AssistantData by calling from_dict on the json representation
        assistant_data_model = AssistantData.from_dict(assistant_data_model_json)
        assert assistant_data_model != False

        # Construct a model instance of AssistantData by calling from_dict on the json representation
        assistant_data_model_dict = AssistantData.from_dict(assistant_data_model_json).__dict__
        assistant_data_model2 = AssistantData(**assistant_data_model_dict)

        # Verify the model instances are equivalent
        assert assistant_data_model == assistant_data_model2

        # Convert model instance back to dict and verify no loss of data
        assistant_data_model_json2 = assistant_data_model.to_dict()
        assert assistant_data_model_json2 == assistant_data_model_json


class TestModel_AssistantSkill:
    """
    Test Class for AssistantSkill
    """

    def test_assistant_skill_serialization(self):
        """
        Test serialization/deserialization for AssistantSkill
        """

        # Construct a json representation of a AssistantSkill model
        assistant_skill_model_json = {}
        assistant_skill_model_json['skill_id'] = 'testString'
        assistant_skill_model_json['type'] = 'dialog'

        # Construct a model instance of AssistantSkill by calling from_dict on the json representation
        assistant_skill_model = AssistantSkill.from_dict(assistant_skill_model_json)
        assert assistant_skill_model != False

        # Construct a model instance of AssistantSkill by calling from_dict on the json representation
        assistant_skill_model_dict = AssistantSkill.from_dict(assistant_skill_model_json).__dict__
        assistant_skill_model2 = AssistantSkill(**assistant_skill_model_dict)

        # Verify the model instances are equivalent
        assert assistant_skill_model == assistant_skill_model2

        # Convert model instance back to dict and verify no loss of data
        assistant_skill_model_json2 = assistant_skill_model.to_dict()
        assert assistant_skill_model_json2 == assistant_skill_model_json


class TestModel_AssistantState:
    """
    Test Class for AssistantState
    """

    def test_assistant_state_serialization(self):
        """
        Test serialization/deserialization for AssistantState
        """

        # Construct a json representation of a AssistantState model
        assistant_state_model_json = {}
        assistant_state_model_json['action_disabled'] = True
        assistant_state_model_json['dialog_disabled'] = True

        # Construct a model instance of AssistantState by calling from_dict on the json representation
        assistant_state_model = AssistantState.from_dict(assistant_state_model_json)
        assert assistant_state_model != False

        # Construct a model instance of AssistantState by calling from_dict on the json representation
        assistant_state_model_dict = AssistantState.from_dict(assistant_state_model_json).__dict__
        assistant_state_model2 = AssistantState(**assistant_state_model_dict)

        # Verify the model instances are equivalent
        assert assistant_state_model == assistant_state_model2

        # Convert model instance back to dict and verify no loss of data
        assistant_state_model_json2 = assistant_state_model.to_dict()
        assert assistant_state_model_json2 == assistant_state_model_json


class TestModel_BaseEnvironmentOrchestration:
    """
    Test Class for BaseEnvironmentOrchestration
    """

    def test_base_environment_orchestration_serialization(self):
        """
        Test serialization/deserialization for BaseEnvironmentOrchestration
        """

        # Construct a json representation of a BaseEnvironmentOrchestration model
        base_environment_orchestration_model_json = {}
        base_environment_orchestration_model_json['search_skill_fallback'] = True

        # Construct a model instance of BaseEnvironmentOrchestration by calling from_dict on the json representation
        base_environment_orchestration_model = BaseEnvironmentOrchestration.from_dict(base_environment_orchestration_model_json)
        assert base_environment_orchestration_model != False

        # Construct a model instance of BaseEnvironmentOrchestration by calling from_dict on the json representation
        base_environment_orchestration_model_dict = BaseEnvironmentOrchestration.from_dict(base_environment_orchestration_model_json).__dict__
        base_environment_orchestration_model2 = BaseEnvironmentOrchestration(**base_environment_orchestration_model_dict)

        # Verify the model instances are equivalent
        assert base_environment_orchestration_model == base_environment_orchestration_model2

        # Convert model instance back to dict and verify no loss of data
        base_environment_orchestration_model_json2 = base_environment_orchestration_model.to_dict()
        assert base_environment_orchestration_model_json2 == base_environment_orchestration_model_json


class TestModel_BaseEnvironmentReleaseReference:
    """
    Test Class for BaseEnvironmentReleaseReference
    """

    def test_base_environment_release_reference_serialization(self):
        """
        Test serialization/deserialization for BaseEnvironmentReleaseReference
        """

        # Construct a json representation of a BaseEnvironmentReleaseReference model
        base_environment_release_reference_model_json = {}
        base_environment_release_reference_model_json['release'] = 'testString'

        # Construct a model instance of BaseEnvironmentReleaseReference by calling from_dict on the json representation
        base_environment_release_reference_model = BaseEnvironmentReleaseReference.from_dict(base_environment_release_reference_model_json)
        assert base_environment_release_reference_model != False

        # Construct a model instance of BaseEnvironmentReleaseReference by calling from_dict on the json representation
        base_environment_release_reference_model_dict = BaseEnvironmentReleaseReference.from_dict(base_environment_release_reference_model_json).__dict__
        base_environment_release_reference_model2 = BaseEnvironmentReleaseReference(**base_environment_release_reference_model_dict)

        # Verify the model instances are equivalent
        assert base_environment_release_reference_model == base_environment_release_reference_model2

        # Convert model instance back to dict and verify no loss of data
        base_environment_release_reference_model_json2 = base_environment_release_reference_model.to_dict()
        assert base_environment_release_reference_model_json2 == base_environment_release_reference_model_json


class TestModel_BulkClassifyOutput:
    """
    Test Class for BulkClassifyOutput
    """

    def test_bulk_classify_output_serialization(self):
        """
        Test serialization/deserialization for BulkClassifyOutput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bulk_classify_utterance_model = {}  # BulkClassifyUtterance
        bulk_classify_utterance_model['text'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        # Construct a json representation of a BulkClassifyOutput model
        bulk_classify_output_model_json = {}
        bulk_classify_output_model_json['input'] = bulk_classify_utterance_model
        bulk_classify_output_model_json['entities'] = [runtime_entity_model]
        bulk_classify_output_model_json['intents'] = [runtime_intent_model]

        # Construct a model instance of BulkClassifyOutput by calling from_dict on the json representation
        bulk_classify_output_model = BulkClassifyOutput.from_dict(bulk_classify_output_model_json)
        assert bulk_classify_output_model != False

        # Construct a model instance of BulkClassifyOutput by calling from_dict on the json representation
        bulk_classify_output_model_dict = BulkClassifyOutput.from_dict(bulk_classify_output_model_json).__dict__
        bulk_classify_output_model2 = BulkClassifyOutput(**bulk_classify_output_model_dict)

        # Verify the model instances are equivalent
        assert bulk_classify_output_model == bulk_classify_output_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_classify_output_model_json2 = bulk_classify_output_model.to_dict()
        assert bulk_classify_output_model_json2 == bulk_classify_output_model_json


class TestModel_BulkClassifyResponse:
    """
    Test Class for BulkClassifyResponse
    """

    def test_bulk_classify_response_serialization(self):
        """
        Test serialization/deserialization for BulkClassifyResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bulk_classify_utterance_model = {}  # BulkClassifyUtterance
        bulk_classify_utterance_model['text'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        bulk_classify_output_model = {}  # BulkClassifyOutput
        bulk_classify_output_model['input'] = bulk_classify_utterance_model
        bulk_classify_output_model['entities'] = [runtime_entity_model]
        bulk_classify_output_model['intents'] = [runtime_intent_model]

        # Construct a json representation of a BulkClassifyResponse model
        bulk_classify_response_model_json = {}
        bulk_classify_response_model_json['output'] = [bulk_classify_output_model]

        # Construct a model instance of BulkClassifyResponse by calling from_dict on the json representation
        bulk_classify_response_model = BulkClassifyResponse.from_dict(bulk_classify_response_model_json)
        assert bulk_classify_response_model != False

        # Construct a model instance of BulkClassifyResponse by calling from_dict on the json representation
        bulk_classify_response_model_dict = BulkClassifyResponse.from_dict(bulk_classify_response_model_json).__dict__
        bulk_classify_response_model2 = BulkClassifyResponse(**bulk_classify_response_model_dict)

        # Verify the model instances are equivalent
        assert bulk_classify_response_model == bulk_classify_response_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_classify_response_model_json2 = bulk_classify_response_model.to_dict()
        assert bulk_classify_response_model_json2 == bulk_classify_response_model_json


class TestModel_BulkClassifyUtterance:
    """
    Test Class for BulkClassifyUtterance
    """

    def test_bulk_classify_utterance_serialization(self):
        """
        Test serialization/deserialization for BulkClassifyUtterance
        """

        # Construct a json representation of a BulkClassifyUtterance model
        bulk_classify_utterance_model_json = {}
        bulk_classify_utterance_model_json['text'] = 'testString'

        # Construct a model instance of BulkClassifyUtterance by calling from_dict on the json representation
        bulk_classify_utterance_model = BulkClassifyUtterance.from_dict(bulk_classify_utterance_model_json)
        assert bulk_classify_utterance_model != False

        # Construct a model instance of BulkClassifyUtterance by calling from_dict on the json representation
        bulk_classify_utterance_model_dict = BulkClassifyUtterance.from_dict(bulk_classify_utterance_model_json).__dict__
        bulk_classify_utterance_model2 = BulkClassifyUtterance(**bulk_classify_utterance_model_dict)

        # Verify the model instances are equivalent
        assert bulk_classify_utterance_model == bulk_classify_utterance_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_classify_utterance_model_json2 = bulk_classify_utterance_model.to_dict()
        assert bulk_classify_utterance_model_json2 == bulk_classify_utterance_model_json


class TestModel_CaptureGroup:
    """
    Test Class for CaptureGroup
    """

    def test_capture_group_serialization(self):
        """
        Test serialization/deserialization for CaptureGroup
        """

        # Construct a json representation of a CaptureGroup model
        capture_group_model_json = {}
        capture_group_model_json['group'] = 'testString'
        capture_group_model_json['location'] = [38]

        # Construct a model instance of CaptureGroup by calling from_dict on the json representation
        capture_group_model = CaptureGroup.from_dict(capture_group_model_json)
        assert capture_group_model != False

        # Construct a model instance of CaptureGroup by calling from_dict on the json representation
        capture_group_model_dict = CaptureGroup.from_dict(capture_group_model_json).__dict__
        capture_group_model2 = CaptureGroup(**capture_group_model_dict)

        # Verify the model instances are equivalent
        assert capture_group_model == capture_group_model2

        # Convert model instance back to dict and verify no loss of data
        capture_group_model_json2 = capture_group_model.to_dict()
        assert capture_group_model_json2 == capture_group_model_json


class TestModel_ChannelTransferInfo:
    """
    Test Class for ChannelTransferInfo
    """

    def test_channel_transfer_info_serialization(self):
        """
        Test serialization/deserialization for ChannelTransferInfo
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {}  # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {}  # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a json representation of a ChannelTransferInfo model
        channel_transfer_info_model_json = {}
        channel_transfer_info_model_json['target'] = channel_transfer_target_model

        # Construct a model instance of ChannelTransferInfo by calling from_dict on the json representation
        channel_transfer_info_model = ChannelTransferInfo.from_dict(channel_transfer_info_model_json)
        assert channel_transfer_info_model != False

        # Construct a model instance of ChannelTransferInfo by calling from_dict on the json representation
        channel_transfer_info_model_dict = ChannelTransferInfo.from_dict(channel_transfer_info_model_json).__dict__
        channel_transfer_info_model2 = ChannelTransferInfo(**channel_transfer_info_model_dict)

        # Verify the model instances are equivalent
        assert channel_transfer_info_model == channel_transfer_info_model2

        # Convert model instance back to dict and verify no loss of data
        channel_transfer_info_model_json2 = channel_transfer_info_model.to_dict()
        assert channel_transfer_info_model_json2 == channel_transfer_info_model_json


class TestModel_ChannelTransferTarget:
    """
    Test Class for ChannelTransferTarget
    """

    def test_channel_transfer_target_serialization(self):
        """
        Test serialization/deserialization for ChannelTransferTarget
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {}  # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a json representation of a ChannelTransferTarget model
        channel_transfer_target_model_json = {}
        channel_transfer_target_model_json['chat'] = channel_transfer_target_chat_model

        # Construct a model instance of ChannelTransferTarget by calling from_dict on the json representation
        channel_transfer_target_model = ChannelTransferTarget.from_dict(channel_transfer_target_model_json)
        assert channel_transfer_target_model != False

        # Construct a model instance of ChannelTransferTarget by calling from_dict on the json representation
        channel_transfer_target_model_dict = ChannelTransferTarget.from_dict(channel_transfer_target_model_json).__dict__
        channel_transfer_target_model2 = ChannelTransferTarget(**channel_transfer_target_model_dict)

        # Verify the model instances are equivalent
        assert channel_transfer_target_model == channel_transfer_target_model2

        # Convert model instance back to dict and verify no loss of data
        channel_transfer_target_model_json2 = channel_transfer_target_model.to_dict()
        assert channel_transfer_target_model_json2 == channel_transfer_target_model_json


class TestModel_ChannelTransferTargetChat:
    """
    Test Class for ChannelTransferTargetChat
    """

    def test_channel_transfer_target_chat_serialization(self):
        """
        Test serialization/deserialization for ChannelTransferTargetChat
        """

        # Construct a json representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model_json = {}
        channel_transfer_target_chat_model_json['url'] = 'testString'

        # Construct a model instance of ChannelTransferTargetChat by calling from_dict on the json representation
        channel_transfer_target_chat_model = ChannelTransferTargetChat.from_dict(channel_transfer_target_chat_model_json)
        assert channel_transfer_target_chat_model != False

        # Construct a model instance of ChannelTransferTargetChat by calling from_dict on the json representation
        channel_transfer_target_chat_model_dict = ChannelTransferTargetChat.from_dict(channel_transfer_target_chat_model_json).__dict__
        channel_transfer_target_chat_model2 = ChannelTransferTargetChat(**channel_transfer_target_chat_model_dict)

        # Verify the model instances are equivalent
        assert channel_transfer_target_chat_model == channel_transfer_target_chat_model2

        # Convert model instance back to dict and verify no loss of data
        channel_transfer_target_chat_model_json2 = channel_transfer_target_chat_model.to_dict()
        assert channel_transfer_target_chat_model_json2 == channel_transfer_target_chat_model_json


class TestModel_CreateAssistantReleaseImportResponse:
    """
    Test Class for CreateAssistantReleaseImportResponse
    """

    def test_create_assistant_release_import_response_serialization(self):
        """
        Test serialization/deserialization for CreateAssistantReleaseImportResponse
        """

        # Construct a json representation of a CreateAssistantReleaseImportResponse model
        create_assistant_release_import_response_model_json = {}
        create_assistant_release_import_response_model_json['skill_impact_in_draft'] = ['action']

        # Construct a model instance of CreateAssistantReleaseImportResponse by calling from_dict on the json representation
        create_assistant_release_import_response_model = CreateAssistantReleaseImportResponse.from_dict(create_assistant_release_import_response_model_json)
        assert create_assistant_release_import_response_model != False

        # Construct a model instance of CreateAssistantReleaseImportResponse by calling from_dict on the json representation
        create_assistant_release_import_response_model_dict = CreateAssistantReleaseImportResponse.from_dict(create_assistant_release_import_response_model_json).__dict__
        create_assistant_release_import_response_model2 = CreateAssistantReleaseImportResponse(**create_assistant_release_import_response_model_dict)

        # Verify the model instances are equivalent
        assert create_assistant_release_import_response_model == create_assistant_release_import_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_assistant_release_import_response_model_json2 = create_assistant_release_import_response_model.to_dict()
        assert create_assistant_release_import_response_model_json2 == create_assistant_release_import_response_model_json


class TestModel_CreateReleaseExportWithStatusErrors:
    """
    Test Class for CreateReleaseExportWithStatusErrors
    """

    def test_create_release_export_with_status_errors_serialization(self):
        """
        Test serialization/deserialization for CreateReleaseExportWithStatusErrors
        """

        # Construct a json representation of a CreateReleaseExportWithStatusErrors model
        create_release_export_with_status_errors_model_json = {}

        # Construct a model instance of CreateReleaseExportWithStatusErrors by calling from_dict on the json representation
        create_release_export_with_status_errors_model = CreateReleaseExportWithStatusErrors.from_dict(create_release_export_with_status_errors_model_json)
        assert create_release_export_with_status_errors_model != False

        # Construct a model instance of CreateReleaseExportWithStatusErrors by calling from_dict on the json representation
        create_release_export_with_status_errors_model_dict = CreateReleaseExportWithStatusErrors.from_dict(create_release_export_with_status_errors_model_json).__dict__
        create_release_export_with_status_errors_model2 = CreateReleaseExportWithStatusErrors(**create_release_export_with_status_errors_model_dict)

        # Verify the model instances are equivalent
        assert create_release_export_with_status_errors_model == create_release_export_with_status_errors_model2

        # Convert model instance back to dict and verify no loss of data
        create_release_export_with_status_errors_model_json2 = create_release_export_with_status_errors_model.to_dict()
        assert create_release_export_with_status_errors_model_json2 == create_release_export_with_status_errors_model_json


class TestModel_DialogLogMessage:
    """
    Test Class for DialogLogMessage
    """

    def test_dialog_log_message_serialization(self):
        """
        Test serialization/deserialization for DialogLogMessage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        # Construct a json representation of a DialogLogMessage model
        dialog_log_message_model_json = {}
        dialog_log_message_model_json['level'] = 'info'
        dialog_log_message_model_json['message'] = 'testString'
        dialog_log_message_model_json['code'] = 'testString'
        dialog_log_message_model_json['source'] = log_message_source_model

        # Construct a model instance of DialogLogMessage by calling from_dict on the json representation
        dialog_log_message_model = DialogLogMessage.from_dict(dialog_log_message_model_json)
        assert dialog_log_message_model != False

        # Construct a model instance of DialogLogMessage by calling from_dict on the json representation
        dialog_log_message_model_dict = DialogLogMessage.from_dict(dialog_log_message_model_json).__dict__
        dialog_log_message_model2 = DialogLogMessage(**dialog_log_message_model_dict)

        # Verify the model instances are equivalent
        assert dialog_log_message_model == dialog_log_message_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_log_message_model_json2 = dialog_log_message_model.to_dict()
        assert dialog_log_message_model_json2 == dialog_log_message_model_json


class TestModel_DialogNodeAction:
    """
    Test Class for DialogNodeAction
    """

    def test_dialog_node_action_serialization(self):
        """
        Test serialization/deserialization for DialogNodeAction
        """

        # Construct a json representation of a DialogNodeAction model
        dialog_node_action_model_json = {}
        dialog_node_action_model_json['name'] = 'testString'
        dialog_node_action_model_json['type'] = 'client'
        dialog_node_action_model_json['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model_json['result_variable'] = 'testString'
        dialog_node_action_model_json['credentials'] = 'testString'

        # Construct a model instance of DialogNodeAction by calling from_dict on the json representation
        dialog_node_action_model = DialogNodeAction.from_dict(dialog_node_action_model_json)
        assert dialog_node_action_model != False

        # Construct a model instance of DialogNodeAction by calling from_dict on the json representation
        dialog_node_action_model_dict = DialogNodeAction.from_dict(dialog_node_action_model_json).__dict__
        dialog_node_action_model2 = DialogNodeAction(**dialog_node_action_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_action_model == dialog_node_action_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_action_model_json2 = dialog_node_action_model.to_dict()
        assert dialog_node_action_model_json2 == dialog_node_action_model_json


class TestModel_DialogNodeOutputConnectToAgentTransferInfo:
    """
    Test Class for DialogNodeOutputConnectToAgentTransferInfo
    """

    def test_dialog_node_output_connect_to_agent_transfer_info_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputConnectToAgentTransferInfo
        """

        # Construct a json representation of a DialogNodeOutputConnectToAgentTransferInfo model
        dialog_node_output_connect_to_agent_transfer_info_model_json = {}
        dialog_node_output_connect_to_agent_transfer_info_model_json['target'] = {'key1': {'anyKey': 'anyValue'}}

        # Construct a model instance of DialogNodeOutputConnectToAgentTransferInfo by calling from_dict on the json representation
        dialog_node_output_connect_to_agent_transfer_info_model = DialogNodeOutputConnectToAgentTransferInfo.from_dict(dialog_node_output_connect_to_agent_transfer_info_model_json)
        assert dialog_node_output_connect_to_agent_transfer_info_model != False

        # Construct a model instance of DialogNodeOutputConnectToAgentTransferInfo by calling from_dict on the json representation
        dialog_node_output_connect_to_agent_transfer_info_model_dict = DialogNodeOutputConnectToAgentTransferInfo.from_dict(dialog_node_output_connect_to_agent_transfer_info_model_json).__dict__
        dialog_node_output_connect_to_agent_transfer_info_model2 = DialogNodeOutputConnectToAgentTransferInfo(**dialog_node_output_connect_to_agent_transfer_info_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_connect_to_agent_transfer_info_model == dialog_node_output_connect_to_agent_transfer_info_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_connect_to_agent_transfer_info_model_json2 = dialog_node_output_connect_to_agent_transfer_info_model.to_dict()
        assert dialog_node_output_connect_to_agent_transfer_info_model_json2 == dialog_node_output_connect_to_agent_transfer_info_model_json


class TestModel_DialogNodeOutputOptionsElement:
    """
    Test Class for DialogNodeOutputOptionsElement
    """

    def test_dialog_node_output_options_element_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputOptionsElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        dialog_node_output_options_element_value_model = {}  # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        # Construct a json representation of a DialogNodeOutputOptionsElement model
        dialog_node_output_options_element_model_json = {}
        dialog_node_output_options_element_model_json['label'] = 'testString'
        dialog_node_output_options_element_model_json['value'] = dialog_node_output_options_element_value_model

        # Construct a model instance of DialogNodeOutputOptionsElement by calling from_dict on the json representation
        dialog_node_output_options_element_model = DialogNodeOutputOptionsElement.from_dict(dialog_node_output_options_element_model_json)
        assert dialog_node_output_options_element_model != False

        # Construct a model instance of DialogNodeOutputOptionsElement by calling from_dict on the json representation
        dialog_node_output_options_element_model_dict = DialogNodeOutputOptionsElement.from_dict(dialog_node_output_options_element_model_json).__dict__
        dialog_node_output_options_element_model2 = DialogNodeOutputOptionsElement(**dialog_node_output_options_element_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_options_element_model == dialog_node_output_options_element_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_options_element_model_json2 = dialog_node_output_options_element_model.to_dict()
        assert dialog_node_output_options_element_model_json2 == dialog_node_output_options_element_model_json


class TestModel_DialogNodeOutputOptionsElementValue:
    """
    Test Class for DialogNodeOutputOptionsElementValue
    """

    def test_dialog_node_output_options_element_value_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputOptionsElementValue
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        # Construct a json representation of a DialogNodeOutputOptionsElementValue model
        dialog_node_output_options_element_value_model_json = {}
        dialog_node_output_options_element_value_model_json['input'] = message_input_model

        # Construct a model instance of DialogNodeOutputOptionsElementValue by calling from_dict on the json representation
        dialog_node_output_options_element_value_model = DialogNodeOutputOptionsElementValue.from_dict(dialog_node_output_options_element_value_model_json)
        assert dialog_node_output_options_element_value_model != False

        # Construct a model instance of DialogNodeOutputOptionsElementValue by calling from_dict on the json representation
        dialog_node_output_options_element_value_model_dict = DialogNodeOutputOptionsElementValue.from_dict(dialog_node_output_options_element_value_model_json).__dict__
        dialog_node_output_options_element_value_model2 = DialogNodeOutputOptionsElementValue(**dialog_node_output_options_element_value_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_options_element_value_model == dialog_node_output_options_element_value_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_options_element_value_model_json2 = dialog_node_output_options_element_value_model.to_dict()
        assert dialog_node_output_options_element_value_model_json2 == dialog_node_output_options_element_value_model_json


class TestModel_DialogNodeVisited:
    """
    Test Class for DialogNodeVisited
    """

    def test_dialog_node_visited_serialization(self):
        """
        Test serialization/deserialization for DialogNodeVisited
        """

        # Construct a json representation of a DialogNodeVisited model
        dialog_node_visited_model_json = {}
        dialog_node_visited_model_json['dialog_node'] = 'testString'
        dialog_node_visited_model_json['title'] = 'testString'
        dialog_node_visited_model_json['conditions'] = 'testString'

        # Construct a model instance of DialogNodeVisited by calling from_dict on the json representation
        dialog_node_visited_model = DialogNodeVisited.from_dict(dialog_node_visited_model_json)
        assert dialog_node_visited_model != False

        # Construct a model instance of DialogNodeVisited by calling from_dict on the json representation
        dialog_node_visited_model_dict = DialogNodeVisited.from_dict(dialog_node_visited_model_json).__dict__
        dialog_node_visited_model2 = DialogNodeVisited(**dialog_node_visited_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_visited_model == dialog_node_visited_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_visited_model_json2 = dialog_node_visited_model.to_dict()
        assert dialog_node_visited_model_json2 == dialog_node_visited_model_json


class TestModel_DialogSuggestion:
    """
    Test Class for DialogSuggestion
    """

    def test_dialog_suggestion_serialization(self):
        """
        Test serialization/deserialization for DialogSuggestion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        dialog_suggestion_value_model = {}  # DialogSuggestionValue
        dialog_suggestion_value_model['input'] = message_input_model

        # Construct a json representation of a DialogSuggestion model
        dialog_suggestion_model_json = {}
        dialog_suggestion_model_json['label'] = 'testString'
        dialog_suggestion_model_json['value'] = dialog_suggestion_value_model
        dialog_suggestion_model_json['output'] = {'anyKey': 'anyValue'}

        # Construct a model instance of DialogSuggestion by calling from_dict on the json representation
        dialog_suggestion_model = DialogSuggestion.from_dict(dialog_suggestion_model_json)
        assert dialog_suggestion_model != False

        # Construct a model instance of DialogSuggestion by calling from_dict on the json representation
        dialog_suggestion_model_dict = DialogSuggestion.from_dict(dialog_suggestion_model_json).__dict__
        dialog_suggestion_model2 = DialogSuggestion(**dialog_suggestion_model_dict)

        # Verify the model instances are equivalent
        assert dialog_suggestion_model == dialog_suggestion_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_suggestion_model_json2 = dialog_suggestion_model.to_dict()
        assert dialog_suggestion_model_json2 == dialog_suggestion_model_json


class TestModel_DialogSuggestionValue:
    """
    Test Class for DialogSuggestionValue
    """

    def test_dialog_suggestion_value_serialization(self):
        """
        Test serialization/deserialization for DialogSuggestionValue
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        # Construct a json representation of a DialogSuggestionValue model
        dialog_suggestion_value_model_json = {}
        dialog_suggestion_value_model_json['input'] = message_input_model

        # Construct a model instance of DialogSuggestionValue by calling from_dict on the json representation
        dialog_suggestion_value_model = DialogSuggestionValue.from_dict(dialog_suggestion_value_model_json)
        assert dialog_suggestion_value_model != False

        # Construct a model instance of DialogSuggestionValue by calling from_dict on the json representation
        dialog_suggestion_value_model_dict = DialogSuggestionValue.from_dict(dialog_suggestion_value_model_json).__dict__
        dialog_suggestion_value_model2 = DialogSuggestionValue(**dialog_suggestion_value_model_dict)

        # Verify the model instances are equivalent
        assert dialog_suggestion_value_model == dialog_suggestion_value_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_suggestion_value_model_json2 = dialog_suggestion_value_model.to_dict()
        assert dialog_suggestion_value_model_json2 == dialog_suggestion_value_model_json


class TestModel_Environment:
    """
    Test Class for Environment
    """

    def test_environment_serialization(self):
        """
        Test serialization/deserialization for Environment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        base_environment_orchestration_model = {}  # BaseEnvironmentOrchestration
        base_environment_orchestration_model['search_skill_fallback'] = True

        environment_skill_model = {}  # EnvironmentSkill
        environment_skill_model['skill_id'] = 'testString'
        environment_skill_model['type'] = 'dialog'
        environment_skill_model['disabled'] = True
        environment_skill_model['snapshot'] = 'testString'
        environment_skill_model['skill_reference'] = 'testString'

        # Construct a json representation of a Environment model
        environment_model_json = {}
        environment_model_json['name'] = 'testString'
        environment_model_json['description'] = 'testString'
        environment_model_json['orchestration'] = base_environment_orchestration_model
        environment_model_json['session_timeout'] = 10
        environment_model_json['skill_references'] = [environment_skill_model]

        # Construct a model instance of Environment by calling from_dict on the json representation
        environment_model = Environment.from_dict(environment_model_json)
        assert environment_model != False

        # Construct a model instance of Environment by calling from_dict on the json representation
        environment_model_dict = Environment.from_dict(environment_model_json).__dict__
        environment_model2 = Environment(**environment_model_dict)

        # Verify the model instances are equivalent
        assert environment_model == environment_model2

        # Convert model instance back to dict and verify no loss of data
        environment_model_json2 = environment_model.to_dict()
        assert environment_model_json2 == environment_model_json


class TestModel_EnvironmentCollection:
    """
    Test Class for EnvironmentCollection
    """

    def test_environment_collection_serialization(self):
        """
        Test serialization/deserialization for EnvironmentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        base_environment_orchestration_model = {}  # BaseEnvironmentOrchestration
        base_environment_orchestration_model['search_skill_fallback'] = True

        environment_skill_model = {}  # EnvironmentSkill
        environment_skill_model['skill_id'] = 'testString'
        environment_skill_model['type'] = 'dialog'
        environment_skill_model['disabled'] = True
        environment_skill_model['snapshot'] = 'testString'
        environment_skill_model['skill_reference'] = 'testString'

        environment_model = {}  # Environment
        environment_model['name'] = 'testString'
        environment_model['description'] = 'testString'
        environment_model['orchestration'] = base_environment_orchestration_model
        environment_model['session_timeout'] = 10
        environment_model['skill_references'] = [environment_skill_model]

        pagination_model = {}  # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a EnvironmentCollection model
        environment_collection_model_json = {}
        environment_collection_model_json['environments'] = [environment_model]
        environment_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of EnvironmentCollection by calling from_dict on the json representation
        environment_collection_model = EnvironmentCollection.from_dict(environment_collection_model_json)
        assert environment_collection_model != False

        # Construct a model instance of EnvironmentCollection by calling from_dict on the json representation
        environment_collection_model_dict = EnvironmentCollection.from_dict(environment_collection_model_json).__dict__
        environment_collection_model2 = EnvironmentCollection(**environment_collection_model_dict)

        # Verify the model instances are equivalent
        assert environment_collection_model == environment_collection_model2

        # Convert model instance back to dict and verify no loss of data
        environment_collection_model_json2 = environment_collection_model.to_dict()
        assert environment_collection_model_json2 == environment_collection_model_json


class TestModel_EnvironmentReference:
    """
    Test Class for EnvironmentReference
    """

    def test_environment_reference_serialization(self):
        """
        Test serialization/deserialization for EnvironmentReference
        """

        # Construct a json representation of a EnvironmentReference model
        environment_reference_model_json = {}
        environment_reference_model_json['name'] = 'testString'

        # Construct a model instance of EnvironmentReference by calling from_dict on the json representation
        environment_reference_model = EnvironmentReference.from_dict(environment_reference_model_json)
        assert environment_reference_model != False

        # Construct a model instance of EnvironmentReference by calling from_dict on the json representation
        environment_reference_model_dict = EnvironmentReference.from_dict(environment_reference_model_json).__dict__
        environment_reference_model2 = EnvironmentReference(**environment_reference_model_dict)

        # Verify the model instances are equivalent
        assert environment_reference_model == environment_reference_model2

        # Convert model instance back to dict and verify no loss of data
        environment_reference_model_json2 = environment_reference_model.to_dict()
        assert environment_reference_model_json2 == environment_reference_model_json


class TestModel_EnvironmentSkill:
    """
    Test Class for EnvironmentSkill
    """

    def test_environment_skill_serialization(self):
        """
        Test serialization/deserialization for EnvironmentSkill
        """

        # Construct a json representation of a EnvironmentSkill model
        environment_skill_model_json = {}
        environment_skill_model_json['skill_id'] = 'testString'
        environment_skill_model_json['type'] = 'dialog'
        environment_skill_model_json['disabled'] = True
        environment_skill_model_json['snapshot'] = 'testString'
        environment_skill_model_json['skill_reference'] = 'testString'

        # Construct a model instance of EnvironmentSkill by calling from_dict on the json representation
        environment_skill_model = EnvironmentSkill.from_dict(environment_skill_model_json)
        assert environment_skill_model != False

        # Construct a model instance of EnvironmentSkill by calling from_dict on the json representation
        environment_skill_model_dict = EnvironmentSkill.from_dict(environment_skill_model_json).__dict__
        environment_skill_model2 = EnvironmentSkill(**environment_skill_model_dict)

        # Verify the model instances are equivalent
        assert environment_skill_model == environment_skill_model2

        # Convert model instance back to dict and verify no loss of data
        environment_skill_model_json2 = environment_skill_model.to_dict()
        assert environment_skill_model_json2 == environment_skill_model_json


class TestModel_IntegrationReference:
    """
    Test Class for IntegrationReference
    """

    def test_integration_reference_serialization(self):
        """
        Test serialization/deserialization for IntegrationReference
        """

        # Construct a json representation of a IntegrationReference model
        integration_reference_model_json = {}
        integration_reference_model_json['integration_id'] = 'testString'
        integration_reference_model_json['type'] = 'testString'

        # Construct a model instance of IntegrationReference by calling from_dict on the json representation
        integration_reference_model = IntegrationReference.from_dict(integration_reference_model_json)
        assert integration_reference_model != False

        # Construct a model instance of IntegrationReference by calling from_dict on the json representation
        integration_reference_model_dict = IntegrationReference.from_dict(integration_reference_model_json).__dict__
        integration_reference_model2 = IntegrationReference(**integration_reference_model_dict)

        # Verify the model instances are equivalent
        assert integration_reference_model == integration_reference_model2

        # Convert model instance back to dict and verify no loss of data
        integration_reference_model_json2 = integration_reference_model.to_dict()
        assert integration_reference_model_json2 == integration_reference_model_json


class TestModel_Log:
    """
    Test Class for Log
    """

    def test_log_serialization(self):
        """
        Test serialization/deserialization for Log
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        log_request_input_model = {}  # LogRequestInput
        log_request_input_model['message_type'] = 'text'
        log_request_input_model['text'] = 'testString'
        log_request_input_model['intents'] = [runtime_intent_model]
        log_request_input_model['entities'] = [runtime_entity_model]
        log_request_input_model['suggestion_id'] = 'testString'
        log_request_input_model['attachments'] = [message_input_attachment_model]
        log_request_input_model['analytics'] = request_analytics_model
        log_request_input_model['options'] = message_input_options_model

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        message_context_global_model = {}  # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        message_context_action_skill_model = {}  # MessageContextActionSkill
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        message_context_skills_model = {}  # MessageContextSkills
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        message_context_model = {}  # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        log_request_model = {}  # LogRequest
        log_request_model['input'] = log_request_input_model
        log_request_model['context'] = message_context_model
        log_request_model['user_id'] = 'testString'

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {}  # RuntimeResponseGenericRuntimeResponseTypeText
        runtime_response_generic_model['response_type'] = 'text'
        runtime_response_generic_model['text'] = 'testString'
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_action_model = {}  # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        message_output_debug_model = {}  # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'
        message_output_debug_model['turn_events'] = [message_output_debug_turn_event_model]

        message_output_spelling_model = {}  # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        log_response_output_model = {}  # LogResponseOutput
        log_response_output_model['generic'] = [runtime_response_generic_model]
        log_response_output_model['intents'] = [runtime_intent_model]
        log_response_output_model['entities'] = [runtime_entity_model]
        log_response_output_model['actions'] = [dialog_node_action_model]
        log_response_output_model['debug'] = message_output_debug_model
        log_response_output_model['user_defined'] = {'anyKey': 'anyValue'}
        log_response_output_model['spelling'] = message_output_spelling_model

        log_response_model = {}  # LogResponse
        log_response_model['output'] = log_response_output_model
        log_response_model['context'] = message_context_model
        log_response_model['user_id'] = 'testString'

        # Construct a json representation of a Log model
        log_model_json = {}
        log_model_json['log_id'] = 'testString'
        log_model_json['request'] = log_request_model
        log_model_json['response'] = log_response_model
        log_model_json['assistant_id'] = 'testString'
        log_model_json['session_id'] = 'testString'
        log_model_json['skill_id'] = 'testString'
        log_model_json['snapshot'] = 'testString'
        log_model_json['request_timestamp'] = 'testString'
        log_model_json['response_timestamp'] = 'testString'
        log_model_json['language'] = 'testString'
        log_model_json['customer_id'] = 'testString'

        # Construct a model instance of Log by calling from_dict on the json representation
        log_model = Log.from_dict(log_model_json)
        assert log_model != False

        # Construct a model instance of Log by calling from_dict on the json representation
        log_model_dict = Log.from_dict(log_model_json).__dict__
        log_model2 = Log(**log_model_dict)

        # Verify the model instances are equivalent
        assert log_model == log_model2

        # Convert model instance back to dict and verify no loss of data
        log_model_json2 = log_model.to_dict()
        assert log_model_json2 == log_model_json


class TestModel_LogCollection:
    """
    Test Class for LogCollection
    """

    def test_log_collection_serialization(self):
        """
        Test serialization/deserialization for LogCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        log_request_input_model = {}  # LogRequestInput
        log_request_input_model['message_type'] = 'text'
        log_request_input_model['text'] = 'testString'
        log_request_input_model['intents'] = [runtime_intent_model]
        log_request_input_model['entities'] = [runtime_entity_model]
        log_request_input_model['suggestion_id'] = 'testString'
        log_request_input_model['attachments'] = [message_input_attachment_model]
        log_request_input_model['analytics'] = request_analytics_model
        log_request_input_model['options'] = message_input_options_model

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        message_context_global_model = {}  # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        message_context_action_skill_model = {}  # MessageContextActionSkill
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        message_context_skills_model = {}  # MessageContextSkills
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        message_context_model = {}  # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        log_request_model = {}  # LogRequest
        log_request_model['input'] = log_request_input_model
        log_request_model['context'] = message_context_model
        log_request_model['user_id'] = 'testString'

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {}  # RuntimeResponseGenericRuntimeResponseTypeText
        runtime_response_generic_model['response_type'] = 'text'
        runtime_response_generic_model['text'] = 'testString'
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_action_model = {}  # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        message_output_debug_model = {}  # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'
        message_output_debug_model['turn_events'] = [message_output_debug_turn_event_model]

        message_output_spelling_model = {}  # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        log_response_output_model = {}  # LogResponseOutput
        log_response_output_model['generic'] = [runtime_response_generic_model]
        log_response_output_model['intents'] = [runtime_intent_model]
        log_response_output_model['entities'] = [runtime_entity_model]
        log_response_output_model['actions'] = [dialog_node_action_model]
        log_response_output_model['debug'] = message_output_debug_model
        log_response_output_model['user_defined'] = {'anyKey': 'anyValue'}
        log_response_output_model['spelling'] = message_output_spelling_model

        log_response_model = {}  # LogResponse
        log_response_model['output'] = log_response_output_model
        log_response_model['context'] = message_context_model
        log_response_model['user_id'] = 'testString'

        log_model = {}  # Log
        log_model['log_id'] = 'testString'
        log_model['request'] = log_request_model
        log_model['response'] = log_response_model
        log_model['assistant_id'] = 'testString'
        log_model['session_id'] = 'testString'
        log_model['skill_id'] = 'testString'
        log_model['snapshot'] = 'testString'
        log_model['request_timestamp'] = 'testString'
        log_model['response_timestamp'] = 'testString'
        log_model['language'] = 'testString'
        log_model['customer_id'] = 'testString'

        log_pagination_model = {}  # LogPagination
        log_pagination_model['next_url'] = 'testString'
        log_pagination_model['matched'] = 38
        log_pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a LogCollection model
        log_collection_model_json = {}
        log_collection_model_json['logs'] = [log_model]
        log_collection_model_json['pagination'] = log_pagination_model

        # Construct a model instance of LogCollection by calling from_dict on the json representation
        log_collection_model = LogCollection.from_dict(log_collection_model_json)
        assert log_collection_model != False

        # Construct a model instance of LogCollection by calling from_dict on the json representation
        log_collection_model_dict = LogCollection.from_dict(log_collection_model_json).__dict__
        log_collection_model2 = LogCollection(**log_collection_model_dict)

        # Verify the model instances are equivalent
        assert log_collection_model == log_collection_model2

        # Convert model instance back to dict and verify no loss of data
        log_collection_model_json2 = log_collection_model.to_dict()
        assert log_collection_model_json2 == log_collection_model_json


class TestModel_LogPagination:
    """
    Test Class for LogPagination
    """

    def test_log_pagination_serialization(self):
        """
        Test serialization/deserialization for LogPagination
        """

        # Construct a json representation of a LogPagination model
        log_pagination_model_json = {}
        log_pagination_model_json['next_url'] = 'testString'
        log_pagination_model_json['matched'] = 38
        log_pagination_model_json['next_cursor'] = 'testString'

        # Construct a model instance of LogPagination by calling from_dict on the json representation
        log_pagination_model = LogPagination.from_dict(log_pagination_model_json)
        assert log_pagination_model != False

        # Construct a model instance of LogPagination by calling from_dict on the json representation
        log_pagination_model_dict = LogPagination.from_dict(log_pagination_model_json).__dict__
        log_pagination_model2 = LogPagination(**log_pagination_model_dict)

        # Verify the model instances are equivalent
        assert log_pagination_model == log_pagination_model2

        # Convert model instance back to dict and verify no loss of data
        log_pagination_model_json2 = log_pagination_model.to_dict()
        assert log_pagination_model_json2 == log_pagination_model_json


class TestModel_LogRequest:
    """
    Test Class for LogRequest
    """

    def test_log_request_serialization(self):
        """
        Test serialization/deserialization for LogRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = True
        message_input_options_model['export'] = True

        log_request_input_model = {}  # LogRequestInput
        log_request_input_model['message_type'] = 'text'
        log_request_input_model['text'] = 'Hello'
        log_request_input_model['intents'] = [runtime_intent_model]
        log_request_input_model['entities'] = [runtime_entity_model]
        log_request_input_model['suggestion_id'] = 'testString'
        log_request_input_model['attachments'] = [message_input_attachment_model]
        log_request_input_model['analytics'] = request_analytics_model
        log_request_input_model['options'] = message_input_options_model

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'my_user_id'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        message_context_global_model = {}  # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        message_context_action_skill_model = {}  # MessageContextActionSkill
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        message_context_skills_model = {}  # MessageContextSkills
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        message_context_model = {}  # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a LogRequest model
        log_request_model_json = {}
        log_request_model_json['input'] = log_request_input_model
        log_request_model_json['context'] = message_context_model
        log_request_model_json['user_id'] = 'testString'

        # Construct a model instance of LogRequest by calling from_dict on the json representation
        log_request_model = LogRequest.from_dict(log_request_model_json)
        assert log_request_model != False

        # Construct a model instance of LogRequest by calling from_dict on the json representation
        log_request_model_dict = LogRequest.from_dict(log_request_model_json).__dict__
        log_request_model2 = LogRequest(**log_request_model_dict)

        # Verify the model instances are equivalent
        assert log_request_model == log_request_model2

        # Convert model instance back to dict and verify no loss of data
        log_request_model_json2 = log_request_model.to_dict()
        assert log_request_model_json2 == log_request_model_json


class TestModel_LogRequestInput:
    """
    Test Class for LogRequestInput
    """

    def test_log_request_input_serialization(self):
        """
        Test serialization/deserialization for LogRequestInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        # Construct a json representation of a LogRequestInput model
        log_request_input_model_json = {}
        log_request_input_model_json['message_type'] = 'text'
        log_request_input_model_json['text'] = 'testString'
        log_request_input_model_json['intents'] = [runtime_intent_model]
        log_request_input_model_json['entities'] = [runtime_entity_model]
        log_request_input_model_json['suggestion_id'] = 'testString'
        log_request_input_model_json['attachments'] = [message_input_attachment_model]
        log_request_input_model_json['analytics'] = request_analytics_model
        log_request_input_model_json['options'] = message_input_options_model

        # Construct a model instance of LogRequestInput by calling from_dict on the json representation
        log_request_input_model = LogRequestInput.from_dict(log_request_input_model_json)
        assert log_request_input_model != False

        # Construct a model instance of LogRequestInput by calling from_dict on the json representation
        log_request_input_model_dict = LogRequestInput.from_dict(log_request_input_model_json).__dict__
        log_request_input_model2 = LogRequestInput(**log_request_input_model_dict)

        # Verify the model instances are equivalent
        assert log_request_input_model == log_request_input_model2

        # Convert model instance back to dict and verify no loss of data
        log_request_input_model_json2 = log_request_input_model.to_dict()
        assert log_request_input_model_json2 == log_request_input_model_json


class TestModel_LogResponse:
    """
    Test Class for LogResponse
    """

    def test_log_response_serialization(self):
        """
        Test serialization/deserialization for LogResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {}  # RuntimeResponseGenericRuntimeResponseTypeText
        runtime_response_generic_model['response_type'] = 'text'
        runtime_response_generic_model['text'] = 'testString'
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        dialog_node_action_model = {}  # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        message_output_debug_model = {}  # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'
        message_output_debug_model['turn_events'] = [message_output_debug_turn_event_model]

        message_output_spelling_model = {}  # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        log_response_output_model = {}  # LogResponseOutput
        log_response_output_model['generic'] = [runtime_response_generic_model]
        log_response_output_model['intents'] = [runtime_intent_model]
        log_response_output_model['entities'] = [runtime_entity_model]
        log_response_output_model['actions'] = [dialog_node_action_model]
        log_response_output_model['debug'] = message_output_debug_model
        log_response_output_model['user_defined'] = {'anyKey': 'anyValue'}
        log_response_output_model['spelling'] = message_output_spelling_model

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        message_context_global_model = {}  # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        message_context_action_skill_model = {}  # MessageContextActionSkill
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        message_context_skills_model = {}  # MessageContextSkills
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        message_context_model = {}  # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a LogResponse model
        log_response_model_json = {}
        log_response_model_json['output'] = log_response_output_model
        log_response_model_json['context'] = message_context_model
        log_response_model_json['user_id'] = 'testString'

        # Construct a model instance of LogResponse by calling from_dict on the json representation
        log_response_model = LogResponse.from_dict(log_response_model_json)
        assert log_response_model != False

        # Construct a model instance of LogResponse by calling from_dict on the json representation
        log_response_model_dict = LogResponse.from_dict(log_response_model_json).__dict__
        log_response_model2 = LogResponse(**log_response_model_dict)

        # Verify the model instances are equivalent
        assert log_response_model == log_response_model2

        # Convert model instance back to dict and verify no loss of data
        log_response_model_json2 = log_response_model.to_dict()
        assert log_response_model_json2 == log_response_model_json


class TestModel_LogResponseOutput:
    """
    Test Class for LogResponseOutput
    """

    def test_log_response_output_serialization(self):
        """
        Test serialization/deserialization for LogResponseOutput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {}  # RuntimeResponseGenericRuntimeResponseTypeText
        runtime_response_generic_model['response_type'] = 'text'
        runtime_response_generic_model['text'] = 'testString'
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        dialog_node_action_model = {}  # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        message_output_debug_model = {}  # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'
        message_output_debug_model['turn_events'] = [message_output_debug_turn_event_model]

        message_output_spelling_model = {}  # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        # Construct a json representation of a LogResponseOutput model
        log_response_output_model_json = {}
        log_response_output_model_json['generic'] = [runtime_response_generic_model]
        log_response_output_model_json['intents'] = [runtime_intent_model]
        log_response_output_model_json['entities'] = [runtime_entity_model]
        log_response_output_model_json['actions'] = [dialog_node_action_model]
        log_response_output_model_json['debug'] = message_output_debug_model
        log_response_output_model_json['user_defined'] = {'anyKey': 'anyValue'}
        log_response_output_model_json['spelling'] = message_output_spelling_model

        # Construct a model instance of LogResponseOutput by calling from_dict on the json representation
        log_response_output_model = LogResponseOutput.from_dict(log_response_output_model_json)
        assert log_response_output_model != False

        # Construct a model instance of LogResponseOutput by calling from_dict on the json representation
        log_response_output_model_dict = LogResponseOutput.from_dict(log_response_output_model_json).__dict__
        log_response_output_model2 = LogResponseOutput(**log_response_output_model_dict)

        # Verify the model instances are equivalent
        assert log_response_output_model == log_response_output_model2

        # Convert model instance back to dict and verify no loss of data
        log_response_output_model_json2 = log_response_output_model.to_dict()
        assert log_response_output_model_json2 == log_response_output_model_json


class TestModel_MessageContext:
    """
    Test Class for MessageContext
    """

    def test_message_context_serialization(self):
        """
        Test serialization/deserialization for MessageContext
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        message_context_global_model = {}  # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        message_context_action_skill_model = {}  # MessageContextActionSkill
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        message_context_skills_model = {}  # MessageContextSkills
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        # Construct a json representation of a MessageContext model
        message_context_model_json = {}
        message_context_model_json['global'] = message_context_global_model
        message_context_model_json['skills'] = message_context_skills_model
        message_context_model_json['integrations'] = {'anyKey': 'anyValue'}

        # Construct a model instance of MessageContext by calling from_dict on the json representation
        message_context_model = MessageContext.from_dict(message_context_model_json)
        assert message_context_model != False

        # Construct a model instance of MessageContext by calling from_dict on the json representation
        message_context_model_dict = MessageContext.from_dict(message_context_model_json).__dict__
        message_context_model2 = MessageContext(**message_context_model_dict)

        # Verify the model instances are equivalent
        assert message_context_model == message_context_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_model_json2 = message_context_model.to_dict()
        assert message_context_model_json2 == message_context_model_json


class TestModel_MessageContextActionSkill:
    """
    Test Class for MessageContextActionSkill
    """

    def test_message_context_action_skill_serialization(self):
        """
        Test serialization/deserialization for MessageContextActionSkill
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a json representation of a MessageContextActionSkill model
        message_context_action_skill_model_json = {}
        message_context_action_skill_model_json['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model_json['system'] = message_context_skill_system_model
        message_context_action_skill_model_json['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model_json['skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a model instance of MessageContextActionSkill by calling from_dict on the json representation
        message_context_action_skill_model = MessageContextActionSkill.from_dict(message_context_action_skill_model_json)
        assert message_context_action_skill_model != False

        # Construct a model instance of MessageContextActionSkill by calling from_dict on the json representation
        message_context_action_skill_model_dict = MessageContextActionSkill.from_dict(message_context_action_skill_model_json).__dict__
        message_context_action_skill_model2 = MessageContextActionSkill(**message_context_action_skill_model_dict)

        # Verify the model instances are equivalent
        assert message_context_action_skill_model == message_context_action_skill_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_action_skill_model_json2 = message_context_action_skill_model.to_dict()
        assert message_context_action_skill_model_json2 == message_context_action_skill_model_json


class TestModel_MessageContextDialogSkill:
    """
    Test Class for MessageContextDialogSkill
    """

    def test_message_context_dialog_skill_serialization(self):
        """
        Test serialization/deserialization for MessageContextDialogSkill
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a json representation of a MessageContextDialogSkill model
        message_context_dialog_skill_model_json = {}
        message_context_dialog_skill_model_json['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model_json['system'] = message_context_skill_system_model

        # Construct a model instance of MessageContextDialogSkill by calling from_dict on the json representation
        message_context_dialog_skill_model = MessageContextDialogSkill.from_dict(message_context_dialog_skill_model_json)
        assert message_context_dialog_skill_model != False

        # Construct a model instance of MessageContextDialogSkill by calling from_dict on the json representation
        message_context_dialog_skill_model_dict = MessageContextDialogSkill.from_dict(message_context_dialog_skill_model_json).__dict__
        message_context_dialog_skill_model2 = MessageContextDialogSkill(**message_context_dialog_skill_model_dict)

        # Verify the model instances are equivalent
        assert message_context_dialog_skill_model == message_context_dialog_skill_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_dialog_skill_model_json2 = message_context_dialog_skill_model.to_dict()
        assert message_context_dialog_skill_model_json2 == message_context_dialog_skill_model_json


class TestModel_MessageContextGlobal:
    """
    Test Class for MessageContextGlobal
    """

    def test_message_context_global_serialization(self):
        """
        Test serialization/deserialization for MessageContextGlobal
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        # Construct a json representation of a MessageContextGlobal model
        message_context_global_model_json = {}
        message_context_global_model_json['system'] = message_context_global_system_model

        # Construct a model instance of MessageContextGlobal by calling from_dict on the json representation
        message_context_global_model = MessageContextGlobal.from_dict(message_context_global_model_json)
        assert message_context_global_model != False

        # Construct a model instance of MessageContextGlobal by calling from_dict on the json representation
        message_context_global_model_dict = MessageContextGlobal.from_dict(message_context_global_model_json).__dict__
        message_context_global_model2 = MessageContextGlobal(**message_context_global_model_dict)

        # Verify the model instances are equivalent
        assert message_context_global_model == message_context_global_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_global_model_json2 = message_context_global_model.to_dict()
        assert message_context_global_model_json2 == message_context_global_model_json


class TestModel_MessageContextGlobalSystem:
    """
    Test Class for MessageContextGlobalSystem
    """

    def test_message_context_global_system_serialization(self):
        """
        Test serialization/deserialization for MessageContextGlobalSystem
        """

        # Construct a json representation of a MessageContextGlobalSystem model
        message_context_global_system_model_json = {}
        message_context_global_system_model_json['timezone'] = 'testString'
        message_context_global_system_model_json['user_id'] = 'testString'
        message_context_global_system_model_json['turn_count'] = 38
        message_context_global_system_model_json['locale'] = 'en-us'
        message_context_global_system_model_json['reference_time'] = 'testString'
        message_context_global_system_model_json['session_start_time'] = 'testString'
        message_context_global_system_model_json['state'] = 'testString'
        message_context_global_system_model_json['skip_user_input'] = True

        # Construct a model instance of MessageContextGlobalSystem by calling from_dict on the json representation
        message_context_global_system_model = MessageContextGlobalSystem.from_dict(message_context_global_system_model_json)
        assert message_context_global_system_model != False

        # Construct a model instance of MessageContextGlobalSystem by calling from_dict on the json representation
        message_context_global_system_model_dict = MessageContextGlobalSystem.from_dict(message_context_global_system_model_json).__dict__
        message_context_global_system_model2 = MessageContextGlobalSystem(**message_context_global_system_model_dict)

        # Verify the model instances are equivalent
        assert message_context_global_system_model == message_context_global_system_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_global_system_model_json2 = message_context_global_system_model.to_dict()
        assert message_context_global_system_model_json2 == message_context_global_system_model_json


class TestModel_MessageContextSkillSystem:
    """
    Test Class for MessageContextSkillSystem
    """

    def test_message_context_skill_system_serialization(self):
        """
        Test serialization/deserialization for MessageContextSkillSystem
        """

        # Construct a json representation of a MessageContextSkillSystem model
        message_context_skill_system_model_json = {}
        message_context_skill_system_model_json['state'] = 'testString'
        message_context_skill_system_model_json['foo'] = 'testString'

        # Construct a model instance of MessageContextSkillSystem by calling from_dict on the json representation
        message_context_skill_system_model = MessageContextSkillSystem.from_dict(message_context_skill_system_model_json)
        assert message_context_skill_system_model != False

        # Construct a model instance of MessageContextSkillSystem by calling from_dict on the json representation
        message_context_skill_system_model_dict = MessageContextSkillSystem.from_dict(message_context_skill_system_model_json).__dict__
        message_context_skill_system_model2 = MessageContextSkillSystem(**message_context_skill_system_model_dict)

        # Verify the model instances are equivalent
        assert message_context_skill_system_model == message_context_skill_system_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_skill_system_model_json2 = message_context_skill_system_model.to_dict()
        assert message_context_skill_system_model_json2 == message_context_skill_system_model_json

        # Test get_properties and set_properties methods.
        message_context_skill_system_model.set_properties({})
        actual_dict = message_context_skill_system_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        message_context_skill_system_model.set_properties(expected_dict)
        actual_dict = message_context_skill_system_model.get_properties()
        assert actual_dict.keys() == expected_dict.keys()


class TestModel_MessageContextSkills:
    """
    Test Class for MessageContextSkills
    """

    def test_message_context_skills_serialization(self):
        """
        Test serialization/deserialization for MessageContextSkills
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        message_context_action_skill_model = {}  # MessageContextActionSkill
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a MessageContextSkills model
        message_context_skills_model_json = {}
        message_context_skills_model_json['main skill'] = message_context_dialog_skill_model
        message_context_skills_model_json['actions skill'] = message_context_action_skill_model

        # Construct a model instance of MessageContextSkills by calling from_dict on the json representation
        message_context_skills_model = MessageContextSkills.from_dict(message_context_skills_model_json)
        assert message_context_skills_model != False

        # Construct a model instance of MessageContextSkills by calling from_dict on the json representation
        message_context_skills_model_dict = MessageContextSkills.from_dict(message_context_skills_model_json).__dict__
        message_context_skills_model2 = MessageContextSkills(**message_context_skills_model_dict)

        # Verify the model instances are equivalent
        assert message_context_skills_model == message_context_skills_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_skills_model_json2 = message_context_skills_model.to_dict()
        assert message_context_skills_model_json2 == message_context_skills_model_json


class TestModel_MessageInput:
    """
    Test Class for MessageInput
    """

    def test_message_input_serialization(self):
        """
        Test serialization/deserialization for MessageInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        # Construct a json representation of a MessageInput model
        message_input_model_json = {}
        message_input_model_json['message_type'] = 'text'
        message_input_model_json['text'] = 'testString'
        message_input_model_json['intents'] = [runtime_intent_model]
        message_input_model_json['entities'] = [runtime_entity_model]
        message_input_model_json['suggestion_id'] = 'testString'
        message_input_model_json['attachments'] = [message_input_attachment_model]
        message_input_model_json['analytics'] = request_analytics_model
        message_input_model_json['options'] = message_input_options_model

        # Construct a model instance of MessageInput by calling from_dict on the json representation
        message_input_model = MessageInput.from_dict(message_input_model_json)
        assert message_input_model != False

        # Construct a model instance of MessageInput by calling from_dict on the json representation
        message_input_model_dict = MessageInput.from_dict(message_input_model_json).__dict__
        message_input_model2 = MessageInput(**message_input_model_dict)

        # Verify the model instances are equivalent
        assert message_input_model == message_input_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_model_json2 = message_input_model.to_dict()
        assert message_input_model_json2 == message_input_model_json


class TestModel_MessageInputAttachment:
    """
    Test Class for MessageInputAttachment
    """

    def test_message_input_attachment_serialization(self):
        """
        Test serialization/deserialization for MessageInputAttachment
        """

        # Construct a json representation of a MessageInputAttachment model
        message_input_attachment_model_json = {}
        message_input_attachment_model_json['url'] = 'testString'
        message_input_attachment_model_json['media_type'] = 'testString'

        # Construct a model instance of MessageInputAttachment by calling from_dict on the json representation
        message_input_attachment_model = MessageInputAttachment.from_dict(message_input_attachment_model_json)
        assert message_input_attachment_model != False

        # Construct a model instance of MessageInputAttachment by calling from_dict on the json representation
        message_input_attachment_model_dict = MessageInputAttachment.from_dict(message_input_attachment_model_json).__dict__
        message_input_attachment_model2 = MessageInputAttachment(**message_input_attachment_model_dict)

        # Verify the model instances are equivalent
        assert message_input_attachment_model == message_input_attachment_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_attachment_model_json2 = message_input_attachment_model.to_dict()
        assert message_input_attachment_model_json2 == message_input_attachment_model_json


class TestModel_MessageInputOptions:
    """
    Test Class for MessageInputOptions
    """

    def test_message_input_options_serialization(self):
        """
        Test serialization/deserialization for MessageInputOptions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a json representation of a MessageInputOptions model
        message_input_options_model_json = {}
        message_input_options_model_json['restart'] = False
        message_input_options_model_json['alternate_intents'] = False
        message_input_options_model_json['async_callout'] = False
        message_input_options_model_json['spelling'] = message_input_options_spelling_model
        message_input_options_model_json['debug'] = False
        message_input_options_model_json['return_context'] = False
        message_input_options_model_json['export'] = False

        # Construct a model instance of MessageInputOptions by calling from_dict on the json representation
        message_input_options_model = MessageInputOptions.from_dict(message_input_options_model_json)
        assert message_input_options_model != False

        # Construct a model instance of MessageInputOptions by calling from_dict on the json representation
        message_input_options_model_dict = MessageInputOptions.from_dict(message_input_options_model_json).__dict__
        message_input_options_model2 = MessageInputOptions(**message_input_options_model_dict)

        # Verify the model instances are equivalent
        assert message_input_options_model == message_input_options_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_options_model_json2 = message_input_options_model.to_dict()
        assert message_input_options_model_json2 == message_input_options_model_json


class TestModel_MessageInputOptionsSpelling:
    """
    Test Class for MessageInputOptionsSpelling
    """

    def test_message_input_options_spelling_serialization(self):
        """
        Test serialization/deserialization for MessageInputOptionsSpelling
        """

        # Construct a json representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model_json = {}
        message_input_options_spelling_model_json['suggestions'] = True
        message_input_options_spelling_model_json['auto_correct'] = True

        # Construct a model instance of MessageInputOptionsSpelling by calling from_dict on the json representation
        message_input_options_spelling_model = MessageInputOptionsSpelling.from_dict(message_input_options_spelling_model_json)
        assert message_input_options_spelling_model != False

        # Construct a model instance of MessageInputOptionsSpelling by calling from_dict on the json representation
        message_input_options_spelling_model_dict = MessageInputOptionsSpelling.from_dict(message_input_options_spelling_model_json).__dict__
        message_input_options_spelling_model2 = MessageInputOptionsSpelling(**message_input_options_spelling_model_dict)

        # Verify the model instances are equivalent
        assert message_input_options_spelling_model == message_input_options_spelling_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_options_spelling_model_json2 = message_input_options_spelling_model.to_dict()
        assert message_input_options_spelling_model_json2 == message_input_options_spelling_model_json


class TestModel_MessageOutput:
    """
    Test Class for MessageOutput
    """

    def test_message_output_serialization(self):
        """
        Test serialization/deserialization for MessageOutput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {}  # RuntimeResponseGenericRuntimeResponseTypeText
        runtime_response_generic_model['response_type'] = 'text'
        runtime_response_generic_model['text'] = 'testString'
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        dialog_node_action_model = {}  # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        message_output_debug_model = {}  # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'
        message_output_debug_model['turn_events'] = [message_output_debug_turn_event_model]

        message_output_spelling_model = {}  # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        # Construct a json representation of a MessageOutput model
        message_output_model_json = {}
        message_output_model_json['generic'] = [runtime_response_generic_model]
        message_output_model_json['intents'] = [runtime_intent_model]
        message_output_model_json['entities'] = [runtime_entity_model]
        message_output_model_json['actions'] = [dialog_node_action_model]
        message_output_model_json['debug'] = message_output_debug_model
        message_output_model_json['user_defined'] = {'anyKey': 'anyValue'}
        message_output_model_json['spelling'] = message_output_spelling_model

        # Construct a model instance of MessageOutput by calling from_dict on the json representation
        message_output_model = MessageOutput.from_dict(message_output_model_json)
        assert message_output_model != False

        # Construct a model instance of MessageOutput by calling from_dict on the json representation
        message_output_model_dict = MessageOutput.from_dict(message_output_model_json).__dict__
        message_output_model2 = MessageOutput(**message_output_model_dict)

        # Verify the model instances are equivalent
        assert message_output_model == message_output_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_model_json2 = message_output_model.to_dict()
        assert message_output_model_json2 == message_output_model_json


class TestModel_MessageOutputDebug:
    """
    Test Class for MessageOutputDebug
    """

    def test_message_output_debug_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebug
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        # Construct a json representation of a MessageOutputDebug model
        message_output_debug_model_json = {}
        message_output_debug_model_json['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model_json['log_messages'] = [dialog_log_message_model]
        message_output_debug_model_json['branch_exited'] = True
        message_output_debug_model_json['branch_exited_reason'] = 'completed'
        message_output_debug_model_json['turn_events'] = [message_output_debug_turn_event_model]

        # Construct a model instance of MessageOutputDebug by calling from_dict on the json representation
        message_output_debug_model = MessageOutputDebug.from_dict(message_output_debug_model_json)
        assert message_output_debug_model != False

        # Construct a model instance of MessageOutputDebug by calling from_dict on the json representation
        message_output_debug_model_dict = MessageOutputDebug.from_dict(message_output_debug_model_json).__dict__
        message_output_debug_model2 = MessageOutputDebug(**message_output_debug_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_model == message_output_debug_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_model_json2 = message_output_debug_model.to_dict()
        assert message_output_debug_model_json2 == message_output_debug_model_json


class TestModel_MessageOutputSpelling:
    """
    Test Class for MessageOutputSpelling
    """

    def test_message_output_spelling_serialization(self):
        """
        Test serialization/deserialization for MessageOutputSpelling
        """

        # Construct a json representation of a MessageOutputSpelling model
        message_output_spelling_model_json = {}
        message_output_spelling_model_json['text'] = 'testString'
        message_output_spelling_model_json['original_text'] = 'testString'
        message_output_spelling_model_json['suggested_text'] = 'testString'

        # Construct a model instance of MessageOutputSpelling by calling from_dict on the json representation
        message_output_spelling_model = MessageOutputSpelling.from_dict(message_output_spelling_model_json)
        assert message_output_spelling_model != False

        # Construct a model instance of MessageOutputSpelling by calling from_dict on the json representation
        message_output_spelling_model_dict = MessageOutputSpelling.from_dict(message_output_spelling_model_json).__dict__
        message_output_spelling_model2 = MessageOutputSpelling(**message_output_spelling_model_dict)

        # Verify the model instances are equivalent
        assert message_output_spelling_model == message_output_spelling_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_spelling_model_json2 = message_output_spelling_model.to_dict()
        assert message_output_spelling_model_json2 == message_output_spelling_model_json


class TestModel_Metadata:
    """
    Test Class for Metadata
    """

    def test_metadata_serialization(self):
        """
        Test serialization/deserialization for Metadata
        """

        # Construct a json representation of a Metadata model
        metadata_model_json = {}
        metadata_model_json['id'] = 38

        # Construct a model instance of Metadata by calling from_dict on the json representation
        metadata_model = Metadata.from_dict(metadata_model_json)
        assert metadata_model != False

        # Construct a model instance of Metadata by calling from_dict on the json representation
        metadata_model_dict = Metadata.from_dict(metadata_model_json).__dict__
        metadata_model2 = Metadata(**metadata_model_dict)

        # Verify the model instances are equivalent
        assert metadata_model == metadata_model2

        # Convert model instance back to dict and verify no loss of data
        metadata_model_json2 = metadata_model.to_dict()
        assert metadata_model_json2 == metadata_model_json


class TestModel_MonitorAssistantReleaseImportArtifactResponse:
    """
    Test Class for MonitorAssistantReleaseImportArtifactResponse
    """

    def test_monitor_assistant_release_import_artifact_response_serialization(self):
        """
        Test serialization/deserialization for MonitorAssistantReleaseImportArtifactResponse
        """

        # Construct a json representation of a MonitorAssistantReleaseImportArtifactResponse model
        monitor_assistant_release_import_artifact_response_model_json = {}
        monitor_assistant_release_import_artifact_response_model_json['skill_impact_in_draft'] = ['action']

        # Construct a model instance of MonitorAssistantReleaseImportArtifactResponse by calling from_dict on the json representation
        monitor_assistant_release_import_artifact_response_model = MonitorAssistantReleaseImportArtifactResponse.from_dict(monitor_assistant_release_import_artifact_response_model_json)
        assert monitor_assistant_release_import_artifact_response_model != False

        # Construct a model instance of MonitorAssistantReleaseImportArtifactResponse by calling from_dict on the json representation
        monitor_assistant_release_import_artifact_response_model_dict = MonitorAssistantReleaseImportArtifactResponse.from_dict(monitor_assistant_release_import_artifact_response_model_json).__dict__
        monitor_assistant_release_import_artifact_response_model2 = MonitorAssistantReleaseImportArtifactResponse(**monitor_assistant_release_import_artifact_response_model_dict)

        # Verify the model instances are equivalent
        assert monitor_assistant_release_import_artifact_response_model == monitor_assistant_release_import_artifact_response_model2

        # Convert model instance back to dict and verify no loss of data
        monitor_assistant_release_import_artifact_response_model_json2 = monitor_assistant_release_import_artifact_response_model.to_dict()
        assert monitor_assistant_release_import_artifact_response_model_json2 == monitor_assistant_release_import_artifact_response_model_json


class TestModel_Pagination:
    """
    Test Class for Pagination
    """

    def test_pagination_serialization(self):
        """
        Test serialization/deserialization for Pagination
        """

        # Construct a json representation of a Pagination model
        pagination_model_json = {}
        pagination_model_json['refresh_url'] = 'testString'
        pagination_model_json['next_url'] = 'testString'
        pagination_model_json['total'] = 38
        pagination_model_json['matched'] = 38
        pagination_model_json['refresh_cursor'] = 'testString'
        pagination_model_json['next_cursor'] = 'testString'

        # Construct a model instance of Pagination by calling from_dict on the json representation
        pagination_model = Pagination.from_dict(pagination_model_json)
        assert pagination_model != False

        # Construct a model instance of Pagination by calling from_dict on the json representation
        pagination_model_dict = Pagination.from_dict(pagination_model_json).__dict__
        pagination_model2 = Pagination(**pagination_model_dict)

        # Verify the model instances are equivalent
        assert pagination_model == pagination_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_model_json2 = pagination_model.to_dict()
        assert pagination_model_json2 == pagination_model_json


class TestModel_ProviderAuthenticationOAuth2:
    """
    Test Class for ProviderAuthenticationOAuth2
    """

    def test_provider_authentication_o_auth2_serialization(self):
        """
        Test serialization/deserialization for ProviderAuthenticationOAuth2
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        # Construct a json representation of a ProviderAuthenticationOAuth2 model
        provider_authentication_o_auth2_model_json = {}
        provider_authentication_o_auth2_model_json['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model_json['flows'] = provider_authentication_o_auth2_flows_model

        # Construct a model instance of ProviderAuthenticationOAuth2 by calling from_dict on the json representation
        provider_authentication_o_auth2_model = ProviderAuthenticationOAuth2.from_dict(provider_authentication_o_auth2_model_json)
        assert provider_authentication_o_auth2_model != False

        # Construct a model instance of ProviderAuthenticationOAuth2 by calling from_dict on the json representation
        provider_authentication_o_auth2_model_dict = ProviderAuthenticationOAuth2.from_dict(provider_authentication_o_auth2_model_json).__dict__
        provider_authentication_o_auth2_model2 = ProviderAuthenticationOAuth2(**provider_authentication_o_auth2_model_dict)

        # Verify the model instances are equivalent
        assert provider_authentication_o_auth2_model == provider_authentication_o_auth2_model2

        # Convert model instance back to dict and verify no loss of data
        provider_authentication_o_auth2_model_json2 = provider_authentication_o_auth2_model.to_dict()
        assert provider_authentication_o_auth2_model_json2 == provider_authentication_o_auth2_model_json


class TestModel_ProviderAuthenticationOAuth2PasswordUsername:
    """
    Test Class for ProviderAuthenticationOAuth2PasswordUsername
    """

    def test_provider_authentication_o_auth2_password_username_serialization(self):
        """
        Test serialization/deserialization for ProviderAuthenticationOAuth2PasswordUsername
        """

        # Construct a json representation of a ProviderAuthenticationOAuth2PasswordUsername model
        provider_authentication_o_auth2_password_username_model_json = {}
        provider_authentication_o_auth2_password_username_model_json['type'] = 'value'
        provider_authentication_o_auth2_password_username_model_json['value'] = 'testString'

        # Construct a model instance of ProviderAuthenticationOAuth2PasswordUsername by calling from_dict on the json representation
        provider_authentication_o_auth2_password_username_model = ProviderAuthenticationOAuth2PasswordUsername.from_dict(provider_authentication_o_auth2_password_username_model_json)
        assert provider_authentication_o_auth2_password_username_model != False

        # Construct a model instance of ProviderAuthenticationOAuth2PasswordUsername by calling from_dict on the json representation
        provider_authentication_o_auth2_password_username_model_dict = ProviderAuthenticationOAuth2PasswordUsername.from_dict(provider_authentication_o_auth2_password_username_model_json).__dict__
        provider_authentication_o_auth2_password_username_model2 = ProviderAuthenticationOAuth2PasswordUsername(**provider_authentication_o_auth2_password_username_model_dict)

        # Verify the model instances are equivalent
        assert provider_authentication_o_auth2_password_username_model == provider_authentication_o_auth2_password_username_model2

        # Convert model instance back to dict and verify no loss of data
        provider_authentication_o_auth2_password_username_model_json2 = provider_authentication_o_auth2_password_username_model.to_dict()
        assert provider_authentication_o_auth2_password_username_model_json2 == provider_authentication_o_auth2_password_username_model_json


class TestModel_ProviderAuthenticationTypeAndValue:
    """
    Test Class for ProviderAuthenticationTypeAndValue
    """

    def test_provider_authentication_type_and_value_serialization(self):
        """
        Test serialization/deserialization for ProviderAuthenticationTypeAndValue
        """

        # Construct a json representation of a ProviderAuthenticationTypeAndValue model
        provider_authentication_type_and_value_model_json = {}
        provider_authentication_type_and_value_model_json['type'] = 'value'
        provider_authentication_type_and_value_model_json['value'] = 'testString'

        # Construct a model instance of ProviderAuthenticationTypeAndValue by calling from_dict on the json representation
        provider_authentication_type_and_value_model = ProviderAuthenticationTypeAndValue.from_dict(provider_authentication_type_and_value_model_json)
        assert provider_authentication_type_and_value_model != False

        # Construct a model instance of ProviderAuthenticationTypeAndValue by calling from_dict on the json representation
        provider_authentication_type_and_value_model_dict = ProviderAuthenticationTypeAndValue.from_dict(provider_authentication_type_and_value_model_json).__dict__
        provider_authentication_type_and_value_model2 = ProviderAuthenticationTypeAndValue(**provider_authentication_type_and_value_model_dict)

        # Verify the model instances are equivalent
        assert provider_authentication_type_and_value_model == provider_authentication_type_and_value_model2

        # Convert model instance back to dict and verify no loss of data
        provider_authentication_type_and_value_model_json2 = provider_authentication_type_and_value_model.to_dict()
        assert provider_authentication_type_and_value_model_json2 == provider_authentication_type_and_value_model_json


class TestModel_ProviderCollection:
    """
    Test Class for ProviderCollection
    """

    def test_provider_collection_serialization(self):
        """
        Test serialization/deserialization for ProviderCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_response_specification_servers_item_model = {}  # ProviderResponseSpecificationServersItem
        provider_response_specification_servers_item_model['url'] = 'testString'

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_response_specification_components_security_schemes_basic_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemesBasic
        provider_response_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        provider_response_specification_components_security_schemes_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemes
        provider_response_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_response_specification_components_security_schemes_model['basic'] = provider_response_specification_components_security_schemes_basic_model
        provider_response_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        provider_response_specification_components_model = {}  # ProviderResponseSpecificationComponents
        provider_response_specification_components_model['securitySchemes'] = provider_response_specification_components_security_schemes_model

        provider_response_specification_model = {}  # ProviderResponseSpecification
        provider_response_specification_model['servers'] = [provider_response_specification_servers_item_model]
        provider_response_specification_model['components'] = provider_response_specification_components_model

        provider_response_model = {}  # ProviderResponse
        provider_response_model['provider_id'] = 'testString'
        provider_response_model['specification'] = provider_response_specification_model

        pagination_model = {}  # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a ProviderCollection model
        provider_collection_model_json = {}
        provider_collection_model_json['conversational_skill_providers'] = [provider_response_model]
        provider_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of ProviderCollection by calling from_dict on the json representation
        provider_collection_model = ProviderCollection.from_dict(provider_collection_model_json)
        assert provider_collection_model != False

        # Construct a model instance of ProviderCollection by calling from_dict on the json representation
        provider_collection_model_dict = ProviderCollection.from_dict(provider_collection_model_json).__dict__
        provider_collection_model2 = ProviderCollection(**provider_collection_model_dict)

        # Verify the model instances are equivalent
        assert provider_collection_model == provider_collection_model2

        # Convert model instance back to dict and verify no loss of data
        provider_collection_model_json2 = provider_collection_model.to_dict()
        assert provider_collection_model_json2 == provider_collection_model_json


class TestModel_ProviderPrivate:
    """
    Test Class for ProviderPrivate
    """

    def test_provider_private_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_private_authentication_model = {}  # ProviderPrivateAuthenticationBearerFlow
        provider_private_authentication_model['token'] = provider_authentication_type_and_value_model

        # Construct a json representation of a ProviderPrivate model
        provider_private_model_json = {}
        provider_private_model_json['authentication'] = provider_private_authentication_model

        # Construct a model instance of ProviderPrivate by calling from_dict on the json representation
        provider_private_model = ProviderPrivate.from_dict(provider_private_model_json)
        assert provider_private_model != False

        # Construct a model instance of ProviderPrivate by calling from_dict on the json representation
        provider_private_model_dict = ProviderPrivate.from_dict(provider_private_model_json).__dict__
        provider_private_model2 = ProviderPrivate(**provider_private_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_model == provider_private_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_model_json2 = provider_private_model.to_dict()
        assert provider_private_model_json2 == provider_private_model_json


class TestModel_ProviderPrivateAuthenticationOAuth2PasswordPassword:
    """
    Test Class for ProviderPrivateAuthenticationOAuth2PasswordPassword
    """

    def test_provider_private_authentication_o_auth2_password_password_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivateAuthenticationOAuth2PasswordPassword
        """

        # Construct a json representation of a ProviderPrivateAuthenticationOAuth2PasswordPassword model
        provider_private_authentication_o_auth2_password_password_model_json = {}
        provider_private_authentication_o_auth2_password_password_model_json['type'] = 'value'
        provider_private_authentication_o_auth2_password_password_model_json['value'] = 'testString'

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2PasswordPassword by calling from_dict on the json representation
        provider_private_authentication_o_auth2_password_password_model = ProviderPrivateAuthenticationOAuth2PasswordPassword.from_dict(provider_private_authentication_o_auth2_password_password_model_json)
        assert provider_private_authentication_o_auth2_password_password_model != False

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2PasswordPassword by calling from_dict on the json representation
        provider_private_authentication_o_auth2_password_password_model_dict = ProviderPrivateAuthenticationOAuth2PasswordPassword.from_dict(provider_private_authentication_o_auth2_password_password_model_json).__dict__
        provider_private_authentication_o_auth2_password_password_model2 = ProviderPrivateAuthenticationOAuth2PasswordPassword(**provider_private_authentication_o_auth2_password_password_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_authentication_o_auth2_password_password_model == provider_private_authentication_o_auth2_password_password_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_authentication_o_auth2_password_password_model_json2 = provider_private_authentication_o_auth2_password_password_model.to_dict()
        assert provider_private_authentication_o_auth2_password_password_model_json2 == provider_private_authentication_o_auth2_password_password_model_json


class TestModel_ProviderResponse:
    """
    Test Class for ProviderResponse
    """

    def test_provider_response_serialization(self):
        """
        Test serialization/deserialization for ProviderResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_response_specification_servers_item_model = {}  # ProviderResponseSpecificationServersItem
        provider_response_specification_servers_item_model['url'] = 'testString'

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_response_specification_components_security_schemes_basic_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemesBasic
        provider_response_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        provider_response_specification_components_security_schemes_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemes
        provider_response_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_response_specification_components_security_schemes_model['basic'] = provider_response_specification_components_security_schemes_basic_model
        provider_response_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        provider_response_specification_components_model = {}  # ProviderResponseSpecificationComponents
        provider_response_specification_components_model['securitySchemes'] = provider_response_specification_components_security_schemes_model

        provider_response_specification_model = {}  # ProviderResponseSpecification
        provider_response_specification_model['servers'] = [provider_response_specification_servers_item_model]
        provider_response_specification_model['components'] = provider_response_specification_components_model

        # Construct a json representation of a ProviderResponse model
        provider_response_model_json = {}
        provider_response_model_json['provider_id'] = 'testString'
        provider_response_model_json['specification'] = provider_response_specification_model

        # Construct a model instance of ProviderResponse by calling from_dict on the json representation
        provider_response_model = ProviderResponse.from_dict(provider_response_model_json)
        assert provider_response_model != False

        # Construct a model instance of ProviderResponse by calling from_dict on the json representation
        provider_response_model_dict = ProviderResponse.from_dict(provider_response_model_json).__dict__
        provider_response_model2 = ProviderResponse(**provider_response_model_dict)

        # Verify the model instances are equivalent
        assert provider_response_model == provider_response_model2

        # Convert model instance back to dict and verify no loss of data
        provider_response_model_json2 = provider_response_model.to_dict()
        assert provider_response_model_json2 == provider_response_model_json


class TestModel_ProviderResponseSpecification:
    """
    Test Class for ProviderResponseSpecification
    """

    def test_provider_response_specification_serialization(self):
        """
        Test serialization/deserialization for ProviderResponseSpecification
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_response_specification_servers_item_model = {}  # ProviderResponseSpecificationServersItem
        provider_response_specification_servers_item_model['url'] = 'testString'

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_response_specification_components_security_schemes_basic_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemesBasic
        provider_response_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        provider_response_specification_components_security_schemes_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemes
        provider_response_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_response_specification_components_security_schemes_model['basic'] = provider_response_specification_components_security_schemes_basic_model
        provider_response_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        provider_response_specification_components_model = {}  # ProviderResponseSpecificationComponents
        provider_response_specification_components_model['securitySchemes'] = provider_response_specification_components_security_schemes_model

        # Construct a json representation of a ProviderResponseSpecification model
        provider_response_specification_model_json = {}
        provider_response_specification_model_json['servers'] = [provider_response_specification_servers_item_model]
        provider_response_specification_model_json['components'] = provider_response_specification_components_model

        # Construct a model instance of ProviderResponseSpecification by calling from_dict on the json representation
        provider_response_specification_model = ProviderResponseSpecification.from_dict(provider_response_specification_model_json)
        assert provider_response_specification_model != False

        # Construct a model instance of ProviderResponseSpecification by calling from_dict on the json representation
        provider_response_specification_model_dict = ProviderResponseSpecification.from_dict(provider_response_specification_model_json).__dict__
        provider_response_specification_model2 = ProviderResponseSpecification(**provider_response_specification_model_dict)

        # Verify the model instances are equivalent
        assert provider_response_specification_model == provider_response_specification_model2

        # Convert model instance back to dict and verify no loss of data
        provider_response_specification_model_json2 = provider_response_specification_model.to_dict()
        assert provider_response_specification_model_json2 == provider_response_specification_model_json


class TestModel_ProviderResponseSpecificationComponents:
    """
    Test Class for ProviderResponseSpecificationComponents
    """

    def test_provider_response_specification_components_serialization(self):
        """
        Test serialization/deserialization for ProviderResponseSpecificationComponents
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_response_specification_components_security_schemes_basic_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemesBasic
        provider_response_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        provider_response_specification_components_security_schemes_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemes
        provider_response_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_response_specification_components_security_schemes_model['basic'] = provider_response_specification_components_security_schemes_basic_model
        provider_response_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        # Construct a json representation of a ProviderResponseSpecificationComponents model
        provider_response_specification_components_model_json = {}
        provider_response_specification_components_model_json['securitySchemes'] = provider_response_specification_components_security_schemes_model

        # Construct a model instance of ProviderResponseSpecificationComponents by calling from_dict on the json representation
        provider_response_specification_components_model = ProviderResponseSpecificationComponents.from_dict(provider_response_specification_components_model_json)
        assert provider_response_specification_components_model != False

        # Construct a model instance of ProviderResponseSpecificationComponents by calling from_dict on the json representation
        provider_response_specification_components_model_dict = ProviderResponseSpecificationComponents.from_dict(provider_response_specification_components_model_json).__dict__
        provider_response_specification_components_model2 = ProviderResponseSpecificationComponents(**provider_response_specification_components_model_dict)

        # Verify the model instances are equivalent
        assert provider_response_specification_components_model == provider_response_specification_components_model2

        # Convert model instance back to dict and verify no loss of data
        provider_response_specification_components_model_json2 = provider_response_specification_components_model.to_dict()
        assert provider_response_specification_components_model_json2 == provider_response_specification_components_model_json


class TestModel_ProviderResponseSpecificationComponentsSecuritySchemes:
    """
    Test Class for ProviderResponseSpecificationComponentsSecuritySchemes
    """

    def test_provider_response_specification_components_security_schemes_serialization(self):
        """
        Test serialization/deserialization for ProviderResponseSpecificationComponentsSecuritySchemes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_response_specification_components_security_schemes_basic_model = {}  # ProviderResponseSpecificationComponentsSecuritySchemesBasic
        provider_response_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        # Construct a json representation of a ProviderResponseSpecificationComponentsSecuritySchemes model
        provider_response_specification_components_security_schemes_model_json = {}
        provider_response_specification_components_security_schemes_model_json['authentication_method'] = 'basic'
        provider_response_specification_components_security_schemes_model_json['basic'] = provider_response_specification_components_security_schemes_basic_model
        provider_response_specification_components_security_schemes_model_json['oauth2'] = provider_authentication_o_auth2_model

        # Construct a model instance of ProviderResponseSpecificationComponentsSecuritySchemes by calling from_dict on the json representation
        provider_response_specification_components_security_schemes_model = ProviderResponseSpecificationComponentsSecuritySchemes.from_dict(provider_response_specification_components_security_schemes_model_json)
        assert provider_response_specification_components_security_schemes_model != False

        # Construct a model instance of ProviderResponseSpecificationComponentsSecuritySchemes by calling from_dict on the json representation
        provider_response_specification_components_security_schemes_model_dict = ProviderResponseSpecificationComponentsSecuritySchemes.from_dict(provider_response_specification_components_security_schemes_model_json).__dict__
        provider_response_specification_components_security_schemes_model2 = ProviderResponseSpecificationComponentsSecuritySchemes(**provider_response_specification_components_security_schemes_model_dict)

        # Verify the model instances are equivalent
        assert provider_response_specification_components_security_schemes_model == provider_response_specification_components_security_schemes_model2

        # Convert model instance back to dict and verify no loss of data
        provider_response_specification_components_security_schemes_model_json2 = provider_response_specification_components_security_schemes_model.to_dict()
        assert provider_response_specification_components_security_schemes_model_json2 == provider_response_specification_components_security_schemes_model_json


class TestModel_ProviderResponseSpecificationComponentsSecuritySchemesBasic:
    """
    Test Class for ProviderResponseSpecificationComponentsSecuritySchemesBasic
    """

    def test_provider_response_specification_components_security_schemes_basic_serialization(self):
        """
        Test serialization/deserialization for ProviderResponseSpecificationComponentsSecuritySchemesBasic
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a json representation of a ProviderResponseSpecificationComponentsSecuritySchemesBasic model
        provider_response_specification_components_security_schemes_basic_model_json = {}
        provider_response_specification_components_security_schemes_basic_model_json['username'] = provider_authentication_type_and_value_model

        # Construct a model instance of ProviderResponseSpecificationComponentsSecuritySchemesBasic by calling from_dict on the json representation
        provider_response_specification_components_security_schemes_basic_model = ProviderResponseSpecificationComponentsSecuritySchemesBasic.from_dict(provider_response_specification_components_security_schemes_basic_model_json)
        assert provider_response_specification_components_security_schemes_basic_model != False

        # Construct a model instance of ProviderResponseSpecificationComponentsSecuritySchemesBasic by calling from_dict on the json representation
        provider_response_specification_components_security_schemes_basic_model_dict = ProviderResponseSpecificationComponentsSecuritySchemesBasic.from_dict(provider_response_specification_components_security_schemes_basic_model_json).__dict__
        provider_response_specification_components_security_schemes_basic_model2 = ProviderResponseSpecificationComponentsSecuritySchemesBasic(**provider_response_specification_components_security_schemes_basic_model_dict)

        # Verify the model instances are equivalent
        assert provider_response_specification_components_security_schemes_basic_model == provider_response_specification_components_security_schemes_basic_model2

        # Convert model instance back to dict and verify no loss of data
        provider_response_specification_components_security_schemes_basic_model_json2 = provider_response_specification_components_security_schemes_basic_model.to_dict()
        assert provider_response_specification_components_security_schemes_basic_model_json2 == provider_response_specification_components_security_schemes_basic_model_json


class TestModel_ProviderResponseSpecificationServersItem:
    """
    Test Class for ProviderResponseSpecificationServersItem
    """

    def test_provider_response_specification_servers_item_serialization(self):
        """
        Test serialization/deserialization for ProviderResponseSpecificationServersItem
        """

        # Construct a json representation of a ProviderResponseSpecificationServersItem model
        provider_response_specification_servers_item_model_json = {}
        provider_response_specification_servers_item_model_json['url'] = 'testString'

        # Construct a model instance of ProviderResponseSpecificationServersItem by calling from_dict on the json representation
        provider_response_specification_servers_item_model = ProviderResponseSpecificationServersItem.from_dict(provider_response_specification_servers_item_model_json)
        assert provider_response_specification_servers_item_model != False

        # Construct a model instance of ProviderResponseSpecificationServersItem by calling from_dict on the json representation
        provider_response_specification_servers_item_model_dict = ProviderResponseSpecificationServersItem.from_dict(provider_response_specification_servers_item_model_json).__dict__
        provider_response_specification_servers_item_model2 = ProviderResponseSpecificationServersItem(**provider_response_specification_servers_item_model_dict)

        # Verify the model instances are equivalent
        assert provider_response_specification_servers_item_model == provider_response_specification_servers_item_model2

        # Convert model instance back to dict and verify no loss of data
        provider_response_specification_servers_item_model_json2 = provider_response_specification_servers_item_model.to_dict()
        assert provider_response_specification_servers_item_model_json2 == provider_response_specification_servers_item_model_json


class TestModel_ProviderSpecification:
    """
    Test Class for ProviderSpecification
    """

    def test_provider_specification_serialization(self):
        """
        Test serialization/deserialization for ProviderSpecification
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_specification_servers_item_model = {}  # ProviderSpecificationServersItem
        provider_specification_servers_item_model['url'] = 'testString'

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_specification_components_security_schemes_basic_model = {}  # ProviderSpecificationComponentsSecuritySchemesBasic
        provider_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        provider_specification_components_security_schemes_model = {}  # ProviderSpecificationComponentsSecuritySchemes
        provider_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_specification_components_security_schemes_model['basic'] = provider_specification_components_security_schemes_basic_model
        provider_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        provider_specification_components_model = {}  # ProviderSpecificationComponents
        provider_specification_components_model['securitySchemes'] = provider_specification_components_security_schemes_model

        # Construct a json representation of a ProviderSpecification model
        provider_specification_model_json = {}
        provider_specification_model_json['servers'] = [provider_specification_servers_item_model]
        provider_specification_model_json['components'] = provider_specification_components_model

        # Construct a model instance of ProviderSpecification by calling from_dict on the json representation
        provider_specification_model = ProviderSpecification.from_dict(provider_specification_model_json)
        assert provider_specification_model != False

        # Construct a model instance of ProviderSpecification by calling from_dict on the json representation
        provider_specification_model_dict = ProviderSpecification.from_dict(provider_specification_model_json).__dict__
        provider_specification_model2 = ProviderSpecification(**provider_specification_model_dict)

        # Verify the model instances are equivalent
        assert provider_specification_model == provider_specification_model2

        # Convert model instance back to dict and verify no loss of data
        provider_specification_model_json2 = provider_specification_model.to_dict()
        assert provider_specification_model_json2 == provider_specification_model_json


class TestModel_ProviderSpecificationComponents:
    """
    Test Class for ProviderSpecificationComponents
    """

    def test_provider_specification_components_serialization(self):
        """
        Test serialization/deserialization for ProviderSpecificationComponents
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_specification_components_security_schemes_basic_model = {}  # ProviderSpecificationComponentsSecuritySchemesBasic
        provider_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        provider_specification_components_security_schemes_model = {}  # ProviderSpecificationComponentsSecuritySchemes
        provider_specification_components_security_schemes_model['authentication_method'] = 'basic'
        provider_specification_components_security_schemes_model['basic'] = provider_specification_components_security_schemes_basic_model
        provider_specification_components_security_schemes_model['oauth2'] = provider_authentication_o_auth2_model

        # Construct a json representation of a ProviderSpecificationComponents model
        provider_specification_components_model_json = {}
        provider_specification_components_model_json['securitySchemes'] = provider_specification_components_security_schemes_model

        # Construct a model instance of ProviderSpecificationComponents by calling from_dict on the json representation
        provider_specification_components_model = ProviderSpecificationComponents.from_dict(provider_specification_components_model_json)
        assert provider_specification_components_model != False

        # Construct a model instance of ProviderSpecificationComponents by calling from_dict on the json representation
        provider_specification_components_model_dict = ProviderSpecificationComponents.from_dict(provider_specification_components_model_json).__dict__
        provider_specification_components_model2 = ProviderSpecificationComponents(**provider_specification_components_model_dict)

        # Verify the model instances are equivalent
        assert provider_specification_components_model == provider_specification_components_model2

        # Convert model instance back to dict and verify no loss of data
        provider_specification_components_model_json2 = provider_specification_components_model.to_dict()
        assert provider_specification_components_model_json2 == provider_specification_components_model_json


class TestModel_ProviderSpecificationComponentsSecuritySchemes:
    """
    Test Class for ProviderSpecificationComponentsSecuritySchemes
    """

    def test_provider_specification_components_security_schemes_serialization(self):
        """
        Test serialization/deserialization for ProviderSpecificationComponentsSecuritySchemes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        provider_specification_components_security_schemes_basic_model = {}  # ProviderSpecificationComponentsSecuritySchemesBasic
        provider_specification_components_security_schemes_basic_model['username'] = provider_authentication_type_and_value_model

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        provider_authentication_o_auth2_flows_model = {}  # ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        provider_authentication_o_auth2_flows_model['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_model['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_model['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_model['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_model['username'] = provider_authentication_o_auth2_password_username_model

        provider_authentication_o_auth2_model = {}  # ProviderAuthenticationOAuth2
        provider_authentication_o_auth2_model['preferred_flow'] = 'password'
        provider_authentication_o_auth2_model['flows'] = provider_authentication_o_auth2_flows_model

        # Construct a json representation of a ProviderSpecificationComponentsSecuritySchemes model
        provider_specification_components_security_schemes_model_json = {}
        provider_specification_components_security_schemes_model_json['authentication_method'] = 'basic'
        provider_specification_components_security_schemes_model_json['basic'] = provider_specification_components_security_schemes_basic_model
        provider_specification_components_security_schemes_model_json['oauth2'] = provider_authentication_o_auth2_model

        # Construct a model instance of ProviderSpecificationComponentsSecuritySchemes by calling from_dict on the json representation
        provider_specification_components_security_schemes_model = ProviderSpecificationComponentsSecuritySchemes.from_dict(provider_specification_components_security_schemes_model_json)
        assert provider_specification_components_security_schemes_model != False

        # Construct a model instance of ProviderSpecificationComponentsSecuritySchemes by calling from_dict on the json representation
        provider_specification_components_security_schemes_model_dict = ProviderSpecificationComponentsSecuritySchemes.from_dict(provider_specification_components_security_schemes_model_json).__dict__
        provider_specification_components_security_schemes_model2 = ProviderSpecificationComponentsSecuritySchemes(**provider_specification_components_security_schemes_model_dict)

        # Verify the model instances are equivalent
        assert provider_specification_components_security_schemes_model == provider_specification_components_security_schemes_model2

        # Convert model instance back to dict and verify no loss of data
        provider_specification_components_security_schemes_model_json2 = provider_specification_components_security_schemes_model.to_dict()
        assert provider_specification_components_security_schemes_model_json2 == provider_specification_components_security_schemes_model_json


class TestModel_ProviderSpecificationComponentsSecuritySchemesBasic:
    """
    Test Class for ProviderSpecificationComponentsSecuritySchemesBasic
    """

    def test_provider_specification_components_security_schemes_basic_serialization(self):
        """
        Test serialization/deserialization for ProviderSpecificationComponentsSecuritySchemesBasic
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a json representation of a ProviderSpecificationComponentsSecuritySchemesBasic model
        provider_specification_components_security_schemes_basic_model_json = {}
        provider_specification_components_security_schemes_basic_model_json['username'] = provider_authentication_type_and_value_model

        # Construct a model instance of ProviderSpecificationComponentsSecuritySchemesBasic by calling from_dict on the json representation
        provider_specification_components_security_schemes_basic_model = ProviderSpecificationComponentsSecuritySchemesBasic.from_dict(provider_specification_components_security_schemes_basic_model_json)
        assert provider_specification_components_security_schemes_basic_model != False

        # Construct a model instance of ProviderSpecificationComponentsSecuritySchemesBasic by calling from_dict on the json representation
        provider_specification_components_security_schemes_basic_model_dict = ProviderSpecificationComponentsSecuritySchemesBasic.from_dict(provider_specification_components_security_schemes_basic_model_json).__dict__
        provider_specification_components_security_schemes_basic_model2 = ProviderSpecificationComponentsSecuritySchemesBasic(**provider_specification_components_security_schemes_basic_model_dict)

        # Verify the model instances are equivalent
        assert provider_specification_components_security_schemes_basic_model == provider_specification_components_security_schemes_basic_model2

        # Convert model instance back to dict and verify no loss of data
        provider_specification_components_security_schemes_basic_model_json2 = provider_specification_components_security_schemes_basic_model.to_dict()
        assert provider_specification_components_security_schemes_basic_model_json2 == provider_specification_components_security_schemes_basic_model_json


class TestModel_ProviderSpecificationServersItem:
    """
    Test Class for ProviderSpecificationServersItem
    """

    def test_provider_specification_servers_item_serialization(self):
        """
        Test serialization/deserialization for ProviderSpecificationServersItem
        """

        # Construct a json representation of a ProviderSpecificationServersItem model
        provider_specification_servers_item_model_json = {}
        provider_specification_servers_item_model_json['url'] = 'testString'

        # Construct a model instance of ProviderSpecificationServersItem by calling from_dict on the json representation
        provider_specification_servers_item_model = ProviderSpecificationServersItem.from_dict(provider_specification_servers_item_model_json)
        assert provider_specification_servers_item_model != False

        # Construct a model instance of ProviderSpecificationServersItem by calling from_dict on the json representation
        provider_specification_servers_item_model_dict = ProviderSpecificationServersItem.from_dict(provider_specification_servers_item_model_json).__dict__
        provider_specification_servers_item_model2 = ProviderSpecificationServersItem(**provider_specification_servers_item_model_dict)

        # Verify the model instances are equivalent
        assert provider_specification_servers_item_model == provider_specification_servers_item_model2

        # Convert model instance back to dict and verify no loss of data
        provider_specification_servers_item_model_json2 = provider_specification_servers_item_model.to_dict()
        assert provider_specification_servers_item_model_json2 == provider_specification_servers_item_model_json


class TestModel_Release:
    """
    Test Class for Release
    """

    def test_release_serialization(self):
        """
        Test serialization/deserialization for Release
        """

        # Construct a json representation of a Release model
        release_model_json = {}
        release_model_json['description'] = 'testString'

        # Construct a model instance of Release by calling from_dict on the json representation
        release_model = Release.from_dict(release_model_json)
        assert release_model != False

        # Construct a model instance of Release by calling from_dict on the json representation
        release_model_dict = Release.from_dict(release_model_json).__dict__
        release_model2 = Release(**release_model_dict)

        # Verify the model instances are equivalent
        assert release_model == release_model2

        # Convert model instance back to dict and verify no loss of data
        release_model_json2 = release_model.to_dict()
        assert release_model_json2 == release_model_json


class TestModel_ReleaseCollection:
    """
    Test Class for ReleaseCollection
    """

    def test_release_collection_serialization(self):
        """
        Test serialization/deserialization for ReleaseCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        release_model = {}  # Release
        release_model['description'] = 'testString'

        pagination_model = {}  # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a ReleaseCollection model
        release_collection_model_json = {}
        release_collection_model_json['releases'] = [release_model]
        release_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of ReleaseCollection by calling from_dict on the json representation
        release_collection_model = ReleaseCollection.from_dict(release_collection_model_json)
        assert release_collection_model != False

        # Construct a model instance of ReleaseCollection by calling from_dict on the json representation
        release_collection_model_dict = ReleaseCollection.from_dict(release_collection_model_json).__dict__
        release_collection_model2 = ReleaseCollection(**release_collection_model_dict)

        # Verify the model instances are equivalent
        assert release_collection_model == release_collection_model2

        # Convert model instance back to dict and verify no loss of data
        release_collection_model_json2 = release_collection_model.to_dict()
        assert release_collection_model_json2 == release_collection_model_json


class TestModel_ReleaseContent:
    """
    Test Class for ReleaseContent
    """

    def test_release_content_serialization(self):
        """
        Test serialization/deserialization for ReleaseContent
        """

        # Construct a json representation of a ReleaseContent model
        release_content_model_json = {}

        # Construct a model instance of ReleaseContent by calling from_dict on the json representation
        release_content_model = ReleaseContent.from_dict(release_content_model_json)
        assert release_content_model != False

        # Construct a model instance of ReleaseContent by calling from_dict on the json representation
        release_content_model_dict = ReleaseContent.from_dict(release_content_model_json).__dict__
        release_content_model2 = ReleaseContent(**release_content_model_dict)

        # Verify the model instances are equivalent
        assert release_content_model == release_content_model2

        # Convert model instance back to dict and verify no loss of data
        release_content_model_json2 = release_content_model.to_dict()
        assert release_content_model_json2 == release_content_model_json


class TestModel_ReleaseSkill:
    """
    Test Class for ReleaseSkill
    """

    def test_release_skill_serialization(self):
        """
        Test serialization/deserialization for ReleaseSkill
        """

        # Construct a json representation of a ReleaseSkill model
        release_skill_model_json = {}
        release_skill_model_json['skill_id'] = 'testString'
        release_skill_model_json['type'] = 'dialog'
        release_skill_model_json['snapshot'] = 'testString'

        # Construct a model instance of ReleaseSkill by calling from_dict on the json representation
        release_skill_model = ReleaseSkill.from_dict(release_skill_model_json)
        assert release_skill_model != False

        # Construct a model instance of ReleaseSkill by calling from_dict on the json representation
        release_skill_model_dict = ReleaseSkill.from_dict(release_skill_model_json).__dict__
        release_skill_model2 = ReleaseSkill(**release_skill_model_dict)

        # Verify the model instances are equivalent
        assert release_skill_model == release_skill_model2

        # Convert model instance back to dict and verify no loss of data
        release_skill_model_json2 = release_skill_model.to_dict()
        assert release_skill_model_json2 == release_skill_model_json


class TestModel_RequestAnalytics:
    """
    Test Class for RequestAnalytics
    """

    def test_request_analytics_serialization(self):
        """
        Test serialization/deserialization for RequestAnalytics
        """

        # Construct a json representation of a RequestAnalytics model
        request_analytics_model_json = {}
        request_analytics_model_json['browser'] = 'testString'
        request_analytics_model_json['device'] = 'testString'
        request_analytics_model_json['pageUrl'] = 'testString'

        # Construct a model instance of RequestAnalytics by calling from_dict on the json representation
        request_analytics_model = RequestAnalytics.from_dict(request_analytics_model_json)
        assert request_analytics_model != False

        # Construct a model instance of RequestAnalytics by calling from_dict on the json representation
        request_analytics_model_dict = RequestAnalytics.from_dict(request_analytics_model_json).__dict__
        request_analytics_model2 = RequestAnalytics(**request_analytics_model_dict)

        # Verify the model instances are equivalent
        assert request_analytics_model == request_analytics_model2

        # Convert model instance back to dict and verify no loss of data
        request_analytics_model_json2 = request_analytics_model.to_dict()
        assert request_analytics_model_json2 == request_analytics_model_json


class TestModel_ResponseGenericChannel:
    """
    Test Class for ResponseGenericChannel
    """

    def test_response_generic_channel_serialization(self):
        """
        Test serialization/deserialization for ResponseGenericChannel
        """

        # Construct a json representation of a ResponseGenericChannel model
        response_generic_channel_model_json = {}
        response_generic_channel_model_json['channel'] = 'testString'

        # Construct a model instance of ResponseGenericChannel by calling from_dict on the json representation
        response_generic_channel_model = ResponseGenericChannel.from_dict(response_generic_channel_model_json)
        assert response_generic_channel_model != False

        # Construct a model instance of ResponseGenericChannel by calling from_dict on the json representation
        response_generic_channel_model_dict = ResponseGenericChannel.from_dict(response_generic_channel_model_json).__dict__
        response_generic_channel_model2 = ResponseGenericChannel(**response_generic_channel_model_dict)

        # Verify the model instances are equivalent
        assert response_generic_channel_model == response_generic_channel_model2

        # Convert model instance back to dict and verify no loss of data
        response_generic_channel_model_json2 = response_generic_channel_model.to_dict()
        assert response_generic_channel_model_json2 == response_generic_channel_model_json


class TestModel_RuntimeEntity:
    """
    Test Class for RuntimeEntity
    """

    def test_runtime_entity_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a json representation of a RuntimeEntity model
        runtime_entity_model_json = {}
        runtime_entity_model_json['entity'] = 'testString'
        runtime_entity_model_json['location'] = [38]
        runtime_entity_model_json['value'] = 'testString'
        runtime_entity_model_json['confidence'] = 72.5
        runtime_entity_model_json['groups'] = [capture_group_model]
        runtime_entity_model_json['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model_json['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model_json['role'] = runtime_entity_role_model
        runtime_entity_model_json['skill'] = 'testString'

        # Construct a model instance of RuntimeEntity by calling from_dict on the json representation
        runtime_entity_model = RuntimeEntity.from_dict(runtime_entity_model_json)
        assert runtime_entity_model != False

        # Construct a model instance of RuntimeEntity by calling from_dict on the json representation
        runtime_entity_model_dict = RuntimeEntity.from_dict(runtime_entity_model_json).__dict__
        runtime_entity_model2 = RuntimeEntity(**runtime_entity_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_model == runtime_entity_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_model_json2 = runtime_entity_model.to_dict()
        assert runtime_entity_model_json2 == runtime_entity_model_json


class TestModel_RuntimeEntityAlternative:
    """
    Test Class for RuntimeEntityAlternative
    """

    def test_runtime_entity_alternative_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntityAlternative
        """

        # Construct a json representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model_json = {}
        runtime_entity_alternative_model_json['value'] = 'testString'
        runtime_entity_alternative_model_json['confidence'] = 72.5

        # Construct a model instance of RuntimeEntityAlternative by calling from_dict on the json representation
        runtime_entity_alternative_model = RuntimeEntityAlternative.from_dict(runtime_entity_alternative_model_json)
        assert runtime_entity_alternative_model != False

        # Construct a model instance of RuntimeEntityAlternative by calling from_dict on the json representation
        runtime_entity_alternative_model_dict = RuntimeEntityAlternative.from_dict(runtime_entity_alternative_model_json).__dict__
        runtime_entity_alternative_model2 = RuntimeEntityAlternative(**runtime_entity_alternative_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_alternative_model == runtime_entity_alternative_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_alternative_model_json2 = runtime_entity_alternative_model.to_dict()
        assert runtime_entity_alternative_model_json2 == runtime_entity_alternative_model_json


class TestModel_RuntimeEntityInterpretation:
    """
    Test Class for RuntimeEntityInterpretation
    """

    def test_runtime_entity_interpretation_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntityInterpretation
        """

        # Construct a json representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model_json = {}
        runtime_entity_interpretation_model_json['calendar_type'] = 'testString'
        runtime_entity_interpretation_model_json['datetime_link'] = 'testString'
        runtime_entity_interpretation_model_json['festival'] = 'testString'
        runtime_entity_interpretation_model_json['granularity'] = 'day'
        runtime_entity_interpretation_model_json['range_link'] = 'testString'
        runtime_entity_interpretation_model_json['range_modifier'] = 'testString'
        runtime_entity_interpretation_model_json['relative_day'] = 72.5
        runtime_entity_interpretation_model_json['relative_month'] = 72.5
        runtime_entity_interpretation_model_json['relative_week'] = 72.5
        runtime_entity_interpretation_model_json['relative_weekend'] = 72.5
        runtime_entity_interpretation_model_json['relative_year'] = 72.5
        runtime_entity_interpretation_model_json['specific_day'] = 72.5
        runtime_entity_interpretation_model_json['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model_json['specific_month'] = 72.5
        runtime_entity_interpretation_model_json['specific_quarter'] = 72.5
        runtime_entity_interpretation_model_json['specific_year'] = 72.5
        runtime_entity_interpretation_model_json['numeric_value'] = 72.5
        runtime_entity_interpretation_model_json['subtype'] = 'testString'
        runtime_entity_interpretation_model_json['part_of_day'] = 'testString'
        runtime_entity_interpretation_model_json['relative_hour'] = 72.5
        runtime_entity_interpretation_model_json['relative_minute'] = 72.5
        runtime_entity_interpretation_model_json['relative_second'] = 72.5
        runtime_entity_interpretation_model_json['specific_hour'] = 72.5
        runtime_entity_interpretation_model_json['specific_minute'] = 72.5
        runtime_entity_interpretation_model_json['specific_second'] = 72.5
        runtime_entity_interpretation_model_json['timezone'] = 'testString'

        # Construct a model instance of RuntimeEntityInterpretation by calling from_dict on the json representation
        runtime_entity_interpretation_model = RuntimeEntityInterpretation.from_dict(runtime_entity_interpretation_model_json)
        assert runtime_entity_interpretation_model != False

        # Construct a model instance of RuntimeEntityInterpretation by calling from_dict on the json representation
        runtime_entity_interpretation_model_dict = RuntimeEntityInterpretation.from_dict(runtime_entity_interpretation_model_json).__dict__
        runtime_entity_interpretation_model2 = RuntimeEntityInterpretation(**runtime_entity_interpretation_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_interpretation_model == runtime_entity_interpretation_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_interpretation_model_json2 = runtime_entity_interpretation_model.to_dict()
        assert runtime_entity_interpretation_model_json2 == runtime_entity_interpretation_model_json


class TestModel_RuntimeEntityRole:
    """
    Test Class for RuntimeEntityRole
    """

    def test_runtime_entity_role_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntityRole
        """

        # Construct a json representation of a RuntimeEntityRole model
        runtime_entity_role_model_json = {}
        runtime_entity_role_model_json['type'] = 'date_from'

        # Construct a model instance of RuntimeEntityRole by calling from_dict on the json representation
        runtime_entity_role_model = RuntimeEntityRole.from_dict(runtime_entity_role_model_json)
        assert runtime_entity_role_model != False

        # Construct a model instance of RuntimeEntityRole by calling from_dict on the json representation
        runtime_entity_role_model_dict = RuntimeEntityRole.from_dict(runtime_entity_role_model_json).__dict__
        runtime_entity_role_model2 = RuntimeEntityRole(**runtime_entity_role_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_role_model == runtime_entity_role_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_role_model_json2 = runtime_entity_role_model.to_dict()
        assert runtime_entity_role_model_json2 == runtime_entity_role_model_json


class TestModel_RuntimeIntent:
    """
    Test Class for RuntimeIntent
    """

    def test_runtime_intent_serialization(self):
        """
        Test serialization/deserialization for RuntimeIntent
        """

        # Construct a json representation of a RuntimeIntent model
        runtime_intent_model_json = {}
        runtime_intent_model_json['intent'] = 'testString'
        runtime_intent_model_json['confidence'] = 72.5
        runtime_intent_model_json['skill'] = 'testString'

        # Construct a model instance of RuntimeIntent by calling from_dict on the json representation
        runtime_intent_model = RuntimeIntent.from_dict(runtime_intent_model_json)
        assert runtime_intent_model != False

        # Construct a model instance of RuntimeIntent by calling from_dict on the json representation
        runtime_intent_model_dict = RuntimeIntent.from_dict(runtime_intent_model_json).__dict__
        runtime_intent_model2 = RuntimeIntent(**runtime_intent_model_dict)

        # Verify the model instances are equivalent
        assert runtime_intent_model == runtime_intent_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_intent_model_json2 = runtime_intent_model.to_dict()
        assert runtime_intent_model_json2 == runtime_intent_model_json


class TestModel_SearchResult:
    """
    Test Class for SearchResult
    """

    def test_search_result_serialization(self):
        """
        Test serialization/deserialization for SearchResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_result_metadata_model = {}  # SearchResultMetadata
        search_result_metadata_model['confidence'] = 72.5
        search_result_metadata_model['score'] = 72.5

        search_result_highlight_model = {}  # SearchResultHighlight
        search_result_highlight_model['body'] = ['testString']
        search_result_highlight_model['title'] = ['testString']
        search_result_highlight_model['url'] = ['testString']
        search_result_highlight_model['foo'] = ['testString']

        search_result_answer_model = {}  # SearchResultAnswer
        search_result_answer_model['text'] = 'testString'
        search_result_answer_model['confidence'] = 0

        # Construct a json representation of a SearchResult model
        search_result_model_json = {}
        search_result_model_json['id'] = 'testString'
        search_result_model_json['result_metadata'] = search_result_metadata_model
        search_result_model_json['body'] = 'testString'
        search_result_model_json['title'] = 'testString'
        search_result_model_json['url'] = 'testString'
        search_result_model_json['highlight'] = search_result_highlight_model
        search_result_model_json['answers'] = [search_result_answer_model]

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model = SearchResult.from_dict(search_result_model_json)
        assert search_result_model != False

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model_dict = SearchResult.from_dict(search_result_model_json).__dict__
        search_result_model2 = SearchResult(**search_result_model_dict)

        # Verify the model instances are equivalent
        assert search_result_model == search_result_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_model_json2 = search_result_model.to_dict()
        assert search_result_model_json2 == search_result_model_json


class TestModel_SearchResultAnswer:
    """
    Test Class for SearchResultAnswer
    """

    def test_search_result_answer_serialization(self):
        """
        Test serialization/deserialization for SearchResultAnswer
        """

        # Construct a json representation of a SearchResultAnswer model
        search_result_answer_model_json = {}
        search_result_answer_model_json['text'] = 'testString'
        search_result_answer_model_json['confidence'] = 0

        # Construct a model instance of SearchResultAnswer by calling from_dict on the json representation
        search_result_answer_model = SearchResultAnswer.from_dict(search_result_answer_model_json)
        assert search_result_answer_model != False

        # Construct a model instance of SearchResultAnswer by calling from_dict on the json representation
        search_result_answer_model_dict = SearchResultAnswer.from_dict(search_result_answer_model_json).__dict__
        search_result_answer_model2 = SearchResultAnswer(**search_result_answer_model_dict)

        # Verify the model instances are equivalent
        assert search_result_answer_model == search_result_answer_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_answer_model_json2 = search_result_answer_model.to_dict()
        assert search_result_answer_model_json2 == search_result_answer_model_json


class TestModel_SearchResultHighlight:
    """
    Test Class for SearchResultHighlight
    """

    def test_search_result_highlight_serialization(self):
        """
        Test serialization/deserialization for SearchResultHighlight
        """

        # Construct a json representation of a SearchResultHighlight model
        search_result_highlight_model_json = {}
        search_result_highlight_model_json['body'] = ['testString']
        search_result_highlight_model_json['title'] = ['testString']
        search_result_highlight_model_json['url'] = ['testString']
        search_result_highlight_model_json['foo'] = ['testString']

        # Construct a model instance of SearchResultHighlight by calling from_dict on the json representation
        search_result_highlight_model = SearchResultHighlight.from_dict(search_result_highlight_model_json)
        assert search_result_highlight_model != False

        # Construct a model instance of SearchResultHighlight by calling from_dict on the json representation
        search_result_highlight_model_dict = SearchResultHighlight.from_dict(search_result_highlight_model_json).__dict__
        search_result_highlight_model2 = SearchResultHighlight(**search_result_highlight_model_dict)

        # Verify the model instances are equivalent
        assert search_result_highlight_model == search_result_highlight_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_highlight_model_json2 = search_result_highlight_model.to_dict()
        assert search_result_highlight_model_json2 == search_result_highlight_model_json

        # Test get_properties and set_properties methods.
        search_result_highlight_model.set_properties({})
        actual_dict = search_result_highlight_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': ['testString']}
        search_result_highlight_model.set_properties(expected_dict)
        actual_dict = search_result_highlight_model.get_properties()
        assert actual_dict.keys() == expected_dict.keys()


class TestModel_SearchResultMetadata:
    """
    Test Class for SearchResultMetadata
    """

    def test_search_result_metadata_serialization(self):
        """
        Test serialization/deserialization for SearchResultMetadata
        """

        # Construct a json representation of a SearchResultMetadata model
        search_result_metadata_model_json = {}
        search_result_metadata_model_json['confidence'] = 72.5
        search_result_metadata_model_json['score'] = 72.5

        # Construct a model instance of SearchResultMetadata by calling from_dict on the json representation
        search_result_metadata_model = SearchResultMetadata.from_dict(search_result_metadata_model_json)
        assert search_result_metadata_model != False

        # Construct a model instance of SearchResultMetadata by calling from_dict on the json representation
        search_result_metadata_model_dict = SearchResultMetadata.from_dict(search_result_metadata_model_json).__dict__
        search_result_metadata_model2 = SearchResultMetadata(**search_result_metadata_model_dict)

        # Verify the model instances are equivalent
        assert search_result_metadata_model == search_result_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_metadata_model_json2 = search_result_metadata_model.to_dict()
        assert search_result_metadata_model_json2 == search_result_metadata_model_json


class TestModel_SearchSettings:
    """
    Test Class for SearchSettings
    """

    def test_search_settings_serialization(self):
        """
        Test serialization/deserialization for SearchSettings
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_settings_discovery_authentication_model = {}  # SearchSettingsDiscoveryAuthentication
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        search_settings_discovery_model = {}  # SearchSettingsDiscovery
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        search_settings_messages_model = {}  # SearchSettingsMessages
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        search_settings_schema_mapping_model = {}  # SearchSettingsSchemaMapping
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        search_settings_elastic_search_model = {}  # SearchSettingsElasticSearch
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        search_settings_conversational_search_response_length_model = {}  # SearchSettingsConversationalSearchResponseLength
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        search_settings_conversational_search_search_confidence_model = {}  # SearchSettingsConversationalSearchSearchConfidence
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        search_settings_conversational_search_model = {}  # SearchSettingsConversationalSearch
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        search_settings_server_side_search_model = {}  # SearchSettingsServerSideSearch
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        search_settings_client_side_search_model = {}  # SearchSettingsClientSideSearch
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a SearchSettings model
        search_settings_model_json = {}
        search_settings_model_json['discovery'] = search_settings_discovery_model
        search_settings_model_json['messages'] = search_settings_messages_model
        search_settings_model_json['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model_json['elastic_search'] = search_settings_elastic_search_model
        search_settings_model_json['conversational_search'] = search_settings_conversational_search_model
        search_settings_model_json['server_side_search'] = search_settings_server_side_search_model
        search_settings_model_json['client_side_search'] = search_settings_client_side_search_model

        # Construct a model instance of SearchSettings by calling from_dict on the json representation
        search_settings_model = SearchSettings.from_dict(search_settings_model_json)
        assert search_settings_model != False

        # Construct a model instance of SearchSettings by calling from_dict on the json representation
        search_settings_model_dict = SearchSettings.from_dict(search_settings_model_json).__dict__
        search_settings_model2 = SearchSettings(**search_settings_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_model == search_settings_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_model_json2 = search_settings_model.to_dict()
        assert search_settings_model_json2 == search_settings_model_json


class TestModel_SearchSettingsClientSideSearch:
    """
    Test Class for SearchSettingsClientSideSearch
    """

    def test_search_settings_client_side_search_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsClientSideSearch
        """

        # Construct a json representation of a SearchSettingsClientSideSearch model
        search_settings_client_side_search_model_json = {}
        search_settings_client_side_search_model_json['filter'] = 'testString'
        search_settings_client_side_search_model_json['metadata'] = {'anyKey': 'anyValue'}

        # Construct a model instance of SearchSettingsClientSideSearch by calling from_dict on the json representation
        search_settings_client_side_search_model = SearchSettingsClientSideSearch.from_dict(search_settings_client_side_search_model_json)
        assert search_settings_client_side_search_model != False

        # Construct a model instance of SearchSettingsClientSideSearch by calling from_dict on the json representation
        search_settings_client_side_search_model_dict = SearchSettingsClientSideSearch.from_dict(search_settings_client_side_search_model_json).__dict__
        search_settings_client_side_search_model2 = SearchSettingsClientSideSearch(**search_settings_client_side_search_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_client_side_search_model == search_settings_client_side_search_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_client_side_search_model_json2 = search_settings_client_side_search_model.to_dict()
        assert search_settings_client_side_search_model_json2 == search_settings_client_side_search_model_json


class TestModel_SearchSettingsConversationalSearch:
    """
    Test Class for SearchSettingsConversationalSearch
    """

    def test_search_settings_conversational_search_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsConversationalSearch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_settings_conversational_search_response_length_model = {}  # SearchSettingsConversationalSearchResponseLength
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        search_settings_conversational_search_search_confidence_model = {}  # SearchSettingsConversationalSearchSearchConfidence
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        # Construct a json representation of a SearchSettingsConversationalSearch model
        search_settings_conversational_search_model_json = {}
        search_settings_conversational_search_model_json['enabled'] = True
        search_settings_conversational_search_model_json['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model_json['search_confidence'] = search_settings_conversational_search_search_confidence_model

        # Construct a model instance of SearchSettingsConversationalSearch by calling from_dict on the json representation
        search_settings_conversational_search_model = SearchSettingsConversationalSearch.from_dict(search_settings_conversational_search_model_json)
        assert search_settings_conversational_search_model != False

        # Construct a model instance of SearchSettingsConversationalSearch by calling from_dict on the json representation
        search_settings_conversational_search_model_dict = SearchSettingsConversationalSearch.from_dict(search_settings_conversational_search_model_json).__dict__
        search_settings_conversational_search_model2 = SearchSettingsConversationalSearch(**search_settings_conversational_search_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_conversational_search_model == search_settings_conversational_search_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_conversational_search_model_json2 = search_settings_conversational_search_model.to_dict()
        assert search_settings_conversational_search_model_json2 == search_settings_conversational_search_model_json


class TestModel_SearchSettingsConversationalSearchResponseLength:
    """
    Test Class for SearchSettingsConversationalSearchResponseLength
    """

    def test_search_settings_conversational_search_response_length_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsConversationalSearchResponseLength
        """

        # Construct a json representation of a SearchSettingsConversationalSearchResponseLength model
        search_settings_conversational_search_response_length_model_json = {}
        search_settings_conversational_search_response_length_model_json['option'] = 'moderate'

        # Construct a model instance of SearchSettingsConversationalSearchResponseLength by calling from_dict on the json representation
        search_settings_conversational_search_response_length_model = SearchSettingsConversationalSearchResponseLength.from_dict(search_settings_conversational_search_response_length_model_json)
        assert search_settings_conversational_search_response_length_model != False

        # Construct a model instance of SearchSettingsConversationalSearchResponseLength by calling from_dict on the json representation
        search_settings_conversational_search_response_length_model_dict = SearchSettingsConversationalSearchResponseLength.from_dict(search_settings_conversational_search_response_length_model_json).__dict__
        search_settings_conversational_search_response_length_model2 = SearchSettingsConversationalSearchResponseLength(**search_settings_conversational_search_response_length_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_conversational_search_response_length_model == search_settings_conversational_search_response_length_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_conversational_search_response_length_model_json2 = search_settings_conversational_search_response_length_model.to_dict()
        assert search_settings_conversational_search_response_length_model_json2 == search_settings_conversational_search_response_length_model_json


class TestModel_SearchSettingsConversationalSearchSearchConfidence:
    """
    Test Class for SearchSettingsConversationalSearchSearchConfidence
    """

    def test_search_settings_conversational_search_search_confidence_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsConversationalSearchSearchConfidence
        """

        # Construct a json representation of a SearchSettingsConversationalSearchSearchConfidence model
        search_settings_conversational_search_search_confidence_model_json = {}
        search_settings_conversational_search_search_confidence_model_json['threshold'] = 'less_often'

        # Construct a model instance of SearchSettingsConversationalSearchSearchConfidence by calling from_dict on the json representation
        search_settings_conversational_search_search_confidence_model = SearchSettingsConversationalSearchSearchConfidence.from_dict(search_settings_conversational_search_search_confidence_model_json)
        assert search_settings_conversational_search_search_confidence_model != False

        # Construct a model instance of SearchSettingsConversationalSearchSearchConfidence by calling from_dict on the json representation
        search_settings_conversational_search_search_confidence_model_dict = SearchSettingsConversationalSearchSearchConfidence.from_dict(search_settings_conversational_search_search_confidence_model_json).__dict__
        search_settings_conversational_search_search_confidence_model2 = SearchSettingsConversationalSearchSearchConfidence(**search_settings_conversational_search_search_confidence_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_conversational_search_search_confidence_model == search_settings_conversational_search_search_confidence_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_conversational_search_search_confidence_model_json2 = search_settings_conversational_search_search_confidence_model.to_dict()
        assert search_settings_conversational_search_search_confidence_model_json2 == search_settings_conversational_search_search_confidence_model_json


class TestModel_SearchSettingsDiscovery:
    """
    Test Class for SearchSettingsDiscovery
    """

    def test_search_settings_discovery_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsDiscovery
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_settings_discovery_authentication_model = {}  # SearchSettingsDiscoveryAuthentication
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        # Construct a json representation of a SearchSettingsDiscovery model
        search_settings_discovery_model_json = {}
        search_settings_discovery_model_json['instance_id'] = 'testString'
        search_settings_discovery_model_json['project_id'] = 'testString'
        search_settings_discovery_model_json['url'] = 'testString'
        search_settings_discovery_model_json['max_primary_results'] = 10000
        search_settings_discovery_model_json['max_total_results'] = 10000
        search_settings_discovery_model_json['confidence_threshold'] = 0.0
        search_settings_discovery_model_json['highlight'] = True
        search_settings_discovery_model_json['find_answers'] = True
        search_settings_discovery_model_json['authentication'] = search_settings_discovery_authentication_model

        # Construct a model instance of SearchSettingsDiscovery by calling from_dict on the json representation
        search_settings_discovery_model = SearchSettingsDiscovery.from_dict(search_settings_discovery_model_json)
        assert search_settings_discovery_model != False

        # Construct a model instance of SearchSettingsDiscovery by calling from_dict on the json representation
        search_settings_discovery_model_dict = SearchSettingsDiscovery.from_dict(search_settings_discovery_model_json).__dict__
        search_settings_discovery_model2 = SearchSettingsDiscovery(**search_settings_discovery_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_discovery_model == search_settings_discovery_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_discovery_model_json2 = search_settings_discovery_model.to_dict()
        assert search_settings_discovery_model_json2 == search_settings_discovery_model_json


class TestModel_SearchSettingsDiscoveryAuthentication:
    """
    Test Class for SearchSettingsDiscoveryAuthentication
    """

    def test_search_settings_discovery_authentication_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsDiscoveryAuthentication
        """

        # Construct a json representation of a SearchSettingsDiscoveryAuthentication model
        search_settings_discovery_authentication_model_json = {}
        search_settings_discovery_authentication_model_json['basic'] = 'testString'
        search_settings_discovery_authentication_model_json['bearer'] = 'testString'

        # Construct a model instance of SearchSettingsDiscoveryAuthentication by calling from_dict on the json representation
        search_settings_discovery_authentication_model = SearchSettingsDiscoveryAuthentication.from_dict(search_settings_discovery_authentication_model_json)
        assert search_settings_discovery_authentication_model != False

        # Construct a model instance of SearchSettingsDiscoveryAuthentication by calling from_dict on the json representation
        search_settings_discovery_authentication_model_dict = SearchSettingsDiscoveryAuthentication.from_dict(search_settings_discovery_authentication_model_json).__dict__
        search_settings_discovery_authentication_model2 = SearchSettingsDiscoveryAuthentication(**search_settings_discovery_authentication_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_discovery_authentication_model == search_settings_discovery_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_discovery_authentication_model_json2 = search_settings_discovery_authentication_model.to_dict()
        assert search_settings_discovery_authentication_model_json2 == search_settings_discovery_authentication_model_json


class TestModel_SearchSettingsElasticSearch:
    """
    Test Class for SearchSettingsElasticSearch
    """

    def test_search_settings_elastic_search_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsElasticSearch
        """

        # Construct a json representation of a SearchSettingsElasticSearch model
        search_settings_elastic_search_model_json = {}
        search_settings_elastic_search_model_json['url'] = 'testString'
        search_settings_elastic_search_model_json['port'] = 'testString'
        search_settings_elastic_search_model_json['username'] = 'testString'
        search_settings_elastic_search_model_json['password'] = 'testString'
        search_settings_elastic_search_model_json['index'] = 'testString'
        search_settings_elastic_search_model_json['filter'] = ['testString']
        search_settings_elastic_search_model_json['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model_json['managed_index'] = 'testString'
        search_settings_elastic_search_model_json['apikey'] = 'testString'

        # Construct a model instance of SearchSettingsElasticSearch by calling from_dict on the json representation
        search_settings_elastic_search_model = SearchSettingsElasticSearch.from_dict(search_settings_elastic_search_model_json)
        assert search_settings_elastic_search_model != False

        # Construct a model instance of SearchSettingsElasticSearch by calling from_dict on the json representation
        search_settings_elastic_search_model_dict = SearchSettingsElasticSearch.from_dict(search_settings_elastic_search_model_json).__dict__
        search_settings_elastic_search_model2 = SearchSettingsElasticSearch(**search_settings_elastic_search_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_elastic_search_model == search_settings_elastic_search_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_elastic_search_model_json2 = search_settings_elastic_search_model.to_dict()
        assert search_settings_elastic_search_model_json2 == search_settings_elastic_search_model_json


class TestModel_SearchSettingsMessages:
    """
    Test Class for SearchSettingsMessages
    """

    def test_search_settings_messages_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsMessages
        """

        # Construct a json representation of a SearchSettingsMessages model
        search_settings_messages_model_json = {}
        search_settings_messages_model_json['success'] = 'testString'
        search_settings_messages_model_json['error'] = 'testString'
        search_settings_messages_model_json['no_result'] = 'testString'

        # Construct a model instance of SearchSettingsMessages by calling from_dict on the json representation
        search_settings_messages_model = SearchSettingsMessages.from_dict(search_settings_messages_model_json)
        assert search_settings_messages_model != False

        # Construct a model instance of SearchSettingsMessages by calling from_dict on the json representation
        search_settings_messages_model_dict = SearchSettingsMessages.from_dict(search_settings_messages_model_json).__dict__
        search_settings_messages_model2 = SearchSettingsMessages(**search_settings_messages_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_messages_model == search_settings_messages_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_messages_model_json2 = search_settings_messages_model.to_dict()
        assert search_settings_messages_model_json2 == search_settings_messages_model_json


class TestModel_SearchSettingsSchemaMapping:
    """
    Test Class for SearchSettingsSchemaMapping
    """

    def test_search_settings_schema_mapping_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsSchemaMapping
        """

        # Construct a json representation of a SearchSettingsSchemaMapping model
        search_settings_schema_mapping_model_json = {}
        search_settings_schema_mapping_model_json['url'] = 'testString'
        search_settings_schema_mapping_model_json['body'] = 'testString'
        search_settings_schema_mapping_model_json['title'] = 'testString'

        # Construct a model instance of SearchSettingsSchemaMapping by calling from_dict on the json representation
        search_settings_schema_mapping_model = SearchSettingsSchemaMapping.from_dict(search_settings_schema_mapping_model_json)
        assert search_settings_schema_mapping_model != False

        # Construct a model instance of SearchSettingsSchemaMapping by calling from_dict on the json representation
        search_settings_schema_mapping_model_dict = SearchSettingsSchemaMapping.from_dict(search_settings_schema_mapping_model_json).__dict__
        search_settings_schema_mapping_model2 = SearchSettingsSchemaMapping(**search_settings_schema_mapping_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_schema_mapping_model == search_settings_schema_mapping_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_schema_mapping_model_json2 = search_settings_schema_mapping_model.to_dict()
        assert search_settings_schema_mapping_model_json2 == search_settings_schema_mapping_model_json


class TestModel_SearchSettingsServerSideSearch:
    """
    Test Class for SearchSettingsServerSideSearch
    """

    def test_search_settings_server_side_search_serialization(self):
        """
        Test serialization/deserialization for SearchSettingsServerSideSearch
        """

        # Construct a json representation of a SearchSettingsServerSideSearch model
        search_settings_server_side_search_model_json = {}
        search_settings_server_side_search_model_json['url'] = 'testString'
        search_settings_server_side_search_model_json['port'] = 'testString'
        search_settings_server_side_search_model_json['username'] = 'testString'
        search_settings_server_side_search_model_json['password'] = 'testString'
        search_settings_server_side_search_model_json['filter'] = 'testString'
        search_settings_server_side_search_model_json['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model_json['apikey'] = 'testString'
        search_settings_server_side_search_model_json['no_auth'] = True
        search_settings_server_side_search_model_json['auth_type'] = 'basic'

        # Construct a model instance of SearchSettingsServerSideSearch by calling from_dict on the json representation
        search_settings_server_side_search_model = SearchSettingsServerSideSearch.from_dict(search_settings_server_side_search_model_json)
        assert search_settings_server_side_search_model != False

        # Construct a model instance of SearchSettingsServerSideSearch by calling from_dict on the json representation
        search_settings_server_side_search_model_dict = SearchSettingsServerSideSearch.from_dict(search_settings_server_side_search_model_json).__dict__
        search_settings_server_side_search_model2 = SearchSettingsServerSideSearch(**search_settings_server_side_search_model_dict)

        # Verify the model instances are equivalent
        assert search_settings_server_side_search_model == search_settings_server_side_search_model2

        # Convert model instance back to dict and verify no loss of data
        search_settings_server_side_search_model_json2 = search_settings_server_side_search_model.to_dict()
        assert search_settings_server_side_search_model_json2 == search_settings_server_side_search_model_json


class TestModel_SearchSkillWarning:
    """
    Test Class for SearchSkillWarning
    """

    def test_search_skill_warning_serialization(self):
        """
        Test serialization/deserialization for SearchSkillWarning
        """

        # Construct a json representation of a SearchSkillWarning model
        search_skill_warning_model_json = {}
        search_skill_warning_model_json['code'] = 'testString'
        search_skill_warning_model_json['path'] = 'testString'
        search_skill_warning_model_json['message'] = 'testString'

        # Construct a model instance of SearchSkillWarning by calling from_dict on the json representation
        search_skill_warning_model = SearchSkillWarning.from_dict(search_skill_warning_model_json)
        assert search_skill_warning_model != False

        # Construct a model instance of SearchSkillWarning by calling from_dict on the json representation
        search_skill_warning_model_dict = SearchSkillWarning.from_dict(search_skill_warning_model_json).__dict__
        search_skill_warning_model2 = SearchSkillWarning(**search_skill_warning_model_dict)

        # Verify the model instances are equivalent
        assert search_skill_warning_model == search_skill_warning_model2

        # Convert model instance back to dict and verify no loss of data
        search_skill_warning_model_json2 = search_skill_warning_model.to_dict()
        assert search_skill_warning_model_json2 == search_skill_warning_model_json


class TestModel_SessionResponse:
    """
    Test Class for SessionResponse
    """

    def test_session_response_serialization(self):
        """
        Test serialization/deserialization for SessionResponse
        """

        # Construct a json representation of a SessionResponse model
        session_response_model_json = {}
        session_response_model_json['session_id'] = 'testString'

        # Construct a model instance of SessionResponse by calling from_dict on the json representation
        session_response_model = SessionResponse.from_dict(session_response_model_json)
        assert session_response_model != False

        # Construct a model instance of SessionResponse by calling from_dict on the json representation
        session_response_model_dict = SessionResponse.from_dict(session_response_model_json).__dict__
        session_response_model2 = SessionResponse(**session_response_model_dict)

        # Verify the model instances are equivalent
        assert session_response_model == session_response_model2

        # Convert model instance back to dict and verify no loss of data
        session_response_model_json2 = session_response_model.to_dict()
        assert session_response_model_json2 == session_response_model_json


class TestModel_Skill:
    """
    Test Class for Skill
    """

    def test_skill_serialization(self):
        """
        Test serialization/deserialization for Skill
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_settings_discovery_authentication_model = {}  # SearchSettingsDiscoveryAuthentication
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        search_settings_discovery_model = {}  # SearchSettingsDiscovery
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        search_settings_messages_model = {}  # SearchSettingsMessages
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        search_settings_schema_mapping_model = {}  # SearchSettingsSchemaMapping
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        search_settings_elastic_search_model = {}  # SearchSettingsElasticSearch
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        search_settings_conversational_search_response_length_model = {}  # SearchSettingsConversationalSearchResponseLength
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        search_settings_conversational_search_search_confidence_model = {}  # SearchSettingsConversationalSearchSearchConfidence
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        search_settings_conversational_search_model = {}  # SearchSettingsConversationalSearch
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        search_settings_server_side_search_model = {}  # SearchSettingsServerSideSearch
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        search_settings_client_side_search_model = {}  # SearchSettingsClientSideSearch
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        search_settings_model = {}  # SearchSettings
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        # Construct a json representation of a Skill model
        skill_model_json = {}
        skill_model_json['name'] = 'testString'
        skill_model_json['description'] = 'testString'
        skill_model_json['workspace'] = {'anyKey': 'anyValue'}
        skill_model_json['dialog_settings'] = {'anyKey': 'anyValue'}
        skill_model_json['search_settings'] = search_settings_model
        skill_model_json['language'] = 'testString'
        skill_model_json['type'] = 'action'

        # Construct a model instance of Skill by calling from_dict on the json representation
        skill_model = Skill.from_dict(skill_model_json)
        assert skill_model != False

        # Construct a model instance of Skill by calling from_dict on the json representation
        skill_model_dict = Skill.from_dict(skill_model_json).__dict__
        skill_model2 = Skill(**skill_model_dict)

        # Verify the model instances are equivalent
        assert skill_model == skill_model2

        # Convert model instance back to dict and verify no loss of data
        skill_model_json2 = skill_model.to_dict()
        assert skill_model_json2 == skill_model_json


class TestModel_SkillImport:
    """
    Test Class for SkillImport
    """

    def test_skill_import_serialization(self):
        """
        Test serialization/deserialization for SkillImport
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_settings_discovery_authentication_model = {}  # SearchSettingsDiscoveryAuthentication
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        search_settings_discovery_model = {}  # SearchSettingsDiscovery
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        search_settings_messages_model = {}  # SearchSettingsMessages
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        search_settings_schema_mapping_model = {}  # SearchSettingsSchemaMapping
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        search_settings_elastic_search_model = {}  # SearchSettingsElasticSearch
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        search_settings_conversational_search_response_length_model = {}  # SearchSettingsConversationalSearchResponseLength
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        search_settings_conversational_search_search_confidence_model = {}  # SearchSettingsConversationalSearchSearchConfidence
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        search_settings_conversational_search_model = {}  # SearchSettingsConversationalSearch
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        search_settings_server_side_search_model = {}  # SearchSettingsServerSideSearch
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        search_settings_client_side_search_model = {}  # SearchSettingsClientSideSearch
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        search_settings_model = {}  # SearchSettings
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        # Construct a json representation of a SkillImport model
        skill_import_model_json = {}
        skill_import_model_json['name'] = 'testString'
        skill_import_model_json['description'] = 'testString'
        skill_import_model_json['workspace'] = {'anyKey': 'anyValue'}
        skill_import_model_json['dialog_settings'] = {'anyKey': 'anyValue'}
        skill_import_model_json['search_settings'] = search_settings_model
        skill_import_model_json['language'] = 'testString'
        skill_import_model_json['type'] = 'action'

        # Construct a model instance of SkillImport by calling from_dict on the json representation
        skill_import_model = SkillImport.from_dict(skill_import_model_json)
        assert skill_import_model != False

        # Construct a model instance of SkillImport by calling from_dict on the json representation
        skill_import_model_dict = SkillImport.from_dict(skill_import_model_json).__dict__
        skill_import_model2 = SkillImport(**skill_import_model_dict)

        # Verify the model instances are equivalent
        assert skill_import_model == skill_import_model2

        # Convert model instance back to dict and verify no loss of data
        skill_import_model_json2 = skill_import_model.to_dict()
        assert skill_import_model_json2 == skill_import_model_json


class TestModel_SkillsAsyncRequestStatus:
    """
    Test Class for SkillsAsyncRequestStatus
    """

    def test_skills_async_request_status_serialization(self):
        """
        Test serialization/deserialization for SkillsAsyncRequestStatus
        """

        # Construct a json representation of a SkillsAsyncRequestStatus model
        skills_async_request_status_model_json = {}

        # Construct a model instance of SkillsAsyncRequestStatus by calling from_dict on the json representation
        skills_async_request_status_model = SkillsAsyncRequestStatus.from_dict(skills_async_request_status_model_json)
        assert skills_async_request_status_model != False

        # Construct a model instance of SkillsAsyncRequestStatus by calling from_dict on the json representation
        skills_async_request_status_model_dict = SkillsAsyncRequestStatus.from_dict(skills_async_request_status_model_json).__dict__
        skills_async_request_status_model2 = SkillsAsyncRequestStatus(**skills_async_request_status_model_dict)

        # Verify the model instances are equivalent
        assert skills_async_request_status_model == skills_async_request_status_model2

        # Convert model instance back to dict and verify no loss of data
        skills_async_request_status_model_json2 = skills_async_request_status_model.to_dict()
        assert skills_async_request_status_model_json2 == skills_async_request_status_model_json


class TestModel_SkillsExport:
    """
    Test Class for SkillsExport
    """

    def test_skills_export_serialization(self):
        """
        Test serialization/deserialization for SkillsExport
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_settings_discovery_authentication_model = {}  # SearchSettingsDiscoveryAuthentication
        search_settings_discovery_authentication_model['basic'] = 'testString'
        search_settings_discovery_authentication_model['bearer'] = 'testString'

        search_settings_discovery_model = {}  # SearchSettingsDiscovery
        search_settings_discovery_model['instance_id'] = 'testString'
        search_settings_discovery_model['project_id'] = 'testString'
        search_settings_discovery_model['url'] = 'testString'
        search_settings_discovery_model['max_primary_results'] = 10000
        search_settings_discovery_model['max_total_results'] = 10000
        search_settings_discovery_model['confidence_threshold'] = 0.0
        search_settings_discovery_model['highlight'] = True
        search_settings_discovery_model['find_answers'] = True
        search_settings_discovery_model['authentication'] = search_settings_discovery_authentication_model

        search_settings_messages_model = {}  # SearchSettingsMessages
        search_settings_messages_model['success'] = 'testString'
        search_settings_messages_model['error'] = 'testString'
        search_settings_messages_model['no_result'] = 'testString'

        search_settings_schema_mapping_model = {}  # SearchSettingsSchemaMapping
        search_settings_schema_mapping_model['url'] = 'testString'
        search_settings_schema_mapping_model['body'] = 'testString'
        search_settings_schema_mapping_model['title'] = 'testString'

        search_settings_elastic_search_model = {}  # SearchSettingsElasticSearch
        search_settings_elastic_search_model['url'] = 'testString'
        search_settings_elastic_search_model['port'] = 'testString'
        search_settings_elastic_search_model['username'] = 'testString'
        search_settings_elastic_search_model['password'] = 'testString'
        search_settings_elastic_search_model['index'] = 'testString'
        search_settings_elastic_search_model['filter'] = ['testString']
        search_settings_elastic_search_model['query_body'] = {'anyKey': 'anyValue'}
        search_settings_elastic_search_model['managed_index'] = 'testString'
        search_settings_elastic_search_model['apikey'] = 'testString'

        search_settings_conversational_search_response_length_model = {}  # SearchSettingsConversationalSearchResponseLength
        search_settings_conversational_search_response_length_model['option'] = 'moderate'

        search_settings_conversational_search_search_confidence_model = {}  # SearchSettingsConversationalSearchSearchConfidence
        search_settings_conversational_search_search_confidence_model['threshold'] = 'less_often'

        search_settings_conversational_search_model = {}  # SearchSettingsConversationalSearch
        search_settings_conversational_search_model['enabled'] = True
        search_settings_conversational_search_model['response_length'] = search_settings_conversational_search_response_length_model
        search_settings_conversational_search_model['search_confidence'] = search_settings_conversational_search_search_confidence_model

        search_settings_server_side_search_model = {}  # SearchSettingsServerSideSearch
        search_settings_server_side_search_model['url'] = 'testString'
        search_settings_server_side_search_model['port'] = 'testString'
        search_settings_server_side_search_model['username'] = 'testString'
        search_settings_server_side_search_model['password'] = 'testString'
        search_settings_server_side_search_model['filter'] = 'testString'
        search_settings_server_side_search_model['metadata'] = {'anyKey': 'anyValue'}
        search_settings_server_side_search_model['apikey'] = 'testString'
        search_settings_server_side_search_model['no_auth'] = True
        search_settings_server_side_search_model['auth_type'] = 'basic'

        search_settings_client_side_search_model = {}  # SearchSettingsClientSideSearch
        search_settings_client_side_search_model['filter'] = 'testString'
        search_settings_client_side_search_model['metadata'] = {'anyKey': 'anyValue'}

        search_settings_model = {}  # SearchSettings
        search_settings_model['discovery'] = search_settings_discovery_model
        search_settings_model['messages'] = search_settings_messages_model
        search_settings_model['schema_mapping'] = search_settings_schema_mapping_model
        search_settings_model['elastic_search'] = search_settings_elastic_search_model
        search_settings_model['conversational_search'] = search_settings_conversational_search_model
        search_settings_model['server_side_search'] = search_settings_server_side_search_model
        search_settings_model['client_side_search'] = search_settings_client_side_search_model

        skill_model = {}  # Skill
        skill_model['name'] = 'testString'
        skill_model['description'] = 'testString'
        skill_model['workspace'] = {'anyKey': 'anyValue'}
        skill_model['dialog_settings'] = {'anyKey': 'anyValue'}
        skill_model['search_settings'] = search_settings_model
        skill_model['language'] = 'testString'
        skill_model['type'] = 'action'

        assistant_state_model = {}  # AssistantState
        assistant_state_model['action_disabled'] = True
        assistant_state_model['dialog_disabled'] = True

        # Construct a json representation of a SkillsExport model
        skills_export_model_json = {}
        skills_export_model_json['assistant_skills'] = [skill_model]
        skills_export_model_json['assistant_state'] = assistant_state_model

        # Construct a model instance of SkillsExport by calling from_dict on the json representation
        skills_export_model = SkillsExport.from_dict(skills_export_model_json)
        assert skills_export_model != False

        # Construct a model instance of SkillsExport by calling from_dict on the json representation
        skills_export_model_dict = SkillsExport.from_dict(skills_export_model_json).__dict__
        skills_export_model2 = SkillsExport(**skills_export_model_dict)

        # Verify the model instances are equivalent
        assert skills_export_model == skills_export_model2

        # Convert model instance back to dict and verify no loss of data
        skills_export_model_json2 = skills_export_model.to_dict()
        assert skills_export_model_json2 == skills_export_model_json


class TestModel_StatefulMessageResponse:
    """
    Test Class for StatefulMessageResponse
    """

    def test_stateful_message_response_serialization(self):
        """
        Test serialization/deserialization for StatefulMessageResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {}  # RuntimeResponseGenericRuntimeResponseTypeText
        runtime_response_generic_model['response_type'] = 'text'
        runtime_response_generic_model['text'] = 'testString'
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        dialog_node_action_model = {}  # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        message_output_debug_model = {}  # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'
        message_output_debug_model['turn_events'] = [message_output_debug_turn_event_model]

        message_output_spelling_model = {}  # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        message_output_model = {}  # MessageOutput
        message_output_model['generic'] = [runtime_response_generic_model]
        message_output_model['intents'] = [runtime_intent_model]
        message_output_model['entities'] = [runtime_entity_model]
        message_output_model['actions'] = [dialog_node_action_model]
        message_output_model['debug'] = message_output_debug_model
        message_output_model['user_defined'] = {'anyKey': 'anyValue'}
        message_output_model['spelling'] = message_output_spelling_model

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        message_context_global_model = {}  # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        message_context_action_skill_model = {}  # MessageContextActionSkill
        message_context_action_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['system'] = message_context_skill_system_model
        message_context_action_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        message_context_action_skill_model['skill_variables'] = {'anyKey': 'anyValue'}

        message_context_skills_model = {}  # MessageContextSkills
        message_context_skills_model['main skill'] = message_context_dialog_skill_model
        message_context_skills_model['actions skill'] = message_context_action_skill_model

        message_context_model = {}  # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = message_context_skills_model
        message_context_model['integrations'] = {'anyKey': 'anyValue'}

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        # Construct a json representation of a StatefulMessageResponse model
        stateful_message_response_model_json = {}
        stateful_message_response_model_json['output'] = message_output_model
        stateful_message_response_model_json['context'] = message_context_model
        stateful_message_response_model_json['user_id'] = 'testString'
        stateful_message_response_model_json['masked_output'] = message_output_model
        stateful_message_response_model_json['masked_input'] = message_input_model

        # Construct a model instance of StatefulMessageResponse by calling from_dict on the json representation
        stateful_message_response_model = StatefulMessageResponse.from_dict(stateful_message_response_model_json)
        assert stateful_message_response_model != False

        # Construct a model instance of StatefulMessageResponse by calling from_dict on the json representation
        stateful_message_response_model_dict = StatefulMessageResponse.from_dict(stateful_message_response_model_json).__dict__
        stateful_message_response_model2 = StatefulMessageResponse(**stateful_message_response_model_dict)

        # Verify the model instances are equivalent
        assert stateful_message_response_model == stateful_message_response_model2

        # Convert model instance back to dict and verify no loss of data
        stateful_message_response_model_json2 = stateful_message_response_model.to_dict()
        assert stateful_message_response_model_json2 == stateful_message_response_model_json


class TestModel_StatelessMessageContext:
    """
    Test Class for StatelessMessageContext
    """

    def test_stateless_message_context_serialization(self):
        """
        Test serialization/deserialization for StatelessMessageContext
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        stateless_message_context_global_model = {}  # StatelessMessageContextGlobal
        stateless_message_context_global_model['system'] = message_context_global_system_model
        stateless_message_context_global_model['session_id'] = 'testString'

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        stateless_message_context_skills_actions_skill_model = {}  # StatelessMessageContextSkillsActionsSkill
        stateless_message_context_skills_actions_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['system'] = message_context_skill_system_model
        stateless_message_context_skills_actions_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['skill_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_skill_variables'] = {'anyKey': 'anyValue'}

        stateless_message_context_skills_model = {}  # StatelessMessageContextSkills
        stateless_message_context_skills_model['main skill'] = message_context_dialog_skill_model
        stateless_message_context_skills_model['actions skill'] = stateless_message_context_skills_actions_skill_model

        # Construct a json representation of a StatelessMessageContext model
        stateless_message_context_model_json = {}
        stateless_message_context_model_json['global'] = stateless_message_context_global_model
        stateless_message_context_model_json['skills'] = stateless_message_context_skills_model
        stateless_message_context_model_json['integrations'] = {'anyKey': 'anyValue'}

        # Construct a model instance of StatelessMessageContext by calling from_dict on the json representation
        stateless_message_context_model = StatelessMessageContext.from_dict(stateless_message_context_model_json)
        assert stateless_message_context_model != False

        # Construct a model instance of StatelessMessageContext by calling from_dict on the json representation
        stateless_message_context_model_dict = StatelessMessageContext.from_dict(stateless_message_context_model_json).__dict__
        stateless_message_context_model2 = StatelessMessageContext(**stateless_message_context_model_dict)

        # Verify the model instances are equivalent
        assert stateless_message_context_model == stateless_message_context_model2

        # Convert model instance back to dict and verify no loss of data
        stateless_message_context_model_json2 = stateless_message_context_model.to_dict()
        assert stateless_message_context_model_json2 == stateless_message_context_model_json


class TestModel_StatelessMessageContextGlobal:
    """
    Test Class for StatelessMessageContextGlobal
    """

    def test_stateless_message_context_global_serialization(self):
        """
        Test serialization/deserialization for StatelessMessageContextGlobal
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        # Construct a json representation of a StatelessMessageContextGlobal model
        stateless_message_context_global_model_json = {}
        stateless_message_context_global_model_json['system'] = message_context_global_system_model
        stateless_message_context_global_model_json['session_id'] = 'testString'

        # Construct a model instance of StatelessMessageContextGlobal by calling from_dict on the json representation
        stateless_message_context_global_model = StatelessMessageContextGlobal.from_dict(stateless_message_context_global_model_json)
        assert stateless_message_context_global_model != False

        # Construct a model instance of StatelessMessageContextGlobal by calling from_dict on the json representation
        stateless_message_context_global_model_dict = StatelessMessageContextGlobal.from_dict(stateless_message_context_global_model_json).__dict__
        stateless_message_context_global_model2 = StatelessMessageContextGlobal(**stateless_message_context_global_model_dict)

        # Verify the model instances are equivalent
        assert stateless_message_context_global_model == stateless_message_context_global_model2

        # Convert model instance back to dict and verify no loss of data
        stateless_message_context_global_model_json2 = stateless_message_context_global_model.to_dict()
        assert stateless_message_context_global_model_json2 == stateless_message_context_global_model_json


class TestModel_StatelessMessageContextSkills:
    """
    Test Class for StatelessMessageContextSkills
    """

    def test_stateless_message_context_skills_serialization(self):
        """
        Test serialization/deserialization for StatelessMessageContextSkills
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        stateless_message_context_skills_actions_skill_model = {}  # StatelessMessageContextSkillsActionsSkill
        stateless_message_context_skills_actions_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['system'] = message_context_skill_system_model
        stateless_message_context_skills_actions_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['skill_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a StatelessMessageContextSkills model
        stateless_message_context_skills_model_json = {}
        stateless_message_context_skills_model_json['main skill'] = message_context_dialog_skill_model
        stateless_message_context_skills_model_json['actions skill'] = stateless_message_context_skills_actions_skill_model

        # Construct a model instance of StatelessMessageContextSkills by calling from_dict on the json representation
        stateless_message_context_skills_model = StatelessMessageContextSkills.from_dict(stateless_message_context_skills_model_json)
        assert stateless_message_context_skills_model != False

        # Construct a model instance of StatelessMessageContextSkills by calling from_dict on the json representation
        stateless_message_context_skills_model_dict = StatelessMessageContextSkills.from_dict(stateless_message_context_skills_model_json).__dict__
        stateless_message_context_skills_model2 = StatelessMessageContextSkills(**stateless_message_context_skills_model_dict)

        # Verify the model instances are equivalent
        assert stateless_message_context_skills_model == stateless_message_context_skills_model2

        # Convert model instance back to dict and verify no loss of data
        stateless_message_context_skills_model_json2 = stateless_message_context_skills_model.to_dict()
        assert stateless_message_context_skills_model_json2 == stateless_message_context_skills_model_json


class TestModel_StatelessMessageContextSkillsActionsSkill:
    """
    Test Class for StatelessMessageContextSkillsActionsSkill
    """

    def test_stateless_message_context_skills_actions_skill_serialization(self):
        """
        Test serialization/deserialization for StatelessMessageContextSkillsActionsSkill
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a json representation of a StatelessMessageContextSkillsActionsSkill model
        stateless_message_context_skills_actions_skill_model_json = {}
        stateless_message_context_skills_actions_skill_model_json['user_defined'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model_json['system'] = message_context_skill_system_model
        stateless_message_context_skills_actions_skill_model_json['action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model_json['skill_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model_json['private_action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model_json['private_skill_variables'] = {'anyKey': 'anyValue'}

        # Construct a model instance of StatelessMessageContextSkillsActionsSkill by calling from_dict on the json representation
        stateless_message_context_skills_actions_skill_model = StatelessMessageContextSkillsActionsSkill.from_dict(stateless_message_context_skills_actions_skill_model_json)
        assert stateless_message_context_skills_actions_skill_model != False

        # Construct a model instance of StatelessMessageContextSkillsActionsSkill by calling from_dict on the json representation
        stateless_message_context_skills_actions_skill_model_dict = StatelessMessageContextSkillsActionsSkill.from_dict(stateless_message_context_skills_actions_skill_model_json).__dict__
        stateless_message_context_skills_actions_skill_model2 = StatelessMessageContextSkillsActionsSkill(**stateless_message_context_skills_actions_skill_model_dict)

        # Verify the model instances are equivalent
        assert stateless_message_context_skills_actions_skill_model == stateless_message_context_skills_actions_skill_model2

        # Convert model instance back to dict and verify no loss of data
        stateless_message_context_skills_actions_skill_model_json2 = stateless_message_context_skills_actions_skill_model.to_dict()
        assert stateless_message_context_skills_actions_skill_model_json2 == stateless_message_context_skills_actions_skill_model_json


class TestModel_StatelessMessageInput:
    """
    Test Class for StatelessMessageInput
    """

    def test_stateless_message_input_serialization(self):
        """
        Test serialization/deserialization for StatelessMessageInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        stateless_message_input_options_model = {}  # StatelessMessageInputOptions
        stateless_message_input_options_model['restart'] = False
        stateless_message_input_options_model['alternate_intents'] = False
        stateless_message_input_options_model['async_callout'] = False
        stateless_message_input_options_model['spelling'] = message_input_options_spelling_model
        stateless_message_input_options_model['debug'] = False

        # Construct a json representation of a StatelessMessageInput model
        stateless_message_input_model_json = {}
        stateless_message_input_model_json['message_type'] = 'text'
        stateless_message_input_model_json['text'] = 'testString'
        stateless_message_input_model_json['intents'] = [runtime_intent_model]
        stateless_message_input_model_json['entities'] = [runtime_entity_model]
        stateless_message_input_model_json['suggestion_id'] = 'testString'
        stateless_message_input_model_json['attachments'] = [message_input_attachment_model]
        stateless_message_input_model_json['analytics'] = request_analytics_model
        stateless_message_input_model_json['options'] = stateless_message_input_options_model

        # Construct a model instance of StatelessMessageInput by calling from_dict on the json representation
        stateless_message_input_model = StatelessMessageInput.from_dict(stateless_message_input_model_json)
        assert stateless_message_input_model != False

        # Construct a model instance of StatelessMessageInput by calling from_dict on the json representation
        stateless_message_input_model_dict = StatelessMessageInput.from_dict(stateless_message_input_model_json).__dict__
        stateless_message_input_model2 = StatelessMessageInput(**stateless_message_input_model_dict)

        # Verify the model instances are equivalent
        assert stateless_message_input_model == stateless_message_input_model2

        # Convert model instance back to dict and verify no loss of data
        stateless_message_input_model_json2 = stateless_message_input_model.to_dict()
        assert stateless_message_input_model_json2 == stateless_message_input_model_json


class TestModel_StatelessMessageInputOptions:
    """
    Test Class for StatelessMessageInputOptions
    """

    def test_stateless_message_input_options_serialization(self):
        """
        Test serialization/deserialization for StatelessMessageInputOptions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a json representation of a StatelessMessageInputOptions model
        stateless_message_input_options_model_json = {}
        stateless_message_input_options_model_json['restart'] = False
        stateless_message_input_options_model_json['alternate_intents'] = False
        stateless_message_input_options_model_json['async_callout'] = False
        stateless_message_input_options_model_json['spelling'] = message_input_options_spelling_model
        stateless_message_input_options_model_json['debug'] = False

        # Construct a model instance of StatelessMessageInputOptions by calling from_dict on the json representation
        stateless_message_input_options_model = StatelessMessageInputOptions.from_dict(stateless_message_input_options_model_json)
        assert stateless_message_input_options_model != False

        # Construct a model instance of StatelessMessageInputOptions by calling from_dict on the json representation
        stateless_message_input_options_model_dict = StatelessMessageInputOptions.from_dict(stateless_message_input_options_model_json).__dict__
        stateless_message_input_options_model2 = StatelessMessageInputOptions(**stateless_message_input_options_model_dict)

        # Verify the model instances are equivalent
        assert stateless_message_input_options_model == stateless_message_input_options_model2

        # Convert model instance back to dict and verify no loss of data
        stateless_message_input_options_model_json2 = stateless_message_input_options_model.to_dict()
        assert stateless_message_input_options_model_json2 == stateless_message_input_options_model_json


class TestModel_StatelessMessageResponse:
    """
    Test Class for StatelessMessageResponse
    """

    def test_stateless_message_response_serialization(self):
        """
        Test serialization/deserialization for StatelessMessageResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {}  # RuntimeResponseGenericRuntimeResponseTypeText
        runtime_response_generic_model['response_type'] = 'text'
        runtime_response_generic_model['text'] = 'testString'
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        dialog_node_action_model = {}  # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {'anyKey': 'anyValue'}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_visited_model = {}  # DialogNodeVisited
        dialog_node_visited_model['dialog_node'] = 'testString'
        dialog_node_visited_model['title'] = 'testString'
        dialog_node_visited_model['conditions'] = 'testString'

        log_message_source_model = {}  # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {}  # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        message_output_debug_turn_event_model = {}  # MessageOutputDebugTurnEventTurnEventActionVisited
        message_output_debug_turn_event_model['event'] = 'action_visited'
        message_output_debug_turn_event_model['source'] = turn_event_action_source_model
        message_output_debug_turn_event_model['action_start_time'] = 'testString'
        message_output_debug_turn_event_model['condition_type'] = 'user_defined'
        message_output_debug_turn_event_model['reason'] = 'intent'
        message_output_debug_turn_event_model['result_variable'] = 'testString'

        message_output_debug_model = {}  # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_node_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'
        message_output_debug_model['turn_events'] = [message_output_debug_turn_event_model]

        message_output_spelling_model = {}  # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        message_output_model = {}  # MessageOutput
        message_output_model['generic'] = [runtime_response_generic_model]
        message_output_model['intents'] = [runtime_intent_model]
        message_output_model['entities'] = [runtime_entity_model]
        message_output_model['actions'] = [dialog_node_action_model]
        message_output_model['debug'] = message_output_debug_model
        message_output_model['user_defined'] = {'anyKey': 'anyValue'}
        message_output_model['spelling'] = message_output_spelling_model

        message_context_global_system_model = {}  # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'
        message_context_global_system_model['skip_user_input'] = True

        stateless_message_context_global_model = {}  # StatelessMessageContextGlobal
        stateless_message_context_global_model['system'] = message_context_global_system_model
        stateless_message_context_global_model['session_id'] = 'testString'

        message_context_skill_system_model = {}  # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_dialog_skill_model = {}  # MessageContextDialogSkill
        message_context_dialog_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        message_context_dialog_skill_model['system'] = message_context_skill_system_model

        stateless_message_context_skills_actions_skill_model = {}  # StatelessMessageContextSkillsActionsSkill
        stateless_message_context_skills_actions_skill_model['user_defined'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['system'] = message_context_skill_system_model
        stateless_message_context_skills_actions_skill_model['action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['skill_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_action_variables'] = {'anyKey': 'anyValue'}
        stateless_message_context_skills_actions_skill_model['private_skill_variables'] = {'anyKey': 'anyValue'}

        stateless_message_context_skills_model = {}  # StatelessMessageContextSkills
        stateless_message_context_skills_model['main skill'] = message_context_dialog_skill_model
        stateless_message_context_skills_model['actions skill'] = stateless_message_context_skills_actions_skill_model

        stateless_message_context_model = {}  # StatelessMessageContext
        stateless_message_context_model['global'] = stateless_message_context_global_model
        stateless_message_context_model['skills'] = stateless_message_context_skills_model
        stateless_message_context_model['integrations'] = {'anyKey': 'anyValue'}

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        # Construct a json representation of a StatelessMessageResponse model
        stateless_message_response_model_json = {}
        stateless_message_response_model_json['output'] = message_output_model
        stateless_message_response_model_json['context'] = stateless_message_context_model
        stateless_message_response_model_json['masked_output'] = message_output_model
        stateless_message_response_model_json['masked_input'] = message_input_model
        stateless_message_response_model_json['user_id'] = 'testString'

        # Construct a model instance of StatelessMessageResponse by calling from_dict on the json representation
        stateless_message_response_model = StatelessMessageResponse.from_dict(stateless_message_response_model_json)
        assert stateless_message_response_model != False

        # Construct a model instance of StatelessMessageResponse by calling from_dict on the json representation
        stateless_message_response_model_dict = StatelessMessageResponse.from_dict(stateless_message_response_model_json).__dict__
        stateless_message_response_model2 = StatelessMessageResponse(**stateless_message_response_model_dict)

        # Verify the model instances are equivalent
        assert stateless_message_response_model == stateless_message_response_model2

        # Convert model instance back to dict and verify no loss of data
        stateless_message_response_model_json2 = stateless_message_response_model.to_dict()
        assert stateless_message_response_model_json2 == stateless_message_response_model_json


class TestModel_StatusError:
    """
    Test Class for StatusError
    """

    def test_status_error_serialization(self):
        """
        Test serialization/deserialization for StatusError
        """

        # Construct a json representation of a StatusError model
        status_error_model_json = {}
        status_error_model_json['message'] = 'testString'

        # Construct a model instance of StatusError by calling from_dict on the json representation
        status_error_model = StatusError.from_dict(status_error_model_json)
        assert status_error_model != False

        # Construct a model instance of StatusError by calling from_dict on the json representation
        status_error_model_dict = StatusError.from_dict(status_error_model_json).__dict__
        status_error_model2 = StatusError(**status_error_model_dict)

        # Verify the model instances are equivalent
        assert status_error_model == status_error_model2

        # Convert model instance back to dict and verify no loss of data
        status_error_model_json2 = status_error_model.to_dict()
        assert status_error_model_json2 == status_error_model_json


class TestModel_TurnEventActionSource:
    """
    Test Class for TurnEventActionSource
    """

    def test_turn_event_action_source_serialization(self):
        """
        Test serialization/deserialization for TurnEventActionSource
        """

        # Construct a json representation of a TurnEventActionSource model
        turn_event_action_source_model_json = {}
        turn_event_action_source_model_json['type'] = 'action'
        turn_event_action_source_model_json['action'] = 'testString'
        turn_event_action_source_model_json['action_title'] = 'testString'
        turn_event_action_source_model_json['condition'] = 'testString'

        # Construct a model instance of TurnEventActionSource by calling from_dict on the json representation
        turn_event_action_source_model = TurnEventActionSource.from_dict(turn_event_action_source_model_json)
        assert turn_event_action_source_model != False

        # Construct a model instance of TurnEventActionSource by calling from_dict on the json representation
        turn_event_action_source_model_dict = TurnEventActionSource.from_dict(turn_event_action_source_model_json).__dict__
        turn_event_action_source_model2 = TurnEventActionSource(**turn_event_action_source_model_dict)

        # Verify the model instances are equivalent
        assert turn_event_action_source_model == turn_event_action_source_model2

        # Convert model instance back to dict and verify no loss of data
        turn_event_action_source_model_json2 = turn_event_action_source_model.to_dict()
        assert turn_event_action_source_model_json2 == turn_event_action_source_model_json


class TestModel_TurnEventCalloutCallout:
    """
    Test Class for TurnEventCalloutCallout
    """

    def test_turn_event_callout_callout_serialization(self):
        """
        Test serialization/deserialization for TurnEventCalloutCallout
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_callout_callout_request_model = {}  # TurnEventCalloutCalloutRequest
        turn_event_callout_callout_request_model['method'] = 'get'
        turn_event_callout_callout_request_model['url'] = 'testString'
        turn_event_callout_callout_request_model['path'] = 'testString'
        turn_event_callout_callout_request_model['query_parameters'] = 'testString'
        turn_event_callout_callout_request_model['headers'] = {'anyKey': 'anyValue'}
        turn_event_callout_callout_request_model['body'] = {'anyKey': 'anyValue'}

        turn_event_callout_callout_response_model = {}  # TurnEventCalloutCalloutResponse
        turn_event_callout_callout_response_model['body'] = 'testString'
        turn_event_callout_callout_response_model['status_code'] = 38
        turn_event_callout_callout_response_model['last_event'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a TurnEventCalloutCallout model
        turn_event_callout_callout_model_json = {}
        turn_event_callout_callout_model_json['type'] = 'integration_interaction'
        turn_event_callout_callout_model_json['internal'] = {'anyKey': 'anyValue'}
        turn_event_callout_callout_model_json['result_variable'] = 'testString'
        turn_event_callout_callout_model_json['request'] = turn_event_callout_callout_request_model
        turn_event_callout_callout_model_json['response'] = turn_event_callout_callout_response_model

        # Construct a model instance of TurnEventCalloutCallout by calling from_dict on the json representation
        turn_event_callout_callout_model = TurnEventCalloutCallout.from_dict(turn_event_callout_callout_model_json)
        assert turn_event_callout_callout_model != False

        # Construct a model instance of TurnEventCalloutCallout by calling from_dict on the json representation
        turn_event_callout_callout_model_dict = TurnEventCalloutCallout.from_dict(turn_event_callout_callout_model_json).__dict__
        turn_event_callout_callout_model2 = TurnEventCalloutCallout(**turn_event_callout_callout_model_dict)

        # Verify the model instances are equivalent
        assert turn_event_callout_callout_model == turn_event_callout_callout_model2

        # Convert model instance back to dict and verify no loss of data
        turn_event_callout_callout_model_json2 = turn_event_callout_callout_model.to_dict()
        assert turn_event_callout_callout_model_json2 == turn_event_callout_callout_model_json


class TestModel_TurnEventCalloutCalloutRequest:
    """
    Test Class for TurnEventCalloutCalloutRequest
    """

    def test_turn_event_callout_callout_request_serialization(self):
        """
        Test serialization/deserialization for TurnEventCalloutCalloutRequest
        """

        # Construct a json representation of a TurnEventCalloutCalloutRequest model
        turn_event_callout_callout_request_model_json = {}
        turn_event_callout_callout_request_model_json['method'] = 'get'
        turn_event_callout_callout_request_model_json['url'] = 'testString'
        turn_event_callout_callout_request_model_json['path'] = 'testString'
        turn_event_callout_callout_request_model_json['query_parameters'] = 'testString'
        turn_event_callout_callout_request_model_json['headers'] = {'anyKey': 'anyValue'}
        turn_event_callout_callout_request_model_json['body'] = {'anyKey': 'anyValue'}

        # Construct a model instance of TurnEventCalloutCalloutRequest by calling from_dict on the json representation
        turn_event_callout_callout_request_model = TurnEventCalloutCalloutRequest.from_dict(turn_event_callout_callout_request_model_json)
        assert turn_event_callout_callout_request_model != False

        # Construct a model instance of TurnEventCalloutCalloutRequest by calling from_dict on the json representation
        turn_event_callout_callout_request_model_dict = TurnEventCalloutCalloutRequest.from_dict(turn_event_callout_callout_request_model_json).__dict__
        turn_event_callout_callout_request_model2 = TurnEventCalloutCalloutRequest(**turn_event_callout_callout_request_model_dict)

        # Verify the model instances are equivalent
        assert turn_event_callout_callout_request_model == turn_event_callout_callout_request_model2

        # Convert model instance back to dict and verify no loss of data
        turn_event_callout_callout_request_model_json2 = turn_event_callout_callout_request_model.to_dict()
        assert turn_event_callout_callout_request_model_json2 == turn_event_callout_callout_request_model_json


class TestModel_TurnEventCalloutCalloutResponse:
    """
    Test Class for TurnEventCalloutCalloutResponse
    """

    def test_turn_event_callout_callout_response_serialization(self):
        """
        Test serialization/deserialization for TurnEventCalloutCalloutResponse
        """

        # Construct a json representation of a TurnEventCalloutCalloutResponse model
        turn_event_callout_callout_response_model_json = {}
        turn_event_callout_callout_response_model_json['body'] = 'testString'
        turn_event_callout_callout_response_model_json['status_code'] = 38
        turn_event_callout_callout_response_model_json['last_event'] = {'anyKey': 'anyValue'}

        # Construct a model instance of TurnEventCalloutCalloutResponse by calling from_dict on the json representation
        turn_event_callout_callout_response_model = TurnEventCalloutCalloutResponse.from_dict(turn_event_callout_callout_response_model_json)
        assert turn_event_callout_callout_response_model != False

        # Construct a model instance of TurnEventCalloutCalloutResponse by calling from_dict on the json representation
        turn_event_callout_callout_response_model_dict = TurnEventCalloutCalloutResponse.from_dict(turn_event_callout_callout_response_model_json).__dict__
        turn_event_callout_callout_response_model2 = TurnEventCalloutCalloutResponse(**turn_event_callout_callout_response_model_dict)

        # Verify the model instances are equivalent
        assert turn_event_callout_callout_response_model == turn_event_callout_callout_response_model2

        # Convert model instance back to dict and verify no loss of data
        turn_event_callout_callout_response_model_json2 = turn_event_callout_callout_response_model.to_dict()
        assert turn_event_callout_callout_response_model_json2 == turn_event_callout_callout_response_model_json


class TestModel_TurnEventCalloutError:
    """
    Test Class for TurnEventCalloutError
    """

    def test_turn_event_callout_error_serialization(self):
        """
        Test serialization/deserialization for TurnEventCalloutError
        """

        # Construct a json representation of a TurnEventCalloutError model
        turn_event_callout_error_model_json = {}
        turn_event_callout_error_model_json['message'] = 'testString'

        # Construct a model instance of TurnEventCalloutError by calling from_dict on the json representation
        turn_event_callout_error_model = TurnEventCalloutError.from_dict(turn_event_callout_error_model_json)
        assert turn_event_callout_error_model != False

        # Construct a model instance of TurnEventCalloutError by calling from_dict on the json representation
        turn_event_callout_error_model_dict = TurnEventCalloutError.from_dict(turn_event_callout_error_model_json).__dict__
        turn_event_callout_error_model2 = TurnEventCalloutError(**turn_event_callout_error_model_dict)

        # Verify the model instances are equivalent
        assert turn_event_callout_error_model == turn_event_callout_error_model2

        # Convert model instance back to dict and verify no loss of data
        turn_event_callout_error_model_json2 = turn_event_callout_error_model.to_dict()
        assert turn_event_callout_error_model_json2 == turn_event_callout_error_model_json


class TestModel_TurnEventNodeSource:
    """
    Test Class for TurnEventNodeSource
    """

    def test_turn_event_node_source_serialization(self):
        """
        Test serialization/deserialization for TurnEventNodeSource
        """

        # Construct a json representation of a TurnEventNodeSource model
        turn_event_node_source_model_json = {}
        turn_event_node_source_model_json['type'] = 'dialog_node'
        turn_event_node_source_model_json['dialog_node'] = 'testString'
        turn_event_node_source_model_json['title'] = 'testString'
        turn_event_node_source_model_json['condition'] = 'testString'

        # Construct a model instance of TurnEventNodeSource by calling from_dict on the json representation
        turn_event_node_source_model = TurnEventNodeSource.from_dict(turn_event_node_source_model_json)
        assert turn_event_node_source_model != False

        # Construct a model instance of TurnEventNodeSource by calling from_dict on the json representation
        turn_event_node_source_model_dict = TurnEventNodeSource.from_dict(turn_event_node_source_model_json).__dict__
        turn_event_node_source_model2 = TurnEventNodeSource(**turn_event_node_source_model_dict)

        # Verify the model instances are equivalent
        assert turn_event_node_source_model == turn_event_node_source_model2

        # Convert model instance back to dict and verify no loss of data
        turn_event_node_source_model_json2 = turn_event_node_source_model.to_dict()
        assert turn_event_node_source_model_json2 == turn_event_node_source_model_json


class TestModel_TurnEventSearchError:
    """
    Test Class for TurnEventSearchError
    """

    def test_turn_event_search_error_serialization(self):
        """
        Test serialization/deserialization for TurnEventSearchError
        """

        # Construct a json representation of a TurnEventSearchError model
        turn_event_search_error_model_json = {}
        turn_event_search_error_model_json['message'] = 'testString'

        # Construct a model instance of TurnEventSearchError by calling from_dict on the json representation
        turn_event_search_error_model = TurnEventSearchError.from_dict(turn_event_search_error_model_json)
        assert turn_event_search_error_model != False

        # Construct a model instance of TurnEventSearchError by calling from_dict on the json representation
        turn_event_search_error_model_dict = TurnEventSearchError.from_dict(turn_event_search_error_model_json).__dict__
        turn_event_search_error_model2 = TurnEventSearchError(**turn_event_search_error_model_dict)

        # Verify the model instances are equivalent
        assert turn_event_search_error_model == turn_event_search_error_model2

        # Convert model instance back to dict and verify no loss of data
        turn_event_search_error_model_json2 = turn_event_search_error_model.to_dict()
        assert turn_event_search_error_model_json2 == turn_event_search_error_model_json


class TestModel_UpdateEnvironmentOrchestration:
    """
    Test Class for UpdateEnvironmentOrchestration
    """

    def test_update_environment_orchestration_serialization(self):
        """
        Test serialization/deserialization for UpdateEnvironmentOrchestration
        """

        # Construct a json representation of a UpdateEnvironmentOrchestration model
        update_environment_orchestration_model_json = {}
        update_environment_orchestration_model_json['search_skill_fallback'] = True

        # Construct a model instance of UpdateEnvironmentOrchestration by calling from_dict on the json representation
        update_environment_orchestration_model = UpdateEnvironmentOrchestration.from_dict(update_environment_orchestration_model_json)
        assert update_environment_orchestration_model != False

        # Construct a model instance of UpdateEnvironmentOrchestration by calling from_dict on the json representation
        update_environment_orchestration_model_dict = UpdateEnvironmentOrchestration.from_dict(update_environment_orchestration_model_json).__dict__
        update_environment_orchestration_model2 = UpdateEnvironmentOrchestration(**update_environment_orchestration_model_dict)

        # Verify the model instances are equivalent
        assert update_environment_orchestration_model == update_environment_orchestration_model2

        # Convert model instance back to dict and verify no loss of data
        update_environment_orchestration_model_json2 = update_environment_orchestration_model.to_dict()
        assert update_environment_orchestration_model_json2 == update_environment_orchestration_model_json


class TestModel_UpdateEnvironmentReleaseReference:
    """
    Test Class for UpdateEnvironmentReleaseReference
    """

    def test_update_environment_release_reference_serialization(self):
        """
        Test serialization/deserialization for UpdateEnvironmentReleaseReference
        """

        # Construct a json representation of a UpdateEnvironmentReleaseReference model
        update_environment_release_reference_model_json = {}
        update_environment_release_reference_model_json['release'] = 'testString'

        # Construct a model instance of UpdateEnvironmentReleaseReference by calling from_dict on the json representation
        update_environment_release_reference_model = UpdateEnvironmentReleaseReference.from_dict(update_environment_release_reference_model_json)
        assert update_environment_release_reference_model != False

        # Construct a model instance of UpdateEnvironmentReleaseReference by calling from_dict on the json representation
        update_environment_release_reference_model_dict = UpdateEnvironmentReleaseReference.from_dict(update_environment_release_reference_model_json).__dict__
        update_environment_release_reference_model2 = UpdateEnvironmentReleaseReference(**update_environment_release_reference_model_dict)

        # Verify the model instances are equivalent
        assert update_environment_release_reference_model == update_environment_release_reference_model2

        # Convert model instance back to dict and verify no loss of data
        update_environment_release_reference_model_json2 = update_environment_release_reference_model.to_dict()
        assert update_environment_release_reference_model_json2 == update_environment_release_reference_model_json


class TestModel_CompleteItem:
    """
    Test Class for CompleteItem
    """

    def test_complete_item_serialization(self):
        """
        Test serialization/deserialization for CompleteItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metadata_model = {}  # Metadata
        metadata_model['id'] = 38

        # Construct a json representation of a CompleteItem model
        complete_item_model_json = {}
        complete_item_model_json['streaming_metadata'] = metadata_model

        # Construct a model instance of CompleteItem by calling from_dict on the json representation
        complete_item_model = CompleteItem.from_dict(complete_item_model_json)
        assert complete_item_model != False

        # Construct a model instance of CompleteItem by calling from_dict on the json representation
        complete_item_model_dict = CompleteItem.from_dict(complete_item_model_json).__dict__
        complete_item_model2 = CompleteItem(**complete_item_model_dict)

        # Verify the model instances are equivalent
        assert complete_item_model == complete_item_model2

        # Convert model instance back to dict and verify no loss of data
        complete_item_model_json2 = complete_item_model.to_dict()
        assert complete_item_model_json2 == complete_item_model_json


class TestModel_LogMessageSourceAction:
    """
    Test Class for LogMessageSourceAction
    """

    def test_log_message_source_action_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceAction
        """

        # Construct a json representation of a LogMessageSourceAction model
        log_message_source_action_model_json = {}
        log_message_source_action_model_json['type'] = 'action'
        log_message_source_action_model_json['action'] = 'testString'

        # Construct a model instance of LogMessageSourceAction by calling from_dict on the json representation
        log_message_source_action_model = LogMessageSourceAction.from_dict(log_message_source_action_model_json)
        assert log_message_source_action_model != False

        # Construct a model instance of LogMessageSourceAction by calling from_dict on the json representation
        log_message_source_action_model_dict = LogMessageSourceAction.from_dict(log_message_source_action_model_json).__dict__
        log_message_source_action_model2 = LogMessageSourceAction(**log_message_source_action_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_action_model == log_message_source_action_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_action_model_json2 = log_message_source_action_model.to_dict()
        assert log_message_source_action_model_json2 == log_message_source_action_model_json


class TestModel_LogMessageSourceDialogNode:
    """
    Test Class for LogMessageSourceDialogNode
    """

    def test_log_message_source_dialog_node_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceDialogNode
        """

        # Construct a json representation of a LogMessageSourceDialogNode model
        log_message_source_dialog_node_model_json = {}
        log_message_source_dialog_node_model_json['type'] = 'dialog_node'
        log_message_source_dialog_node_model_json['dialog_node'] = 'testString'

        # Construct a model instance of LogMessageSourceDialogNode by calling from_dict on the json representation
        log_message_source_dialog_node_model = LogMessageSourceDialogNode.from_dict(log_message_source_dialog_node_model_json)
        assert log_message_source_dialog_node_model != False

        # Construct a model instance of LogMessageSourceDialogNode by calling from_dict on the json representation
        log_message_source_dialog_node_model_dict = LogMessageSourceDialogNode.from_dict(log_message_source_dialog_node_model_json).__dict__
        log_message_source_dialog_node_model2 = LogMessageSourceDialogNode(**log_message_source_dialog_node_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_dialog_node_model == log_message_source_dialog_node_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_dialog_node_model_json2 = log_message_source_dialog_node_model.to_dict()
        assert log_message_source_dialog_node_model_json2 == log_message_source_dialog_node_model_json


class TestModel_LogMessageSourceHandler:
    """
    Test Class for LogMessageSourceHandler
    """

    def test_log_message_source_handler_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceHandler
        """

        # Construct a json representation of a LogMessageSourceHandler model
        log_message_source_handler_model_json = {}
        log_message_source_handler_model_json['type'] = 'handler'
        log_message_source_handler_model_json['action'] = 'testString'
        log_message_source_handler_model_json['step'] = 'testString'
        log_message_source_handler_model_json['handler'] = 'testString'

        # Construct a model instance of LogMessageSourceHandler by calling from_dict on the json representation
        log_message_source_handler_model = LogMessageSourceHandler.from_dict(log_message_source_handler_model_json)
        assert log_message_source_handler_model != False

        # Construct a model instance of LogMessageSourceHandler by calling from_dict on the json representation
        log_message_source_handler_model_dict = LogMessageSourceHandler.from_dict(log_message_source_handler_model_json).__dict__
        log_message_source_handler_model2 = LogMessageSourceHandler(**log_message_source_handler_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_handler_model == log_message_source_handler_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_handler_model_json2 = log_message_source_handler_model.to_dict()
        assert log_message_source_handler_model_json2 == log_message_source_handler_model_json


class TestModel_LogMessageSourceStep:
    """
    Test Class for LogMessageSourceStep
    """

    def test_log_message_source_step_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceStep
        """

        # Construct a json representation of a LogMessageSourceStep model
        log_message_source_step_model_json = {}
        log_message_source_step_model_json['type'] = 'step'
        log_message_source_step_model_json['action'] = 'testString'
        log_message_source_step_model_json['step'] = 'testString'

        # Construct a model instance of LogMessageSourceStep by calling from_dict on the json representation
        log_message_source_step_model = LogMessageSourceStep.from_dict(log_message_source_step_model_json)
        assert log_message_source_step_model != False

        # Construct a model instance of LogMessageSourceStep by calling from_dict on the json representation
        log_message_source_step_model_dict = LogMessageSourceStep.from_dict(log_message_source_step_model_json).__dict__
        log_message_source_step_model2 = LogMessageSourceStep(**log_message_source_step_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_step_model == log_message_source_step_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_step_model_json2 = log_message_source_step_model.to_dict()
        assert log_message_source_step_model_json2 == log_message_source_step_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventActionFinished:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventActionFinished
    """

    def test_message_output_debug_turn_event_turn_event_action_finished_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventActionFinished
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventActionFinished model
        message_output_debug_turn_event_turn_event_action_finished_model_json = {}
        message_output_debug_turn_event_turn_event_action_finished_model_json['event'] = 'action_finished'
        message_output_debug_turn_event_turn_event_action_finished_model_json['source'] = turn_event_action_source_model
        message_output_debug_turn_event_turn_event_action_finished_model_json['action_start_time'] = 'testString'
        message_output_debug_turn_event_turn_event_action_finished_model_json['condition_type'] = 'user_defined'
        message_output_debug_turn_event_turn_event_action_finished_model_json['reason'] = 'all_steps_done'
        message_output_debug_turn_event_turn_event_action_finished_model_json['action_variables'] = {'anyKey': 'anyValue'}

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventActionFinished by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_action_finished_model = MessageOutputDebugTurnEventTurnEventActionFinished.from_dict(message_output_debug_turn_event_turn_event_action_finished_model_json)
        assert message_output_debug_turn_event_turn_event_action_finished_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventActionFinished by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_action_finished_model_dict = MessageOutputDebugTurnEventTurnEventActionFinished.from_dict(message_output_debug_turn_event_turn_event_action_finished_model_json).__dict__
        message_output_debug_turn_event_turn_event_action_finished_model2 = MessageOutputDebugTurnEventTurnEventActionFinished(**message_output_debug_turn_event_turn_event_action_finished_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_action_finished_model == message_output_debug_turn_event_turn_event_action_finished_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_action_finished_model_json2 = message_output_debug_turn_event_turn_event_action_finished_model.to_dict()
        assert message_output_debug_turn_event_turn_event_action_finished_model_json2 == message_output_debug_turn_event_turn_event_action_finished_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventActionVisited:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventActionVisited
    """

    def test_message_output_debug_turn_event_turn_event_action_visited_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventActionVisited
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventActionVisited model
        message_output_debug_turn_event_turn_event_action_visited_model_json = {}
        message_output_debug_turn_event_turn_event_action_visited_model_json['event'] = 'action_visited'
        message_output_debug_turn_event_turn_event_action_visited_model_json['source'] = turn_event_action_source_model
        message_output_debug_turn_event_turn_event_action_visited_model_json['action_start_time'] = 'testString'
        message_output_debug_turn_event_turn_event_action_visited_model_json['condition_type'] = 'user_defined'
        message_output_debug_turn_event_turn_event_action_visited_model_json['reason'] = 'intent'
        message_output_debug_turn_event_turn_event_action_visited_model_json['result_variable'] = 'testString'

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventActionVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_action_visited_model = MessageOutputDebugTurnEventTurnEventActionVisited.from_dict(message_output_debug_turn_event_turn_event_action_visited_model_json)
        assert message_output_debug_turn_event_turn_event_action_visited_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventActionVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_action_visited_model_dict = MessageOutputDebugTurnEventTurnEventActionVisited.from_dict(message_output_debug_turn_event_turn_event_action_visited_model_json).__dict__
        message_output_debug_turn_event_turn_event_action_visited_model2 = MessageOutputDebugTurnEventTurnEventActionVisited(**message_output_debug_turn_event_turn_event_action_visited_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_action_visited_model == message_output_debug_turn_event_turn_event_action_visited_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_action_visited_model_json2 = message_output_debug_turn_event_turn_event_action_visited_model.to_dict()
        assert message_output_debug_turn_event_turn_event_action_visited_model_json2 == message_output_debug_turn_event_turn_event_action_visited_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventCallout:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventCallout
    """

    def test_message_output_debug_turn_event_turn_event_callout_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventCallout
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        turn_event_callout_callout_request_model = {}  # TurnEventCalloutCalloutRequest
        turn_event_callout_callout_request_model['method'] = 'get'
        turn_event_callout_callout_request_model['url'] = 'testString'
        turn_event_callout_callout_request_model['path'] = 'testString'
        turn_event_callout_callout_request_model['query_parameters'] = 'testString'
        turn_event_callout_callout_request_model['headers'] = {'anyKey': 'anyValue'}
        turn_event_callout_callout_request_model['body'] = {'anyKey': 'anyValue'}

        turn_event_callout_callout_response_model = {}  # TurnEventCalloutCalloutResponse
        turn_event_callout_callout_response_model['body'] = 'testString'
        turn_event_callout_callout_response_model['status_code'] = 38
        turn_event_callout_callout_response_model['last_event'] = {'anyKey': 'anyValue'}

        turn_event_callout_callout_model = {}  # TurnEventCalloutCallout
        turn_event_callout_callout_model['type'] = 'integration_interaction'
        turn_event_callout_callout_model['internal'] = {'anyKey': 'anyValue'}
        turn_event_callout_callout_model['result_variable'] = 'testString'
        turn_event_callout_callout_model['request'] = turn_event_callout_callout_request_model
        turn_event_callout_callout_model['response'] = turn_event_callout_callout_response_model

        turn_event_callout_error_model = {}  # TurnEventCalloutError
        turn_event_callout_error_model['message'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventCallout model
        message_output_debug_turn_event_turn_event_callout_model_json = {}
        message_output_debug_turn_event_turn_event_callout_model_json['event'] = 'callout'
        message_output_debug_turn_event_turn_event_callout_model_json['source'] = turn_event_action_source_model
        message_output_debug_turn_event_turn_event_callout_model_json['callout'] = turn_event_callout_callout_model
        message_output_debug_turn_event_turn_event_callout_model_json['error'] = turn_event_callout_error_model

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventCallout by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_callout_model = MessageOutputDebugTurnEventTurnEventCallout.from_dict(message_output_debug_turn_event_turn_event_callout_model_json)
        assert message_output_debug_turn_event_turn_event_callout_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventCallout by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_callout_model_dict = MessageOutputDebugTurnEventTurnEventCallout.from_dict(message_output_debug_turn_event_turn_event_callout_model_json).__dict__
        message_output_debug_turn_event_turn_event_callout_model2 = MessageOutputDebugTurnEventTurnEventCallout(**message_output_debug_turn_event_turn_event_callout_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_callout_model == message_output_debug_turn_event_turn_event_callout_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_callout_model_json2 = message_output_debug_turn_event_turn_event_callout_model.to_dict()
        assert message_output_debug_turn_event_turn_event_callout_model_json2 == message_output_debug_turn_event_turn_event_callout_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventHandlerVisited:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventHandlerVisited
    """

    def test_message_output_debug_turn_event_turn_event_handler_visited_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventHandlerVisited
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventHandlerVisited model
        message_output_debug_turn_event_turn_event_handler_visited_model_json = {}
        message_output_debug_turn_event_turn_event_handler_visited_model_json['event'] = 'handler_visited'
        message_output_debug_turn_event_turn_event_handler_visited_model_json['source'] = turn_event_action_source_model
        message_output_debug_turn_event_turn_event_handler_visited_model_json['action_start_time'] = 'testString'

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventHandlerVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_handler_visited_model = MessageOutputDebugTurnEventTurnEventHandlerVisited.from_dict(message_output_debug_turn_event_turn_event_handler_visited_model_json)
        assert message_output_debug_turn_event_turn_event_handler_visited_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventHandlerVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_handler_visited_model_dict = MessageOutputDebugTurnEventTurnEventHandlerVisited.from_dict(message_output_debug_turn_event_turn_event_handler_visited_model_json).__dict__
        message_output_debug_turn_event_turn_event_handler_visited_model2 = MessageOutputDebugTurnEventTurnEventHandlerVisited(**message_output_debug_turn_event_turn_event_handler_visited_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_handler_visited_model == message_output_debug_turn_event_turn_event_handler_visited_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_handler_visited_model_json2 = message_output_debug_turn_event_turn_event_handler_visited_model.to_dict()
        assert message_output_debug_turn_event_turn_event_handler_visited_model_json2 == message_output_debug_turn_event_turn_event_handler_visited_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventNodeVisited:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventNodeVisited
    """

    def test_message_output_debug_turn_event_turn_event_node_visited_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventNodeVisited
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_node_source_model = {}  # TurnEventNodeSource
        turn_event_node_source_model['type'] = 'dialog_node'
        turn_event_node_source_model['dialog_node'] = 'testString'
        turn_event_node_source_model['title'] = 'testString'
        turn_event_node_source_model['condition'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventNodeVisited model
        message_output_debug_turn_event_turn_event_node_visited_model_json = {}
        message_output_debug_turn_event_turn_event_node_visited_model_json['event'] = 'node_visited'
        message_output_debug_turn_event_turn_event_node_visited_model_json['source'] = turn_event_node_source_model
        message_output_debug_turn_event_turn_event_node_visited_model_json['reason'] = 'welcome'

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventNodeVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_node_visited_model = MessageOutputDebugTurnEventTurnEventNodeVisited.from_dict(message_output_debug_turn_event_turn_event_node_visited_model_json)
        assert message_output_debug_turn_event_turn_event_node_visited_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventNodeVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_node_visited_model_dict = MessageOutputDebugTurnEventTurnEventNodeVisited.from_dict(message_output_debug_turn_event_turn_event_node_visited_model_json).__dict__
        message_output_debug_turn_event_turn_event_node_visited_model2 = MessageOutputDebugTurnEventTurnEventNodeVisited(**message_output_debug_turn_event_turn_event_node_visited_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_node_visited_model == message_output_debug_turn_event_turn_event_node_visited_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_node_visited_model_json2 = message_output_debug_turn_event_turn_event_node_visited_model.to_dict()
        assert message_output_debug_turn_event_turn_event_node_visited_model_json2 == message_output_debug_turn_event_turn_event_node_visited_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventSearch:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventSearch
    """

    def test_message_output_debug_turn_event_turn_event_search_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventSearch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        turn_event_search_error_model = {}  # TurnEventSearchError
        turn_event_search_error_model['message'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventSearch model
        message_output_debug_turn_event_turn_event_search_model_json = {}
        message_output_debug_turn_event_turn_event_search_model_json['event'] = 'search'
        message_output_debug_turn_event_turn_event_search_model_json['source'] = turn_event_action_source_model
        message_output_debug_turn_event_turn_event_search_model_json['error'] = turn_event_search_error_model

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventSearch by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_search_model = MessageOutputDebugTurnEventTurnEventSearch.from_dict(message_output_debug_turn_event_turn_event_search_model_json)
        assert message_output_debug_turn_event_turn_event_search_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventSearch by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_search_model_dict = MessageOutputDebugTurnEventTurnEventSearch.from_dict(message_output_debug_turn_event_turn_event_search_model_json).__dict__
        message_output_debug_turn_event_turn_event_search_model2 = MessageOutputDebugTurnEventTurnEventSearch(**message_output_debug_turn_event_turn_event_search_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_search_model == message_output_debug_turn_event_turn_event_search_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_search_model_json2 = message_output_debug_turn_event_turn_event_search_model.to_dict()
        assert message_output_debug_turn_event_turn_event_search_model_json2 == message_output_debug_turn_event_turn_event_search_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventStepAnswered:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventStepAnswered
    """

    def test_message_output_debug_turn_event_turn_event_step_answered_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventStepAnswered
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventStepAnswered model
        message_output_debug_turn_event_turn_event_step_answered_model_json = {}
        message_output_debug_turn_event_turn_event_step_answered_model_json['event'] = 'step_answered'
        message_output_debug_turn_event_turn_event_step_answered_model_json['source'] = turn_event_action_source_model
        message_output_debug_turn_event_turn_event_step_answered_model_json['condition_type'] = 'user_defined'
        message_output_debug_turn_event_turn_event_step_answered_model_json['action_start_time'] = 'testString'
        message_output_debug_turn_event_turn_event_step_answered_model_json['prompted'] = True

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventStepAnswered by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_step_answered_model = MessageOutputDebugTurnEventTurnEventStepAnswered.from_dict(message_output_debug_turn_event_turn_event_step_answered_model_json)
        assert message_output_debug_turn_event_turn_event_step_answered_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventStepAnswered by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_step_answered_model_dict = MessageOutputDebugTurnEventTurnEventStepAnswered.from_dict(message_output_debug_turn_event_turn_event_step_answered_model_json).__dict__
        message_output_debug_turn_event_turn_event_step_answered_model2 = MessageOutputDebugTurnEventTurnEventStepAnswered(**message_output_debug_turn_event_turn_event_step_answered_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_step_answered_model == message_output_debug_turn_event_turn_event_step_answered_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_step_answered_model_json2 = message_output_debug_turn_event_turn_event_step_answered_model.to_dict()
        assert message_output_debug_turn_event_turn_event_step_answered_model_json2 == message_output_debug_turn_event_turn_event_step_answered_model_json


class TestModel_MessageOutputDebugTurnEventTurnEventStepVisited:
    """
    Test Class for MessageOutputDebugTurnEventTurnEventStepVisited
    """

    def test_message_output_debug_turn_event_turn_event_step_visited_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebugTurnEventTurnEventStepVisited
        """

        # Construct dict forms of any model objects needed in order to build this model.

        turn_event_action_source_model = {}  # TurnEventActionSource
        turn_event_action_source_model['type'] = 'action'
        turn_event_action_source_model['action'] = 'testString'
        turn_event_action_source_model['action_title'] = 'testString'
        turn_event_action_source_model['condition'] = 'testString'

        # Construct a json representation of a MessageOutputDebugTurnEventTurnEventStepVisited model
        message_output_debug_turn_event_turn_event_step_visited_model_json = {}
        message_output_debug_turn_event_turn_event_step_visited_model_json['event'] = 'step_visited'
        message_output_debug_turn_event_turn_event_step_visited_model_json['source'] = turn_event_action_source_model
        message_output_debug_turn_event_turn_event_step_visited_model_json['condition_type'] = 'user_defined'
        message_output_debug_turn_event_turn_event_step_visited_model_json['action_start_time'] = 'testString'
        message_output_debug_turn_event_turn_event_step_visited_model_json['has_question'] = True

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventStepVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_step_visited_model = MessageOutputDebugTurnEventTurnEventStepVisited.from_dict(message_output_debug_turn_event_turn_event_step_visited_model_json)
        assert message_output_debug_turn_event_turn_event_step_visited_model != False

        # Construct a model instance of MessageOutputDebugTurnEventTurnEventStepVisited by calling from_dict on the json representation
        message_output_debug_turn_event_turn_event_step_visited_model_dict = MessageOutputDebugTurnEventTurnEventStepVisited.from_dict(message_output_debug_turn_event_turn_event_step_visited_model_json).__dict__
        message_output_debug_turn_event_turn_event_step_visited_model2 = MessageOutputDebugTurnEventTurnEventStepVisited(**message_output_debug_turn_event_turn_event_step_visited_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_turn_event_turn_event_step_visited_model == message_output_debug_turn_event_turn_event_step_visited_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_turn_event_turn_event_step_visited_model_json2 = message_output_debug_turn_event_turn_event_step_visited_model.to_dict()
        assert message_output_debug_turn_event_turn_event_step_visited_model_json2 == message_output_debug_turn_event_turn_event_step_visited_model_json


class TestModel_ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode:
    """
    Test Class for ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode
    """

    def test_provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_serialization(self):
        """
        Test serialization/deserialization for ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode
        """

        # Construct a json representation of a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode model
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json = {}
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json['authorization_url'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json['redirect_uri'] = 'testString'

        # Construct a model instance of ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode by calling from_dict on the json representation
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode.from_dict(provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json)
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model != False

        # Construct a model instance of ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode by calling from_dict on the json representation
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_dict = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode.from_dict(provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json).__dict__
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model2 = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode(**provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_dict)

        # Verify the model instances are equivalent
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model == provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model2

        # Convert model instance back to dict and verify no loss of data
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json2 = provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model.to_dict()
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json2 == provider_authentication_o_auth2_flows_provider_authentication_o_auth2_authorization_code_model_json


class TestModel_ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials:
    """
    Test Class for ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials
    """

    def test_provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_serialization(self):
        """
        Test serialization/deserialization for ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials
        """

        # Construct a json representation of a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials model
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json = {}
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json['header_prefix'] = 'testString'

        # Construct a model instance of ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials by calling from_dict on the json representation
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials.from_dict(provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json)
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model != False

        # Construct a model instance of ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials by calling from_dict on the json representation
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_dict = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials.from_dict(provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json).__dict__
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model2 = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials(**provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_dict)

        # Verify the model instances are equivalent
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model == provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model2

        # Convert model instance back to dict and verify no loss of data
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json2 = provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model.to_dict()
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json2 == provider_authentication_o_auth2_flows_provider_authentication_o_auth2_client_credentials_model_json


class TestModel_ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password:
    """
    Test Class for ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
    """

    def test_provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_serialization(self):
        """
        Test serialization/deserialization for ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_o_auth2_password_username_model = {}  # ProviderAuthenticationOAuth2PasswordUsername
        provider_authentication_o_auth2_password_username_model['type'] = 'value'
        provider_authentication_o_auth2_password_username_model['value'] = 'testString'

        # Construct a json representation of a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password model
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json = {}
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json['token_url'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json['refresh_url'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json['client_auth_type'] = 'Body'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json['content_type'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json['header_prefix'] = 'testString'
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json['username'] = provider_authentication_o_auth2_password_username_model

        # Construct a model instance of ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password by calling from_dict on the json representation
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password.from_dict(provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json)
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model != False

        # Construct a model instance of ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password by calling from_dict on the json representation
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_dict = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password.from_dict(provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json).__dict__
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model2 = ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password(**provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_dict)

        # Verify the model instances are equivalent
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model == provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model2

        # Convert model instance back to dict and verify no loss of data
        provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json2 = provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model.to_dict()
        assert provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json2 == provider_authentication_o_auth2_flows_provider_authentication_o_auth2_password_model_json


class TestModel_ProviderPrivateAuthenticationBasicFlow:
    """
    Test Class for ProviderPrivateAuthenticationBasicFlow
    """

    def test_provider_private_authentication_basic_flow_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivateAuthenticationBasicFlow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a json representation of a ProviderPrivateAuthenticationBasicFlow model
        provider_private_authentication_basic_flow_model_json = {}
        provider_private_authentication_basic_flow_model_json['password'] = provider_authentication_type_and_value_model

        # Construct a model instance of ProviderPrivateAuthenticationBasicFlow by calling from_dict on the json representation
        provider_private_authentication_basic_flow_model = ProviderPrivateAuthenticationBasicFlow.from_dict(provider_private_authentication_basic_flow_model_json)
        assert provider_private_authentication_basic_flow_model != False

        # Construct a model instance of ProviderPrivateAuthenticationBasicFlow by calling from_dict on the json representation
        provider_private_authentication_basic_flow_model_dict = ProviderPrivateAuthenticationBasicFlow.from_dict(provider_private_authentication_basic_flow_model_json).__dict__
        provider_private_authentication_basic_flow_model2 = ProviderPrivateAuthenticationBasicFlow(**provider_private_authentication_basic_flow_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_authentication_basic_flow_model == provider_private_authentication_basic_flow_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_authentication_basic_flow_model_json2 = provider_private_authentication_basic_flow_model.to_dict()
        assert provider_private_authentication_basic_flow_model_json2 == provider_private_authentication_basic_flow_model_json


class TestModel_ProviderPrivateAuthenticationBearerFlow:
    """
    Test Class for ProviderPrivateAuthenticationBearerFlow
    """

    def test_provider_private_authentication_bearer_flow_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivateAuthenticationBearerFlow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_authentication_type_and_value_model = {}  # ProviderAuthenticationTypeAndValue
        provider_authentication_type_and_value_model['type'] = 'value'
        provider_authentication_type_and_value_model['value'] = 'testString'

        # Construct a json representation of a ProviderPrivateAuthenticationBearerFlow model
        provider_private_authentication_bearer_flow_model_json = {}
        provider_private_authentication_bearer_flow_model_json['token'] = provider_authentication_type_and_value_model

        # Construct a model instance of ProviderPrivateAuthenticationBearerFlow by calling from_dict on the json representation
        provider_private_authentication_bearer_flow_model = ProviderPrivateAuthenticationBearerFlow.from_dict(provider_private_authentication_bearer_flow_model_json)
        assert provider_private_authentication_bearer_flow_model != False

        # Construct a model instance of ProviderPrivateAuthenticationBearerFlow by calling from_dict on the json representation
        provider_private_authentication_bearer_flow_model_dict = ProviderPrivateAuthenticationBearerFlow.from_dict(provider_private_authentication_bearer_flow_model_json).__dict__
        provider_private_authentication_bearer_flow_model2 = ProviderPrivateAuthenticationBearerFlow(**provider_private_authentication_bearer_flow_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_authentication_bearer_flow_model == provider_private_authentication_bearer_flow_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_authentication_bearer_flow_model_json2 = provider_private_authentication_bearer_flow_model.to_dict()
        assert provider_private_authentication_bearer_flow_model_json2 == provider_private_authentication_bearer_flow_model_json


class TestModel_ProviderPrivateAuthenticationOAuth2Flow:
    """
    Test Class for ProviderPrivateAuthenticationOAuth2Flow
    """

    def test_provider_private_authentication_o_auth2_flow_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivateAuthenticationOAuth2Flow
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_private_authentication_o_auth2_password_password_model = {}  # ProviderPrivateAuthenticationOAuth2PasswordPassword
        provider_private_authentication_o_auth2_password_password_model['type'] = 'value'
        provider_private_authentication_o_auth2_password_password_model['value'] = 'testString'

        provider_private_authentication_o_auth2_flow_flows_model = {}  # ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password
        provider_private_authentication_o_auth2_flow_flows_model['client_id'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_model['client_secret'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_model['access_token'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_model['refresh_token'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_model['password'] = provider_private_authentication_o_auth2_password_password_model

        # Construct a json representation of a ProviderPrivateAuthenticationOAuth2Flow model
        provider_private_authentication_o_auth2_flow_model_json = {}
        provider_private_authentication_o_auth2_flow_model_json['flows'] = provider_private_authentication_o_auth2_flow_flows_model

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2Flow by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_model = ProviderPrivateAuthenticationOAuth2Flow.from_dict(provider_private_authentication_o_auth2_flow_model_json)
        assert provider_private_authentication_o_auth2_flow_model != False

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2Flow by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_model_dict = ProviderPrivateAuthenticationOAuth2Flow.from_dict(provider_private_authentication_o_auth2_flow_model_json).__dict__
        provider_private_authentication_o_auth2_flow_model2 = ProviderPrivateAuthenticationOAuth2Flow(**provider_private_authentication_o_auth2_flow_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_authentication_o_auth2_flow_model == provider_private_authentication_o_auth2_flow_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_authentication_o_auth2_flow_model_json2 = provider_private_authentication_o_auth2_flow_model.to_dict()
        assert provider_private_authentication_o_auth2_flow_model_json2 == provider_private_authentication_o_auth2_flow_model_json


class TestModel_ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode:
    """
    Test Class for ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode
    """

    def test_provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode
        """

        # Construct a json representation of a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode model
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json = {}
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json['client_id'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json['client_secret'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json['access_token'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json['refresh_token'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json['authorization_code'] = 'testString'

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode.from_dict(provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json)
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model != False

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_dict = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode.from_dict(provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json).__dict__
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model2 = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode(**provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model == provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json2 = provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model.to_dict()
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json2 == provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_authorization_code_model_json


class TestModel_ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials:
    """
    Test Class for ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials
    """

    def test_provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials
        """

        # Construct a json representation of a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials model
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json = {}
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json['client_id'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json['client_secret'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json['access_token'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json['refresh_token'] = 'testString'

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials.from_dict(provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json)
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model != False

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_dict = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials.from_dict(provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json).__dict__
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model2 = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials(**provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model == provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json2 = provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model.to_dict()
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json2 == provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_client_credentials_model_json


class TestModel_ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password:
    """
    Test Class for ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password
    """

    def test_provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_serialization(self):
        """
        Test serialization/deserialization for ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_private_authentication_o_auth2_password_password_model = {}  # ProviderPrivateAuthenticationOAuth2PasswordPassword
        provider_private_authentication_o_auth2_password_password_model['type'] = 'value'
        provider_private_authentication_o_auth2_password_password_model['value'] = 'testString'

        # Construct a json representation of a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password model
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json = {}
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json['client_id'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json['client_secret'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json['access_token'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json['refresh_token'] = 'testString'
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json['password'] = provider_private_authentication_o_auth2_password_password_model

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password.from_dict(provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json)
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model != False

        # Construct a model instance of ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password by calling from_dict on the json representation
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_dict = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password.from_dict(provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json).__dict__
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model2 = ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password(**provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_dict)

        # Verify the model instances are equivalent
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model == provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model2

        # Convert model instance back to dict and verify no loss of data
        provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json2 = provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model.to_dict()
        assert provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json2 == provider_private_authentication_o_auth2_flow_flows_provider_private_authentication_o_auth2_password_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeAudio:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeAudio
    """

    def test_runtime_response_generic_runtime_response_type_audio_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeAudio
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeAudio model
        runtime_response_generic_runtime_response_type_audio_model_json = {}
        runtime_response_generic_runtime_response_type_audio_model_json['response_type'] = 'audio'
        runtime_response_generic_runtime_response_type_audio_model_json['source'] = 'testString'
        runtime_response_generic_runtime_response_type_audio_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_audio_model_json['description'] = 'testString'
        runtime_response_generic_runtime_response_type_audio_model_json['channels'] = [response_generic_channel_model]
        runtime_response_generic_runtime_response_type_audio_model_json['channel_options'] = {'anyKey': 'anyValue'}
        runtime_response_generic_runtime_response_type_audio_model_json['alt_text'] = 'testString'

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeAudio by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_audio_model = RuntimeResponseGenericRuntimeResponseTypeAudio.from_dict(runtime_response_generic_runtime_response_type_audio_model_json)
        assert runtime_response_generic_runtime_response_type_audio_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeAudio by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_audio_model_dict = RuntimeResponseGenericRuntimeResponseTypeAudio.from_dict(runtime_response_generic_runtime_response_type_audio_model_json).__dict__
        runtime_response_generic_runtime_response_type_audio_model2 = RuntimeResponseGenericRuntimeResponseTypeAudio(**runtime_response_generic_runtime_response_type_audio_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_audio_model == runtime_response_generic_runtime_response_type_audio_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_audio_model_json2 = runtime_response_generic_runtime_response_type_audio_model.to_dict()
        assert runtime_response_generic_runtime_response_type_audio_model_json2 == runtime_response_generic_runtime_response_type_audio_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeChannelTransfer:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeChannelTransfer
    """

    def test_runtime_response_generic_runtime_response_type_channel_transfer_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeChannelTransfer
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {}  # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {}  # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {}  # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeChannelTransfer model
        runtime_response_generic_runtime_response_type_channel_transfer_model_json = {}
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['response_type'] = 'channel_transfer'
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['message_to_user'] = 'testString'
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['transfer_info'] = channel_transfer_info_model
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeChannelTransfer by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_channel_transfer_model = RuntimeResponseGenericRuntimeResponseTypeChannelTransfer.from_dict(runtime_response_generic_runtime_response_type_channel_transfer_model_json)
        assert runtime_response_generic_runtime_response_type_channel_transfer_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeChannelTransfer by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_channel_transfer_model_dict = RuntimeResponseGenericRuntimeResponseTypeChannelTransfer.from_dict(runtime_response_generic_runtime_response_type_channel_transfer_model_json).__dict__
        runtime_response_generic_runtime_response_type_channel_transfer_model2 = RuntimeResponseGenericRuntimeResponseTypeChannelTransfer(**runtime_response_generic_runtime_response_type_channel_transfer_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_channel_transfer_model == runtime_response_generic_runtime_response_type_channel_transfer_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_channel_transfer_model_json2 = runtime_response_generic_runtime_response_type_channel_transfer_model.to_dict()
        assert runtime_response_generic_runtime_response_type_channel_transfer_model_json2 == runtime_response_generic_runtime_response_type_channel_transfer_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeConnectToAgent:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeConnectToAgent
    """

    def test_runtime_response_generic_runtime_response_type_connect_to_agent_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeConnectToAgent
        """

        # Construct dict forms of any model objects needed in order to build this model.

        agent_availability_message_model = {}  # AgentAvailabilityMessage
        agent_availability_message_model['message'] = 'testString'

        dialog_node_output_connect_to_agent_transfer_info_model = {}  # DialogNodeOutputConnectToAgentTransferInfo
        dialog_node_output_connect_to_agent_transfer_info_model['target'] = {'key1': {'anyKey': 'anyValue'}}

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeConnectToAgent model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json = {}
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['response_type'] = 'connect_to_agent'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['message_to_human_agent'] = 'testString'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['agent_available'] = agent_availability_message_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['agent_unavailable'] = agent_availability_message_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['transfer_info'] = dialog_node_output_connect_to_agent_transfer_info_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['topic'] = 'testString'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeConnectToAgent by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_connect_to_agent_model = RuntimeResponseGenericRuntimeResponseTypeConnectToAgent.from_dict(runtime_response_generic_runtime_response_type_connect_to_agent_model_json)
        assert runtime_response_generic_runtime_response_type_connect_to_agent_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeConnectToAgent by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_connect_to_agent_model_dict = RuntimeResponseGenericRuntimeResponseTypeConnectToAgent.from_dict(runtime_response_generic_runtime_response_type_connect_to_agent_model_json).__dict__
        runtime_response_generic_runtime_response_type_connect_to_agent_model2 = RuntimeResponseGenericRuntimeResponseTypeConnectToAgent(**runtime_response_generic_runtime_response_type_connect_to_agent_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_connect_to_agent_model == runtime_response_generic_runtime_response_type_connect_to_agent_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json2 = runtime_response_generic_runtime_response_type_connect_to_agent_model.to_dict()
        assert runtime_response_generic_runtime_response_type_connect_to_agent_model_json2 == runtime_response_generic_runtime_response_type_connect_to_agent_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeDate:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeDate
    """

    def test_runtime_response_generic_runtime_response_type_date_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeDate
        """

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeDate model
        runtime_response_generic_runtime_response_type_date_model_json = {}
        runtime_response_generic_runtime_response_type_date_model_json['response_type'] = 'date'

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeDate by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_date_model = RuntimeResponseGenericRuntimeResponseTypeDate.from_dict(runtime_response_generic_runtime_response_type_date_model_json)
        assert runtime_response_generic_runtime_response_type_date_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeDate by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_date_model_dict = RuntimeResponseGenericRuntimeResponseTypeDate.from_dict(runtime_response_generic_runtime_response_type_date_model_json).__dict__
        runtime_response_generic_runtime_response_type_date_model2 = RuntimeResponseGenericRuntimeResponseTypeDate(**runtime_response_generic_runtime_response_type_date_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_date_model == runtime_response_generic_runtime_response_type_date_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_date_model_json2 = runtime_response_generic_runtime_response_type_date_model.to_dict()
        assert runtime_response_generic_runtime_response_type_date_model_json2 == runtime_response_generic_runtime_response_type_date_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeIframe:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeIframe
    """

    def test_runtime_response_generic_runtime_response_type_iframe_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeIframe
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeIframe model
        runtime_response_generic_runtime_response_type_iframe_model_json = {}
        runtime_response_generic_runtime_response_type_iframe_model_json['response_type'] = 'iframe'
        runtime_response_generic_runtime_response_type_iframe_model_json['source'] = 'testString'
        runtime_response_generic_runtime_response_type_iframe_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_iframe_model_json['description'] = 'testString'
        runtime_response_generic_runtime_response_type_iframe_model_json['image_url'] = 'testString'
        runtime_response_generic_runtime_response_type_iframe_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeIframe by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_iframe_model = RuntimeResponseGenericRuntimeResponseTypeIframe.from_dict(runtime_response_generic_runtime_response_type_iframe_model_json)
        assert runtime_response_generic_runtime_response_type_iframe_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeIframe by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_iframe_model_dict = RuntimeResponseGenericRuntimeResponseTypeIframe.from_dict(runtime_response_generic_runtime_response_type_iframe_model_json).__dict__
        runtime_response_generic_runtime_response_type_iframe_model2 = RuntimeResponseGenericRuntimeResponseTypeIframe(**runtime_response_generic_runtime_response_type_iframe_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_iframe_model == runtime_response_generic_runtime_response_type_iframe_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_iframe_model_json2 = runtime_response_generic_runtime_response_type_iframe_model.to_dict()
        assert runtime_response_generic_runtime_response_type_iframe_model_json2 == runtime_response_generic_runtime_response_type_iframe_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeImage:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeImage
    """

    def test_runtime_response_generic_runtime_response_type_image_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeImage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeImage model
        runtime_response_generic_runtime_response_type_image_model_json = {}
        runtime_response_generic_runtime_response_type_image_model_json['response_type'] = 'image'
        runtime_response_generic_runtime_response_type_image_model_json['source'] = 'testString'
        runtime_response_generic_runtime_response_type_image_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_image_model_json['description'] = 'testString'
        runtime_response_generic_runtime_response_type_image_model_json['channels'] = [response_generic_channel_model]
        runtime_response_generic_runtime_response_type_image_model_json['alt_text'] = 'testString'

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeImage by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_image_model = RuntimeResponseGenericRuntimeResponseTypeImage.from_dict(runtime_response_generic_runtime_response_type_image_model_json)
        assert runtime_response_generic_runtime_response_type_image_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeImage by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_image_model_dict = RuntimeResponseGenericRuntimeResponseTypeImage.from_dict(runtime_response_generic_runtime_response_type_image_model_json).__dict__
        runtime_response_generic_runtime_response_type_image_model2 = RuntimeResponseGenericRuntimeResponseTypeImage(**runtime_response_generic_runtime_response_type_image_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_image_model == runtime_response_generic_runtime_response_type_image_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_image_model_json2 = runtime_response_generic_runtime_response_type_image_model.to_dict()
        assert runtime_response_generic_runtime_response_type_image_model_json2 == runtime_response_generic_runtime_response_type_image_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeOption:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeOption
    """

    def test_runtime_response_generic_runtime_response_type_option_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeOption
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        dialog_node_output_options_element_value_model = {}  # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        dialog_node_output_options_element_model = {}  # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeOption model
        runtime_response_generic_runtime_response_type_option_model_json = {}
        runtime_response_generic_runtime_response_type_option_model_json['response_type'] = 'option'
        runtime_response_generic_runtime_response_type_option_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_option_model_json['description'] = 'testString'
        runtime_response_generic_runtime_response_type_option_model_json['preference'] = 'dropdown'
        runtime_response_generic_runtime_response_type_option_model_json['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_runtime_response_type_option_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeOption by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_option_model = RuntimeResponseGenericRuntimeResponseTypeOption.from_dict(runtime_response_generic_runtime_response_type_option_model_json)
        assert runtime_response_generic_runtime_response_type_option_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeOption by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_option_model_dict = RuntimeResponseGenericRuntimeResponseTypeOption.from_dict(runtime_response_generic_runtime_response_type_option_model_json).__dict__
        runtime_response_generic_runtime_response_type_option_model2 = RuntimeResponseGenericRuntimeResponseTypeOption(**runtime_response_generic_runtime_response_type_option_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_option_model == runtime_response_generic_runtime_response_type_option_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_option_model_json2 = runtime_response_generic_runtime_response_type_option_model.to_dict()
        assert runtime_response_generic_runtime_response_type_option_model_json2 == runtime_response_generic_runtime_response_type_option_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypePause:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypePause
    """

    def test_runtime_response_generic_runtime_response_type_pause_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypePause
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypePause model
        runtime_response_generic_runtime_response_type_pause_model_json = {}
        runtime_response_generic_runtime_response_type_pause_model_json['response_type'] = 'pause'
        runtime_response_generic_runtime_response_type_pause_model_json['time'] = 38
        runtime_response_generic_runtime_response_type_pause_model_json['typing'] = True
        runtime_response_generic_runtime_response_type_pause_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypePause by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_pause_model = RuntimeResponseGenericRuntimeResponseTypePause.from_dict(runtime_response_generic_runtime_response_type_pause_model_json)
        assert runtime_response_generic_runtime_response_type_pause_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypePause by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_pause_model_dict = RuntimeResponseGenericRuntimeResponseTypePause.from_dict(runtime_response_generic_runtime_response_type_pause_model_json).__dict__
        runtime_response_generic_runtime_response_type_pause_model2 = RuntimeResponseGenericRuntimeResponseTypePause(**runtime_response_generic_runtime_response_type_pause_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_pause_model == runtime_response_generic_runtime_response_type_pause_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_pause_model_json2 = runtime_response_generic_runtime_response_type_pause_model.to_dict()
        assert runtime_response_generic_runtime_response_type_pause_model_json2 == runtime_response_generic_runtime_response_type_pause_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeSearch:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeSearch
    """

    def test_runtime_response_generic_runtime_response_type_search_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeSearch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_result_metadata_model = {}  # SearchResultMetadata
        search_result_metadata_model['confidence'] = 72.5
        search_result_metadata_model['score'] = 72.5

        search_result_highlight_model = {}  # SearchResultHighlight
        search_result_highlight_model['body'] = ['testString']
        search_result_highlight_model['title'] = ['testString']
        search_result_highlight_model['url'] = ['testString']
        search_result_highlight_model['foo'] = ['testString']

        search_result_answer_model = {}  # SearchResultAnswer
        search_result_answer_model['text'] = 'testString'
        search_result_answer_model['confidence'] = 0

        search_result_model = {}  # SearchResult
        search_result_model['id'] = 'testString'
        search_result_model['result_metadata'] = search_result_metadata_model
        search_result_model['body'] = 'testString'
        search_result_model['title'] = 'testString'
        search_result_model['url'] = 'testString'
        search_result_model['highlight'] = search_result_highlight_model
        search_result_model['answers'] = [search_result_answer_model]

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeSearch model
        runtime_response_generic_runtime_response_type_search_model_json = {}
        runtime_response_generic_runtime_response_type_search_model_json['response_type'] = 'search'
        runtime_response_generic_runtime_response_type_search_model_json['header'] = 'testString'
        runtime_response_generic_runtime_response_type_search_model_json['primary_results'] = [search_result_model]
        runtime_response_generic_runtime_response_type_search_model_json['additional_results'] = [search_result_model]
        runtime_response_generic_runtime_response_type_search_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSearch by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_search_model = RuntimeResponseGenericRuntimeResponseTypeSearch.from_dict(runtime_response_generic_runtime_response_type_search_model_json)
        assert runtime_response_generic_runtime_response_type_search_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSearch by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_search_model_dict = RuntimeResponseGenericRuntimeResponseTypeSearch.from_dict(runtime_response_generic_runtime_response_type_search_model_json).__dict__
        runtime_response_generic_runtime_response_type_search_model2 = RuntimeResponseGenericRuntimeResponseTypeSearch(**runtime_response_generic_runtime_response_type_search_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_search_model == runtime_response_generic_runtime_response_type_search_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_search_model_json2 = runtime_response_generic_runtime_response_type_search_model.to_dict()
        assert runtime_response_generic_runtime_response_type_search_model_json2 == runtime_response_generic_runtime_response_type_search_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeSuggestion:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeSuggestion
    """

    def test_runtime_response_generic_runtime_response_type_suggestion_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeSuggestion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {}  # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5
        runtime_intent_model['skill'] = 'testString'

        capture_group_model = {}  # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {}  # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {}  # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {}  # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {}  # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model
        runtime_entity_model['skill'] = 'testString'

        message_input_attachment_model = {}  # MessageInputAttachment
        message_input_attachment_model['url'] = 'testString'
        message_input_attachment_model['media_type'] = 'testString'

        request_analytics_model = {}  # RequestAnalytics
        request_analytics_model['browser'] = 'testString'
        request_analytics_model['device'] = 'testString'
        request_analytics_model['pageUrl'] = 'testString'

        message_input_options_spelling_model = {}  # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {}  # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['async_callout'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {}  # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['attachments'] = [message_input_attachment_model]
        message_input_model['analytics'] = request_analytics_model
        message_input_model['options'] = message_input_options_model

        dialog_suggestion_value_model = {}  # DialogSuggestionValue
        dialog_suggestion_value_model['input'] = message_input_model

        dialog_suggestion_model = {}  # DialogSuggestion
        dialog_suggestion_model['label'] = 'testString'
        dialog_suggestion_model['value'] = dialog_suggestion_value_model
        dialog_suggestion_model['output'] = {'anyKey': 'anyValue'}

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeSuggestion model
        runtime_response_generic_runtime_response_type_suggestion_model_json = {}
        runtime_response_generic_runtime_response_type_suggestion_model_json['response_type'] = 'suggestion'
        runtime_response_generic_runtime_response_type_suggestion_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_suggestion_model_json['suggestions'] = [dialog_suggestion_model]
        runtime_response_generic_runtime_response_type_suggestion_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSuggestion by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_suggestion_model = RuntimeResponseGenericRuntimeResponseTypeSuggestion.from_dict(runtime_response_generic_runtime_response_type_suggestion_model_json)
        assert runtime_response_generic_runtime_response_type_suggestion_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSuggestion by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_suggestion_model_dict = RuntimeResponseGenericRuntimeResponseTypeSuggestion.from_dict(runtime_response_generic_runtime_response_type_suggestion_model_json).__dict__
        runtime_response_generic_runtime_response_type_suggestion_model2 = RuntimeResponseGenericRuntimeResponseTypeSuggestion(**runtime_response_generic_runtime_response_type_suggestion_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_suggestion_model == runtime_response_generic_runtime_response_type_suggestion_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_suggestion_model_json2 = runtime_response_generic_runtime_response_type_suggestion_model.to_dict()
        assert runtime_response_generic_runtime_response_type_suggestion_model_json2 == runtime_response_generic_runtime_response_type_suggestion_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeText:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeText
    """

    def test_runtime_response_generic_runtime_response_type_text_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeText
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeText model
        runtime_response_generic_runtime_response_type_text_model_json = {}
        runtime_response_generic_runtime_response_type_text_model_json['response_type'] = 'text'
        runtime_response_generic_runtime_response_type_text_model_json['text'] = 'testString'
        runtime_response_generic_runtime_response_type_text_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeText by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_text_model = RuntimeResponseGenericRuntimeResponseTypeText.from_dict(runtime_response_generic_runtime_response_type_text_model_json)
        assert runtime_response_generic_runtime_response_type_text_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeText by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_text_model_dict = RuntimeResponseGenericRuntimeResponseTypeText.from_dict(runtime_response_generic_runtime_response_type_text_model_json).__dict__
        runtime_response_generic_runtime_response_type_text_model2 = RuntimeResponseGenericRuntimeResponseTypeText(**runtime_response_generic_runtime_response_type_text_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_text_model == runtime_response_generic_runtime_response_type_text_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_text_model_json2 = runtime_response_generic_runtime_response_type_text_model.to_dict()
        assert runtime_response_generic_runtime_response_type_text_model_json2 == runtime_response_generic_runtime_response_type_text_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeUserDefined:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeUserDefined
    """

    def test_runtime_response_generic_runtime_response_type_user_defined_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeUserDefined
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeUserDefined model
        runtime_response_generic_runtime_response_type_user_defined_model_json = {}
        runtime_response_generic_runtime_response_type_user_defined_model_json['response_type'] = 'user_defined'
        runtime_response_generic_runtime_response_type_user_defined_model_json['user_defined'] = {'anyKey': 'anyValue'}
        runtime_response_generic_runtime_response_type_user_defined_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeUserDefined by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_user_defined_model = RuntimeResponseGenericRuntimeResponseTypeUserDefined.from_dict(runtime_response_generic_runtime_response_type_user_defined_model_json)
        assert runtime_response_generic_runtime_response_type_user_defined_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeUserDefined by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_user_defined_model_dict = RuntimeResponseGenericRuntimeResponseTypeUserDefined.from_dict(runtime_response_generic_runtime_response_type_user_defined_model_json).__dict__
        runtime_response_generic_runtime_response_type_user_defined_model2 = RuntimeResponseGenericRuntimeResponseTypeUserDefined(**runtime_response_generic_runtime_response_type_user_defined_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_user_defined_model == runtime_response_generic_runtime_response_type_user_defined_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_user_defined_model_json2 = runtime_response_generic_runtime_response_type_user_defined_model.to_dict()
        assert runtime_response_generic_runtime_response_type_user_defined_model_json2 == runtime_response_generic_runtime_response_type_user_defined_model_json


class TestModel_RuntimeResponseGenericRuntimeResponseTypeVideo:
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeVideo
    """

    def test_runtime_response_generic_runtime_response_type_video_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeVideo
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {}  # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeVideo model
        runtime_response_generic_runtime_response_type_video_model_json = {}
        runtime_response_generic_runtime_response_type_video_model_json['response_type'] = 'video'
        runtime_response_generic_runtime_response_type_video_model_json['source'] = 'testString'
        runtime_response_generic_runtime_response_type_video_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_video_model_json['description'] = 'testString'
        runtime_response_generic_runtime_response_type_video_model_json['channels'] = [response_generic_channel_model]
        runtime_response_generic_runtime_response_type_video_model_json['channel_options'] = {'anyKey': 'anyValue'}
        runtime_response_generic_runtime_response_type_video_model_json['alt_text'] = 'testString'

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeVideo by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_video_model = RuntimeResponseGenericRuntimeResponseTypeVideo.from_dict(runtime_response_generic_runtime_response_type_video_model_json)
        assert runtime_response_generic_runtime_response_type_video_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeVideo by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_video_model_dict = RuntimeResponseGenericRuntimeResponseTypeVideo.from_dict(runtime_response_generic_runtime_response_type_video_model_json).__dict__
        runtime_response_generic_runtime_response_type_video_model2 = RuntimeResponseGenericRuntimeResponseTypeVideo(**runtime_response_generic_runtime_response_type_video_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_video_model == runtime_response_generic_runtime_response_type_video_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_video_model_json2 = runtime_response_generic_runtime_response_type_video_model.to_dict()
        assert runtime_response_generic_runtime_response_type_video_model_json2 == runtime_response_generic_runtime_response_type_video_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
