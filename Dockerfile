FROM python:3
COPY *.py ~
RUN pip install black pydocstyle discord.py pytest pytest-mock python-dotenv pytest-asyncio flask pytest-cov pdoc radon