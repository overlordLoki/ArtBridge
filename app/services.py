import json, random, uuid, time, os
from io import BytesIO
from flask import jsonify, send_file
from .utils import get_last_image, queue_prompt
from config.config import OUTPUTFOLDER, workflow_file_path, server_address

def is_online_service():
    return jsonify({"online": True})  # Adjusted to always be online for now

def generate_image_service(request_data):
    try:
        prompt_text = request_data.get('prompt')
        steps = request_data.get('steps', 20)
        dev_model = 'flux1-dev.safetensors'
        schnell_model = 'flux1-schnell.safetensors'

        # Load workflow from JSON file
        with open(workflow_file_path, 'r') as f:
            workflow = json.load(f)

        # Update workflow details
        workflow["6"]["inputs"]["text"] = prompt_text
        workflow["25"]["inputs"]["noise_seed"] = random.randint(0, 1000000000000000)
        workflow["17"]["inputs"]["steps"] = steps
        workflow["12"]["inputs"]["unet_name"] = schnell_model

        # Get last generated image for comparison
        last_img = get_last_image()

        # Queue the prompt
        client_id = str(uuid.uuid4())
        queue_prompt(workflow, client_id)

        # Wait for a new image to be generated
        while get_last_image() == last_img:
            time.sleep(1)

        # Send the generated image back to the client
        path = f"{OUTPUTFOLDER}/{get_last_image()}"
        with open(path, 'rb') as f:
            image_data = f.read()

        image_stream = BytesIO(image_data)
        return send_file(image_stream, mimetype='image/png', as_attachment=True, download_name='generated_image.png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def test_image_service():
    file_path = '/path/to/example.png'
    
    try:
        with open(file_path, 'rb') as f:
            image_data = f.read()

        image_stream = BytesIO(image_data)
        return send_file(image_stream, mimetype='image/png', as_attachment=True, download_name='test_image.png')
    except FileNotFoundError:
        return "File not found", 404
