import tkinter as tk
from tkinter import ttk as ttk

root = tk.Tk()
root.title("Python Command")
root.geometry("600x670")

notebook = ttk.Notebook(root)

tab_command = tk.Frame(notebook, bg='black')
tab_git = tk.Frame(notebook, bg='black')
notebook.add(tab_command, text="command",)
notebook.add(tab_git, text="git")
notebook.pack()

terminal_commands = [
    "ls カレントディレクトリ内にあるファイルを表示する",
    "cd カレントディレクトリにあるファイルに移動する",
    "pwd カレントディレクトリのパスを表示する",
    "touch 中身が空のファイルを作る",
    "mkdir 新しい空のディレクトリを作る",
    "mv ファイルを移動したりファイル名を変更する",
    "cp ファイルをコピーする",
    "rm ファイルを削除する",
    "open ターミナルからFinderでファイルを開く",
    "source ファイルの読み込み有効にする",
    "history これまでのコマンド履歴を表示する",
]

git_commands = [
    "git init リポジトリを新規作成",
    "git clone リポジトリをコピー",
    "git gc リポジトリを最適化",
    "git push ローカルリポジトリの変更点をリモートリポジトリへマージ",
    "git pull リモートリポジトリの変更点をローカルリポジトリへマージ",
    "git add コミットの対象ファイルを登録",
    "git commit 変更されたファイルをコミット",
    "git reset 直前のコミットを取り消し",
    "git revert 特定のコミットを取り消し",
    "git tag コミットにタグを付ける",
    "git log コミット履歴を表示",
    "git status 作業ツリー内の差分ファイルを表示",
    "git diff ファイル内の差分箇所を表示",
    "git mv ファイルを移動／ファイル名を変更",
    "git stash 作業ツリーの状態を一時的に保存",
    "git branch ブランチの作成／一覧表示",
    "git checkout 処理対象ブランチの切り替え",
    "git merge 別のブランチから変更点をマージ",
    "git revbase 派生元ブランチに変更点をマージ",
]

for terminal_command in terminal_commands:
    terminal = tk.Label(tab_command, text=terminal_command, background='black')
    terminal.pack(anchor="w")

for git_command in git_commands:
    git = tk.Label(tab_git, text=git_command, background='black')
    git.pack(anchor="w")

root.mainloop()