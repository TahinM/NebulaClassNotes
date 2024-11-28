import requests

# PokeAPI endpoint for listing Pokémon
url = "https://pokeapi.co/api/v2/pokemon?limit=1000"  # Adjust the limit as needed

# Make the request
response = requests.get(url)
data = response.json()

# Extract and print Pokémon names
if 'results' in data:
    pokemon_names = [pokemon['name'] for pokemon in data['results']]
    pokemon_type = [pokemon['type'] for pokemon in data['results']]
    
    print("List of Pokémon:")
    for name in pokemon_names:
        print(name)
    for name in pokemon_type:
        print(name)
else:
    print("Couldn't fetch Pokémon data. Try again!")
