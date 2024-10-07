# Hello, this is Nerds From Space

This repo contains our code for the 2024 Windsor NASA Space Apps Challenge

# Todo List

- [ ] Svelte frontend
    - [ ] Main Page
    - [ ] Detailed Page
    - [ ] Notification Page
        - [ ] Rough draft of how the page will be laid out
- [ ] Flask backend
    - [ ] Complete app.py server
    - [ ] Change API queries to be more specific
    - [ ] Submit coordinates for notifications to SQL server
    - [ ] Landsat 8 & 9 Position Prediction Function
    - [ ] Query SQL servers to see if emails need to be sent
- [ ] Make everything work together
    - [ ] Make a flask-svelte project
    - [ ] Integrate the Svelte frontend to run on the Flask backend
    - [ ] Change the Svelte frontend to interface with the existing Flask functions

# Suggested Objectives

- [x] Allow users to define the target location. Will they specify the place name, latitude and longitude, or select a location on a map?

- [ ] Determine when a Landsat satellite is passing over the defined target location.

- [ ] Enable users to select the appropriate lead time for notifications about the overpass time and the method of notification.

- [ ] Display a 3x3 grid including a total of 9 Landsat pixels centered on the user-defined location (target pixel).

- [ ] Determine which Landsat scene contains the target pixel using the Worldwide Reference System-2 (WRS-2) and display the Landsat scene extent on a map.

- [ ] Allow users to set a threshold for cloud coverage (e.g., only return data with less than 15% land cloud cover).

- [ ] Permit users to specify whether they want access to only the most recent Landsat acquisition or acquisitions spanning a particular time span.

- [ ] Acquire scene metadata such as acquisition satellite, date, time, latitude/longitude, Worldwide Reference System path and row, percent cloud cover, and image quality.

- [ ] Access and acquire Landsat SR data values (and possibly display the surface temperature data from the thermal infrared bands) for the target pixel by leveraging cloud data catalogs and existing applications.

- [ ] Display a graph of the Landsat SR data along the spectrum (i.e., the spectral signature) in addition to scene metadata.

- [ ] Allow users to download or share data in a useful format (e.g., csv).
