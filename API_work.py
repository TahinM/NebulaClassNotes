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


url = 'https://pokeapi.co/api/v2/pokemon?limit=1000'
payload = {'name': 'John Doe', 'email': 'john.doe@example.com'}
response = requests.post(url, json=payload)

if response.status_code == 201:
    print('User created successfully.')
    print(response.json())
else:
    print(f'Failed to create user. Status code: {response.status_code}')

