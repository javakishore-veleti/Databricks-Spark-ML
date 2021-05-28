


```sh
# https://github.com/big-data-europe/docker-spark/blob/master/worker/Dockerfile

# https://maelfabien.github.io/bigdata/SparkInstall/#step-6-modify-your-bashrc

# How can I install multiple versions of Python on latest OS X and use them in parallel?
# https://stackoverflow.com/questions/36968425/how-can-i-install-multiple-versions-of-python-on-latest-os-x-and-use-them-in-par
brew install pyenv
pyenv install 3.7.2


cd Databricks-Spark-ML-Solutions/devops/sparkcluster
source Databricks-Spark-venv/bin/activate 
pyenv install 3.7.2 
pip install -r requirements.txt

 pyenv local 3.7.2


brew install scala
brew install gcc
xcode-select --install
brew install --build-from-source gcc
brew install apache-spark

 

```