import urllib.request
import gzip
import shutil
import os

KANJIDIC2_URL = 'http://www.edrdg.org/kanjidic/kanjidic2.xml.gz'
KRADFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz'
RADKFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/radkfile.gz'


def download_file(url, filename):
    # Get the directory of the current module
    module_dir = os.path.dirname(os.path.abspath(__file__))

    # Join the directory of the module and the filename to get the full path
    file_path = os.path.join(module_dir, filename)

    # Download the file to the path
    response = urllib.request.urlopen(url)
    with open(file_path, 'wb') as out_file:
        out_file.write(response.content)
    del response


def unzip_file(filename):
    # Get the directory of the current module
    module_dir = os.path.dirname(os.path.abspath(__file__))

    # Join the directory of the module and the filename to get the full path
    zip_file_path = os.path.join(module_dir, filename)
    unzip_file_path = os.path.join(module_dir, filename[:-3])

    print('Unzipping ' + zip_file_path + '...')
    with gzip.open(zip_file_path, 'rb') as f_in:
        with open(unzip_file_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def delete_file(filename):
    # Get the directory of the current module
    module_dir = os.path.dirname(os.path.abspath(__file__))

    # Join the directory of the module and the filename to get the full path
    file_path = os.path.join(module_dir, filename)

    print('Deleting ' + file_path + '...')
    os.remove(file_path)


def rename_file(filename, new_filename):
    # Get the directory of the current module
    module_dir = os.path.dirname(os.path.abspath(__file__))

    # Join the directory of the module and the filename to get the full path
    old_file_path = os.path.join(module_dir, filename)
    new_file_path = os.path.join(module_dir, new_filename)

    print('Renaming ' + old_file_path + ' to ' + new_file_path + '...')
    os.rename(old_file_path, new_file_path)

