import requests
import os
from dotenv import load_dotenv


class VideoAggregator:
    def __init__(self):
        self.generated_video = None
        self.template_id = "4abe1b16-390c-45a4-910f-19faea4fbc82"

    def generate_video(self, image_urls, headlines):
        load_dotenv()
        v_api_key = os.getenv("VIDEO_API_KEY")
        options = {
            'template_id': f"{self.template_id}",

            "modifications": {
                "Music": "https://creatomate.com/files/assets/b5dc815e-dcc9-4c62-9405-f94913936bf5",
                "Background-1": f"{image_urls[0]}",
                "Text-1": f"{headlines[0]}",
                "Background-2": f"{image_urls[1]}",
                "Text-2": f"{headlines[1]}",
                "Background-3": f"{image_urls[2]}",
                "Text-3": f"{headlines[2]}",
                "Background-4": f"{image_urls[3]}",
                "Text-4": f"{headlines[3]}"
            }
        }

        response = requests.post(
            'https://api.creatomate.com/v1/renders',
            headers={
                'Authorization': f"{v_api_key}",
                'Content-Type': 'application/json',
            },
            json=options
        )

        return response.content
