import requests
 
api_key = 'live_gRBXtHLTaRaZkLRP14QajRVGnAOxF4EsHCxzONeDNFW6FxKJGDZMZVlHNnftiGzY'
BASE_URL = "https://api.thecatapi.com/v1"
headers = {'x-api-key': api_key}
def get_random_image():
    try:
        response = requests.get('https://api.thecatapi.com/v1/images/search', headers=headers)
        response.raise_for_status()
        cat_image = response.json()[0]
        print(f"Here is a random Cat image! {cat_image["url"]}")
    except:
        e = requests.exceptions.RequestException
        print(f"Error fetching cat image: {e}")
        if response.status_code == 200:
            cat_image = response.json()[0]
        print(f"Cat Image URL: {cat_image['url']}")
    print(f'Cat_id',cat_image['id'])
        

def vote_cat(cat_id):
    try:
        date = {"image_id": cat_id}
        response = requests.post(f"{BASE_URL}/favourites", json=vote_cat, headers=headers)
        response.raise_for_status()

        favorite = response.json()
        cookies = input('Enter ID: ')        
        print(f"Successfully added cat to favorites! Favorite ID: {favorite[cookies]}")    
    except requests.exceptions.RequestException as e:        
        print(f"Error favoriting cat: {e}")
    if response.status_code == 201:  
        print("Successfully voted for the cat image!")

def main():
    print("Welcome to the CatAPI Client")
    while True:
          print('\nOption:')
          print("1: Get Cat Image")
          print("2: Favourite Cat Image (Requires Cat Image ID)")
          print("3: Exit")

          choice = input("Enter your choice: ").strip()
          if choice == '1':
            get_random_image()
          elif choice == '2':
            cat_id = input("Enter Cat Image ID to favourite the Image")
            vote_cat(cat_id)
          elif choice == '3':
              print("You have Exited")
              break
          else:
              print("Invalid Choice, pick the right one")

if __name__ == '__main__':
    main()

                    