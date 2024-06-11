import os.path

from lxml import etree

xml_path = os.path.join(os.path.abspath(os.path.pardir), '.config.xml')
root = etree.parse(xml_path)


def load_config(label, conf=None):
    if conf is None:
        conf = {}
    conf_tree = root.xpath(f"config/{label}/*")
    if conf_tree is not None:
        for item in conf_tree:
            tag = item.tag

    return conf



if __name__ == '__main__':
    CONF = load_config('ui_base')
    print(CONF)
