from generation.utils.fetch_files import download_file, delete_file, ungzip_file

KANJIDIC2_URL = 'http://www.edrdg.org/kanjidic/kanjidic2.xml.gz'
KRADFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz'
RADKFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/radkfile.gz'


def fetch_kanji_files():
    print('Fetching kanji files...')
    download_file(KANJIDIC2_URL, 'data/kanjidic2.xml.gz')
    download_file(KRADFILE_URL, 'data/kradfile.gz')
    download_file(RADKFILE_URL, 'data/radkfile.gz')
    ungzip_file('data/kanjidic2.xml.gz')
    ungzip_file('data/kradfile.gz')
    ungzip_file('data/radkfile.gz')
    delete_file('data/kanjidic2.xml.gz')
    delete_file('data/kradfile.gz')
    delete_file('data/radkfile.gz')
    print('Done fetching kanji files.')
