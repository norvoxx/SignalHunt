from modules.registry import loadPlugins
import os 
import inspect
plugins = loadPlugins()

#TODO A modifer est a completer
forceName = {"_" : [" ","-",""],"@" : [""]} 

NAME = "norvoxx"
NAME_LIST = [NAME]

ALLPRINT = False 
print("""
   _____ _                   _ _    _             _   
  / ____(_)                 | | |  | |           | |  
 | (___  _  __ _ _ __   __ _| | |__| |_   _ _ __ | |_ 
  \\___ \\| |/ _` | '_ \\ / _` | |  __  | | | | '_ \\| __|
  ____) | | (_| | | | | (_| | | |  | | |_| | | | | |_ 
 |_____/|_|\\__, |_| |_|\\__,_|_|_|  |_|\\__,_|_| |_|\\__|
            __/ | \033[91mCreate by norvoxx\033[00m                                 
           |___/                                      
""")

print(f"Nombre de module charger \033[92m{len(plugins)} \033[00m")
print(f"Rechereh sur le speudo : {NAME} or {NAME_LIST}")
print("\n1 : Recherche speudo\n2 : Use spcifique module")

choix = int(input("\nQuelle est votre choix : "))

if choix == 2:
    print("\n=== PLUGINS DISPONIBLES ===")
    for ind, plugin in enumerate(plugins):
        plugin_name = getattr(plugin, 'pluginName', getattr(plugin, '__name__', f"Plugin_{ind}"))
        print(f"[{ind}] {plugin_name}")

    try:
        choixPlugin = int(input("\nChoisir le numéro du plugin : "))
        selected_plugin = plugins[choixPlugin]
    except (ValueError, IndexError):
        print("Choix de plugin invalide.")
        selected_plugin = None

    if selected_plugin:
        available_methods = [
            method for method in dir(selected_plugin)
            if not method.startswith('_') and callable(getattr(selected_plugin, method))
        ]

        print(f"\n=== MÉTHODES DISPONIBLES POUR {getattr(selected_plugin, 'pluginName', 'ce plugin')} ===")
        for index, method_name in enumerate(available_methods):
            print(f" [{index}] --> {method_name}")

        try:
            choixMethod = int(input("\nChoisir le numéro de la méthode à exécuter : "))
            MethodWanted = available_methods[choixMethod]
        except (ValueError, IndexError):
            print("Choix de méthode invalide.")
            MethodWanted = None

        if MethodWanted:
            target_function = getattr(selected_plugin, MethodWanted)
            if inspect.isclass(selected_plugin):
                instance = selected_plugin(NAME)
                recherche = getattr(instance, MethodWanted)()
            else:
                recherche = target_function()

            print("\n--- RÉSULTAT DE LA RECHERCHE ---")
            print(recherche)

elif choix == 1:
    for key in forceName:
        if key in NAME:
            for m in forceName[key]:
                NAME_LIST.append(NAME.replace(key,m))

    for plugin in plugins:    
        try :
            for n in NAME_LIST:   
                    search = plugin(n).UsernameSearch()
                    searchExist = search["data"]["exist"]
                    if searchExist or ALLPRINT:
                        print(f'{n} in {plugin.pluginName} : {"\033[92m" if searchExist else "\033[91m"}  \033[00m')
                        print(f"    |---> Link : {search["data"]["htmlUrl"]}")
        except:
            print(f"erreur to {plugin.pluginName}")



