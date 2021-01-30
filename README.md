<img src="https://gblobscdn.gitbook.com/spaces%2F-Lu3bOY-QFMriwg4jjtu%2Favatar-1602380943572.png?alt=media"/>

# Import
To import metalabs module simply `import metalabs`

# Usage
First set your api key using `Metalabs.apiKey(YourApiKey)`

# Then you can use all functions:
Simple license validation: `Metalabs.validate(licenseKey)` return `True` or `False`
License validation using machine fingerprint: `Metalabs.validateLicenseFingerPrint(licenseKey)` return `True` or `False`
Set a fingerprint: `Metalabs.setFingerPrint(licenseKey)` return the fingerprint if well set
Reset a fingerprint: `Metalabs.resetFingerPrint(licenseKey)` return `Fingerprint reseted` if well reseted
Get a fingerprint: `Metalabs.getFingerPrint(licenseKey)` return user fingerprint
Get all meta datas: `Metalabs.getMetaDatas(licenseKey)` return all meta datas
Get the user plan type: `Metalabs.getUserPlanType(licenseKey)` return `Free` or `Paid`
Get the user plan amount: `Metalabs.getUserPlanAmount(licenseKey)` return the user plan amount
Check if user can unbind and resell his key: `Metalabs.getUserSAllows(licenseKey)` return `True` or `False`
Check if user license key is active: `Metalabs.getUserStatus(licenseKey)` return `active` if yes
Get user discord profil picture: `Metalabs.getDiscordAvatar(licenseKey)` return image url
Get user discord name and tag: `Metalabs.getDiscordTag(licenseKey)` return user discord full tag
Get user discord ID: `Metalabs.getDiscordID(licenseKey)` return user discord id
Get user email: `Metalabs.getEmail(licenseKey)` return user email
Get timestamp of when user was created: `Metalabs.getUserCreatedAt(licenseKey)` return the timestamp
