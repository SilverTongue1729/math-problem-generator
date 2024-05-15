# Math Problem Generator

This project generates simple math problems for addition and multiplication, writes them in LaTeX, and saves them as a PDF. It can be run from the command line with a configuration file.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/SilverTongue1729/math-problem-generator.git
    cd math-problem-generator
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Command Line

You can run the LaTeX generation from the command line using a configuration file:

```sh
python main.py config.yaml
```

### Configuration File

The `config.yaml` file specifies the type of output, output file, and a list of problem configurations.

```yaml
type: latex
output_file: output/problems
font_size: Large
problems:
  - ['+', 10, 1, 10]
  - ['*', 10, 1, 10]
```

- `type`: Specifies the output type (`latex` for now, more types can be added later).
- `output_file`: The file path where the output will be saved.
- `font_size`: The font size for the LaTeX document (e.g., `normalsize`, `Large`, `small`).
- `problems`: A list of problem configurations where each configuration is a tuple containing:
  - The symbol (`+` for addition, `*` for multiplication).
  - The number of problems.
  - The lower bound for the numbers.
  - The upper bound for the numbers.

### Example Output

Check the `examples` directory for example LaTeX output.
