import os

models = ['deepseek', 'llama', 'mistral', 'phi', 'gemini']
tasks = [f'task_{i}' for i in range(1, 10)]
runs = [f'run_{str(i).zfill(2)}.py' for i in range(1, 11)]

base_dir = r"c:\Users\kalup\Desktop\Thesis\results"

for model in models:
    for task in tasks:
        dir_path = os.path.join(base_dir, model, task)
        os.makedirs(dir_path, exist_ok=True)
        for run in runs:
            file_path = os.path.join(dir_path, run)
            with open(file_path, 'w') as f:
                pass
print("Directories and files created successfully.")
