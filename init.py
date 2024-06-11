from lxml import etree
import sys
import os


class CONF:
    def __init__(self):
        pass

    def up_conf(self):
        pass


class InitEXE:
    def __init__(self):
        pass

    def initConf(self):
        self.conf = etree.parse("./.config.xml")

    def upXml(self):
        absPath = os.getcwd()
        ui_base = self.conf.xpath("//ui_base")[0]
        ui_base.attrib['abspath'] = absPath
        self.conf.write("./.config.xml", pretty_print=True)


if __name__ == '__main__':
    e = InitEXE()
