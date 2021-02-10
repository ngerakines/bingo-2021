from typing import List, Dict
import argparse
import uuid
import logging
import yaml

parser = argparse.ArgumentParser(prog="create-item", description="Create a board item")
parser.add_argument(
    "--dest",
    dest="destination",
    default="data.yaml",
    help="The destination file for the board item. (default: data.yaml)",
)
parser.add_argument(
    "--id",
    dest="id",
    help="The unique id of the board item.",
)
parser.add_argument(
    "--name",
    dest="name",
    help="The name of the board item.",
)
parser.add_argument(
    "--description",
    dest="description",
    help="The description of the board item. (optional)",
)
parser.add_argument(
    "--score",
    dest="score",
    type=int,
    default=1,
    help="The point value of the board item. (default: 1)",
)
parser.add_argument(
    "--tag",
    dest="tags",
    help="The tags applicable to the board item.",
    action="extend",
    nargs="+",
    type=str,
    default=[],
)
parser.add_argument("--verbose", "-v", action="count", default=1)


def validate(items: List[Dict[str, any]], new_id: str, new_name: str):
    ids: Dict[str, bool] = {
        new_id: True,
    }
    names: Dict[str, bool] = {
        new_name: True,
    }
    for item in items:
        if "id" not in item:
            raise Exception("id attribute missing from item")

        if "name" not in item:
            raise Exception("name attribute missing from item")

        item_id = item["id"]
        if item_id in ids:
            raise Exception(f"duplicate id: {item_id}")
        else:
            ids[item_id] = True

        item_name = item["name"]
        if item_name in names:
            raise Exception(f"duplicate name: {item_name}")
        else:
            names[item_name] = True


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

    item_id = args.id
    if item_id is None:
        logging.warning("item id not set, generating random item id")
        item_id = uuid.uuid4()
    else:
        item_id = uuid.UUID(item_id)

    logging.info(f"item id: {item_id}")

    items: List[Dict[str, str]] = []

    with open(args.destination, "r") as f:
        items = yaml.load(f, Loader=yaml.FullLoader)
        logging.debug(f"read {len(items)} items")
        validate(items, str(item_id), args.name)

    with open(args.destination, "w") as f:
        items.append(
            {
                "id": str(item_id),
                "name": args.name,
                "description": args.description,
                "score": args.score,
                "tags": args.tags,
            }
        )
        yaml.dump(items, f)


if __name__ == "__main__":
    main()
