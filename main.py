import yaml
import os
import numpy as np
from problem_generator import generate_problems
from latex_writer import write_problems_to_latex

def main(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    output_type = config.get('type', 'latex')
    output_file = config.get('output_file', 'output/problems')
    font_size = config.get('font_size', 'Large')
    num_columns = config.get('columns', 4)
    title = config.get('title', 'Math Problems')
    array_stretch = config.get('vertical_spacing', 1.5)
    seed = config.get('seed', None)

    if seed is not None:
        np.random.seed(seed)

    all_problems = []

    for problem_config in config.get('problems', []):
        problems = generate_problems(problem_config)        
        all_problems.extend(problems)

    if output_type == 'latex':
        write_problems_to_latex(all_problems, output_file, font_size, num_columns, array_stretch, title)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate math problems and write them to a file.')
    parser.add_argument('config_path', type=str, help='Path to the config YAML file')
    args = parser.parse_args()

    main(args.config_path)
