def instructorWithLongestName(instructors):
    return max(instructors, key=lambda instructor: len(instructor["name"]), default=None)

print(instructorWithLongestName([
  {"name": "Samuel", "course": "iOS"},
  {"name": "Jeremiah", "course": "Data"},
  {"name": "Ophilia", "course": "Web"},
  {"name": "Donald", "course": "Web"}
]))  
