from jobs import read


def get_unique_job_types(path):
    result = read(path)
    unique_jobs = set(job["job_type"] for job in result if job["job_type"])
    return list(unique_jobs)


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    result = read(path)
    unique_industries = set(
        job["industry"] for job in result if job["industry"]
    )
    return list(unique_industries)


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    result = read(path)
    unique_salaries = set(
        int(job["max_salary"]) for job in result if job["max_salary"].isdigit()
    )
    return max(list(unique_salaries))


def get_min_salary(path):
    result = read(path)
    unique_salaries = set(
        int(job["min_salary"]) for job in result if job["min_salary"].isdigit()
    )
    return min(list(unique_salaries))


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("missing min_salary or max_salary")
    if not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError("min_salary and max_salary must be valid integers")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("max_salary must be greater than min_salary")
    if not isinstance(salary, int):
        raise ValueError("salary must be valid integer")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    valid_jobs = [
        job
        for job in jobs
        if (
            isinstance(job["min_salary"], int)
            and isinstance(job["max_salary"], int)
            and job["min_salary"] < job["max_salary"]
        )
    ]
    if not isinstance(salary, int):
        return []
    return [job for job in valid_jobs if matches_salary_range(job, salary)]
