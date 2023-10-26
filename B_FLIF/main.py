from PIL import Image
from utility import *
import sys
import os
# Get the path to the 'lib' directory within your project
lib_path = os.path.join(os.path.dirname(__file__), 'lib')

# Add the 'lib' directory to sys.path
sys.path.append(lib_path)
from lib.pyflif.flif_convenience import write_flif, read_flif, imwrite, imread

def check_folder():
    folder_input_path = 'res/'
    folder_output_path = 'output/'
    create_folder(folder_input_path)
    create_folder(folder_output_path)


def print_compression_info(input_file_name, output_file_name):
    original_size = Compression.get_file_size(input_file_name)
    compressed_size = Compression.get_file_size(output_file_name)
    compression_ratio = Compression.calculate_compression_ratio(
        original_size, compressed_size)

    print('**************************************************')
    print(f'File: {input_file_name}')
    print(f'Original Size: \t\t{original_size:>8,} \t bytes')
    print(f'Compressed Size: \t{compressed_size:>8,} \t bytes')
    print(f'Compression Ratio: \t{compression_ratio:.4f}')
    print('--------------------------------------------------\n\n')


def compress_as_jpeg(input_file_name, output_file_name):
    check_folder()
    image = Image.open(input_file_name)
    image.save(output_file_name, 'JPEG')


def compress_as_flif(input_file_name, output_file_name):
    check_folder()
    with open(input_file_name, 'rb') as image_file:
        image_data = image_file.read()

    write_flif(output_file_name, image_data)


if __name__ == "__main__":
    folder_input_path = 'res/'
    folder_output_path = 'output/'
    input_file_name = joinPath(folder_input_path, 'file.tiff')

    output_jpeg_file_name = joinPath(folder_output_path, "output_file.jpg")
    compress_as_jpeg(input_file_name, output_jpeg_file_name)

    output_flif_file__name = joinPath(folder_output_path, "output_file.flif")
    compress_as_flif(input_file_name, output_flif_file__name)
