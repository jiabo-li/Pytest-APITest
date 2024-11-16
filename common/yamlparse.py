import yaml
import os
# case {filename:}
base_path = f"/TestCases"
class yamlparser:
    def __init__(self):
        self.g_tasks = []

    def get_all_tasks(self,path):
        files = [os.path.join(path,file) for file in os.listdir(path)]
        case_infor = {}
        for file in files:
            print(file.title())
            with open(file ,"r",encoding="utf-8") as file:
                file_tasks = yaml.safe_load(file)
            self.g_tasks.append(file_tasks)

    def show_all_task(self):
        for task in self.g_tasks:
            print(task)

if __name__ == "__main__":
    ypaser = yamlparser()
    ypaser.get_all_tasks(base_path)
    ypaser.show_all_task()
