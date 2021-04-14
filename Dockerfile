FROM python:3.8.2

RUN apt-get update \
  && apt-get upgrade -y \
  # imageのサイズを小さくするためにキャッシュ削除
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && pip install --upgrade pip 
  # && apt-get install -y locales \
  # && locale-gen ja_JP.UTF-8

# ENV LANG ja_JP.UTF-8
# ENV LANGUAGE ja_JP:ja
# ENV LC_ALL ja_JP.UTF-8
# ENV TZ JST-9
# RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8
ENV TERM xterm
# 作業ディレクトリ
WORKDIR /python_101/

# RUN apt-get install -y vim less
RUN pip install --upgrade setuptools

COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt

WORKDIR /python_101/src