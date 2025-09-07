# ml_practice

[![codecov](https://codecov.io/gh/shoyu-21/mlops_cicd_training/branch/main/graph/badge.svg)](https://codecov.io/gh/shoyu-21/mlops_cicd_training)

## pytest のサンプルを追加しました

- サンプルコード: `app/sample.py`
- パッケージエクスポート: `app/__init__.py`
- テスト: `tests/test_sample.py`

関数 `add` と `is_palindrome` を用意し、pytest の基本（パラメタ化、fixture 使用）を示すテストを用意しています。

### 実行方法（uv を使用）

1. 依存関係を同期（開発用依存も含む）
   - `uv sync --dev`
2. テストを実行
   - `uv run pytest -q`

`pytest -q` だけでも `.venv` が有効化されていれば動作します。
