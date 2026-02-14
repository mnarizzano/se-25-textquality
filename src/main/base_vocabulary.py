def load_voc(voc_path):
    with open(voc_path, encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}

class BaseVocabulary:
    def __init__(self):
        self.fo = load_voc("VdB/FO.txt")
        self.au = load_voc("VdB/AU.txt")
        self.ad = load_voc("VdB/AD.txt")

