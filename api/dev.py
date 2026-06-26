from playwright.sync_api import Playwright, APIRequest
import pytest

# @pytest.fixture()
def api_context(playwright: Playwright):
    api_context = playwright.request.new_context(base_url='https://api-rc.cnext.vn')
    yield api_context
    api_context.dispose()   

print("API context fixture created and ready to use in tests."+(api_context))