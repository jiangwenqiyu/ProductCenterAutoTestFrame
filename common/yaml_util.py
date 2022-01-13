import yaml


class YamlUtil:

    def read_yaml(self, name):
        with open('./testcases/' + name, 'r', encoding='utf-8') as f:
            data = yaml.load(f, yaml.FullLoader)
            return data


    def write_yaml(self, name, data):
        with open('./testcases/' + name, 'a', encoding='utf-8') as f:
            yaml.dump(data, stream=f, allow_unicode = True)

    def rewrite_yaml(self, name, data):
        with open('./testcases/' + name, 'w', encoding='utf-8') as f:
            yaml.dump(data, stream=f, allow_unicode = True)


    def clear_yaml(self, name):
        with open('./testcases/' + name, 'w', encoding='utf-8') as f:
            f.truncate()





