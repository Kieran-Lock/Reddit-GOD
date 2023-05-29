from base64 import b64decode
from io import BytesIO
from requests import post
from .voices import Voices


class Speech:
    API_ENDPOINT = "https://tiktoktts.com/api/functions"

    def __init__(self, text: str, voice: Voices) -> None:
        request_headers = {
            "accept": "*/*",
            "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
            "content-type": "application/json",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin"
        }
        request_body = {
            "jsonrpc": "2.0",
            "id": 27,
            "method": "generateTikTokVoice",
            "params": [{"text": text, "voice": voice.value}]
        }
        json = post(
            self.__class__.API_ENDPOINT, json=request_body, headers=request_headers
        ).json()
        self.speech = BytesIO(b64decode(json.get("result").get("base64")))

    def save_to_file(self, save_path: str) -> None:
        with open(f"{save_path}.mp3", "wb+") as f:
            f.write(bytes(self.speech.getbuffer()))
