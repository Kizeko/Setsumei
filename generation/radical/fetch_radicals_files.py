from generation.utils.fetch_files import download_file, delete_file, ungzip_file

RADKFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/radkfile.gz'
KRADFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz'


def fetch_radical_files():
    print('Fetching radical files...')
    download_file(RADKFILE_URL, 'data/radkfile.gz')
    download_file(KRADFILE_URL, 'data/kradfile.gz')
    ungzip_file('data/radkfile.gz')
    ungzip_file('data/kradfile.gz')
    delete_file('data/radkfile.gz')
    delete_file('data/kradfile.gz')
    print('Done fetching radical files.')


fetch_radical_files()
