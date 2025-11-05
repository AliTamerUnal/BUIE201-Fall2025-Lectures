import requests

def get_author_works(author_olid, limit=1000):
    """
    Fetches works for an author given their OL ID (e.g., "OL26320A").
    Returns a list of work documents.
    """
    url = f"https://openlibrary.org/authors/{author_olid}/works.json"
    works = []
    offset = 0
    while True:
        params = {"limit": limit, "offset": offset}
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        works.extend(data.get("entries", []))
        # if there are no more, break
        if "links" in data and data["links"].get("next"):
            offset += limit
        else:
            break
    return works

def count_works_in_period(works, year_from, year_to):
    """
    Counts works whose `first_publish_year` is between year_from and year_to inclusive.
    """
    count = 0
    for w in works:
        fy = w.get("first_publish_year")
        if fy is not None and year_from <= fy <= year_to:
            count += 1
    return count

def main():
    # OLID for Tolkien; you may want to verify via the authors search API
    author_olid = "OL26320A"  # J. R. R. Tolkien
    works = get_author_works(author_olid)
    print(f"Total works found for author {author_olid}: {len(works)}")

    year_from = 2000
    year_to   = 2010
    cnt = count_works_in_period(works, year_from, year_to)
    print(f"Number of works with first_publish_year between {year_from} and {year_to}: {cnt}")



main()