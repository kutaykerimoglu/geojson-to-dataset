import requests
from config import Config

class StreetViewImage:
    def __init__(self, location: str) -> None:
        self.radius = Config.RADIUS
        self.pitch = Config.PITCH
        self.location = location
        self.size = Config.SIZE
        self.meta = None
        self.content = None
    
    def get_image_from_google(self, heading):
        base_url = 'https://maps.googleapis.com/maps/api/streetview?'
        request_params = dict(size=self.size,
                              location=self.location,
                              radius=self.radius,
                              heading=heading,
                              key=Config.GOOGLE_API_KEY)
        response = requests.get(url=base_url, params=request_params)
        self.content = response.content
        return self.content
    
    def get_meta_of_location(self):
        base_url = 'https://maps.googleapis.com/maps/api/streetview/metadata?'
        request_params = dict(location=self.location,
                              radius=self.radius,
                              key=Config.GOOGLE_API_KEY)
        response = requests.get(url=base_url, params=request_params)
        self.meta = response.json()
        return self.meta
    
    def is_meta_ok(self):
        return self.meta['status'] == 'OK'

    