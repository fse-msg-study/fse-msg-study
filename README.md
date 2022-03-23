# Revisiting Learning-based Commit Message Generation  

This is the replication package for "Revisiting Learning-based Commit Message Generation". We provide the scripts to reproduce all the results of the paper.

## 1 Preparation

We provide a requirements file `requirements.txt` containing all the packages needed for reproduction. You can run the following commands to create the conda environment and install all the packages.

```shell
$ conda create -n fse-msg-study python=3.8
$ conda activate fse-msg-study
$ python3 -m pip install -r requirements.txt
```

## 2 Commit Messages

In this section, we introduce the commit messages used in each RQ.

#### Default Models (RQ1)

In RQ1, the commit messages generated by **the default models** are used and analyzed. For each technique , the commit messages generated by the default model are placed in the file `CommitMessages/DefaultModels/output_modelname_train`  and `CommitMessages/DefaultModels/output_modelname` for the training set and testing set respectively ,  and `modelname`  is one of NMT, PtrGNCMsg, CODISUM, and CoreGen. 

#### Modified Dataset (RQ2)

In RQ2, the commit messages generated by **the models training with various modified datasets** are used and analyzed. For each technique, the commit messages generated by the model training with the dataset which decreases the pattern ratio by ***R*** are placed in the file `CommitMessages/ModifiedDataset/output_modelname_R`, and ***R*** is from 0 to 0.9. For example, the commit messages generated by NMT training with the dataset which decreases the pattern ratio by 20% are placed in `CommitMessages/ModifiedDataset/output_nmt_0.2`.

#### Input Representation (RQ3)

In RQ3,  the commit messages generated by **the models training with various input representations** are used and analyzed. For each technique, the commit messages generated by the model training with mark representation and code representation are placed in the file`CommitMessages/InputRepresentation/output_modelname_onlymark` and `CommitMessages/InputRresentation/output_modelname_onlyword` respectively.

#### Component (RQ4)

In RQ4, the commit messages generated by **the models removing each component** are used and analyzed. For each technique, the commit messages generated by the model removing different components are placed in the file `CommitMessages/Component/output_modelname_noatten`, `CommitMessages/Component/output_modelname_nocopy`, or `CommitMessages/Component/output_modelname_noanony`.

## 3 Patterns

In this section, we introduce the steps to obtain the patterns.  We use the MaxSP [1], a sequential pattern mining algorithm, to mine frequent patterns
from the commit messages generated by each technique.  We use the implementation of MaxSP provided by the data mining library SPMF [2], and the documentation is in this [website](https://www.philippe-fournier-viger.com/spmf/MaxSP.php).  Switch to the directory `Patterns`, you can execute `get_patterns.sh`  to get the frequent patterns of each technique, which will be saved in `Patterns/results`.

```shell
$ bash get_patterns.sh
```

## 4 Reproduction 

In this section, we show the scripts and steps to reproduce the results present in the paper. We name the scripts to get the Table ***X***/Figure ***X*** presented in RQ ***Y*** of the paper as  `get_rqY_tableX.py`/`get_rqY_figureX.py`, which is placed in the folder `Scripts`. For example, the Figure 5 is presented in RQ2, so the script to get it is `get_rq2_table5.py`.  Switch to the directory  `Scripts`, you can run each script to get the corresponding table/figure, which will be saved in `Scripts/TablesAndFigures/rqY_tableX.tex` or `Scripts/TablesAndFigures/rqY_figureX.png`.  The table is in the format of *latex*, and can be compiled to *pdf*, and the package *multirow* and *booktabs* are needed for compilation.

```shell
$ python get_rqY_tableX.py
```

or

```shell
$ python get_rqY_figureX.py
```

In addition, we put the commands to execute all the scrips to one single script `run_total.sh`, and you can switch to the directory  `Scripts` and get all the tables/figures of the paper by running

```shell
$ bash run_total.sh
```

## 5 Reference

[1] Fournier-Viger P, Wu C W, Tseng V S. Mining maximal sequential patterns without candidate maintenance[C]//International Conference on Advanced Data Mining and Applications. Springer, Berlin, Heidelberg, 2013: 169-180.

[2] Fournier-Viger P, Lin J C W, Gomariz A, et al. The SPMF open-source data mining library version 2[C]//Joint European conference on machine learning and knowledge discovery in databases. Springer, Cham, 2016: 36-40.







