try:
    from PyQt5.QtWidgets import QInputDialog, QLineEdit
    from PyQt5.QtCore import QCoreApplication
    from PyQt5 import QtWidgets
except:
    from PyQt6.QtWidgets import QInputDialog, QLineEdit
    from PyQt6.QtCore import QCoreApplication
    from PyQt6 import QtWidgets
from ..reinstaller_plugin import ReinstallerPlugin
import mobase, shutil, os

class ReinstallerDeleteTool(ReinstallerPlugin, mobase.IPluginTool):
    
    def __init__(self):
        self.dialog = QtWidgets.QWidget()
        super().__init__()

    def init(self, organiser=mobase.IOrganizer):
        return super().init(organiser)

    def __tr(self, trstr):
        return QCoreApplication.translate(self.pluginName, trstr)

    def master(self):
        return self.pluginName

    def settings(self):
        return []

    def icon(self):
        return self.icons.minusIcon()
        
    def name(self):
        return f"{self.baseName()} Delete Tool"

    def displayName(self):
        return f"{self.baseDisplayName()}/Delete"

    def description(self):
        return self.__tr("Deletes a downloaded file.")

    def display(self):
        installers = self.reinstaller.files.getSubFolderList(self.reinstaller.paths.pluginDataPath())
        names = [os.path.basename(folder) for folder in installers]
        item, ok = QInputDialog.getItem(self.dialog, "Delete Installer", "Installer:", names, 0, False)
        if ok and item:
            installerOpts = self.reinstaller.files.getFolderFileList(self.reinstaller.paths.pluginDataPath() / item)
            files = [file for file in installerOpts if not str(file).endswith('.meta')]
            if len(files) == 1:
                self.reinstaller.delete(item, os.path.basename(files[0]))
            if (len(files)) > 1:
                optionFiles = [os.path.basename(opt) for opt in files]
                item2, ok = QInputDialog.getItem(self.dialog, "Delete File", "File:", optionFiles, 0, False)
                if ok and item2:
                    self.reinstaller.delete(item, item2)



