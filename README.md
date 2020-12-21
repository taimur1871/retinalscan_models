# Retinal Scan Models

Retinal scans are useful tools for detecting a number of eye conditions. However, it requires an expert to read and decipher these images. The goal of this project is to develop models for detecting various types of disease. In the first iteration the model created will try to distinguish between,

* Diabetic Retinopathy
* Glaucoma
* Normal scans
* Other ailments

This dataset was taken from a Kaggle competition. The details can be found here (https://www.kaggle.com/c/vietai-advance-course-retinal-disease-detection/overview)

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


# Models Tested

A number of models were used from tensorflow applications. The following models were tested,

* VGG19
* EfficinetNet B5
* MobileNet V2
* ResNet50

Out of all these Resnet50 showed the best results on both 7 category dataset and the 4 category dataset.

# HeatMaps

Heatmaps were created using EfficientNet B5 and Resnet50 outputs. The heat maps show that the models focused mainly on the visual disc and brighter spots on the retinal scans. The model does not at the moment do a very good job however of separating different conditions.

