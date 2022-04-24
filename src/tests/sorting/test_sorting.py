import pytest
from datetime import date
from src.sorting import sort_by


jobs = [
    {"max_salary": 10, "min_salary": 100, "date_posted": "2013-01-24"},
    {"max_salary": 0, "min_salary": 10, "date_posted": "2013-02-01"},
    {"max_salary": 15000, "min_salary": 0, "date_posted": "2013-02-11"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2013-01-12"},
]


def test_sort_by_criteria():
    min_salary = "min_salary"
    assert sort_by(jobs, min_salary) == jobs.sort(
        key=lambda job: int(job["min_salary"])
    )

    max_salary = "max_salary"
    assert sort_by(jobs, max_salary) == jobs.sort(
        key=lambda job: int(job["max_salary"])
    )

    date_posted = "date_posted"
    assert sort_by(jobs, date_posted) == jobs.sort(
        key=lambda job: date.fromisoformat(job["date_posted"])
    )

    key = "date"
    error_message = f"invalid sorting criteria: {key}"
    with pytest.raises(ValueError, match=error_message):
        assert sort_by(jobs, key)
