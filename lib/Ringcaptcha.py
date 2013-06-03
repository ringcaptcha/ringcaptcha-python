import urllib, urllib2, json, sys

'''
# Ringcaptcha class
#
# Provides simplified interaction with the Ringcaptcha verification REST API.
#
# @package Ringcaptcha
# @author  Martin Cocaro <martin@ringcaptcha.com>
# @license http://www.gnu.org/licenses/gpl-3.0.html GNU General Public License
# @link    http://ringcaptcha.com/
'''

class Ringcaptcha(object):
    '''
    Ringcaptcha API verification implementation
    '''

    RC_SERVER     = 'api.ringcaptcha.com'
    USER_AGENT    = 'ringcaptcha-php/1.0'
    VERSION       = '1.0';
    
    def __init__(self, appKey, secretKey):
        self.appKey = appKey
        self.secretKey = secretKey
        self.retryAttempts = 0
        self.isSecure = True
        self.status = -1

    def isValid(self, pinCode, token):
        url = ("https://" if self.isSecure else "http://") + self.RC_SERVER + '/' + self.appKey + '/verify'
        values = {
                  'token' : token,
                  'code' : pinCode,
                  'secret_key' : self.secretKey
        }
        headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "application/json"}

        self.sanitizeData(values);
        
        try:
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data, headers)
            response = urllib2.urlopen(req)
            rsp = response.read()
            rspJson = json.loads(rsp) 
            if (rspJson['status'] == 'SUCCESS'):
                self.status = 1
            else:
                self.status = 0
        except:
            self.status = 0
            self.message = sys.exc_info()[0]
            return False

        self.transactionID = rspJson['id'] if 'id' in rspJson else False
        self.phoneNumber = rspJson['phone'] if 'phone' in rspJson else False
        self.geolocation = rspJson['geolocation'] if 'geolocation' in rspJson else False
        self.message = rspJson['message'] if 'message' in rspJson else False
        self.phoneType = rspJson['phone_type'] if 'phone_type' in rspJson else False
        self.carrierName = rspJson['carrierName'] if 'carrierName' in rspJson else False
        self.deviceName = rspJson['device'] if 'device' in rspJson else False
        self.ispName = rspJson['isp'] if 'isp' in rspJson else False

        return (self.status == 1)

    def setSecure(self,secure):
        self.isSecure = secure

    def getStatus(self):
        return {
                '1': 'SUCCESS',
                '0': 'ERROR'
                }[self.status]

    def getMessage(self):
        return self.message

    def getId(self):
        return self.transactionID

    def getPhoneNumber(self):
        return self.phoneNumber

    def isGeolocated(self):
        return self.geolocation
    
    def getPhoneType(self):
        return self.phoneType
        
    def getCarrierName(self):
        return self.carrierName
    
    def getDeviceName(self):
        return self.deviceName
        
    def getIspName(self):
        return self.ispName

    def sanitizeData(self, data):
        for k, val in data.iteritems():
            data[k] = val.strip(' \t\n\r')

        