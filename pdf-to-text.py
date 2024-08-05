import pathlib
import os
import tqdm

# Ensure tqdm is installed
try:
    import tqdm
except ImportError:
    os.system('pip install tqdm')

# Download the PDF if it doesn't exist
if not pathlib.Path('Iterative-Attention.pdf').exists():
    os.system('curl -o Iterative-Attention.pdf https://arxiv.org/pdf/2103.03206')

# Define the page range
first = 8
last = 11

# Create output directory
os.makedirs('output', exist_ok=True)
# Create output directory and subdirectories
os.makedirs('output/image-files', exist_ok=True)
os.makedirs('output/text-files', exist_ok=True)

# Extract images from the specified range of PDF pages
print("Extracting images...")
image_extraction_command = f'pdftoppm Iterative-Attention.pdf -f {first} -l {last} output/image-files/images -jpeg'
print(f"Running command: {image_extraction_command}")
os.system(image_extraction_command)

# List the files in the output directory
print("Listing files in output directory after extracting images...")
os.system('ls output')

from PIL import Image
# Display the first extracted image
image_path = f"output/image-files/images-{first}.jpg"
if pathlib.Path(image_path).exists():
    img = Image.open(image_path)
    img.thumbnail([600, 600])
    img.show()
else:
    print(f"Image {image_path} not found.")

# Extract text from the specified range of PDF pages
print("Extracting text...")
for page_number in range(first, last + 1):
    page_str = f"{page_number:03d}"
    text_extraction_command = f'pdftotext -f {page_number} -l {page_number} Iterative-Attention.pdf output/text-files/text-{page_str}.txt'
    print(f"Running command: {text_extraction_command}")
    os.system(text_extraction_command)

# List the files in the output directory
print("Listing files in output directory after extracting text...")
os.system('ls output')

# Display the content of the first extracted text file
text_file_path = f'output/text-files/text-{first:03d}.txt'
if pathlib.Path(text_file_path).exists():
    print(f"Content of {text_file_path}:")
    os.system(f'cat {text_file_path}')
else:
    print(f"Text file {text_file_path} not found.")

