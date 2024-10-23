## Suno Music Automation

## Objective
This project automates the process of music generation on the Suno website using API automation. The automation includes logging in, generating music based on user prompts, downloading the generated songs, and handling account switching if necessary.

## Steps Undertaken

### 1. Collecting the Token
- I obtained the API token required for authentication by using DevTools. First, I logged into the Suno website, then inspected the network activity via Inspect, this token is essential for making API requests.

### 2. Extracting Information from JWT
- I used [JWT.io](https://jwt.io/) to decode the token. This allowed me to inspect the claims and payload data, ensuring that the token provided the necessary permissions for the operations I intended to perform.

### 3. Verifying the Token
- The token was verified using [Postman](https://www.postman.com/). I sent a test request to the Suno API to confirm that the token was valid and functional.


### 4. Obtaining the Audio URL
- I made requests to the Suno API to generate music based on prompts and extracted the audio URL from the responses. This URL is used to download the generated songs.

### 5. Writing the Program
- I created the `program.py` file, which contains the implementation for generating music and downloading the songs. The program utilizes the API for generating music based on a prompt and handles the download of the generated songs.

### 6. Screenshots and downloaded audio as Proof
- Screenshots have been included in the repository to demonstrate the successful steps, including:
  - Verification of the token in Postman.
  - The decoding process on JWT.io.
  - audio url.
  
## Features
- **Logging In**: Utilizes API tokens for authentication.
- **Generating Music**: Sends prompts to the Suno API for music generation.
- **Downloading Songs**: Fetches the generated song URLs and downloads them.
- **Switching Accounts**: Implements logic to switch accounts if the current account runs out of credits.

## Setup Instructions
1. Clone this repository.
2. Ensure you have the `requests` library installed:
   ```bash
   pip install requests
## Important: Ensure both your initial and backup tokens and URLs are tested in Postman before running the application to avoid unexpected issues.