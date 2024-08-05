# PDF to Text and Image Converter

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Files](#project-files)
3. [How to Run](#how-to-run)
4. [Steps](#steps)
5. [Requirements](#requirements)

## Project Overview

This project is a Python script that converts PDF files into text and image files. It extracts specific pages from a PDF, converts them to JPG images, and also extracts the text content from these pages. The extracted images and text are saved in separate folders within an output directory.

## Project Files

- `pdf-to-text.py`: The main Python script that performs the PDF conversion.
- `requirements.txt`: A file listing the Python dependencies for the project.
- `Iterative-Attention.pdf`: The sample PDF file used for conversion (downloaded automatically if not present).
- `output/image-files/`: Directory where extracted images are saved.
- `output/text-files/`: Directory where extracted text files are saved.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the script:
   ```
   python pdf-to-text.py
   ```

## Steps

The script performs the following steps:

1. Checks if the required PDF file exists, downloading it if necessary.
2. Creates output directories for images and text files.
3. Extracts specified pages from the PDF as JPEG images.
4. Displays the first extracted image.
5. Extracts text from the specified PDF pages.
6. Saves extracted images and text files in their respective directories.
7. Displays the content of the first extracted text file.

## Requirements

This project uses the following tools and libraries:
- `pdftoppm` for PDF to image conversion
- `pdftotext` for PDF to text conversion
- Python Imaging Library (PIL) for image processing
- `tqdm` for progress bars (automatically installed if not present)

Please ensure you have the necessary permissions and comply with any relevant licenses when using external PDFs or tools.
