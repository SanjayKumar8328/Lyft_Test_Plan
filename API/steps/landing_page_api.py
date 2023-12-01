from behave import given, when, then
import requests
import helper
from jsonschema import validate
from schemas import main_api_schema

@given(u'call the main API')
def api_request(self):
    # api = helper[api_type]
    res = requests.get("https://api.lyft.com/v1/terms")
    self.res = res
    
@then('verify the main api status code and schema')    
def status_code_validation(self):
    status_code = self.res.status_code
    if status_code != 200:
        raise AssertionError("'{}' api retuens '{}' instead of 200".format("https://api.lyft.com/v1/terms",status_code))
    try:
        validate(instance=self.res.json(),schema=main_api_schema.schema_data)
    except:
        raise AssertionError("Schema defined for the main API is not matching")
    
@given('call the Post API with user number')
def user_info_api(self):
    payload = {"phone":"+14372992887","ride_with_lyft_form":"2M6S2EM113r30RSdF0y5Bt","source":"lyftcomfe_ride_with_lyft"}
    self.res = requests.get("https://www.lyft.com/api/app",params=payload)

@then('verify the post api status code and schema')    
def status_code_validation(self):
    status_code = self.res.status_code
    if status_code != 200:
        raise AssertionError("'{}' api retuens '{}' instead of 200".format("https://www.lyft.com/api/app",status_code))