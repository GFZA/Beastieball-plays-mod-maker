import os
import csv
from pathlib import Path

NAME : str = "Thriller's modded plays"
AUTHOR : str = "GFZA"
URL : str = "3833664965"
INTERNAL_ID : str = "1VY50B84633067"

CSV_PATH : str = "data.csv"
OUTPUT_PATH : str = NAME

plays : dict[str, dict[str, str]] = {}


def main() -> None:
    _output_mod()


def _assign_plays() -> bool:
    if not os.path.exists(CSV_PATH):
        print(f"CSV at {CSV_PATH} doesn't exist!")
        return False

    with open(CSV_PATH, mode="r") as file:
        reader = csv.reader(file)
        datas = list(reader)

        for row in datas:
            if len(row) != 7:
                print(len(row))
                print("Missing data! Please recheck the CSV if there's any missing data!")
                return False
            plays[f"{row[0]}"] = {
                "type" : f"{row[1]}",
                "use" : f"{row[2]}",
                "pow" : f"{row[3]}",
                "target" : f"{row[4]}",
                "effects" : f"{str(row[5])}",
                "distribution" : f"{str(row[6])}",
            }

    return True


def _output_play(output_dir : Path) -> None:
    for play in plays.keys():
        output_play_dir = output_dir.joinpath("Play_" + play)
        output_play_dir.mkdir(parents=True, exist_ok=True)
        output_ini = output_play_dir.joinpath("play_data.ini")
        play_data : dict[str, str] = plays[play]

        content : str = "[basic]\n"
        content += f"name = \"{play}\"\n"
        content += f"type = {play_data["type"]}\n"
        content += f"use = {play_data["use"]}\n"
        content += f"pow = {play_data["pow"]}\n"
        content += f"target = {play_data["target"]}\n"
        content += "\n[effects]\n"
        content += f"effects = \"{play_data["effects"]}\"\n"
        content += "\n[distribution]\n"
        content += f"learnedby = \"{play_data["distribution"]}\""

        with open(output_ini, mode="w") as file:
            file.write(content)


def _output_config(output_dir : Path) -> None:
    content : str = "[general]\n"
    content += f"finished = \"1.000000\"\n"
    content += f"author = \"{AUTHOR}\"\n"
    content += f"url = \"{URL}\"\n"
    content += f"major_version = \"1\"\n"
    content += f"minor_version = \"0\"\n"
    content += f"name = \"{NAME}\"\n"
    content += f"description = \"\"\n"
    content += f"internal_id = \"{INTERNAL_ID}\"\n"
    
    with open(output_dir.joinpath("config.ini"), mode="w") as file:
        file.write(content)


def _output_mod() -> None:
    if not _assign_plays():
        return
    output_dir = Path(OUTPUT_PATH)
    output_dir.mkdir(parents=True, exist_ok=True)
    _output_play(output_dir)
    _output_config(output_dir)
    print("Plays mod created successfully!")


if __name__ == "__main__":
    main()