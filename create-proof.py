import argparse
import uuid
import logging
import yaml

parser = argparse.ArgumentParser(prog="create-proof", description="Records game proof")
parser.add_argument(
    "--game",
    dest="game",
    default="game.yaml",
    help="The destination file for the board item. (default: game.yaml)",
)
parser.add_argument(
    "--item",
    dest="item",
    help="The unique id of the board item.",
)
parser.add_argument(
    "--player",
    dest="player",
    help="The player identifier for the proof (optional)",
)
parser.add_argument("--verbose", "-v", action="count", default=1)
parser.add_argument(
    "proof",
    type=str,
    help="The proof reference.",
)


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

    item = args.item
    if item is None:
        raise Exception("item id is required")
    else:
        item = str(uuid.UUID(item))

    logging.info(f"item id: {item}")

    with open(args.game, "r") as f:
        game = yaml.load(f, Loader=yaml.FullLoader)
        if game is None:
            game = {}

    if "proofs" not in game:
        game["proofs"] = []

    found = False
    for value in game["proofs"]:

        value_player = None
        if "player" in value:
            value_player = value["player"]

        if args.player == value_player and value["item"] == item:
            logging.info("found item")
            found = True

            if args.proof not in value["proof"]:
                value["proof"].append(args.proof)

            break

    if found is False:
        value = {
            "item": str(item),
            "proof": [args.proof],
        }
        if args.player is not None:
            value["player"] = args.player
        game["proofs"].append(value)

    with open(args.game, "w") as f:
        yaml.dump(game, f)


if __name__ == "__main__":
    main()
