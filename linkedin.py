from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# Step 1: Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 2: Open LinkedIn Jobs page (example: Data Analyst jobs in Chennai)
driver.get("https://www.linkedin.com/jobs/search/?keywords=Data%20Analyst&location=Chennai%2C%20Tamil%20Nadu%2C%20India")

# Step 3: Wait for page to load
time.sleep(5)

# Step 4: Find job cards
jobs = driver.find_elements(By.CLASS_NAME, "base-card")

# Step 5: Load resume text
with open("resume.txt", "r") as file:
    resume_text = file.read().lower()

# Step 6: Loop through scraped jobs and calculate match score
for job in jobs[:10]:  # limit to first 10 jobs
    try:
        title = job.find_element(By.CLASS_NAME, "base-search-card__title").text
        company = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
        location = job.find_element(By.CLASS_NAME, "job-search-card__location").text
        description = job.text.lower()  # simple job description

        # Extract keywords
        job_keywords = set(re.findall(r'\b\w+\b', description))
        resume_keywords = set(re.findall(r'\b\w+\b', resume_text))

        # Find matches
        matched = job_keywords & resume_keywords
        score = (len(matched) / len(job_keywords)) * 100 if job_keywords else 0

        # Print results
        print(f"Job Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print("Matched Keywords:", matched)
        print("Match Score:", round(score, 2), "%")
        print("-" * 40)

    except Exception as e:
        continue

# Step 7: Close browser
driver.quit()
