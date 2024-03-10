import json
import os
import zipfile


CWD = os.getcwd()
LANG = "assets/minecraft/lang/en_us.json"
VERSIONS = os.path.join(
    os.getenv('appdata'),
    ".minecraft",
    "versions"
    )
OUTPUT = os.path.join(
    CWD,
    "ExtractedItems.txt"
    )


def main():
    # Ask user for current Minecraft version.
    msg = "Input Minecraft Version: "
    while True:
        ver = input(msg)
        jar_file = os.path.join(VERSIONS, ver)

        # Check if version exists & finalize dir.
        if os.path.exists(jar_file) and jar_file != VERSIONS+"\\":
            jar_file = os.path.join(jar_file, ver+".jar")
            break
        else:
            print("Version not detected! Try again..")

    # Open and grab contents of lang file.
    with zipfile.ZipFile(jar_file) as jar:
        with jar.open(LANG) as jar_lang_file:
            lang_file = json.load(jar_lang_file)

    view_lang_keys_paths(lang_file)


def view_lang_keys_paths(lang_file):
    """View the first few asset path of lang file keys."""
    # TODO: Remove function & related code before finalizing.
    paths = []
    paths_final = []

    # Extract first 2 paths of keys.
    for key in lang_file.keys():
        path = key.split('.')
        final = '.'.join(path[:2])
        paths.append(final)

    # Remove duplicates.
    for i in paths:
        if i not in paths_final:
            paths_final.append(i)
    for i in paths_final: print(i)


if __name__ == "__main__":
    main()
