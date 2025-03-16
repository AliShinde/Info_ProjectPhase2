# Info_ProjectPhase2
Information retrieval Project Phase2
Download the model folder and add to the path. Create a model folder and follow the commands mentioned

## Data for civilsum
[train.csv](https://drive.google.com/file/d/1WX5w-ClK82Yy916350bRp3hcuqab1D-x/view?usp=sharing)


[test.csv](https://drive.google.com/file/d/1v0EM35CFWxFPc5D4bFxpf59mV_kEv0pw/view?usp=sharing)

To create the paragraphs use the utils method as shown 
```
import pandas as pd
from util import find_paragraph_refs, process_data

train = pd.read_csv("train.csv")
train_paragraphs = find_paragraph_refs(train.summary)
processed_data = process_data(train, train_paragraphs)
pd.to_csv("paragraphs_train.csv", index=False)
```


Save the csv files to a /data folder in the project directory. 
To generate the preprocessed data in terms of paragraphs reference use the command


```$ python model/fsum.py preprocess_folder path/to/data```


## Evaluation and Results
To generate the evaluation results


```  python model/fsum.py evaluate --data_dir  path/to/data --content_type oracle --output_dir output ```


## Data for medical reports
Link for test and train samples


[Data](https://github.com/Franck-Dernoncourt/pubmed-rct/tree/master/PubMed_20k_RCT)

Store the training samples in medical_data folder and run the following command to preprocess

``` python model/fsum.py preprocess_folder path/to/medical_data```

## Evaluate

To generate evaluation results


```  python model/fsum.py evaluate --data_dir  path/to/medical_data --dataset_name medical --training_domain medical --content_type oracle --output_dir output ```
