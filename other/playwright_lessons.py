from playwright.sync_api import sync_playwright, Request, Response

def log_request(request: Request):
    """
    Логирование информации о запросе
    """
    print("Request URL: %s" % request.url)
    print("Request Body: %s" % request.post_data)

def log_response(response: Response):
    """
    Логирование информации об ответе
    """
    print("Response URL: %s" % response.url)
    print("Response Body: %s" % response.body)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.on("request", log_request)
    page.on("response", log_response)

    email_input = page.get_by_test_id("login-form-email-input").locator("input") # поиск кнопки login по data-testid
    email_input.focus() # установка фокуса на поле
    for char in "user.name@gmail.com":
        page.keyboard.type(char, delay=100) # заполнение поля email с паузой в 100 мс

    page.keyboard.press("ControlOrMeta+A", delay=100) # установка фокуса на поле
    page.keyboard.press("Backspace") # удаление символа

    page.wait_for_timeout(3000)

