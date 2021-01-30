import requests
import json
from datetime import datetime
from uuid import getnode as get_mac
import hashlib


class MetaLabs:

    def __init__(self):
        self.h = {'Authorization': f'Basic {self.api_Key}'}

    @classmethod
    def apiKey(self, api_Key):
        self.api_Key = api_Key
        print(api_Key)

    @classmethod
    def validate(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                return True, r.json()
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getEmail(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                email = r.json()['email']
                return email
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getDiscordID(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                discordID = r.json()['member']['discord']['id']
                return discordID
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getDiscordTag(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                discordTag = r.json()['member']['discord']['tag']
                return discordTag
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getDiscordAvatar(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                discordAvatar = r.json()['member']['discord']['avatar']
                discordID = r.json()['member']['discord']['id']
                discordAvatar = f'https://cdn.discordapp.com/avatars/{discordID}/{discordAvatar}.png'
                return discordAvatar
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getUserID(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                UserID = r.json()['id']
                return UserID
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getUserCreatedAt(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                UserCreatedAt = r.json()['created']
                return UserCreatedAt
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getUserStatus(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                UserStatus = r.json()['status']
                return UserStatus
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getUserSAllows(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                allowUnbinding = r.json()['plan']['allow_unbinding']
                allowReselling = r.json()['plan']['allow_reselling']
                return f'Allow unbind: {allowUnbinding}', f'Allow resell: {allowReselling}'
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getUserPlanAmount(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                UserPlanAmount = r.json()['plan']['amount']
                return UserPlanAmount
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getUserPlanType(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                UserPlanType = r.json()['plan']['type']
                return UserPlanType
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getMetaDatas(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                MetaData = r.json()['metadata']
                return MetaData
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def getFingerPrint(self, licenseKey):
        try:
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if licenseKey == r.json()['key']:
                FingerPrint = r.json()['metadata']['fingerprint']
                return FingerPrint
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except KeyError:
            print('Make sur to set fingerprint by using Metalabs.setFingerprint(licenseKey) before getting it')
            return False
        except Exception as e:
            return print(e)

    @classmethod
    def setFingerPrint(self, licenseKey):
        try:
            machine_fingerprint = hashlib.sha256(str(get_mac()).encode('utf-8')).hexdigest()
            r = requests.patch(f'https://api.metalabs.io/v2/licenses/{licenseKey}',
                headers = {
                    'content-type': 'application/json',
                    'Authorization': f'Basic {self.api_Key}'},
                data = json.dumps({'metadata': {'fingerprint': machine_fingerprint}}))
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if machine_fingerprint == r.json()['metadata']['fingerprint']:
                return f'Fingerprint set: {machine_fingerprint}'
            else:
                return 'Error'
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except Exception as e:
            return print(e)

    @classmethod
    def resetFingerPrint(self, licenseKey):
        try:
            machine_fingerprint = hashlib.sha256(str(get_mac()).encode('utf-8')).hexdigest()
            r = requests.patch(f'https://api.metalabs.io/v2/licenses/{licenseKey}',
                headers = {
                    'content-type': 'application/json',
                    'Authorization': f'Basic {self.api_Key}'},
                data = json.dumps({'metadata': {'fingerprint': ''}}))
            r = requests.get(f'https://api.metalabs.io/v2/licenses/{licenseKey}', headers={'Authorization': f'Basic {self.api_Key}'})
            if '' == r.json()['metadata']['fingerprint']:
                return f'Fingerprint reseted'
            else:
                return False
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except KeyError:
            print('Make sur to set fingerprint by using Metalabs.setFingerprint(licenseKey) before getting it')
            return False
        except Exception as e:
            return print(e)

    @classmethod
    def validateLicenseFingerPrint(self, licenseKey):
        machine_fingerprint = hashlib.sha256(str(get_mac()).encode('utf-8')).hexdigest()
        try:
            validation = requests.get(f"https://api.metalabs.io/v2/licenses/{licenseKey}",
                                      headers={'Authorization': f'Basic {self.api_Key}'})
            try:
                if validation.json()['key'] == licenseKey:
                    pass
                else:
                    return False
            except Exception as e:
                return False
            try:
                if validation.json()['metadata']['fingerprint'] == machine_fingerprint:
                    return True
                if validation.json()['metadata']['fingerprint'] == '':
                    requests.patch(f"https://api.metalabs.io/v2/licenses/{licenseKey}",
                                   headers={'content-type': 'application/json',
                                            'Authorization': f'Basic {self.api_Key}'}, data=json.dumps({
                            'metadata': {'fingerprint': machine_fingerprint}}))
                    return True
                else:
                    return False
            except KeyError:
                requests.patch(f"https://api.metalabs.io/v2/licenses/{licenseKey}",
                               headers={'content-type': 'application/json',
                                        'Authorization': f'Basic {self.api_Key}'}, data=json.dumps({
                        'metadata': {'fingerprint': machine_fingerprint}}))
                return True
        except AttributeError:
            return print('Make sur to set your API Key: MetaLabs.apiKey(apiKey)')
        except KeyError:
            print('Make sur to set fingerprint by using Metalabs.setFingerprint(licenseKey) before getting it')
            return False
        except Exception as e:
            return print(e)
