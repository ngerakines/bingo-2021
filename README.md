# bingo-2021

Welcome to Bingo 2021!

> I didn't have X on my 2020 bingo card, but ...

Seems to be something we've all said or heard, right? Well with Bingo 2021, we're going to have some fun with it.

# Game Play

**Bingo 2021** is a game that you play with friends, co-workers, or strangers to race to fill a bingo card with fun, hopefully lighthearted, and random events that *could* occur over the course of the year. Anyone can contribute to the event list that is used to generate the bingo cards. At the end of a game, scores are tallied, winners declared, and reminiscing to be had. 

## Set Up

From January 1st, 2021 through March 31st, 2021, contributes to `data.yaml` will be made.

## Card Distribution

On April 1st, 2021, cards will be generated and assigned to players listed in `players.yaml`.

## Proof

As events occur, proof is added to data.yaml.

## Bingo

When proof occurs that marks a card in such a way that bingo is triggered, players are notified.

## Party

Have a drink with your friends (hopefully in real life) in December and look back at all of the crazy things that happened in 2021.

# Board Data

Board data is stored in `data.yaml` as a big list of items. Each item has an id, name, description, zero or more tags, and a point value.

To generate a unique ID for an item, use `uuidgen` or https://www.uuidgenerator.net/. All items must be uniquely identified.

By default, items have 1 point.

```yaml
- id: 74ca1acf-25af-4b08-a59a-816d6172dbf1
  name: "The onion strikes again."
  description: The onion publishes another painfully funny article that strikes too close to home.
  score: 1
  tags: ["culture"]
```

Suggested tags include:
* "personal" -- The item is personal or self-targeting. For example, a personal item would be something that applies to you or you accomplish.
* "politics"
* "technology"
* "culture"
* "finance"

# Proofs

Proofs are strongly encouraged to be verifiable either with a link or reference to a credible source or with two (2) or more witnesses. Witnesses can comment on the pull-request, acknowledge through social media, etc. We're all adults.

Proofs are stored in `proofs.yaml` and must reference the ID of the item.

```yaml
- item: "74ca1acf-25af-4b08-a59a-816d6172dbf1"
  proof:
  - "https://twitter.com/ngerakines/status/1347238662103298049"
```

A proof may also apply to only a single user. For example "Changed jobs" could be an item on the board, but only applies to yourself. In those situations, the proof should include the player it applies to.

```yaml
- item: "a2556568-e717-4599-8b6a-f04b11c9ef07"
  player: nick
  proof:
  - "https://www.linkedin.com/in/ngerakines"
```

# Tools

## create-item.py

The `create-item.py` script can be used to safely record a board item.

Example:

    $ python create-item.py --name "Went dancing" --description "Hit the dance floor" --tag social

Usage:

```
usage: create-item [-h] [--dest DESTINATION] [--id ID] [--name NAME] [--description DESCRIPTION] [--score SCORE] [--tag TAGS [TAGS ...]] [--verbose]

Create a board item

optional arguments:
  -h, --help            show this help message and exit
  --dest DESTINATION    The destination file for the board item. (default: data.yaml)
  --id ID               The unique id of the board item.
  --name NAME           The name of the board item.
  --description DESCRIPTION
                        The description of the board item. (optional)
  --score SCORE         The point value of the board item. (default: 1)
  --tag TAGS [TAGS ...]
                        The tags applicable to the board item.
  --verbose, -v
```

## create-proof.py

The `create-proof.py` script can be used to safely record a proof in a game.

Example:

    $ python create-proof.py --item 74ca1acf-25af-4b08-a59a-816d6172dbf1 "https://twitter.com/ngerakines/status/1347238662103298049"

Usage:

```
usage: create-proof [-h] [--game GAME] [--item ITEM] [--player PLAYER] [--verbose] proof

Records game proof

positional arguments:
  proof            The proof reference.

optional arguments:
  -h, --help       show this help message and exit
  --game GAME      The destination file for the board item. (default: game.yaml)
  --item ITEM      The unique id of the board item.
  --player PLAYER  The player identifier for the proof (optional)
  --verbose, -v
```

## create-board.py

The `create-board.py` script can be used to safely record a player board in a game.

Example:

    $ python create-board.py --player nick

Usage:

```
usage: create-proof [-h] [--game GAME] [--source SOURCE] [--player PLAYER] [--verbose]

Records game proof

optional arguments:
  -h, --help       show this help message and exit
  --game GAME      The destination game file for the board. (default: game.yaml)
  --source SOURCE  The source file for the board item. (default: data.yaml)
  --player PLAYER  The board player
  --verbose, -v
```
