import mobase, os
from datetime import datetime, timedelta
from .plugin_version import PluginVersion
from ...shared.shared_json import SharedJson
from ...shared.shared_utilities import SharedUtilities
try:
    from PyQt5.QtCore import QCoreApplication, qInfo
except:
    from PyQt6.QtCore import QCoreApplication, qInfo

class PluginData(SharedJson):

    def __init__(self, jsonObject=dict):
        self.utilities = SharedUtilities()
        super().__init__(jsonObject)
        
    def identifier(self):
        return str(self.getJsonProperty("Identifier"))

    def name(self):
        return str(self.getJsonProperty("Name"))

    def author(self):
        return str(self.getJsonProperty("Author"))

    def description(self):
        return str(self.getJsonProperty("Description"))

    def nexusUrl(self):
        return str(self.getJsonProperty("NexusUrl"))

    def githubUrl(self):
        return str(self.getJsonProperty("GithubUrl"))

    def docsUrl(self):
        return str(self.getJsonProperty("DocsUrl"))
    
    def versions(self):
        if data := self.getJsonArray("Versions"):
            return [PluginVersion(version) for version in data]
        else:
            return None

    def current(self, moVersion=str):
        """ The most recent working version for a given Mod Organizer version. """
        allVersions = self.versions()
        workingVersions = []
        if allVersions and len(allVersions) > 0:
            for version in allVersions:
                if version.maxWorking() == "" or not self.utilities.versionIsNewer(version.maxWorking(), moVersion):
                    if version.minWorking() == "" or not self.utilities.versionIsNewer(moVersion, version.minWorking()):
                        workingVersions.append(version)

        if workingVersions:
            latestVersion = workingVersions[0]
            latest = latestVersion.version()
            for version in workingVersions:
                if self.utilities.versionIsNewer(latest, version.version()):
                    latestVersion = version
                    latest = version.version()

            return latestVersion
        return None

    def latest(self):
        """ The most recent overall version. """
        allVersions = self.versions()
        if allVersions and len(allVersions) > 0:
            latestVersion = allVersions[0]
            latest = latestVersion.version()
            for version in allVersions:
                if self.utilities.versionIsNewer(latest, version.version()):
                    latestVersion = version
                    latest = version.version()
            return latestVersion
            
        return None
    
    def currentOrLatest(self, moVersion=str):
        if current := self.current(moVersion):
            return current
        return latest if (latest := self.latest()) else None

    def specificVersion(self, version=str):
        p1 = self.utilities.parseVersion(version)
        allVersions = self.versions()
        for ver in allVersions:
            p2 = self.utilities.parseVersion(ver.version()) 
            if p1 == p2:
                return ver
        return None