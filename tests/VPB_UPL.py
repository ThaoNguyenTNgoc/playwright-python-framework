import asyncio
from playwright.async_api import async_playwright, Playwright


async def test_open_vpb_upl(playwright: Playwright):
    async with async_playwright() as playwright:
        chromium = playwright.chromium
        browser = await chromium.launch(headless=False, slow_mo=5000)
        page = await browser.new_page()
        await page.goto("https://aff-dev.cnext.vn/fin/VPB_UPL/C240400025")
        # Cách 1: Dùng placeholder (Khuyên dùng vì trực quan)
        full_name_input = page.get_by_placeholder("Họ tên đầy đủ trên CCCD")
        # Cách 2: Nếu có thẻ label đi kèm
        # full_name_input = page.g et_by_label("Họ và tên *")
        await full_name_input.highlight()
        await full_name_input.fill("Nguyễn Văn A")
        # Chọn Nam
        male_radio = page.get_by_role("radio", name="Nam")
        # Hoặc đơn giản là click vào chữ "Nam"
        # male_radio = page.get_by_text("Nam")
        # Chọn Nữ
        female_radio = page.get_by_role("radio", name="Nữ")
        await female_radio.click()
        phone_input = page.get_by_placeholder("Số điện thoại di động")
        await phone_input.fill("0123456789")
        # full_name_input = page.get_by_label("Họ và tên *")
        cccd_input = page.get_by_placeholder("Nhập 12 số CCCD gắn chip/Căn cước phôi mới")
        await cccd_input.fill("123456789012")
        dob_input = page.get_by_placeholder("DD-MM-YYYY")
        await dob_input.fill("01-01-1990")
        # Thường các checkbox này sẽ dùng role là checkbox
        terms_checkbox = page.get_by_role("checkbox")
        # Nếu có nhiều checkbox và cần phân biệt bằng text đi kèm:
        # terms_checkbox = page.locator("label:has-text('Tôi đã đọc, hiểu và đồng ý')").get_by_role("checkbox")
        await terms_checkbox.check()
        # Dùng role button là chuẩn nhất trong Playwright
        submit_button = page.get_by_role("button", name="Xác nhận")
        await submit_button.click()
        await page.wait_for_timeout(100)
        otp_code = "123456"

        # Tìm tất cả các ô input nằm bên trong khu vực hiển thị OTP
        # (Thông thường các ô này có type="tel" hoặc type="number")
        
        otp_inputs = page.locator("input[type='tel']") 
        # Nếu locator trên không tìm thấy, bạn có thể thử đổi thành: page.locator(".otp-input") hoặc page.locator("input")

        # Chạy vòng lặp điền từng số vào từng ô
        for i in range(6):
            await otp_inputs.nth(i).fill(otp_code[i])




async def main():
    async with async_playwright() as playwright:
        await test_open_vpb_upl(playwright)


asyncio.run(main())
