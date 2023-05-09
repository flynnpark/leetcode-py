import os
import shutil


def get_solution_directory(file: str):
    number = file[5:9]
    return f'./solutions/solution_{number}'


def main():
    files = os.listdir('./tests')

    for file in files:
        if file.startswith('test_'):
            directory = get_solution_directory(file)

            source_path = f'./tests/{file}'
            destination_path = f'{directory}/test_solution.py'
            shutil.copy(source_path, destination_path)


if __name__ == '__main__':
    main()
