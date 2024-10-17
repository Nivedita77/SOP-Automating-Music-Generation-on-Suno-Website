import requests

# List of tokens for multiple accounts
TOKENS = [
    'cqaggnfx5vl87axa818rwpv5924zwtqm1ze9erdf',  # Account 1
    'whuf2ohhbg3ztc8x8pl6z8fx0jp04l2vza7x3fvf',  # Account 2 or you can add more tokens if needed
]

BASE_URL = 'https://studio-api.prod.suno.com/api/generate/v2/'

# Function to generate music using the provided prompt
def generate_music(prompt, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "prompt": prompt,
        "parameters": {}
    }
    
    response = requests.post(BASE_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        song_url = data.get('audio_url')  # Extract song URL from response
        if song_url:
            print(f"Music generated for prompt '{prompt}': {song_url}")
        return song_url
    else:
        print(f"Failed to generate music with token {token}: {response.status_code} - {response.text}")
        return None

# Function to download the song from the given URL
def download_song(song_url, filename):
    response = requests.get(song_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Song downloaded and saved as {filename}")
    else:
        print(f"Failed to download the song. Status code: {response.status_code}")

# Main function to automate the process for one song with account switching
def automate_music_generation(prompt):
    print(f"Starting music generation process...\n")
    
    for token in TOKENS:
        print(f"Using token: {token[:5]}...")  # Print only part of the token for visibility
        
        # Generate music
        song_url = generate_music(prompt, token)
        
        # If music is generated successfully, download the song
        if song_url:
            filename = f"{prompt.replace(' ', '_')}_song.mp3"
            download_song(song_url, filename)
            break  # Exit the loop after successful download
        else:
            print("Switching to the next account due to failure.\n")
    
    else:
        print("All accounts failed to generate music.")

# Example of running the full process for one song
if __name__ == "__main__":
    prompt = "a scary song"  # Example prompt
    automate_music_generation(prompt)
