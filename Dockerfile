FROM python:3.12.9-bookworm

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

# 環境変数の設定
ENV LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8 \
    TZ=Asia/Tokyo

RUN pip install --upgrade pip

# Poetryのパスの設定
ENV PATH /root/.local/bin:$PATH

# Poetryをインストール. バージョンは1.8.5を指定.
RUN curl -sSL https://install.python-poetry.org | python - --version 1.8.5

# Poetryが仮想環境を生成しないようにする
RUN poetry config virtualenvs.create false

# `pyproject.toml` と `poetry.lock` をコピー
COPY pyproject.toml poetry.lock* ./

# 依存関係をインストール
RUN poetry install --no-root

# PYTHONPATH 環境変数にプロジェクトの src ディレクトリを追加する
# - これにより、コンテナ内で `mutation` モジュールをインポートする際に
#   フルパスではなく、`from mutation.script import ...` のように
#   直接インポートできるようになる
# - `${PYTHONPATH}` は既存の PYTHONPATH を維持するための記述
ENV PYTHONPATH="${PYTHONPATH}:/root/mutation-testing/src"