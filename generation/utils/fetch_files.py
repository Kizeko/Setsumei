import urllib.request
import tarfile
import os
import gzip
import shutil


def download_file(url, filename):
    # Download the file from `url` and save it locally under `filename`:
    print('Downloading ' + url + ' ...')
    urllib.request.urlretrieve(url, filename)


def untgz_file(filename):
    # Get the current working directory
    working_dir = os.getcwd()

    # Join the directory of the module and the filename to get the full path
    file_path = os.path.join(working_dir, filename)

    # Check if the file is a tarfile
    if tarfile.is_tarfile(file_path):
        # Untar the file and extract it next to the archive
        with tarfile.open(file_path) as tar:
            tar.extractall(os.path.dirname(file_path))


def ungzip_file(filename):
    # Get the current working directory
    working_dir = os.getcwd()

    # Join the directory of the module and the filename to get the full path
    file_path = os.path.join(working_dir, filename)

    # Output file path (remove .gz extension)
    output_file_path = file_path[:-3]

    # Decompress the file
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def delete_file(filename):
    # Get the current working directory
    working_dir = os.getcwd()

    # Join the directory of the module and the filename to get the full path
    file_path = os.path.join(working_dir, filename)

    # Delete the file
    os.remove(file_path)


def rename_file(filename, new_filename):
    # Get the directory of the current module
    module_dir = os.path.dirname(os.path.abspath(__file__))

    # Join the directory of the module and the filename to get the full path
    old_file_path = os.path.join(module_dir, filename)
    new_file_path = os.path.join(module_dir, new_filename)

    print('Renaming ' + old_file_path + ' to ' + new_file_path + '...')
    os.rename(old_file_path, new_file_path)
