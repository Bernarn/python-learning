# A dictionary stores data in key–value pairs — like a real dictionary that maps a word (key) to its definition (value).
student_details={
    "name": "Bernard",
    "age":22,
    "nationality":"Beninese"
}
# Accessing and Modifying Data
student_details()

| Method     | Example              | Meaning                                      |
| ---------- | -------------------- | -------------------------------------------- |
| `keys()`   | `student.keys()`     | Returns all keys                             |
| `values()` | `student.values()`   | Returns all values                           |
| `items()`  | `student.items()`    | Returns key–value pairs                      |
| `pop(key)` | `student.pop("age")` | Removes a specific key                       |
| `get(key)` | `student.get("age")` | Safely get a value (no error if key missing) |
