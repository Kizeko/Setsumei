from setsumei.generation.utils.fetch_files import download_file, unzip_file, delete_file

KANJIDIC2_URL = 'http://www.edrdg.org/kanjidic/kanjidic2.xml.gz'
KRADFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/kradfile.gz'
RADKFILE_URL = 'http://ftp.edrdg.org/pub/Nihongo/radkfile.gz'


def fetch_kanji_files():
    print('Fetching kanji files...')
    download_file(KANJIDIC2_URL, 'kanjidic2.xml.gz')
    download_file(KRADFILE_URL, 'kradfile.gz')
    download_file(RADKFILE_URL, 'radkfile.gz')
    unzip_file('kanjidic2.xml.gz')
    unzip_file('kradfile.gz')
    unzip_file('radkfile.gz')
    delete_file('kanjidic2.xml.gz')
    delete_file('kradfile.gz')
    delete_file('radkfile.gz')
    print('Done fetching kanji files.')
