import os
import mlflow
import argparse #Provides tools for parsing command-line arguments.
import time


def eval(p1, p2):
    output_metric = p1**2 + p2**2
    return output_metric

def main(inp1, inp2):
    mlflow.set_experiment("Demo_Experiment")        #	Sets or creates an MLflow experiment named Demo_Experiment where all logs for this script will be stored.
    #with mlflow.start_run(run_name='Example Demo'):
    with mlflow.start_run():                       #	Starts a new MLflow run within the Demo_Experiment. Logging of parameters, metrics, and artifacts occurs inside this block.
        mlflow.set_tag("version","1.0.0")
        mlflow.log_param("param1",inp1)
        mlflow.log_param("param2",inp2) # key, value
        metric = eval(p1 = inp1, p2 = inp2)            #Calls the eval function with inp1 and inp2 to compute the metric and stores it in the variable metric.
        mlflow.log_metric("Eval_Metric",metric)  
        os.makedirs("dummy", exist_ok=True)             #Creates a directory named dummy if it doesn’t already exist.
        with open("dummy/example.txt", "wt") as f:      #Opens a file named example.txt inside the dummy directory in write mode (wt).
            f.write(f"Artifact created at {time.asctime()}")
        mlflow.log_artifacts("dummy")


if __name__ == '__main__': #Checks if the script is being executed directly (not imported as a module).
    args = argparse.ArgumentParser() #Initializes an argument parser to handle command-line inputs.
    args.add_argument("--param1","-p1", type=int, default=5)
    args.add_argument("--param2","-p2", type=int, default=10)
    parsed_args = args.parse_args()
    # parsed_args.param1
    main(parsed_args.param1, parsed_args.param2)