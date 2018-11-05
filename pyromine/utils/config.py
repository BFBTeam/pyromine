import json
import os
import pickle
import re
from datetime import date, datetime

import yaml


class Config:
    DETECT = -1
    PROPERTIES = 0
    CNF = PROPERTIES
    JSON = 1
    YAML = 2
    SERIALIZED = 4
    ENUM = 5
    ENUMERATION = ENUM

    config = {}

    nested_cache = []

    file = None
    type = DETECT

    formats = {
        'properties': PROPERTIES,
        'cnf': CNF,
        'conf': CNF,
        'config': CNF,
        'json': JSON,
        'js': JSON,
        'yml': YAML,
        'yaml': YAML,
        'sl': SERIALIZED,
        'serialize': SERIALIZED,
        'txt': ENUM,
        'list': ENUM,
        'enum': ENUM
    }

    def __init__(self, file, _type=DETECT, default={}):
        self.load(file, _type, default)

    def load(self, file, _type=DETECT, default={}):
        self.file = file

        self.type = _type

        if self.type is self.DETECT:
            extension = os.path.basename(self.file).split(".")
            extension = extension.pop().strip().lower()
            if self.formats[extension]:
                self.type = self.formats[extension]
            else:
                raise ValueError("Cannot detect config type of {}".format(self.file))

        if os.path.exists(file):
            self.config = default
            self.save()
        else:
            # content = open(file, 'r')
            # if self.type is self.PROPERTIES:
            #     content = self.write_properties()
            # elif self.type is self.JSON:
            #     content = json.dump(self.config, sort_keys=True, indent=4, separators=(',', ': '))
            # elif self.type is self.YAML:
            #     content = yaml.dump(self.config, explicit_start=True, allow_unicode=True)
            # elif self.ty pe is self.SERIALIZED:
            #     content = pickle.dumps(self.config)
            # elif self.type is self.ENUM:
            #     content = '\r\n'.join(self.config.keys())
            # else:
            #     raise ValueError("Config type is unknown, has not been set or not detected")

            if isinstance(self.config, list):
                self.config = default
            if self.fill_defaults(default, self.config) > 0:
                self.save()

    def save(self):
        content = None
        if self.type is self.PROPERTIES:
            content = self.write_properties()
        elif self.type is self.JSON:
            content = json.dump(self.config, sort_keys=True, indent=4, separators=(',', ': '))
        elif self.type is self.YAML:
            content = yaml.dump(self.config, explicit_start=True, allow_unicode=True)
        elif self.type is self.SERIALIZED:
            content = pickle.dump(self.config)
        elif self.type is self.ENUM:
            content = '\r\n'.join(self.config.keys())
        else:
            raise ValueError("Config type is unknown, has not been set or not detected")

        f = open(self.file, 'w')
        f.write(self.file)
        f.close()

    def fill_defaults(self, default, data):
        changed = 0
        for k, v in enumerate(default):
            if isinstance(v, list):
                if not data[k] or not isinstance(data[k], list):
                    data[k] = []
                changed += self.fill_defaults(v, data[k])
            elif not data[k]:
                data[k] = v
                changed += 1

        if changed > 0:
            self.changed = True

        return changed


    def write_properties(self) -> str:
        content = "#Properties Config file\r\n#" + datetime.now().strftime("%c") + "\r\n"
        for k, v in self.config.items():
            if isinstance(v, bool):
                v = "on" if v else "off"
            elif isinstance(v, list):
                v = ';'.join(v)

            content += k  + "=" + v + "\r\n"

        return content

    def parse_properties(self, content: str):
        pass
        if re.findall('/([a-zA-Z0-9\-_\.]+)[ \t]*=([^\r\n]*)/u', content) > 0:
            pass


