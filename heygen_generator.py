import os
import time
import requests
from dotenv import load_dotenv
import logging
from typing import Optional, Dict, Any

class HeyGenVideoProcessor:
    def __init__(self):
        # Configure logging
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

        # Load environment variables
        load_dotenv()
        self.api_key = os.getenv('HEYGEN_API_KEY')
        if not self.api_key:
            raise ValueError("HEYGEN_API_KEY not found in .env file")

    def generate_video(self, 
                       avatar_id: str = "Monica_inSleeveless _20220819", 
                       input_text: str = "Bonjour", 
                       voice_id: str = "ff2ecc8fbdef4273a28bed7b5e35bb57") -> str:
        """
        Generate a video using HeyGen API
        
        :param avatar_id: ID of the avatar to use
        :param input_text: Text to be spoken
        :param voice_id: ID of the voice to use
        :return: Video generation task ID
        """
        url = "https://api.heygen.com/v2/video/generate"
        headers = {
            'X-Api-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        payload = {
            "video_inputs": [
                {
                    "character": {
                        "type": "avatar",
                        "avatar_id": avatar_id,
                        "avatar_style": "normal"
                    },
                    "voice": {
                        "type": "text",
                        "input_text": input_text,
                        "voice_id": voice_id,
                        "speed": 1.1
                    },
                    "background": {
                        "type": "color",
                        "value": "#008000"
                    }
                }
            ],
            "dimension": {
                "width": 1280,
                "height": 720
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            
            video_data = response.json()
            video_id = video_data.get('data', {}).get('video_id')
            
            if not video_id:
                raise ValueError("No video ID received from HeyGen")
            
            self.logger.info(f"Video generation started with ID: {video_id}")
            return video_id
        
        except requests.exceptions.RequestException as req_err:
            self.logger.error(f"Video generation request failed: {req_err}")
            raise

    def check_video_status(self, video_id: str, max_attempts: int = 120, polling_interval: int = 5) -> Optional[str]:
        """
        Check video status with consistent polling interval
        
        :param video_id: ID of the video to check
        :param max_attempts: Maximum number of status check attempts
        :param polling_interval: Time between status checks in seconds
        :return: Video URL when completed, None otherwise
        """
        url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
        headers = {
            "accept": "application/json",
            "x-api-key": self.api_key
        }

        for attempt in range(max_attempts):
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                
                status_data: Dict[str, Any] = response.json()
                status = status_data.get('data', {}).get('status')
                
                self.logger.info(f"Attempt {attempt + 1}: Video status is {status}")

                if status == 'completed':
                    video_url = status_data.get('data', {}).get('video_url')
                    if video_url:
                        self.logger.info(f"Video generation completed. URL: {video_url}")
                        return video_url
                
                elif status == 'failed':
                    error = status_data.get('data', {}).get('error')
                    self.logger.error(f"Video generation failed: {error}")
                    return None

                # Consistent 5-second interval
                self.logger.info(f"Waiting {polling_interval} seconds before next check")
                time.sleep(polling_interval)

            except requests.exceptions.RequestException as req_err:
                self.logger.error(f"Status check request failed: {req_err}")
                time.sleep(polling_interval)

        self.logger.warning("Max attempts reached. Video not completed.")
        return None

    def process_video(self, 
                      input_text: str = "Bonjour", 
                      avatar_id: str = "Monica_inSleeveless _20220819", 
                      voice_id: str = "ff2ecc8fbdef4273a28bed7b5e35bb57") -> Optional[str]:
        """
        Comprehensive method to generate and retrieve video
        
        :return: Video URL or None
        """
        try:
            video_id = self.generate_video(
                avatar_id=avatar_id, 
                input_text=input_text, 
                voice_id=voice_id
            )
            return self.check_video_status(video_id)
        
        except Exception as e:
            self.logger.error(f"Video processing failed: {e}")
            return None

# Example usage
if __name__ == "__main__":
    processor = HeyGenVideoProcessor()
    video_url = processor.process_video(input_text="Hello, world!")
    
    if video_url:
        print(f"Video URL: {video_url}")
    else:
        print("Failed to generate video.")