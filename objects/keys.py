from fs.json_files import JsonFiles


class Keys(object):
    def __init__(self):
        super().__init__()
        self.__path = './data/keys.json'

    def set_keys(self, keys=[]):
        obj = {}
        for key in keys:
            obj[key["name"]] = key["value"]

        JsonFiles().write_data(self.__path, obj)

    def get_keys(self):
        return JsonFiles().get_data(self.__path)

    def delete_keys(self):
        JsonFiles().del_file(self.__path)
