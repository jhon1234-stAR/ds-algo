
queue = ["Alice", "Bob", "Charlie"]

# New arrival
queue.append("David")

while queue:
    person = queue.pop(0)
    print(f"{person} bought a ticket.")
