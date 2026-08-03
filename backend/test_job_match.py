from app.services.ai_service import AIService
from app.services.parser_service import ParserService

parser = ParserService()
ai = AIService()

resume_text = parser.extract_text("uploads/resumes/37d58c42-6b81-4670-89fb-47dadaa90b20.pdf")

job_description = """
We are looking for a QA Engineer with experience in:

- Selenium
- Python
- REST API Testing
- SQL
- Docker
- Jenkins
- Git
- Agile
"""

result = ai.match_resume_with_job(
    resume_text,
    job_description
)

print(result)