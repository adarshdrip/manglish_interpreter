# executor.py

import subprocess
import uuid
import os

def execute_python_code(code):
    filename = f"temp_{uuid.uuid4().hex}.py"

    with open(filename, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["python", filename],
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout
        error = result.stderr

    except subprocess.TimeoutExpired:
        output = ""
        error = "Execution timed out!"

    finally:
        if os.path.exists(filename):
            os.remove(filename)

    return output, error