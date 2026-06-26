from playwright.sync_api import Playwright, APIRequest
import pytest
from data.data_test import phone_customer, id_number_customer   
from api.dev import api_context  

# @pytest.fixture()
# def api_context(playwright: Playwright):
#     api_context = playwright.request.new_context(base_url='https://api-rc.cnext.vn')
#     yield api_context
#     api_context.dispose()   


# def test_api_testing(api_context: APIRequest):
#     body = {
#     "sale_code": "C240400025",
#     "gender": 2,
#     "project_code": "VPB_UPL",
#     "full_name": "Ngọc Thảo",
#     "phone": phone_customer,
#     "id_number": id_number_customer,
#     "date_of_birth": "1996-02-29",
#     "consent": "true",
#     "source": "LANDING_PAGE",
#     "place_of_residence": "kiên giang"
    
#     }
#     response = api_context.post(
#         url='/api/projects/validatesubmitfin', 
#         data=body,
#         headers={'Content-Type': 'application/json'}
#         )
#     assert response.status == 201
#     result= response.json()
#     print(result)
#     assert result['status'] == 'true'
#     assert result['data']['call_otp'] == 'true'


def test_api_call_otp(api_context: APIRequest):
    body = {   
    "phone": phone_customer,
    "source_code": "LANDING_PAGE",
    "sale_channel_code": "AFFILIATE"
    }
    response = api_context.post(
        url='/api/projects/requestotpphonesubmitfin',    
        data=body,
        headers={'Content-Type': 'application/json'}
        )
    assert response.status == 201
    result_otp= response.json()
    print(result_otp['data']['otp_token'])

