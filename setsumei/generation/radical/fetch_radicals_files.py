from setsumei.generation.utils.fetch_files import download_file, unzip_file, delete_file

RADKFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/radkfile.gz'
KRADFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz'


def fetch_radical_files():
    print('Fetching radical files...')
    download_file(RADKFILE_URL, 'radkfile.gz')
    download_file(KRADFILE_URL, 'kradfile.gz')
    unzip_file('radkfile.gz')
    unzip_file('kradfile.gz')
    delete_file('radkfile.gz')
    delete_file('kradfile.gz')
    print('Done fetching radical files.')
