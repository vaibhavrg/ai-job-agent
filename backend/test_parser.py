from app.services.parser_service import ParserService

parser = ParserService()

text = parser.extract_pdf_text(
    "uploads/resumes/37d58c42-6b81-4670-89fb-47dadaa90b20.pdf"
)

print("\nNAME:")
print(parser.extract_name(text))

print("\nEMAIL:")
print(parser.extract_email(text))

print("\nPHONE:")
print(parser.extract_phone(text))

print("\nSKILLS:")
print(parser.extract_skills(text))