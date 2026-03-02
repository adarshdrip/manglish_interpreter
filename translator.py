# translator.py

def classify_line(line):
    stripped = line.strip()

    if stripped.startswith("allenkil enkil "):
        return "ELIF"
    elif stripped.startswith("enkil "):
        return "IF"
    elif stripped.startswith("allenkil"):
        return "ELSE"
    elif stripped.startswith("varunna vare "):
        return "WHILE"
    elif stripped.startswith("vendiy "):
        return "FOR"
    elif stripped.startswith("parayuka "):
        return "PRINT"
    else:
        return "OTHER"


def translate_line(line):
    indent = len(line) - len(line.lstrip())
    indentation = " " * indent
    stripped = line.strip()

    line_type = classify_line(line)

    if line_type == "IF":
        condition = stripped.replace("enkil ", "")
        return indentation + f"if {condition}"

    elif line_type == "ELIF":
        condition = stripped.replace("allenkil enkil ", "")
        return indentation + f"elif {condition}"

    elif line_type == "ELSE":
        return indentation + "else:"

    elif line_type == "WHILE":
        condition = stripped.replace("varunna vare ", "")
        return indentation + f"while {condition}"

    elif line_type == "FOR":
        condition = stripped.replace("vendiy ", "")
        return indentation + f"for {condition}"

    elif line_type == "PRINT":
        content = stripped.replace("parayuka ", "")
        return indentation + f"print({content})"

    else:
        return line


def translate_to_python(code):
    lines = code.split("\n")
    translated_lines = []

    for line in lines:
        translated_lines.append(translate_line(line))

    return "\n".join(translated_lines)