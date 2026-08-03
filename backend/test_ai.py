from app.services.ai_service import AIService
from app.services.parser_service import ParserService

parser = ParserService()

text = parser.extract_pdf_text(
    "uploads/resumes/37d58c42-6b81-4670-89fb-47dadaa90b20.pdf"
)

ai = AIService()

result = ai.analyze_resume(text)

print(result)