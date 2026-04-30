<h1 align="center">
    🤝 Contributing 🤝
</h1>

<p align="center">
  <img src="images/collaboration.png" alt="logo" width="=450px" height="300px"/>
  <br>
  Thank you for contributing to the project! 😊
  <br>
</p>

<hr>

## 📜 Code of conduct 📜

There is a [code of conduct](https://github.com/antoinebrunet1/word-reactor/blob/main/CODE_OF_CONDUCT.md).

## 📝 Issues 📝

You can look at open issues or create a new one by choosing from the 3 available templates.

## 📥 Pull requests 📥

You can make pull requests. Before creating a pull request, please recreate the GitHub Actions pipeline as explained below.

### 💻 Recreating the GitHub Actions pipeline locally 💻

#### 📖 Documentation 📖

Please make sure that the pydoc documentation is valid by running the command

```
pydocstyle main.py
```

The output of the command will indicate if the documentation is valid or not. If it is not, the issues will be explained.

#### 🧪 Unit tests 🧪

Please make sure that the unit tests pass by running the command

```
python3 -m pytest
```

Please make sure that the coverage is at least 80% by running the command

```
python3 -m pytest --cov=main --cov-fail-under=80
```

## 💬 Support 💬

If you have any questions, you can go under Discussions in the repository.
