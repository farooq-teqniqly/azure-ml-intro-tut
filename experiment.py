from azureml.core import Run
import pandas as pd

run = Run.get_context()
data = pd.read_csv("vehicles.csv")
row_count = len(data)
run.log("observations", row_count)
data.sample(100).to_csv("outputs/vehicles_sample.csv", index=False, header=True)
run.complete()
