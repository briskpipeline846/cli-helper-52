# cli-helper-52

`cli-helper-52` is a lightweight Python utility designed to streamline common command-line interface interactions and task automation. It provides a robust wrapper for handling shell commands, file system operations, and standard logging within your terminal workflows.

### Features

*   **Command Orchestration:** Effortlessly execute shell subprocesses with real-time stream handling and customizable error reporting.
*   **Intuitive Argument Parsing:** Simplified decorators to define CLI flags, environment variables, and positional arguments without the boilerplate of `argparse`.
*   **Task Chaining:** Easily define sequences of terminal operations that execute conditionally based on the exit codes of previous steps.
*   **Structured Logging:** Integrated colorful terminal output streams that differentiate between status updates, debug data, and critical failures.

### Installation

Ensure you have Python 3.8+ installed. You can install the package directly via pip:

```bash
pip install cli-helper-52
```

To install from source for development purposes:

```bash
git clone https://github.com/Developer/cli-helper-52.git
cd cli-helper-52
pip install -e .
```

### Basic Usage

Import the main controller to manage your subprocesses and handle shell commands seamlessly:

```python
from cli_helper import CommandRunner

runner = CommandRunner()

# Execute a system command and capture the output
result = runner.execute("git status")

if result.success:
    print(f"Current branch status: {result.stdout}")
else:
    print(f"Error: {result.stderr}")
```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions for new utility modules or improvements to the current API.

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.