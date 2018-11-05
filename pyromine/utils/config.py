class Config:
    DETECT = -1
    PROPERTIES = 0
    CNF = PROPERTIES
    JSON = 1
    YAML = 2
    SERIALIZED = 4
    ENUM = 5
    ENUMERATION = ENUM

    config = []
    nestedCache = []
    file = None
    __type = DETECT
    json_options = None

    format = {
        "properties": PROPERTIES,
        "cnf": CNF,
        "conf": CNF,
        "config": CNF,
        "json": JSON,
        "js": JSON,
        "yml": YAML,
        "yaml": YAML,
        "sl": SERIALIZED,
        "serialize": SERIALIZED,
        "txt": ENUM,
        "list": ENUM,
        "enum": ENUM,
    }

    def __init__(self, file: str, __type: int=DETECT, default = None):
        self.load(file, __type, default)

    def reload(self):
        self.config = []
        self.nested_cache = []
        self.load(self.file, self.__type)