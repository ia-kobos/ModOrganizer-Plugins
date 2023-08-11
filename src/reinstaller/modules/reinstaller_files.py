import mobase, os, re
from pathlib import Path
from os import listdir
from .reinstaller_paths import ReinstallerPaths
from .reinstaller_settings import ReinstallerSettings
from ...shared.shared_files import SharedFiles
try:
    from PyQt5.QtCore import QCoreApplication, qInfo
except:
    from PyQt6.QtCore import QCoreApplication, qInfo

class ReinstallerFiles(SharedFiles):
    """ Reinstaller file module. Used to get collections of files from different game paths. """

    def __init__(self, organiser=mobase.IOrganizer, paths=ReinstallerPaths):
        self.paths = paths
        super().__init__("Reinstaller", organiser)

    def getDownloadFileOptions(self):
        downloadFiles = self.getFolderFileList(self.paths.downloadsPath())
        return [
            str(os.path.basename(file))
            for file in downloadFiles
            if not str(file).endswith('.meta')
            and not str(file).endswith('.unfinished')
        ]

    metaRegex = r"^modName=(.+)$"
    def getDownloadFileName(self, downloadName=str):
        defaultName = str(downloadName).split("_")[0].split("-")[0].split(".")[0].strip()
        metaPath = str(self.paths.downloadsPath() / f"{str(downloadName)}.meta")
        if Path(metaPath).exists():
            try:
                with open(metaPath, "r") as metaFile:
                    metaText = metaFile.read()
                if matches := re.search(self.metaRegex, metaText, re.MULTILINE):
                    grp = str(matches[1])
                    if grp and grp != "":
                        return grp
            except:
                return defaultName
        return defaultName
    
    def getInstallerOptions(self):
        installers = self.getSubFolderList(self.paths.pluginDataPath())
        return [os.path.basename(folder) for folder in installers]

    def getInstallerFileOptions(self, name):
        installerOpts = self.getFolderFileList(self.paths.pluginDataPath() / name)
        return [str(file) for file in installerOpts if not str(file).endswith('.meta')]
