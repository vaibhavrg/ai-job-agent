import json
import time

from google import genai

from app.core.settings import settings


class AIService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        # Try models in this order
        self.models = [
            "gemini-3.5-flash",
            "gemini-2.0-flash",
            "gemini-flash-lite-latest",
        ]

    def _clean_json(self, text: str) -> str:
        text = text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")

        return text.strip()

    def _generate(self, prompt: str):
        """
        Tries multiple Gemini models with retries.
        """

        last_error = None

        for model_name in self.models:

            for attempt in range(3):

                try:
                    response = self.client.models.generate_content(
                        model=model_name,
                        contents=prompt,
                    )

                    return response.text

                except Exception as e:
                    last_error = e

                    print(
                        f"{model_name} failed "
                        f"(attempt {attempt + 1}/3): {e}"
                    )

                    time.sleep(2)

            print(f"Switching to next model...")

        raise last_error

    def analyze_resume(self, resume_text: str):

        prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume.

Return ONLY valid JSON.

Format:

{{
    "summary": "",
    "ats_score": 0,
    "strengths": [],
    "missing_skills": [],
    "recommendations": []
}}

Rules:

- ats_score must be between 0 and 100.
- Return ONLY valid JSON.
- No markdown.
- No explanation.

Resume:

{resume_text}
"""

        try:

            text = self._generate(prompt)

            text = self._clean_json(text)

            return json.loads(text)

        except json.JSONDecodeError:

            return {
                "summary": "Unable to parse AI response.",
                "ats_score": 0,
                "strengths": [],
                "missing_skills": [],
                "recommendations": [
                    "Gemini returned invalid JSON."
                ],
            }

        except Exception as e:

            return {
                "summary": "",
                "ats_score": 0,
                "strengths": [],
                "missing_skills": [],
                "recommendations": [],
                "error": str(e),
            }

    def match_resume_with_job(
        self,
        resume_text: str,
        job_description: str,
    ):

        prompt = f"""
You are an ATS Resume Matching Expert.

Compare the resume with the job description.

Return ONLY valid JSON.

Format:

{{
    "match_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "recommendations": []
}}

Rules:

- match_score must be an integer between 0 and 100.
- Return ONLY JSON.
- No markdown.
- No explanation.

Resume:

{resume_text}

Job Description:

{job_description}
"""

        try:

            text = self._generate(prompt)

            text = self._clean_json(text)

            return json.loads(text)

        except json.JSONDecodeError:

            return {
                "match_score": 0,
                "matching_skills": [],
                "missing_skills": [],
                "recommendations": [
                    "Gemini returned invalid JSON."
                ],
            }

        except Exception as e:

            return {
                "match_score": 0,
                "matching_skills": [],
                "missing_skills": [],
                "recommendations": [],
                "error": str(e),
            }