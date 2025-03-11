# positional and keyword arguments
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"{location} is an amazing place")

# keyword arguments

greet_with(name="Rakshit Bagait", location="Jaipur")
greet_with( location="Jaipur",name="Rakshit Bagait")

# positional arguments


greet_with("Rakshit Bagait", "Jaipur")