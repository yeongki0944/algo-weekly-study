N, K = map(int, input().split())

# Initialize the list of people
people = list(range(1, N + 1))

# Initialize the index for the person to be removed
index = 0

# Initialize the result list
result = []


K = K-1

while people:
    # Calculate the new index
    index = (index + K) % len(people)

    # Remove the person at the calculated index
    removed_person = people.pop(index)

    # Add the removed person to the result
    result.append(removed_person)

print("<" + ", ".join(map(str, result)) + ">")