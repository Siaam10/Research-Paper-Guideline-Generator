#generated via chatgpt, link and filename edited for different websites
from playwright.sync_api import Playwright, sync_playwright

def scrape_data(playwright: Playwright) -> None:
    with playwright.firefox.launch(headless=True) as browser:
        with browser.new_context() as context:
            page = context.new_page()
            page.goto("https://theaisummer.com/vision-transformer/")
            text = page.inner_text("body")  # Replace "body" with your desired selector
            
            # Open the file for writing with UTF-8 encoding
            with open("outputaisummer.txt", "w", encoding="utf-8") as file:
                # Write the scraped text to the file
                file.write(text)
                
            print("Scraped data saved to output.txt")

with sync_playwright() as playwright:
    scrape_data(playwright)
