from typing import List, Dict
import argparse
import uuid
import logging
import yaml


def validate_data(items: List[Dict[str, any]]):
    ids: Dict[str, bool] = {}
    names: Dict[str, bool] = {}
    for item in items:
        for i in ["id", "name", "description", "score", "tags"]:
            if i not in item:
                raise Exception(f"{i}: attribute missing")
        for i in ["id", "name", "description"]:
            if not isinstance(item[i], str):
                raise Exception(f"{i}: invalid type: must be str")
        for i in ["score"]:
            if not isinstance(item[i], int):
                raise Exception(f"{i}: invalid type: must be int")
        for i in ["tags"]:
            if not isinstance(item[i], list):
                raise Exception(f"{i}: invalid type: must be list")

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

        item_score = item["score"]
        if item_score < 0 or item_score > 100:
            raise Exception(f"score must satisfy 0 <= {item_score} <= 100")

        item_tags = item["tags"]
        if len(item_tags) > 10:
            raise Exception("item cannot have more than 10 tags")
        for tag in item_tags:
            if not isinstance(tag, str):
                raise Exception(f"{tag}: invalid type: tag must be str")


def main():
    with open("data.yaml", "r") as f:
        items = yaml.load(f, Loader=yaml.FullLoader)
        validate_data(items)


if __name__ == "__main__":
    main()
