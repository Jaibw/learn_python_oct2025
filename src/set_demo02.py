bucket01 = {
    "apple", "banana", "orange", "strawberry"
}

bucket02 = {
    "banana", "cherry", "orange", "pineapple"
}

print("Union: ", bucket01 | bucket02)
print("Intersection: ", bucket01 & bucket02)
print("Difference: ", bucket01 - bucket02)
print("Symmetric difference: ", bucket01 ^ bucket02)
