from common.yaml_util import YamlUtil


# 配置环境参数
class productEnv:

    host = ''
    token = ''
    db_link = ''
    db_user = ''
    db_pass = ''
    db_database = ''

    saveValue = dict()

    def __init__(self, env):
        data = YamlUtil().read_yaml(path = './configs/', name = 'envConfig.yml')[env]

        productEnv.host = data['host']
        productEnv.token = data['token']
        productEnv.db_link = data['db_link']
        productEnv.db_user = data['db_user']
        productEnv.db_pass = data['db_pass']
        productEnv.db_database = data['db_database']

        self.dataConfig(env)

    def dataConfig(self, env):
        productEnv.saveValue = YamlUtil().read_yaml(path = './configs/', name = 'dataConfig.yml')[env]