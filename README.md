<h1 align="center">
    Word Reactor
</h1>

<p align="center">
  <em>Discord chatbot in Python that reacts to indicated messages with given words formed with emoji letters</em>
  <br>
</p>

<p align="center">
  <a href="CONTRIBUTING.md">Contributing guidelines</a>
  ·
  <a href="https://github.com/antoinebrunet1/word-reactor/issues">Submit an issue</a>
  ·
  <a href="https://github.com/antoinebrunet1/word-reactor/discussions">Ask a question</a>
  <br>
  <br>
</p>

<div align="center">

[![Build](https://github.com/antoinebrunet1/word-reactor/actions/workflows/build.yml/badge.svg)](https://github.com/antoinebrunet1/word-reactor/actions/workflows/build.yml)

</div>

<hr>

## Slash command

It contains 1 slash command named `react` that takes two parameters:

1. `message_id`
2. `word`

`message_id` is the ID of the message you want the bot to react to. It can be copied from the same contextual menu used to reply to a message.

`word` is the word you want the bot to react with. It should contain only A-Z letters. The case is not important. No letter should repeat.

## CI/CD pipeline

This project uses a CI/CD pipeline with GitHub Actions. The pipeline is activated on push. It has 3 jobs:

1. `style`
2. `documentation`
3. `unit-tests`

The `unit-tests` job checks the following points:

1. All the unit tests pass.
2. The unit tests cover at least 80% of `main.py`.

## Demo

![Image](https://github.com/user-attachments/assets/7e0b7b9a-53ad-498a-b82f-fc83b96bdf14)

## Setup instructions

Create a bot on Discord's website.

### Dependencies

The code uses these dependencies:

1. `black`
2. `pydocstyle`
3. `discord.py`
4. `pytest`
5. `pytest-mock`
6. `python-dotenv`
7. `pytest-asyncio`
8. `pytest-cov`

All these dependencies can be installed using pip.

### `.env` file

If you have this project locally, you need to add a file called `.env` with those 2 properties:

1. `TOKEN`
2. `SERVER_ID`

`TOKEN` is your bot token.

`SERVER_ID` is the ID of your server. You can set up the code not to use `SERVER_ID` if you are not in the process of testing the `react` slash command.

⚠️ Do not make this file public. ⚠️

### Running the bot

Use the latest release of this code to run the bot by running `main.py`.