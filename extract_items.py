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
    "item.minecraft",
    "enchantment.minecraft",
]
PATH_EXCLUSIONS = [
    ".attached",
    ".banner",
    ".bed.",
    ".bundle",
    ".debug_stick",
    ".desc",
    ".player_head",
    ".smithing_template.",
    "candle_cake",
    "firework_rocket.",
    "firework_star.",
    "spawn_egg",
    "spawn.",
    "spawner.",
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
    pull_data = True
    for path in PATHS:
        for key in lang_file:
            if key.startswith(path):
                for p in PATH_EXCLUSIONS:
                    if p in key:
                        pull_data = False
                        break
                    else:
                        pull_data = True
                if pull_data:
                    data = lang_file[key]
                    pull_data = True
                    if data not in final_items:
                        final_items.append(data)
    final_items.sort()
    data = [i+"\n" for i in final_items]

    # Write data into output file.
    with open(OUTPUT, 'w') as f:
        f.writelines(data)


if __name__ == "__main__":
    main()
