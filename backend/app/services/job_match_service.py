from app.models.job_match import JobMatch


class JobMatchService:

    def save_match(
        self,
        db,
        resume_id: int,
        job_description: str,
        result: dict,
    ):

        match = JobMatch(
            resume_id=resume_id,
            job_description=job_description,
            match_score=result["match_score"],
            matching_skills=result["matching_skills"],
            missing_skills=result["missing_skills"],
            recommendations=result["recommendations"],
        )

        db.add(match)
        db.commit()
        db.refresh(match)

        return match