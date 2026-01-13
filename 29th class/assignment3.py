courses = {
    "Data Structures": {"Alice": 85, "Bob": 90, "Charlie": 75},
    "Algorithms": {"Alice": 95, "Dave": 88},
    "Machine Learning": {"Bob": 82, "Eve": 91, "Frank": 78}
}

courses["Data Structures"]["Alice"] = 90
courses["Data Structures"].pop("Charlie")
courses["Web Development"] = {"Grace": 92, "Henry": 85}

courses["Algorithms"].setdefault("Bob", 80)
courses.pop("Machine Learning", None)

ds = courses.get("Data Structures")
print("Average grade in Data Structures:", round(sum(ds.values())/len(ds),2))

print("Updated Courses:", courses)
