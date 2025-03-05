import sys
sys.path.insert(0, "/workspaces/markitdown")  # markitdownのフォルダをパスに追加

from markitdown import MarkItDown

input_file = "test.xlsx"
markitdown = MarkItDown()
result = markitdown.convert(input_file)

with open("test.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)

print("変換完了: test.md に保存しました。")