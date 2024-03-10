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
TEMP = os.path.join(
    CWD,
    "temp"
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


if __name__ == "__main__":
    main()
