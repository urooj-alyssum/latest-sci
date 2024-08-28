import os
import time
import boto3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": os.path.abspath("/Users/uroojkhan/Desktop/selenium/downloaded_pdfs"),  # Update this to your download directory
    "plugins.always_open_pdf_externally": True
})

# Manually set the path to the ChromeDriver
chromedriver_path = "/Users/uroojkhan/Desktop/selenium/chromedriver"  # Update this to the path where you downloaded chromedriver

# Initialize the WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the judgments page
judgments_page_url = "https://www.sci.gov.in/#1697446384453-9aeef8cc-5f35"  # Update this to the actual URL of the judgments page

# Open the judgments page
driver.get(judgments_page_url)

# Wait for the page to load
time.sleep(5)

# Find all the PDF links in the judgments column
pdf_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'get_court_pdf') and contains(@href, 'type=j&order_date')]")

# Extract the URLs from the links
urls = set(link.get_attribute('href') for link in pdf_links if "latest_judgements_order" in link.get_attribute('href'))  # Filter to include only the 'latest_judgements_order' type

# Create download directory if it doesn't exist
download_dir = "/Users/uroojkhan/Desktop/selenium/downloaded_pdfs"
os.makedirs(download_dir, exist_ok=True)

# Iterate through the list of URLs and download the PDFs
for url in urls:
    print(f"Downloading from: {url}")
    driver.get(url)
    # Display metadata
    print(f"Metadata: URL - {url}")
    time.sleep(5)  # Wait for the download to complete (adjust time if needed)

# Close the WebDriver
driver.quit()

print("All PDFs related to 'latest_judgements_order' have been downloaded to the local directory.")

# AWS S3 setup
s3_bucket_name = "datacrux-dev"
s3_prefix = "sci/Latest/August/"
s3 = boto3.client('s3')

# Upload PDFs to S3
for root, dirs, files in os.walk(download_dir):
    for file in files:
        if file.endswith(".pdf"):
            local_file_path = os.path.join(root, file)
            s3_key = os.path.join(s3_prefix, file)
            print(f"Uploading")
            s3.upload_file(local_file_path, s3_bucket_name, s3_key)

print("All PDFs have been uploaded to the S3 bucket.")
