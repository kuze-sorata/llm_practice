# 🚀 Colab → GitHub 運用テンプレ

## 🔧 初期セットアップ（毎回）

```bash
# リポジトリを取得
!git clone https://github.com/sora1871/llm.git
%cd llm

# Gitのユーザー情報設定
!git config --global user.name "sora1871"
!git config --global user.email "<YOUR_EMAIL>"  ← 公開しない

#リポジトリ接続
!git remote add origin https://github.com/sora1871/llm.git
```

---

## ✏️ 作業後のアップロード手順

```bash
# 変更確認
!git status

# 変更を追加
!git add .

# コミット
!git commit -m "update"

# GitHubへ送信
!git push origin main
```

---

## 🔐 認証（必要なとき）

* Username: `sora1871`
* Password: `<personal_token>` ← 絶対に公開しない

---

## 🔁 最新を取得（必要なとき）

```bash
!git pull origin main
```

---

## ⚠️ 注意

* Colabは毎回環境がリセットされる
* 認証（PAT）は毎回求められることがある
* PATはコードやREADMEに書かないこと

---

## 🧠 メモ

* `git add` → 変更を選ぶ
* `git commit` → ローカル保存
* `git push` → GitHubにアップロード

---

## 🔒 置き換える箇所
* `<personal_token>` → 認証用トークン(非公開)
* `<YOUR_EMAIL>` → メール（非公開）

---

## ⚡ ワンライナー（慣れたら）

```bash
!git add . && git commit -m "update" && git push origin main
```
