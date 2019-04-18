from essense.fs.json_files import JsonFiles
import json
import datetime

jsObj = JsonFiles()

class Block(object):
    """Класс для генерации и рассылки блока"""
    def create_block(self, header, body):
        """Метод создания блока"""
        block = {
            "type": "block",
            "data": {
                "header": header,
                "body": body
            }
        }
        print("created block")
        return block

    def build_head(self, sign):
        """Метод генерации шапки блока"""
        block_id = jsObj.get_json('data/data.json')

        pre_hash = jsObj.get_json('data/blockchain/' + str(block_id["id_finish"]) + '.json')
        pre_hash = jsObj.get_prop(pre_hash, "data.header.pre_hash")

        block_id["id_finish"] = int(block_id["id_finish"]) + 1
        print('1111111111111111111111')
        print(block_id)
        jsObj.set_json_in_file('/data/data.json', block_id)
        block_id = int(block_id["id_finish"])

        user_id = jsObj.get_json('data/user.json')
        user_id = user_id["id"]

        time = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")

        header = {
            "block_id": block_id,
            "time": time,
            "id": user_id,
            "sign": sign,
            "pre_hash": pre_hash,
            "hash": ""
        }
        print("head was built")
        return header

    def build_body(self, tranzactions):
        """Метод сборки тела блока"""
        nonce = "0"

        body = {
            "tranzactions": tranzactions,
            "nonce": nonce
        }
        print("body was built")
        return body