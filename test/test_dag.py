from Dag.etl_dag import dag

def test_dag_loaded():assert dag is not None

def test_dag_id():assert dag.dag_id == "simple_etl"

def test_dag_has_task():assert "run_etl" in dag.task_ids

def test_dag_has_one_task():assert len(dag.tasks) == 1
