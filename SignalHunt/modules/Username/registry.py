import pkgutil
import importlib
import inspect

from modules.Username.base import BaseSocialMedia

def load_plugins():
    plugins = []
    base_package = "modules.Username.plugins"

    package = importlib.import_module(base_package)
    for finder, name, ispkg in pkgutil.walk_packages(

        package.__path__,
        prefix=package.__name__ + "."
    ):
        print(finder)
        try:
            module = importlib.import_module(name)
        except Exception:
            continue
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseSocialMedia) and obj is not BaseSocialMedia:
                plugins.append(obj)
    return plugins