import os
import re

def replace_display_math_notation(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    content = re.sub(r'\$\$(.*?)\$\$', r'{{< katex display >}}\1{{< /katex >}}', content)

    with open(file_path, "w") as f:
        f.write(content)

def replace_inline_math_notation(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    content = re.sub(r'\$(.*?)\$', r'{{< katex >}}\1{{< /katex >}}', content)

    with open(file_path, "w") as f:
        f.write(content)


root_dir = os.path.dirname(os.path.realpath(__file__))
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = subdir + os.sep + file
        if file_path.endswith(".md"):
            replace_display_math_notation(file_path)
            replace_inline_math_notation(file_path)