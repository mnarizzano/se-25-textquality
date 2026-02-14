class GulpeaseGrade:
    LEVELS = {
        "elem": [
            (95, "really easy to read", "icons/really_easy.png"),
            (80, "easy to read", "icons/easy.png"),
            (70, "hard to read", "icons/hard.png"),
            (55, "really hard to read", "icons/really_hard.png"),
            (0, "almost incomprehensible", "icons/impossible.png"),
        ],
        "mid": [
            (80, "really easy to read", "icons/really_easy.png"),
            (60, "easy to read", "icons/easy.png"),
            (50, "hard to read", "icons/hard.png"),
            (35, "really hard to read", "icons/really_hard.png"),
            (0, "almost incomprehensible", "icons/impossible.png"),
        ],
        "high": [
            (70, "really easy to read", "icons/really_easy.png"),
            (40, "easy to read", "icons/easy.png"),
            (30, "hard to read", "icons/hard.png"),
            (10, "really hard to read", "icons/really_hard.png"),
            (0, "almost incomprehensible", "icons/impossible.png"),
        ],
    }

    def __init__(self, index, level="elem"):
        self.grade = ""
        self.img = ""

        thresholds = self.LEVELS.get(level)
        if not thresholds:
            return

        for limit, grade, img in thresholds:
            if index >= limit:
                self.grade = grade
                self.img = img
                break

def calculate(sentences, letters, words):
    index = round(89 + ((300 * sentences - 10 * letters) / words))
    if index > 100:
        index = 100

    grades = dict()
    for level in GulpeaseGrade.LEVELS.keys():
        grades[level] = GulpeaseGrade(index, level)

    return index, grades