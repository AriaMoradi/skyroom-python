import requests

try:
    import json
except ImportError:
    import simplejson as json


class APIException(Exception):
    pass


class HTTPException(Exception):
    pass


class SkyroomAPI(object):
    def __init__(self, apikey):
        self.host = 'www.skyroom.online'
        self.apikey = apikey
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'charset': 'utf-8'
        }

    def __repr__(self):
        return "skyroom.SkyroomAPI({!r})".format(self.apikey)

    def __str__(self):
        return "skyroom.SkyroomAPI({!s})".format(self.apikey)

    def _request(self, action, params=None, **requests_kwargs):
        url = 'https://' + self.host + '/skyroom/api/' + self.apikey
        data = {
            'action': action
        }
        if params:
            data['params'] = params
        try:
            content_data = requests.post(url, headers=self.headers, auth=None, json=data, **requests_kwargs).content
            try:
                response = json.loads(content_data.decode("utf-8"))
                if (response['ok'] == True):
                    response = response['result']
                else:
                    raise APIException(
                        (u'APIException[error_code: %s]: %s' % (
                            response['error_code'], response['error_message']))
                    )
            except ValueError as e:
                raise HTTPException(e)
            return response
        except requests.exceptions.RequestException as e:
            raise HTTPException(e)

    # 1.Service Management

    # to-be-implemented by Skyroom (hopefully) :)

    # 2.Rooms Management

    def getRooms(self, params=None, **requests_kwargs):
        return self._request('getRooms', params, **requests_kwargs)

    def countRooms(self, params=None, **requests_kwargs):
        return self._request('countRooms', params, **requests_kwargs)

    def getRoom(self, params=None, **requests_kwargs):
        return self._request('getRoom', params, **requests_kwargs)

    def getRoomUrl(self, params=None, **requests_kwargs):
        return self._request('getRoomUrl', params, **requests_kwargs)

    def createRoom(self, params=None, **requests_kwargs):
        return self._request('createRoom', params, **requests_kwargs)

    def updateRoom(self, params=None, **requests_kwargs):
        return self._request('updateRoom', params, **requests_kwargs)

    def deleteRoom(self, params=None, **requests_kwargs):
        return self._request('deleteRoom', params, **requests_kwargs)

    def getRoomUsers(self, params=None, **requests_kwargs):
        return self._request('getRoomUsers', params, **requests_kwargs)

    def addRoomUsers(self, params=None, **requests_kwargs):
        return self._request('addRoomUsers', params, **requests_kwargs)

    def removeRoomUsers(self, params=None, **requests_kwargs):
        return self._request('removeRoomUsers', params, **requests_kwargs)

    def updateRoomUser(self, params=None, **requests_kwargs):
        return self._request('updateRoomUser', params, **requests_kwargs)

    # 3. Users Management

    def getUsers(self, params=None, **requests_kwargs):
        return self._request('getUsers', params, **requests_kwargs)

    def countUsers(self, params=None, **requests_kwargs):
        return self._request('countUsers', params, **requests_kwargs)

    def getUser(self, params=None, **requests_kwargs):
        return self._request('getUser', params, **requests_kwargs)

    def createUser(self, params=None, **requests_kwargs):
        return self._request('createUser', params, **requests_kwargs)

    def updateUser(self, params=None, **requests_kwargs):
        return self._request('updateUser', params, **requests_kwargs)

    def deleteUser(self, params=None, **requests_kwargs):
        return self._request('deleteUser', params, **requests_kwargs)

    def getUserRooms(self, params=None, **requests_kwargs):
        return self._request('getUserRooms', params, **requests_kwargs)

    def addUserRooms(self, params=None, **requests_kwargs):
        return self._request('addUserRooms', params, **requests_kwargs)

    def removeUserRooms(self, params=None, **requests_kwargs):
        return self._request('removeUserRooms', params, **requests_kwargs)

    def getLoginUrl(self, params=None, **requests_kwargs):
        return self._request('getLoginUrl', params, **requests_kwargs)
