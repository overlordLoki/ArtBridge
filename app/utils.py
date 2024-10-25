import os
import urllib.request
import urllib.parse
import json
from config.config import server_address, OUTPUTFOLDER

def get_last_image():
    files = os.listdir(OUTPUTFOLDER)
    files = [f for f in files if f.endswith('.png')]
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(OUTPUTFOLDER, x)))
    return files[-1]

def queue_prompt(workflow, client_id):
    p = {"prompt": workflow, "client_id": client_id}
    data = json.dumps(p).encode('utf-8')
    req = urllib.request.Request(f"http://{server_address}/prompt", data=data)
    return json.loads(urllib.request.urlopen(req).read())
