<h1 align="center">
    Word Reactor
</h1>

<p align="center">
  <img src="logo.png" alt="logo" width="120px" height="120px"/>
  <br>
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

## Local setup instructions

1. Create a bot on Discord's website.
2. Run the following command: `python3 -m pip install black pydocstyle discord.py pytest pytest-mock python-dotenv pytest-asyncio pytest-cov`.
3. Fork the repository.
4. Uncomment all the commented out code and comment out the `token = ...` line that does not use `gentenv`.
5. Add a **non-public** file called `.env` with those 2 properties:
   1. `TOKEN` (Your bot token)
   2. `SERVER_ID` (The ID of your server. You can set up the code not to use `SERVER_ID` if you are not in the process of testing the `react` slash command.)
6. Run the bot by running `main.py`.

## Usage instructions

You can add the bot to your server using this link: https://discord.com/oauth2/authorize?client_id=1488295878849597581.

It contains 1 slash command named `react` that takes two parameters:

1. `message_id`
2. `word`

`message_id` is the ID of the message you want the bot to react to. It can be copied from the same contextual menu used to reply to a message.

`word` is the word you want the bot to react with. It should contain only A-Z letters. The case is not important. No letter should repeat.

### Demo

![Image](https://github.com/user-attachments/assets/cc2319f2-8457-4c40-bdee-43421ca23875)