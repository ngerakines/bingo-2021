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
