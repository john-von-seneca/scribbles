# ml-and-what-not
Explorations in Machine Learning


**Installing jupyter and extensions**

1. pip[3] install [--user --upgrade] jupyter
1. Installing extensions 
   1. clone https://github.com/ipython-contrib/IPython-notebook-extensions to \<ipy-ext-dir\>
   1. go to (ipython-extensions)[https://github.com/ipython-contrib/IPython-notebook-extensions/wiki/Home-4.x-(Jupyter)]
   1. scroll down to the part about finding nbextensions directory and find the path of the directory.
   1. Say \<jup_data_dir\> is the fullpath to it
      * On ubuntu, it might be "~/.local/share/jupyter/" if jupyter was installed using the --user switch of pip install
      * On OSX, it might be "~/Library/Jupyter/extensions"
   1. cd <ipy-ext-dir>
   1. cp -R nbextensions/ \<jup_data_dir\>/
   1. cp -R extensions/   \<jup_data_dir\>/
   1. cp -R templates/    \<jup_data_dir\>/


**Using pyspark with ipython notebook**

```
PYSPARK_PYTHON=python2 PYSPARK_DRIVER_PYTHON=ipython2 PYSPARK_DRIVER_PYTHON_OPTS="notebook" $SPARK_HOME/bin/pyspark
```
