import os

class DagProcessor():
    def __init__(self, base_folder_path: str="dags"):
        self.base_folder_path = base_folder_path
        self.dag_files = self.get_dag_files_from_folder()

    def get_dag_files_from_folder(self) -> list:
        '''
        returns list of dag files in the Dag Directory to process it
        '''
        dag_folder = os.path.join(self.base_folder_path)
        files = [f for f in os.listdir(dag_folder)]

        return files

    def process_dag_files(self) -> str: 
        dags = {}

        for file in self.dag_files: 
            file_path = os.path.join(self.base_folder_path, file)
            

def main():
    dag_processor = DagProcessor()
    dag_processor.process_dag_files()

if __name__ == "__main__":
    main()
