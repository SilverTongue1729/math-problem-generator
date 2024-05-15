from pylatex import Document, Section, NoEscape, Command

def write_problems_to_latex(problems, filename, font_size='normalsize'):
    doc = Document()
    doc.preamble.append(Command('usepackage', 'geometry'))
    doc.preamble.append(Command('geometry', 'margin=1in'))
    doc.preamble.append(Command('usepackage', 'array'))
    doc.preamble.append(Command('usepackage', 'tabularx'))

    with doc.create(Section('Math Problems')):
        doc.append(NoEscape(f'\\{font_size}'))

        num_problems = len(problems)
        num_columns = 4
        num_rows = (num_problems + num_columns - 1) // num_columns  # ceiling division

        # Create the table manually as a LaTeX string
        table_content = []
        for i in range(num_rows):
            row = []
            for j in range(num_columns):
                index = i + j * num_rows
                if index < num_problems:
                    [operand1, operand2], _, operator = problems[index]
                    problem_str = f"{operand1} {operator} {operand2} ="
                    row.append(problem_str)
                else:
                    row.append('')
            table_content.append("& ".join(row) + " \\\\")
        
        table_latex = "\\begin{tabularx}{\\textwidth}{>{\\centering\\arraybackslash}X>{\\centering\\arraybackslash}X>{\\centering\\arraybackslash}X>{\\centering\\arraybackslash}X}\n" + "\n".join(table_content) + "\n\\end{tabularx}"

        doc.append(NoEscape(table_latex))
    
    doc.generate_pdf(filename, clean_tex=False)