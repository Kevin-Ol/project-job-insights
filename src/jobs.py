from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        beach_status_reader = csv.DictReader(
            file, delimiter=",", quotechar='"'
        )
        return [row for row in beach_status_reader]
