from lxml import etree
import os

xml_file_path = os.path.join(os.path.abspath(os.pardir), '.config.xml')


def load_conf(label):
    root = etree.parse(xml_file_path)
    tree = root.xpath(f'/config/{label}/*')
    conf = {}
    for item in tree:
        # print(etree.tostring(item))
        tag = item.tag
        data = item.text
        conf[tag] = data
    return conf


CONF = load_conf('mysql')

if __name__ == '__main__':
    conf = load_conf('mysql')
    print(conf)
