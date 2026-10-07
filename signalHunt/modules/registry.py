import os 
import importlib
import inspect
import pkgutil
from pathlib import Path


from modules.template import BaseSocialMedia

def loadPlugins():
    plugins = []
    fichiers = [p for p in Path('./modules/plugins').iterdir() if p.is_dir()]
    
    for fichier in fichiers:
        base_package = f"modules.plugins.{str(fichier).split("/")[2]}"
        package = importlib.import_module(base_package)
        for finder ,name ,ispkg in pkgutil.walk_packages(package.__path__,prefix=package.__name__ + "."):
            try:
                module = importlib.import_module(name)
            except Exception:
                continue
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseSocialMedia) and obj is not BaseSocialMedia:
                    plugins.append(obj)
            
    return plugins