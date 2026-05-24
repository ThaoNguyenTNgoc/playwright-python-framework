from playwright.sync_api import Page, Playwright

def test_api_testing(playwright: Playwright):
    api_context = playwright.request.new_context(base_url='https://api-rc.cnext.vn')
    
    body = {
    "sale_code": "C240400025",
    "gender": 2,
    "project_code": "VPB_UPL",
    "full_name": "Ngọc Thảo",
    "phone": "0948339596",
    "id_number": "089196013310",
    "date_of_birth": "1996-02-29",
    "consent": "true",
    "source": "LANDING_PAGE",
    "place_of_residence": "kiên giang"
    
    }
    response = api_context.post(url='/api/projects/validatesubmitfin', data=body, headers={'Content-Type': 'application/json'})
    assert response.status == 201
    result= response.json()
    assert result['status'] == 'true'
    assert result['data']['call_otp'] == 'true'
