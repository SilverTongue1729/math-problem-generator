import yaml
import os
from problem_generator import generate_addition_problems, generate_multiplication_problems
from latex_writer import write_problems_to_latex

def main(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    output_type = config.get('type', 'latex')
    output_file = config.get('output_file', 'output/problems')
    font_size = config.get('font_size', 'normalsize')

    all_problems = []

    for problem_config in config.get('problems', []):
        symbol = problem_config[0]
        num_problems = problem_config[1]
        lower_bound = problem_config[2]
        upper_bound = problem_config[3]

        if symbol == '+':
            problems = generate_addition_problems(num_problems, lower_bound, upper_bound)
        elif symbol == '*':
            problems = generate_multiplication_problems(num_problems, lower_bound, upper_bound)
        
        all_problems.extend(problems)

    if output_type == 'latex':
        write_problems_to_latex(all_problems, output_file, font_size)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate math problems and write them to a file.')
    parser.add_argument('config_path', type=str, help='Path to the config YAML file')
    args = parser.parse_args()

    main(args.config_path)
