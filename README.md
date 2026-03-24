*This project has been created as part of the 42 curriculum by hwakatsu.*

# Cosmic Data

## Description / 説明

### English
Cosmic Data is a Python project focused on learning Pydantic models and validation through space-themed exercises. The goal is to build reliable data models, apply field constraints, implement custom validation rules, and validate nested data structures using Pydantic 2.x.

This repository contains three exercises:

- `ex0/space_station.py`: basic `BaseModel` and `Field` validation
- `ex1/alien_contact.py`: custom business rules with `@model_validator`
- `ex2/space_crew.py`: nested models and mission-level validation

The project progressively moves from simple validated models to more complex real-world validation scenarios.

### 日本語
Cosmic Data は、宇宙をテーマにした演習を通して Pydantic モデルとバリデーションを学ぶ Python プロジェクトです。目的は、信頼できるデータモデルを作成し、フィールド制約を設定し、独自のバリデーションルールを実装し、Pydantic 2.x を使ってネストしたデータ構造を検証できるようになることです。

このリポジトリには 3 つの exercise があります。

- `ex0/space_station.py`: `BaseModel` と `Field` を使った基本的なバリデーション
- `ex1/alien_contact.py`: `@model_validator` を使った業務ルールの検証
- `ex2/space_crew.py`: ネストしたモデルとミッション全体の検証

シンプルなモデル検証から、より実践的で複雑な検証へ段階的に進む構成です。

## Instructions / 実行方法

### English

Requirements:

- Python 3.10 or later
- `pip`
- Pydantic 2.x

Recommended setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pydantic
```

Run each exercise from the repository root:

```bash
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

Optional lint check:

```bash
flake8 ex0 ex1 ex2
```

There is no compilation step. After installing dependencies, execute each file directly with Python.

### 日本語

必要環境:

- Python 3.10 以上
- `pip`
- Pydantic 2.x

推奨セットアップ:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pydantic
```

リポジトリのルートで、各 exercise は次のように実行できます。

```bash
python3 ex0/space_station.py
python3 ex1/alien_contact.py
python3 ex2/space_crew.py
```

任意の lint チェック:

```bash
flake8 ex0 ex1 ex2
```

コンパイルは不要です。依存関係をインストールしたあと、各 Python ファイルを直接実行してください。

## Features / 主な内容

### English

- Pydantic `BaseModel` definitions
- Validation constraints with `Field`
- Custom validation with `@model_validator(mode="after")`
- Enum-based constrained values
- Nested model validation for mission and crew data

### 日本語

- Pydantic の `BaseModel` 定義
- `Field` を使った制約付きバリデーション
- `@model_validator(mode="after")` による独自検証
- Enum を使った値の制約
- ミッションとクルーデータに対するネストモデル検証

## Usage Overview / 使い方の概要

### English

- `ex0` validates space station monitoring data and shows a failure case.
- `ex1` validates alien contact logs with custom business rules.
- `ex2` validates mission data that contains a list of crew members.

### 日本語

- `ex0` では宇宙ステーションの監視データを検証し、失敗例も表示します。
- `ex1` ではエイリアン接触ログを独自ルール込みで検証します。
- `ex2` では乗組員リストを含む宇宙ミッションデータを検証します。

## Resources / 参考資料

### English

Classic references related to the topic:

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic Fields Documentation](https://docs.pydantic.dev/latest/concepts/fields/)
- [Pydantic Validators Documentation](https://docs.pydantic.dev/latest/concepts/validators/)
- [Python Documentation: enum](https://docs.python.org/3/library/enum.html)
- [Python Documentation: datetime](https://docs.python.org/3/library/datetime.html)
- [flake8 Documentation](https://flake8.pycqa.org/)

AI usage in this project:

- AI was used for documentation support and README drafting.
- It was used to summarize the subject requirements, organize sections, and provide bilingual English/Japanese wording.
- Any generated text or suggestions should still be reviewed manually to ensure they accurately match the actual implementation.

### 日本語

この課題に関連する代表的な参考資料:

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic Fields Documentation](https://docs.pydantic.dev/latest/concepts/fields/)
- [Pydantic Validators Documentation](https://docs.pydantic.dev/latest/concepts/validators/)
- [Python Documentation: enum](https://docs.python.org/3/library/enum.html)
- [Python Documentation: datetime](https://docs.python.org/3/library/datetime.html)
- [flake8 Documentation](https://flake8.pycqa.org/)

このプロジェクトにおける AI の利用:

- AI はドキュメント補助と README 作成支援に使用しました。
- 課題要件の整理、セクション構成、英語と日本語の文章調整に利用しました。
- 生成された内容や提案は、実装と一致しているかを手動で確認する前提です。

## More Information / 補足

### English
This project is designed to demonstrate how Pydantic helps create safer and clearer Python data models for structured application data.

### 日本語
このプロジェクトは、Pydantic によって構造化データを安全かつ明確に扱える Python モデルを作る方法を示すことを目的としています。
