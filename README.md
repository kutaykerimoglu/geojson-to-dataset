# Street View Image Scraper

This repository contains Python scripts for scraping street view images from Google Maps for academic purposes. The code is organized into several modules:

## 1. `main.py`

This script is the main entry point for the street view image scraping process. It imports necessary modules and performs the following tasks:

- Reads a GeoJSON dataset from the file `data.geojson`.
- Creates output directories based on configuration settings.
- Iterates over each row in the dataset and scrapes street view images for specified locations.
- Uses functions from `polygon_utils.py`, `config.py`, and `street_view_image.py`.

## 2. `polygon_utils.py`

This module provides utility functions for working with geometric shapes, particularly polygons. It includes the following functions:

- `get_random_point_in_polygon(polygon: Polygon) -> Point`: Generates a random point within a given polygon.
- `get_random_point_in_multipolygon(multipolygon: MultiPolygon) -> Point`: Generates a random point within a multipolygon.
- `get_random_point_in_geometry(geometry) -> Point`: Determines the type of geometry and generates a random point accordingly.

## 3. `street_view_image.py`

This module defines a class `StreetViewImage` for interacting with Google Street View API. It includes methods for fetching street view images and metadata. Key functionalities include:

- `get_image_from_google(heading)`: Fetches street view image for a specific location and heading.
- `get_meta_of_location()`: Retrieves metadata of a given location from Google Street View API.
- `is_meta_ok()`: Checks if the metadata status is 'OK', indicating successful retrieval.

## 4. `config.py`

This module contains configuration settings for the street view image scraper. It includes constants such as file paths, image parameters, and Google API key.

**Note**: To use this scraper, you will need to obtain a Google API key and configure it in `config.py`.

The repository aims to provide a simple and modular solution for scraping street view images for academic research or analysis.
