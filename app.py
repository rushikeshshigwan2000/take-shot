import streamlit as st
from playwright.sync_api import sync_playwright
import io
import base64

def take_screenshot(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        screenshot_bytes = page.screenshot()
        browser.close()
    return screenshot_bytes

def save_image_to_db(image_bytes):
    # Example: Just save to local file for now
    with open("screenshot.png", "wb") as f:
        f.write(image_bytes)
    # TODO: Implement DB storage here

st.title("Virtual Screenshot App")

url = st.text_input("Enter URL to screenshot", "https://example.com")

if st.button("Take Screenshot"):
    with st.spinner("Taking screenshot..."):
        img_bytes = take_screenshot(url)
        save_image_to_db(img_bytes)
    st.success("Screenshot taken and saved!")
