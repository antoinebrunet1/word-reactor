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

You can also run the command

```
make check_style
```

which uses `Makefile`.

#### 📖 Documentation 📖

Please make sure that the pydoc documentation is valid by running the command

```
pydocstyle src/main.py
```

The output of the command will indicate if the documentation is valid or not. If it is not, the issues will be explained.

You can also run the command

```
make check_docs
```

which uses `Makefile`.

#### 🧪 Unit tests coverage 🧪

Please make sure that the coverage is at least 80% by running the command

```
python3 -m pytest --cov=main --cov-fail-under=80
```

You can also run the command

```
make check_cov
```

which uses `Makefile`.

To see the missed lines, you can run the command

```
python3 -m pytest --cov=main --cov-fail-under=80 --cov-report json
```

This will produce `coverage.json` which indicates the missed lines.

You can also run the command

```
make check_cov_with_report
```

which uses `Makefile`.

To run all the unit tests, you can run the command

```
python3 -m pytest test/test_main.py
```

You can also run the command

```
make run_all_tests
```

which uses `Makefile`.

If you are using PyCharm, you can also right-click on `test_main.py` and select the option to run all the tests.

To run a specific unit test, you can run the command

```
make run_specific_test TEST_NAME=test_name
```

with the name of the unit test from `test/test_main.py` instead of `test_name`.

## 💬 Support 💬

If you have any questions, you can go under Discussions in the repository.
