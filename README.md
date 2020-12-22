# Retinal Scan Models

Retinal scans are useful tools for detecting a number of eye conditions. However, it requires an expert to read and decipher these images. The goal of this project is to develop models for detecting various types of disease. In the first iteration the model created will try to distinguish between,

* Diabetic Retinopathy
* Glaucoma
* Normal scans
* Other ailments

This dataset was taken from a Kaggle competition. The details can be found here (https://www.kaggle.com/c/vietai-advance-course-retinal-disease-detection/overview)

## Tools Used
* Jupyter Notebooks
* OpenCV
* PIL (pillow)
* Python 3.8
* Tensorflow 2.3

### What is Diabetic Retinopathy?

The image below shows a high contrast example of Diabetic Retinopathy

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/high_contrast_images/dbr.jpg" alt="Diabetic Retinopathy" width="250"/>

### What is Glaucoma?

The image below shows an example of Glaucoma. The area affected by Glaucoma is around the optic disk.

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/high_contrast_images/g4.jpg" alt="Glaucoma" width="250"/>

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/processed_images/glc%20from%20paper.png" alt="Glaucoma Explanation" width="400"/>

image taken from 
H. Fu et al., "Disc-Aware Ensemble Network for Glaucoma Screening From Fundus Image," in IEEE Transactions on Medical Imaging, vol. 37, no. 11, pp. 2493-2501, Nov. 2018, doi: 10.1109/TMI.2018.2837012.

### Normal Scan

The image below is an example of a normal scan.

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/high_contrast_images/n2.jpg" alt="Normal" width="250"/>

## Processing
Based on the observations above the following image processing techniques were tried.

### 1. Channel Selection
An analysis was carried out to see if a particular channel represents dataset separation better than other. The results are shown below.

### Diabetic Retinopathy
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/processed_images/dbr.png" alt="Diabetic Retinopathy" width="400"/>

### Glaucoma
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/processed_images/glc.png" alt="Glaucoma" width="400"/>

### Normal
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/processed_images/normal.png" alt="Normal" width="400"/>

The channels do show variations within an image but the separation between images is not very clear.

### 2. Contrast & Brightness

The images below show increased contrast. This does enhance differences between Diabetic Retinopathy and Glaucoma and to some extent normal images as well.

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/high_contrast_images/dbr.jpg" alt="Diabetic Retinopathy" width="250"/>
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/high_contrast_images/g4.jpg" alt="Glaucoma" width="250"/>
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/high_contrast_images/n2.jpg" alt="Normal" width="250"/>

# Data Selection

The original dataset contains 7 categories. However, for the first model these were separted into 4 categories as mentioned above. The other category contained more than 1500 images which made the samples imbalanced. So about 750 examples were randomly chosen from these images to ensure more balanced training data.

# First Approach
The first approach was to try and create a single multiclassification model. For second approach please scroll below to that section.

## Models Tested

A number of models were used from tensorflow applications. The following models were tested,

* VGG19
* EfficinetNet B5
* MobileNet V2
* ResNet50

Out of all these Resnet50 showed the best results on both 7 category dataset and the 4 category dataset.

# HeatMaps

Heatmaps were created using EfficientNet B5 and Resnet50 outputs. The heat maps show that the models focused mainly on the visual disc and brighter spots on the retinal scans. The model does not at the moment do a very good job however of separating different conditions.

### Diabetic Retinopathy

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/orig_dbr1.jpg" alt="Original_DBR1" width="200"/><img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/dbr1.jpg" alt="DBR1" width="200"/>
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/orig_dbr2.jpg" alt="Original_DBR2" width="200"/><img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/dbr2.jpg" alt="DBR1" width="200"/>

### Glaucoma

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/orig_glc1.jpg" alt="Original_glc1" width="200"/><img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/glc1.jpg" alt="glc1" width="200"/>
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/orig_glc2.jpg" alt="Original_glc2" width="200"/><img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/glc2.jpg" alt="glc2" width="200"/>

### Normal

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/orig_normal1.jpg" alt="Original_norm1" width="200"/><img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/normal1.jpg" alt="norm1" width="200"/>
<img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/orig_normal2.jpg" alt="Original_norm2" width="250"/><img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps/normal2.jpg" alt="norm2" width="250"/>

# Label Propogation

For label propogation K-nearest-neighbor algrithm was used.

## Loading Model and Getting Predictions

The pretrained model was loaded and output from final prediction layer was fed to a knn model with 4 categories. The model was then used for making predictions on the test data.
Based on these predictions the test data was moved to in a new training dataset. A new resnet50 model was initiated with same datagen parameters. The training results however were not very encouraging. The accuracy did increase to around 40% compared to about 30% for the original model.

One of the reasons could be that the original model was not doing a very good job at identifying the true categories.

# Second Approach
In this approach one vs normal models were trained.

## Logic
Based on the scans it was oserved that each eye ailment addresses different areas/problems. 
So a normal vs diabetic retinopathy  approach enhanced the images by increasing contrast and brightness to highlight damage to retina.
A normal vs Glaucoma approach increased contrast only to shift the focus to visual disc only.

## Model Used
A custom architecture with a residual connection was used to train these models. This was done to test the concept and speed up the training process.

## Results

The Diabetic Retinopathy test resulted in 87% accuracy
The Glaucoma test resulted in 
The other test resulted in

## Heat Maps

The heat maps generated for Diabetic Retinopathy are given below,
The custom model does not have a very good representation in the heat maps but work is being done to fix this.

<img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps_binary/dbr/dbr1.jpg" alt="dbr1" width="200"/><img src="https://github.com/taimur1871/retinalscan_models/blob/main/heatmaps_binary/dbr/dbr2.jpg" alt="dbr2" width="200"/>

## Label Transfer
The problem that arose in label transfer is that all three models need to be working well to ensure good propogation. This would involved checking each image multiple times and assigning labels based on highest confidence. In this case when only one model was tested it was able to identify normal images well but missclassified a lot of other images.

The notebook custom_arch_label-prop explores this in more detail.
