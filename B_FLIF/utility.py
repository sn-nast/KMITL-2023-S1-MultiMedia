import os


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# def writeFile(folder_path, file_name, content):
#     file_path = os.path.join(folder_path, file_name)
#     with open(file_path, 'w') as file:
#         file.write(content)


def joinPath(folder_path, file_name):
    return os.path.join(folder_path, file_name)


def calculate_compression_ratio(original_size, compressed_size):
    return compressed_size / original_size


def calculate_compression_speed(original_size, compression_time):
    return original_size / compression_time


def calculate_decompression_speed(decompressed_size, decompression_time):
    return decompressed_size / decompression_time


class Compression:
    @staticmethod
    def get_file_size(file_name):
        return os.path.getsize(file_name)

    @staticmethod
    def calculate_compression_ratio(original_size, compressed_size):
        return compressed_size / original_size

    @staticmethod
    def calculate_compression_speed(original_size, compression_time):
        return original_size / compression_time

    @staticmethod
    def calculate_decompression_speed(decompressed_size, decompression_time):
        return decompressed_size / decompression_time
