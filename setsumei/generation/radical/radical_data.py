import json


def create_kanji_to_radicals_data():
    with open('data/kradfile', 'r', encoding='EUC-JP') as f:
        data = f.readlines()
    kanji_to_radicals_dict = {}
    kanji_to_radicals_array = []
    for line in data:
        if line[0] == "#":
            continue
        line = line.split(" : ")
        kanji = line[0]
        radicals = line[1].replace("\n", "").split(" ")
        kanji_to_radicals_dict["literal"] = kanji
        kanji_to_radicals_dict["radicals"] = radicals
        kanji_to_radicals_array.append(kanji_to_radicals_dict)

    with open('build/kanji_to_radicals.json', 'w') as f:
        json.dump(kanji_to_radicals_array, f, indent=4, ensure_ascii=False)


create_kanji_to_radicals_data()
