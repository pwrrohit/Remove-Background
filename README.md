# Background Removal and Enhancement App

## Overview

This Streamlit app allows users to remove the background from images and apply various filters to enhance the processed image. Users can upload an image, select a filter to apply, and choose the format (PNG or WEBP) for downloading the final image.

## Features

- **Background Removal**: Utilizes the `rembg` library to remove the background from images.
- **Filter Options**: Apply one of the following filters to enhance the image:
  - **Smooth**: Reduces image noise.
  - **Blur**: Applies a Gaussian blur to the image.
  - **Edge Enhance**: Enhances the edges in the image.
  - **Sharpen**: Sharpens the image.
- **Format Selection**: Download the processed image in either PNG or WEBP format.

## Requirements

- Python 3.x
- Streamlit
- Pillow (PIL)
- rembg
- numpy

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pwrrohit/Remove-Background.git
   cd Remove-Background
