1. Add Miniconda(Anaconda) to PATH. (c:\ProgramData\Miniconda3\Scripts)
2. Create conda environment ```conda create -n myenv python=3.6.5```
3. Activate conda environment ```conda activate myenv```
4. ```conda install notebook ipykernel```
5. ```ipython kernel install --user --name myenv --display-name "Python (myenv)"```
6. ```pip install azureml-sdk[notebooks,automl]```
7. ```pip install python-dotenv```