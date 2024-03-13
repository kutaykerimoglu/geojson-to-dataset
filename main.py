import geopandas as gpd
from street_view_image import StreetViewImage
from polygon_utils import get_random_point_in_geometry
from config import Config
import os

if __name__ == '__main__':
    dataset = gpd.read_file('data.geojson')
    os.mkdir('output')
    for i, row in dataset.iterrows():
        name = row['name']
        images_scraped = 0
        folder_name = f'output/class_{name}'
        os.makedirs(folder_name)
        images_scraped = 0
        while images_scraped < Config.IMAGE_PER_CLASS:
            point = get_random_point_in_geometry(row['geometry'])
            print(f'{point.y},{point.x}')
            svi = StreetViewImage(f'{point.y},{point.x}')
            meta = svi.get_meta_of_location()
            if svi.is_meta_ok():
                for heading in [0, 90, 180, 270]:
                    try:
                        svi.get_image_from_google(heading=heading)
                        pic_path = os.path.join(folder_name, f'{name}_image_{heading}_{images_scraped}.jpeg')
                        with open(pic_path, 'wb') as image:
                            image.write(svi.content)
                        images_scraped = images_scraped + 1
                        print(f'images scrapped for city {name} is {images_scraped}')   
                    except:
                        print(f'couldn"t find image for heading {heading} for city {name}')              

