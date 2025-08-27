from core.dag_processor import dag

def main():
    @dag(dag_id="sample_dag", start_date="2023-01-01", scheduled_interval="@daily")
    def example_dag(dag_obj):
        def extract():
            print("Extracting...")

        def transform():
            print("Transforming...")
            raise Exception("Simulating a failure in our system")

        def load():
            print("Loading...")

        dag_obj.create_task("123", extract)
        dag_obj.create_task("123", transform)
        dag_obj.create_task("123", load)
    
    dag_instance = example_dag()
    dag_instance.run()
    
if __name__ == "__main__":
    main()