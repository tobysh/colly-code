capitals={
    "France":"Paris",
    "England":"London",
    "Germany":"Munich"
}

capitals.update({"Germany":"Berlin"})

for capital in capitals.items():
    print(f"The capital of {capital[0]} is {capital[1]}")