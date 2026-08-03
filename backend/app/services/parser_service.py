import re

from pypdf import PdfReader

from app.core.skills import KNOWN_SKILLS


class ParserService:

    def extract_pdf_text(self, file_path: str) -> str:
        """Extract all text from a PDF."""
        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    def extract_text(self, file_path: str) -> str:
        """
        Alias for extract_pdf_text().
        This allows other services to call extract_text().
        """
        return self.extract_pdf_text(file_path)

    def extract_email(self, text: str):
        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )
        return match.group(0) if match else None

    def extract_phone(self, text: str):
        match = re.search(
            r"(\+91[\s-]?)?[6-9]\d{9}",
            text,
        )
        return match.group(0) if match else None

    def extract_name(self, text: str):
        lines = text.splitlines()

        for line in lines:
            line = line.strip()

            if len(line.split()) >= 2:
                return line

        return None

    def extract_skills(self, text: str):
        found = []

        lower = text.lower()

        for skill in KNOWN_SKILLS:
            if skill.lower() in lower:
                found.append(skill)

        return sorted(set(found))

    def parse_resume(self, file_path: str):
        """
        Parse a resume and return structured information.
        """
        text = self.extract_pdf_text(file_path)

        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "skills": self.extract_skills(text),
            "text": text,
        }