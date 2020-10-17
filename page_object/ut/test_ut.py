# 这个是用来测yaml的加载
# pyyaml
import yaml
class TestYaml():
    def test_yaml(self):
        # dict = yaml.load(open("page_object/data/login_page.yaml","r")) 这样写绝对路径会报错
        dict = yaml.load(open("../data/login_page.yaml", "r"))
        # print(dict)
        for step in dict["LoginByPassword"]:
            print(step['locator'])
