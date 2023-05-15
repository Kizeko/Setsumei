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


def create_radical_to_kanji():
    with open('data/radkfile', 'r', encoding='EUC-JP') as f:
        data = f.readlines()
    radicals_to_kanji_dict = {}
    radicals_to_kanji_array = []
    counter = 0
    for line in data:
        if line[0] == "#":
            continue
        if line[0] == "$":
            counter += 1
            if len(radicals_to_kanji_dict) > 0:
                radicals_to_kanji_array.append(radicals_to_kanji_dict)
            radical = line[2]
            radicals_to_kanji_dict = {}
            stroke_count = line[4:6].strip().replace("\n", "")
            radicals_to_kanji_dict["radical"] = radical
            radicals_to_kanji_dict["stroke_count"] = int(stroke_count)
            radicals_to_kanji_dict["literals"] = []
            continue
        for character in line:
            if character == "" or character == "\n":
                continue
            radicals_to_kanji_dict["literals"].append(character)

        if data.index(line) == len(data) - 1:
            radicals_to_kanji_array.append(radicals_to_kanji_dict)

    with open('build/radical_to_kanji.json', 'w') as f:
        json.dump(radicals_to_kanji_array, f, indent=4, ensure_ascii=False)
