import abc
import yaml

class PluginInfo(object):
    def __init__(self, infoFile):
        self.__infoFile = infoFile
        self.__initFile()

    def __initFile(self):
        fh = open(self.__infoFile, 'r')
        self.__data = yaml.load(fh.read())
        fh.close()

    @property
    def name(self):
        return self.__data['name']

    @property
    def description(self):
        return self.__data['description']

    @property
    def groups(self):
        return self.__data['groups']

    @property
    def dependencies(self):
        return self.__data['dependencies']

    @property
    def help(self):
        return self.__data['help']

class AbstractPlugin(PluginInfo):
    __metaclass__ = abc.ABCMeta

    def __init__(self, pluginInfoFile):
        PluginInfo.__init__(self, pluginInfoFile)
        pass

    @abc.abstractmethod
    def run(self):
        pass
