
## Setting up Environment

Python version: 3.12.7

### Mac 使用 pyenv 來管理 python 版本(跟 rbenv 一樣來管理 ruby 版本)
- install pyenv: <https://github.com/pyenv/pyenv>

- Install Python

  ```bash
  pyenv install 3.12.7
  ```

- Set local Python version

  ```bash
  pyenv local 3.12.7
  ```
  設定完畢會出現一個 .python-version 的檔案

- create the project virtaul enviroment

  ```bash
  python -m venv .venv
  ```

-  activate the env

  ```bash
  source .venv/bin/activate
  ```

- install default pip

  先用來建立基本的 pip 套件, 包括 poetry
  ```bash
  pip install -r requirements.txt
  ```

- install dependencies via poetry

  ``` bash
  poetry install
  ```


## 設定key及啟動測試

- copy .env.example
  
```
mv .env.example .env
```
- set up .env api key
```
OPENAI_API_KEY=sk-proj-api-key
```
- run
```
python main.py
```

