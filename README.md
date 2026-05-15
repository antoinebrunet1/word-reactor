<h1 align="center">
   <picture>
      <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f916/512.webp" type="image/webp">
      <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f916/512.gif" alt="🤖" width="32" height="32">
   </picture> Word Reactor <picture>
      <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/1f916/512.webp" type="image/webp">
      <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/1f916/512.gif" alt="🤖" width="32" height="32">
   </picture>
</h1>

<p align="center">
  <img src="images/logo.gif" alt="logo" width="120px" height="120px"/>
  <br>
  <b>Discord chatbot in Python that reacts to indicated messages with given words formed with emoji letters</b>
  <br>
</p>

<p align="center">
  <a href="CONTRIBUTING.md" target="_blank">Contributing guidelines</a>
  ·
  <a href="https://github.com/antoinebrunet1/word-reactor/issues" target="_blank">Submit an issue</a>
  ·
  <a href="https://github.com/antoinebrunet1/word-reactor/discussions" target="_blank">Ask a question</a>
  <br>
  <br>
</p>

<div align="center">

<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a> ![Uptime Robot status](https://img.shields.io/uptimerobot/status/m802773349-5ba32cd4d7433312200a5d32)
 ![version](https://img.shields.io/badge/version-2.0.5-brightgreen) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/antoinebrunet1/word-reactor)
 ![GitHub last commit](https://img.shields.io/github/last-commit/antoinebrunet1/word-reactor)
 [![Build](https://github.com/antoinebrunet1/word-reactor/actions/workflows/build.yml/badge.svg)](https://github.com/antoinebrunet1/word-reactor/actions/workflows/build.yml) [![cov](https://antoinebrunet1.github.io/word-reactor/badges/coverage.svg)](https://github.com/antoinebrunet1/word-reactor/actions) ![Dependabot](https://img.shields.io/badge/dependabot-025E8C?logo=dependabot&logoColor=white) ![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?logo=discord&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54) <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a> ![PyCharm](https://img.shields.io/badge/pycharm-143?logo=pycharm&logoColor=black&color=black&labelColor=green) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?logo=Windows%2011&logoColor=white) ![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?logo=powershell&logoColor=white) ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?logo=GoogleChrome&logoColor=white) ![Flask](https://img.shields.io/badge/flask-%23000.svg?logo=flask&logoColor=white) ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?logo=pytest&logoColor=2f9fe3) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white) 	![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black) ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white) ![Alpine Linux](https://img.shields.io/badge/Alpine_Linux-%230D597F.svg?logo=alpine-linux&logoColor=white) ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?logo=render&logoColor=white) <img alt="Static Badge" src="https://img.shields.io/badge/UptimeRobot-white?logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOTgiIGhlaWdodD0iMjk4Ij48ZyBmaWxsPSIjM0JENzcxIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguOSAuOSkiPjxjaXJjbGUgY3g9IjE0OC4xIiBjeT0iMTQ4LjEiIHI9IjE0OC4xIiBvcGFjaXR5PSIuMyIvPjxjaXJjbGUgY3g9IjE0OC4xIiBjeT0iMTQ4LjEiIHI9Ijk4LjkiLz48L2c%2BPC9zdmc%2B"> ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?logo=Canva&logoColor=white) ![Android](https://img.shields.io/badge/Android-3DDC84?logo=android&logoColor=white) ![Reddit](https://img.shields.io/badge/Reddit-%23FF4500.svg?logo=Reddit&logoColor=white) ![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white) ![Google](https://img.shields.io/badge/google-4285F4?logo=google&logoColor=white) <img alt="Static Badge" src="https://tinyurl.com/na6z24tv">

</div>

<hr>

## 📂 Structure 📂

Only certain folders and files are explained.

### `.github` folder

#### `workflows`

This folder contains the GitHub Actions file (`build.yml`).

#### `dependabot.yml`

This is the Dependabot file.

### `images`

This folder contains images that are in `README.md`.

### Python files

`test_main.py` contains the unit tests. `webserver.py` contains the code needed for Render (the service used for hosting the bot). The rest of the Python code is in `main.py`.

### `requirements.txt`

This file was added for hosting purposes. It contains all the dependencies of the project.

## 💻 Local setup instructions 💻

1. Create a bot on Discord's website.
2. Run the following command:
   ```
   python3 -m pip install black pydocstyle discord.py pytest pytest-mock python-dotenv pytest-asyncio pytest-cov
   ```
3. Fork the repository.
4. Uncomment all the commented out code and comment out the `token = ...` line that does not use `gentenv`.
5. Add a **non-public** file called `.env` with those 2 properties:
   1. `TOKEN` (Your bot token)
   2. `SERVER_ID` (The ID of your server. You can set up the code not to use `SERVER_ID` if you are not in the process of testing the `react` slash command.)
6. Run the bot by running `main.py`.

:warning: **Warning:** Do not push `.env`.

## 📖 Usage instructions 📖

You can add the bot to your server using <a href="https://discord.com/oauth2/authorize?client_id=1488295878849597581" target="_blank">this link</a>.

It contains 1 slash command named `react` that takes two parameters:

1. `message_id`
2. `word`

`message_id` is the ID of the message you want the bot to react to. It can be copied from the same contextual menu used to reply to a message.

`word` is the word you want the bot to react with. No letter should repeat.

### ▶️ Demo ▶️

<img src="images/demo.gif" alt="demo"/>

## ✅ Code quality ✅

The `main` branch of this repository contains a GitHub Actions CI/CD pipeline to indicate if the code meets the below quality checks or not.

1. The <a href="https://pypi.org/project/black/" target="_blank">Black</a> style is respected for every Python file.
2. The pydoc documentation is valid.
3. The unit tests pass.
4. The coverage of the unit tests is at least 80%.

<a href="https://github.com/antoinebrunet1/word-reactor?tab=contributing-ov-file#-recreating-the-github-actions-pipeline-locally-" target="_blank">In the contributing section of this repository, I explain how to recreate the GitHub Actions pipeline locally.</a>

## 🛡️ Dependabot 🛡️

This project uses Dependabot to automatically open PRs for security issues and also for general library version updates.

## 🔒 `main` branch protection 🔒

The `main` branch is protected by a ruleset called "No deletions and force push for main".

## 🐋 Docker 🐋

This repository uses a custom Docker image located on Docker Hub for every job of the GitHub Actions pipeline. That image has been built using the `Dockerfile` file located at the root of this repository before being pushed to Docker Hub. The reason for using this custom image instead of `ubuntu:latest` is that the custom image already has the `pip` dependencies installed which means that they do not need to be installed every time the pipeline runs.

## 🌐 Hosting 🌐

This bot is hosted using Render. UptimeRobot is used to keep it alive.