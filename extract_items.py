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
PATHS = [
    "block.minecraft",
    "item.minecraft"
]


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

    # Extract keys from designated PATHS.
    final_items = []
    for path in PATHS:
        for key in lang_file:
            if key.startswith(path):
                final_items.append(lang_file[key])
    final_items.sort()


if __name__ == "__main__":
    main()
