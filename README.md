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

## Demo

![Image](https://github.com/user-attachments/assets/7e0b7b9a-53ad-498a-b82f-fc83b96bdf14)

## Local setup instructions

1. Create a bot on Discord's website.
2. Install the following dependencies using the `pip` command:
   1. `black`
   2. `pydocstyle`
   3. `discord.py`
   4. `pytest`
   5. `pytest-mock`
   6. `python-dotenv`
   7. `pytest-asyncio`
   8. `pytest-cov`
3. Add a **non-public** file called `.env` with those 2 properties:
   1. `TOKEN` (Your bot token)
   2. `SERVER_ID` (The ID of your server. You can set up the code not to use `SERVER_ID` if you are not in the process of testing the `react` slash command.)
4. Use the latest release of this code to run the bot by running `main.py`.