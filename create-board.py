import random
from typing import List, Dict
import argparse
import logging
import yaml

parser = argparse.ArgumentParser(prog="create-proof", description="Records game proof")
parser.add_argument(
    "--game",
    dest="game",
    default="game.yaml",
    help="The destination game file for the board. (default: game.yaml)",
)
parser.add_argument(
    "--source",
    dest="source",
    default="data.yaml",
    help="The source file for the board item. (default: data.yaml)",
)
parser.add_argument(
    "--player",
    dest="player",
    help="The board player",
)
parser.add_argument("--verbose", "-v", action="count", default=1)


def main():
    args = parser.parse_args()

    if args.verbose >= 4:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose >= 3:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose >= 2:
        logging.basicConfig(level=logging.WARNING)
    elif args.verbose >= 1:
        logging.basicConfig(level=logging.ERROR)

    logging.debug("debugging enabled")
    logging.debug("%s", args)

    board_player = args.player
    if board_player is None:
        raise Exception("player is required")

    with open(args.source, "r") as f:
        items: List[Dict[str, any]] = yaml.load(f, Loader=yaml.FullLoader)
        logging.debug(f"read {len(items)} items")

    random.shuffle(items)

    with open(args.game, "r") as f:
        boards: Dict[str, any] = yaml.load(f, Loader=yaml.FullLoader)
        if boards is None:
            boards: Dict[str, any] = {}
        logging.debug(f"read {len(boards)} boards")

    if "boards" not in boards:
        boards["boards"] = []

    if board_player in [x["player"] for x in boards["boards"]]:
        raise Exception("player already has a board")

    boards["boards"].append({
        "player": board_player,
        "board": [[{"item": items.pop()["id"]} for _ in range(10)] for _ in range(10)]
    })

    with open(args.game, "w") as f:
        yaml.dump(boards, f)


if __name__ == "__main__":
    main()
