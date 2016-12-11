import logging
import glob
import sys
import yaml
import os
from baseplugin import AbstractPlugin, PluginInfo
from constants import BASE_DEPENDENCIES, BASE_PLUGIN_PATH

DEBUG = True

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
LOGGER.addHandler(ch)

def log(msg):
    if DEBUG:
        LOGGER.debug(msg)

class Delegator(object):
    PLUGIN_PATH = BASE_PLUGIN_PATH.split(":")

    """
    Main class for instantiating plugin objects.
    """

    def __init__(self):
        self.__setup()

    def __setup(self):
        # TODO check for environ var
        self.__pluginPath = self.PLUGIN_PATH

    @property
    def pluginPath(self):
        return self.__pluginPath

    @pluginPath.setter
    def pluginPath(self, pathIn):
        pass

    def listPlugins(self, groups=None, dependencies=None):
        pluginList = []

        if dependencies == None:
            dependencies = BASE_DEPENDENCIES

        for path in self.pluginPath:
            for pluginFile in glob.glob("{0}/*.plugin".format(path)):
                pluginInfo = PluginInfo(pluginFile)

                for dependency in pluginInfo.dependencies:
                    if dependency in dependencies.__dict__.keys():
                        pluginList.append(pluginInfo)
        return pluginInfo

if __name__ == "__main__":
    d = Delegator()
    plugins = d.listPlugins()
    print(plugins)
