import requests
import os

# Constants (replace with your actual token and base URL)
BASE_URL = 'https://studio-api.prod.suno.com/api/generate/v2/'  # Use the base URL you found
TOKEN = '2tl0lgf80n5baeliwka1or5xjntfdi58000g1fmm'  # Replace with your actual token
PROMPT = 'a scary song'  # Example prompt, you can change it

# Function to generate music using the provided token and prompt
def generate_music(prompt):
    headers = {
        'Authorization': f'Bearer {TOKEN}',  # Use the token for authorization
        'Content-Type': 'application/json'
    }
    
    payload = {
        "prompt": prompt,
        "parameters": {}  # Add any additional parameters if needed
    }
    
    response = requests.post(BASE_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        print("Music generation successful!")
        return data
    else:
        print(f"Failed to generate music: {response.status_code} - {response.text}")
        return None

# Function to download files (audio, image, and video)
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download {filename}: {response.status_code}")

# Main function to generate and download the music, image, and video
def automate_music_generation(prompt):
    # Generate music data
    data = generate_music(prompt)
    
    if data and 'clips' in data:
        for clip in data['clips']:
            audio_url = clip.get('audio_url')
            image_url = clip.get('image_url')
            video_url = clip.get('video_url')  # Assuming video_url exists
            clip_id = clip.get('id')
            
            # Download audio file
            if audio_url:
                audio_filename = os.path.join('downloads', f"{clip_id}_audio.mp3")
                download_file(audio_url, audio_filename)
            
            # Download image file
            if image_url:
                image_filename = os.path.join('downloads', f"{clip_id}_image.jpeg")
                download_file(image_url, image_filename)
            
            # Download video file (if video URL exists)
            if video_url:
                video_filename = os.path.join('downloads', f"{clip_id}_video.mp4")
                download_file(video_url, video_filename)
    else:
        print("No clips found in the response.")

# Example usage
if __name__ == "__main__":
    # Create a downloads directory if it doesn't exist
    os.makedirs('downloads', exist_ok=True)
    
    # Automate the music generation and download process
    automate_music_generation(PROMPT)
