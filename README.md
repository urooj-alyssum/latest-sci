# Latest sci Judgment Scraper

**Latest Judgment Scraper** automates the process of downloading the latest judgment PDFs from a specified website and uploading them to an AWS S3 bucket. This tool is particularly useful for users who need to regularly collect and archive legal documents.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver
- Selenium
- Boto3

# Install the required packages
pip install selenium boto3

# Configuration 
- chromedriver_path = "/Users/yourusername/Desktop/selenium/chromedriver"
- download_dir = "/Users/yourusername/Desktop/selenium/downloaded_pdfs"
- judgments_page_url = "https://www.sci.gov.in/#1697446384453-9aeef8cc-5f35"
- s3_bucket_name = "your-s3-bucket-name"
- s3_prefix = "your/s3/prefix/"

# AWS Credentials 
- Ensure aws credentials are configured in .env
- AWS_DEFAULT_REGION="Your_Region"
- AWS_ACCESS_KEY_ID="Your_Access_key_id"
- AWS_SECRET_ACCESS_KEY="Your_aws_secret_access_key" 

# Important note
Ensure to "allow" selenium driver in mac by going to Privacy & Security in System setting 

# Run the automation 
python3 your_scriptname.py (example : python3 latestsci.py) 

# Scrapping & Uploading to S3 



# Sucessfully upload latest judgements On S3 bucket 





