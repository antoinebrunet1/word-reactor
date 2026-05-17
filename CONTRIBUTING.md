<h1 align="center">
    <picture>
        <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/2728/512.webp" type="image/webp">
        <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/2728/512.gif" alt="✨" width="32" height="32">
    </picture> Contributing <picture>
        <source srcset="https://fonts.gstatic.com/s/e/notoemoji/latest/2728/512.webp" type="image/webp">
        <img src="https://fonts.gstatic.com/s/e/notoemoji/latest/2728/512.gif" alt="✨" width="32" height="32">
    </picture>
</h1>

<p align="center">
  Thank you for contributing to the project! 😊
  <br>
</p>

<hr>

## 📜 Code of conduct 📜

There is a <a href="https://github.com/antoinebrunet1/word-reactor/blob/main/CODE_OF_CONDUCT.md" target="_blank">code of conduct</a>.

## 📝 Issues 📝

You can look at open issues or create a new one by choosing from the 3 available templates.

## 📥 Pull requests 📥

You can make pull requests. Before creating a pull request, please recreate the GitHub Actions pipeline as explained below.

### 💻 Recreating the GitHub Actions pipeline locally 💻

#### 📐 Style 📐

Please make sure the <a href="https://pypi.org/project/black/" target="_blank">Black</a> style is followed. You can apply the style to all files by running the command

```
python3 -m black .
```

and you can check if the style is followed in all files by running the command

```
python3 -m black --check .
```

#### 📖 Documentation 📖

Please make sure that the pydoc documentation is valid by running the command

```
pydocstyle main.py
```

The output of the command will indicate if the documentation is valid or not. If it is not, the issues will be explained.

#### 🧪 Unit tests coverage 🧪

Please make sure that the coverage is at least 80% by running the command

```
python3 -m pytest --cov=main --cov-fail-under=80
```

## 💬 Support 💬

If you have any questions, you can go under Discussions in the repository.
