from os import getenv

from azureml.core import (
    Workspace,
    Experiment,
    ScriptRunConfig,
    Environment,
)
from dotenv import load_dotenv


def get_workspace(name: str, subscription_id: str, resource_group: str) -> Workspace:
    return Workspace.get(
        name=name, subscription_id=subscription_id, resource_group=resource_group,
    )


def run_experiment(name: str, workspace: Workspace):

    run_config = ScriptRunConfig(source_directory=".", script="experiment.py")

    run_config.run_config.target = "local"
    run_config.run_config.environment = Environment.from_existing_conda_environment(
        "fm-azureml-tut", "azureml-tut"
    )

    exp = Experiment(workspace, name)
    run = exp.submit(run_config)
    run.wait_for_completion(True)


if __name__ == "__main__":
    load_dotenv()
    ws = get_workspace(getenv("ML_WS"), getenv("SUB_ID"), getenv("ML_RG"))
    run_experiment("experiment-farooq-003", ws)
