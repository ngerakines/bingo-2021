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

def validate_proof(proofs: List[Dict[str, any]]):
    all_values: Dict[str, List[str]] = {}
    for proof in proofs:
        for i in ["item", "proof"]:
            if i not in proof:
                raise Exception(f"{i}: attribute missing")
        for i in ["item"]:
            if not isinstance(proof[i], str):
                raise Exception(f"{i}: invalid type: must be str")
        for i in ["proof"]:
            if not isinstance(proof[i], list):
                raise Exception(f"{i}: invalid type: must be list")

        proof_player = ""
        if "player" in proof:
            if not isinstance(proof["player"], str):
                raise Exception(f"player: invalid type: must be str")
            proof_player = proof["player"]
        proof_item = proof["item"]

        key = ":".join([proof["item"], proof_player])

        if key in all_values:
            raise Exception(f"duplicate proof: {proof_item} {proof_player}")
        
        proof_values = []
        for v in proof["proof"]:
            if v in proof_values:
                raise Exception(f"duplicate proof: {proof_item} {proof_player}: {v}")
            proof_values.append(v)

        all_values[key] = proof_values


def main():
    with open("data.yaml", "r") as f:
        items = yaml.load(f, Loader=yaml.FullLoader)
        validate_data(items)

    with open("game.yaml", "r") as f:
        game = yaml.load(f, Loader=yaml.FullLoader)
        if "proofs" in game:
            validate_proof(game["proofs"])


if __name__ == "__main__":
    main()
