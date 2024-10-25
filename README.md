
# ArtBridge

**ArtBridge** is a middleware designed to facilitate communication between a frontend and an AI-powered art generation backend. It allows users to generate images from prompts, fetch historical data, and serve images to the client seamlessly.

## Features

- **Generate Images**: Accepts a prompt and returns a generated image in PNG format.
- **History Retrieval**: Fetches the history of image generations.
- **Serve Images**: Sends the generated images to the frontend via API.
- **CORS Support**: Allows cross-origin resource sharing for easy frontend integration.
  
## Requirements

- Python 3.x
- Flask
- Flask-CORS
- Required Libraries:
  - `urllib`
  - `json`
  - `os`
  - `random`
  - `uuid`
  - `time`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ArtBridge.git
    cd ArtBridge
    ```

2. Install required dependencies:
    ```bash
    pip install Flask Flask-CORS
    ```

3. Make sure you have your backend art generation system running at the server address specified in the script.

## Usage

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Access the API endpoints.

### Endpoints

#### Check Online Status
- **URL**: `/is_online`
- **Method**: `GET`
- **Response**: Returns the server online status.

#### Generate Image
- **URL**: `/generate_image`
- **Method**: `POST`
- **Body**:
    ```json
    {
      "prompt": "your art description",
      "steps": 20
    }
    ```
- **Response**: Returns a PNG image generated based on the prompt.

#### Serve Test Image
- **URL**: `/test_image`
- **Method**: `GET`
- **Response**: Returns a sample image from the output folder.

## Configuration

- **Server Address**: Set the `server_address` variable to point to the art generation backend server.
- **Output Folder**: Update the `OUTPUTFOLDER` variable to match the path of the folder where the generated images are stored.
