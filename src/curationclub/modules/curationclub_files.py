import mobase, glob, os
from .curationclub_settings import CurationClubSettings
from .curationclub_paths import CurationClubPaths
from ...shared.shared_files import SharedFiles
from pathlib import Path
try:
    from PyQt5.QtCore import QCoreApplication, qInfo
except:
    from PyQt6.QtCore import QCoreApplication, qInfo

class CurationClubFiles(SharedFiles):
    """ Curation Club file module. Used to get collections of files from different game paths. """

    def __init__(self, settings=CurationClubSettings, paths=CurationClubPaths, organiser=mobase.IOrganizer):
        self.paths = paths
        self.settings = settings
        super().__init__("CurationClub", organiser) 

    def creationMetaFiles(self):
        metaFiles = []
        qInfo(f"Searching {str(self.paths.creationsMetaFolder())}")
        if self.paths.creationsMetaFolder().exists():
            metaFiles += self.getFolderFileList(str(self.paths.creationsMetaFolder()))
        if self.settings.rootBuilderSupport():
            modlist = self.organiser.modList().allModsByProfilePriority()
            for mod in modlist:
                if self.organiser.modList().state(mod) & mobase.ModState.ACTIVE:
                    qInfo(f"Searching {str(self.paths.creationsRootFolder(mod))}")
                    if self.paths.creationsRootFolder(mod).exists():
                        metaFiles = metaFiles + self.getFolderFileList(str(self.paths.creationsRootFolder(mod)))
            qInfo(f"Searching {str(self.paths.creationsOverwriteFolder())}")
            if Path(self.paths.creationsOverwriteFolder()).exists():
                metaFiles = metaFiles + self.getFolderFileList(str(self.paths.creationsOverwriteFolder()))
        return metaFiles

    def findFileInMod(self, fileName):
        modlist = self.organiser.modList().allModsByProfilePriority()
        for mod in modlist:
            if self.organiser.modList().state(mod) & mobase.ModState.ACTIVE:
                filePath = self.paths.modsPath() / mod / fileName
                if filePath.exists():
                    return str(filePath)
        return None

    def findba2Files(self, preName=str):
        searchName = "*.ba2"
        gameSearch = str(Path(self.paths.gamePath()) / self.paths.gameDataDir() / searchName)
        res = glob.glob(gameSearch)
        if self.settings.rootBuilderSupport():
            modlist = self.organiser.modList().allModsByProfilePriority()
            for mod in modlist:
                if self.organiser.modList().state(mod) & mobase.ModState.ACTIVE:
                    modSearch = str(self.paths.modsPath() / str(mod) / searchName)
                    res = res + glob.glob(modSearch)
            overSearch = str(Path(self.organiser.overwritePath()) / searchName)
            res = res + glob.glob(overSearch)

        output = []
        for r in res:
            bn = os.path.basename(str(r)).lower()
            if bn.startswith(preName.lower()):
                output.append(os.path.basename(str(r)))
        return output
        
