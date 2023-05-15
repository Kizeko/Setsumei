import requests
import re

from generation.utils.fetch_files import download_file, untgz_file, delete_file


def fetch_vocabulary_files():
    furigana_url = get_github_resource("Doublevil", "JmdictFurigana", "^JmdictFurigana.*.json")
    jmdict_all_url = get_github_resource("scriptin", "jmdict-simplified", "^jmdict-all.*.json.tgz")
    download_file(furigana_url, "data/JmdictFurigana.json")
    download_file(jmdict_all_url, "data/jmdict-all.json.tgz")
    untgz_file("data/jmdict-all.json.tgz")
    delete_file("data/jmdict-all.json.tgz")


def get_github_resource(username: str, repository: str, pattern: str):
    # Fetch the latest release
    response = requests.get(f"https://api.github.com/repos/{username}/{repository}/releases/latest")
    response.raise_for_status()  # Raise exception if invalid response
    release_data = response.json()

    json_asset = next((asset for asset in release_data["assets"] if re.search(pattern, asset["name"])), None)

    if json_asset is None:
        raise Exception("No JSON asset found in the latest release")

    # Get the URL of the JSON asset
    return json_asset["browser_download_url"]


fetch_vocabulary_files()
