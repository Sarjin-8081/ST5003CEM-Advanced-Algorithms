"""
Dataset loader for ST5003CEM Task 1 (Advanced Data Structures).

Loads worldcities.csv and produces reproducible subsets of N cities
in two orderings:
  - random   : shuffled order (average-case insertion)
  - sorted   : sorted by id ascending (worst-case insertion for plain BST)

Each city record is reduced to (id, name, lat, lng) -- id is used as the
key for BST / AVL / Hash Table; lat/lng could be used for a route-planning
distance calc later in Task 2 if you want to reuse this same file.
"""

import csv
import math
import random

SOURCE_CSV = "/mnt/user-data/uploads/worldcities.csv"
SEED = 42  # fixed seed -> identical subsets every run, for reproducibility
REF_LAT, REF_LNG = 51.5072, -0.1276  # London -- reference point for distance


def load_all_cities(path=SOURCE_CSV):
    """Load the full city list into memory as lightweight dicts."""
    cities = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lat, lng = float(row["lat"]), float(row["lng"])
            cities.append({
                "id": int(row["id"]),
                "name": row["city_ascii"],
                "lat": lat,
                "lng": lng,
                "population": int(float(row["population"])) if row["population"] else 0,
                "distance": math.dist((lat, lng), (REF_LAT, REF_LNG)),
            })
    return cities


def get_subset(n, ordering="random", seed=SEED):
    """
    Return a list of n city dicts.

    ordering: "random" -> random sample, shuffled
              "sorted" -> random sample, then sorted by id ascending
    """
    all_cities = load_all_cities()
    rng = random.Random(seed)
    sample = rng.sample(all_cities, n)  # sample without replacement

    if ordering == "random":
        rng.shuffle(sample)
    elif ordering == "sorted":
        sample.sort(key=lambda c: c["id"])
    else:
        raise ValueError("ordering must be 'random' or 'sorted'")

    return sample


if __name__ == "__main__":
    # quick sanity check
    for n in (100, 1000, 10000):
        for ordering in ("random", "sorted"):
            subset = get_subset(n, ordering)
            assert len(subset) == n
            print(f"N={n:>6}  ordering={ordering:<7}  "
                  f"first_id={subset[0]['id']}  last_id={subset[-1]['id']}")