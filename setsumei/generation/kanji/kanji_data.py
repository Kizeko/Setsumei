from xml.dom import minidom
import json

ALL_LABELS = ["literal", "codepoints", "radicals", "grade", "stroke_count", "frequency", "jlpt", "pinyin_readings",
              "korean_r_readings", "korean_h_readings", "onyomi_readings", "kunyomi_readings", "meanings", "nanori"]


class KanjiParser:
    """
    This class parses the kanjidic2.xml file and creates a json file with the generation.
    """
    def __init__(self, needed_labels=None):
        if needed_labels is None:
            needed_labels = ALL_LABELS
        self.needed_labels = needed_labels
        self.jlpt_data = {}
        self.get_jlpt_data()
        self.radicals_data = {}
        self.get_radicals()

    def create_json_data(self) -> None:
        """
        Creates a json file with the generation from the kanjidic2.xml file.
        :return:
        """
        file = minidom.parse('data/kanjidic2.xml')
        kanji_list = file.getElementsByTagName("character")
        data_file = {}
        characters_array = []
        data_file["version"] = "1.0.0"
        for character in kanji_list:
            kanji_data = self.get_kanji_data(character)
            characters_array.append(kanji_data)

        data_file["characters"] = characters_array

        with open("build/kanji_data.json", "w") as f:
            json.dump(data_file, f, indent=4, ensure_ascii=False)

    def get_kanji_data(self, character: minidom.Element):
        literal = character.getElementsByTagName("literal")[0].firstChild.data
        codepoints_dict = {x.getAttribute("cp_type"): x.firstChild.data for x in character.getElementsByTagName("cp_value")}
        codepoints_array = [{"type": key, "value": value} for key, value in codepoints_dict.items()]
        radicals = self.radicals_data[literal] if literal in self.radicals_data else None
        grade = int(character.getElementsByTagName("grade")[0].firstChild.data) if len(
            character.getElementsByTagName("grade")) > 0 else None
        stroke_count = int(character.getElementsByTagName("stroke_count")[0].firstChild.data)
        frequency = int(character.getElementsByTagName("freq")[0].firstChild.data) if len(
            character.getElementsByTagName("freq")) > 0 else None
        jlpt = self.jlpt_data[literal]["jlpt_new"] if literal in self.jlpt_data else None
        pinyin = []
        korean_r_reading = []
        korean_h_reading = []
        onyomi = []
        kunyomi = []
        for reading in character.getElementsByTagName("reading"):
            if reading.getAttribute("r_type") == "pinyin":
                pinyin.append(reading.firstChild.data)
            elif reading.getAttribute("r_type") == "korean_r":
                korean_r_reading.append(reading.firstChild.data)
            elif reading.getAttribute("r_type") == "korean_h":
                korean_h_reading.append(reading.firstChild.data)
            elif reading.getAttribute("r_type") == "ja_on":
                onyomi.append(reading.firstChild.data)
            elif reading.getAttribute("r_type") == "ja_kun":
                kunyomi.append(reading.firstChild.data)

        meanings_dict = {}
        for meaning in character.getElementsByTagName("meaning"):
            label = meaning.getAttribute("m_lang") if meaning.getAttribute("m_lang") else "en"
            if label not in meanings_dict:
                meanings_dict[label] = []
            meanings_dict[label].append(meaning.firstChild.data)

        meanings_array = [{"lang": key, "value": value} for key, value in meanings_dict.items()]

        nanori = [x.firstChild.data for x in character.getElementsByTagName("nanori")]

        return {
            "literal": literal,
            "codepoints": codepoints_array,
            "radicals": radicals,
            "grade": grade,
            "stroke_count": stroke_count,
            "frequency": frequency,
            "jlpt": jlpt,
            "pinyin_readings": pinyin,
            "korean_r_readings": korean_r_reading,
            "korean_h_readings": korean_h_reading,
            "onyomi_readings": onyomi,
            "kunyomi_readings": kunyomi,
            "meanings": meanings_array,
            "nanori": nanori
        }

    def get_radicals(self):
        # 唖 : ｜ 一 口
        with open('../radical/data/kradfile', 'r', encoding='EUC-JP') as f:
            for line in f:
                if line[0] == "#":
                    continue
                line = line.split(" : ")
                kanji = line[0]
                radicals = line[1].replace("\n", "").split(" ")
                self.radicals_data[kanji] = radicals

    def get_jlpt_data(self):
        with open('jlpt/kanji.json', 'r') as f:
            data = json.load(f)
        self.jlpt_data = data
