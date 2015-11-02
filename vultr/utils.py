'''Helper classes'''
import requests
import time
import json as json_module

API_ENDPOINT = 'https://api.vultr.com'


class VultrError(RuntimeError):
    '''Vultr custom exception'''
    pass


class VultrBase(object):
    '''Base class for Vultr inheritance'''
    def __init__(self, api_key):
        self.api_endpoint = API_ENDPOINT
        self.api_key = api_key
        self.set_requests_per_second(1)

    def set_requests_per_second(self, req_per_second):
        '''Adjusts the request/second at run-time'''
        self.req_per_second = req_per_second
        self.req_duration = 1 / self.req_per_second

    def _request_get_helper(self, url, params=None):
        '''API GET request helper'''
        if not isinstance(params, dict):
            params = dict()

        if self.api_key:
            params['api_key'] = self.api_key
        return requests.get(url, params=params, timeout=60)

    def _request_post_helper(self, url, params=None):
        '''API POST helper'''
        if self.api_key:
            query = {'api_key': self.api_key}
        return requests.post(url, params=query, data=params, timeout=60)

    def _request_helper(self, url, params, method):
        '''API request helper method'''
        try:
            if method == 'POST':
                return self._request_post_helper(url, params)
            elif method == 'GET':
                return self._request_get_helper(url, params)
            raise VultrError('Unsupported method %s' % method)
        except requests.RequestException as ex:
            raise RuntimeError(ex)

    def request(self, path, params=None, method='GET'):
        '''API request / call method'''
        _start = time.time()

        if not path.startswith('/'):
            path = '/' + path

        resp = self._request_helper(self.api_endpoint + path, params, method)

        if resp.status_code != 200:
            if resp.status_code == 400:
                raise VultrError('Invalid API location. Check the URL that' +
                                 ' you are using')
            elif resp.status_code == 403:
                raise VultrError('Invalid or missing API key. Check that' +
                                 ' your API key is present and matches' +
                                 ' your assigned key')
            elif resp.status_code == 405:
                raise VultrError('Invalid HTTP method. Check that the' +
                                 ' method (POST|GET) matches what the' +
                                 ' documentation indicates')
            elif resp.status_code == 412:
                raise VultrError('Request failed. Check the response body ' +
                                 'for a more detailed description. Body: \n' +
                                 resp.text)
            elif resp.status_code == 500:
                raise VultrError('Internal server error. Try again at a' +
                                 ' later time')
            elif resp.status_code == 503:
                raise VultrError('Rate limit hit. API requests are limited' +
                                 ' to an average of 1/s. Try your request' +
                                 ' again later.')

        # very simplistic synchronous rate limiting;
        _elapsed = time.time() - _start
        if _elapsed < self.req_duration:
            time.sleep(self.req_duration - _elapsed)

        # return an empty json object if the API doesn't respond with a value.
        return resp.json() if resp.text else json_module.loads('{}')


def update_params(params, updates):
    '''Merges updates into params'''
    params = params.copy() if isinstance(params, dict) else dict()
    params.update(updates)
    return params
