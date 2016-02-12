
try:
    from http.client import HTTPSConnection
    from urllib.parse import urlencode
except ImportError:
    from httplib import HTTPSConnection
    from urllib import urlencode

import json

class SMSException(Exception):
    def __init__(self, reason):
        Exception.__init__(self, reason)


class SMSConnection:
    SMS_HOST = "sms.yunpian.com"
    VOICE_HOST = "voice.yunpian.com"
    API_VERSION = "v1"
    TIMEOUT = 30

    def __init__(self, apikey):
        self.apikey = apikey

    def request(self, uri, params, host):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }

        args = {"apikey": self.apikey}
        args.update(params)

        conn = HTTPSConnection(host, timeout = self.TIMEOUT)
        conn.request("POST", "/" + self.API_VERSION + uri, 
            urlencode(args))

        data = conn.getresponse().read()

        return json.loads(data)

    @property
    def userinfo(self):
        data = self.request("/user/get.json", {}, self.SMS_HOST)
        return data

    def send_sms(self, text, mobile):
        data = self.request("/sms/send.json", 
            {
                "text": text,
                "mobile": mobile,
            },
            self.SMS_HOST)
        return data

    def send_tpl_sms(self, tpl_value, mobile, tpl_id):
        data = self.request("/sms/send.json", 
            {
                "tpl_id": tpl_id,
                "tpl_value": tpl_value,
                "mobile": mobile,
            },
            self.SMS_HOST)
        return data

    def send_voice_sms(self, code, mobile):
        data = self.request("/voice/send.json", 
            {
                "code": code,
                "mobile": mobile,
            },
            self.SMS_HOST)
        return data

if __name__ == '__main__':

    import argparse, sys
    parser = argparse.ArgumentParser()

    parser.add_argument("-k", "--key", required=True,
        help="API Key")
    parser.add_argument("-m", "--mobile", 
        help="Mobile phone number")
    parser.add_argument("-t", 
        "--text", help="Send TEXT")
    parser.add_argument("-c", 
        "--code", help="Send CODE with voice")
    parser.add_argument("-u", 
        dest="user", 
        action="store_true",
        help="Get account info.")

    args = parser.parse_args()
    conn = SMSConnection(args.key)
    if args.user is True:
        print(conn.userinfo)
        sys.exit(0)
    
    if args.mobile is None:
        print("error: argument -k/--key: expected one argument")
        parser.print_help()
        sys.exit(0)
    if args.text is not None:
        obj = conn.send_sms(args.text, args.mobile)
        print(obj)
    elif args.code is not None:
        obj = conn.send_voice_sms(args.code, args.mobile)
        print(obj)


