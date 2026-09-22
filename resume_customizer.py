import re

# Step 1: Load resume template
with open("resume.txt", "r") as file:
    template = file.read()

# Step 2: Example job description (later connect with scraped jobs)
job_description = "We are looking for a Data Analyst with Python, SQL, and Data Visualization experience."

# Step 3: Extract keywords
job_keywords = set(re.findall(r'\b\w+\b', job_description.lower()))

# Step 4: Match with your resume skills/projects
resume_skills = "Python, SQL, Machine Learning, Data Analysis"
resume_projects = "IPL Dashboard, Chatbot, Hangman Game"
resume_experience = "Internship at Data Analytics Firm"

matched_skills = [skill for skill in resume_skills.split(", ") if skill.lower() in job_keywords]
matched_projects = [proj for proj in resume_projects.split(", ") if any(word in job_keywords for word in proj.lower().split())]

# Step 5: Replace placeholders
custom_resume = template.replace("{{skills}}", ", ".join(matched_skills))
custom_resume = custom_resume.replace("{{projects}}", ", ".join(matched_projects))
custom_resume = custom_resume.replace("{{experience}}", resume_experience)

# Step 6: Save customized resume
with open("resume.txt", "w") as file:
    file.write(custom_resume)

print("Customized resume created: resume.txt")
