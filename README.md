# bhashan2pathtak
Simple Python application to convert speech into text using Wit.ai

## Prerequisites for MacOS
* `brew install portaudio`
* `brew install flac`

## Installation
1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   Note: This project uses PyAudio 0.2.14. If you encounter issues with installation, try upgrading to this version.
3. Sign up for a Wit.ai account and create a new app to get an access token

## Configuration
To run this application, you need to provide your Wit.ai token. You have two options:

1. Environment Variable:
   Set the `WIT_AI_TOKEN` environment variable:
   ```
   export WIT_AI_TOKEN=your_wit_ai_token_here
   ```

2. Configuration File:
   Copy `config.json.example` to `config.json` and add your Wit.ai token:
   ```
   cp config.json.example config.json
   ```
   Then edit `config.json` and replace `your_wit_ai_token_here` with your actual token.

**Important:** Never commit your `config.json` file to the repository. It's listed in `.gitignore` to prevent accidental commits.

## How to run
After setting up the configuration:
```
python3 speech_to_text.py
```

## Features
- Continuous speech recognition
- Improved accuracy using Wit.ai
- Ambient noise adjustment
- Error handling and user-friendly feedback

## Troubleshooting
If you encounter any issues with PyAudio, make sure you have version 0.2.14 installed:
```
pip install PyAudio==0.2.14
```

For any other issues, please check the Wit.ai documentation or open an issue in this repository.