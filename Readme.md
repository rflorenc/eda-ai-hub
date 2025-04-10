# EDA AI Hub

EDA AI Hub is a playground for Exploratory Data Analysis (EDA), Machine Learning and Deep Learning projects (AI), using a common code base for multiple jupyter notebooks.    

## Projects

Sample projects included:  

- [Image Caption Generation using COCO dataset](nb_ImageCaptionGeneration_COCO.ipynb) (Deep Learning)  
  - Uses a subset of the [COCO "Common Objects in Context" dataset](https://cocodataset.org/) for image caption generation  
  - Features transfer learning, by using a pretrained ResNet152 on the ImageNet dataset  
  - Compares prediction results using BLEU score and cosine similarity  

- [DARWIN (Diagnosis Alzheimer's With Handwriting)](nb_DARWIN.ipynb) (Machine Learning)  
  - Analyzes Alzheimer's patients handwriting patterns using the DARWIN (Diagnosis Alzheimer's With Handwriting) dataset  
  - Features in-depth overfitting analysis, i.e.: PCA vs NonPCA  
  - Compares Logistic Regression and Support Vector Classifier results
  
- [Adventure Works 2022 business analysis](nb_adventureworks.ipynb) (Data Science)  
  - Uses the [Adventure Works 2022](https://www.kaggle.com/datasets/algorismus/adventure-works-in-excel-tables/data) dataset and provides sports equipment sales metrics and business information.  

Note that these projects are extensive, so it's recommended to use an IDE's Outline view for navigating notebook sections.  

## Learning examples  

Simpler learning examples using Kaggle datasts, include:
- GPU vs CPU analysis
- NASA Facilities dataset analysis
- World Cities statistics

Refer to the available jupyter notebooks (`*.ipynb`) for details.  

### Requirements  

We need to install all the required python modules.  
This can be done by executing `make requirements` in the base project folder.    

```bash 
cd $HOME/workspace/eda-hub  
make requirements
```