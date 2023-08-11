import mobase 
from ..shared.shared_plugin import SharedPlugin
from .curationclub import CurationClub
try:
    from PyQt5.QtCore import QCoreApplication, qInfo
except:
    from PyQt6.QtCore import QCoreApplication, qInfo

class CurationClubPlugin(SharedPlugin):

    def __init__(self):
        super().__init__("CurationClub", "Curation Club", mobase.VersionInfo(1,0,0, mobase.ReleaseType.ALPHA))

    def init(self, organiser=mobase.IOrganizer):
        self.curationclub = CurationClub(organiser)
        return super().init(organiser)

    def __tr(self, trstr):
        return QCoreApplication.translate(self.pluginName, trstr)
    
    def settings(self):
        """ Current list of game settings for Mod Organizer. """
        return [
            mobase.PluginSetting("enabled","Enables Curation Club",True),
            mobase.PluginSetting("rootbuildersupport","Enables support for Root Builder.", False),
            mobase.PluginSetting("modnameformat","Format for mod names.", "Creation Club - {creation}")
            ]