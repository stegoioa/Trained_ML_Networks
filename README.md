# Architectural Image Datasets

This GitHub repository contains a collection of image-based datasets for architectural applications. The main use of these datasets is for training image-based StyleGAN2ADA and Pix2PixHD workflows. 

The datasets included in this repository have been used in various architectural projects, and previews of their application are provided within each folder. I also include links to the outcomes of these projects, where the datasets were used to create images or 3D models.

Please note that the use of these datasets is at one's own risk, as some of them were created through automatic image scraping and the licenses for these images may vary. It is the responsibility of the user to ensure that they have the appropriate permissions to use the images in their own work.

I hope that these datasets will be useful for researchers, artists, and developers who are interested in exploring the use of machine learning techniques in architectural design. 


## Urban Scale

### Height Information and Density of Vienna, AT

Dataset Input

![Urban Scale Preview Image](content/urban_heightmap/21_3.jpg)

**[Tesselated HeightMap DataSet](https://drive.google.com/file/d/1yluRfJOm0j5zO3CsAXJ4i0svnm7Y5-RR/view?usp=share_link)** 

Segmentation Scale of DataSet is variable. To further reduce scale and increase dataset image count, use this script:

[Batch Image Segmentation .py](/image_processing_tools/image_segmentation_and_stich.py)

In order to preprocess Images for StyleGan2ADA and PIx2PIXHD wokflows refer to:

[Image PreProcessing .py](/image_processing_tools/preprocess_images_ml.py)

### Typological Information of Vienna, AT

Dataset Input

![Urban Scale Preview Image](/content/dataset_maps_preview2.jpg)

**[Tesselated HeightMap DataSet](https://drive.google.com/drive/folders/1K5diQ3pUusKVF9E_v_GBK5JxtNN_99UA?usp=share_link)**

Segmentation Scale of DataSet is variable. To further reduce scale and increase dataset image count, use this script:

[Batch Image Segmentation .py](/image_processing_tools/image_segmentation_and_stich.py)

Model Output

![Urban Scale Preview Image](/content/urbangan_preview.gif)

## Floorplans

Model Output

![Floorplans Preview Image](/content/floorplan_model.gif)

A series of pretrained StyleGan2ADA .plk models. They have varying degree of abstraction and visual gradients for dynamic privacy visualisation.

**[PreTrained_Models](https://drive.google.com/drive/folders/1Vb2muDMs6b3YCdFgbTsCYYDSI2v3E9Bv?usp=sharing)**

## Facades

### Sacral Architecture Motifs

Dataset Input

![Global Altar Image Dataset](content/altar_preview.jpg)

**[Altar DataSet](https://drive.google.com/drive/folders/1DZkYbFLu9nIpemP4tfRJkyxAFVj9qGnn?usp=sharing)**

Model Output

![Model Output](/content/altar_model_output.gif)

**[Pretrained .plk Model](https://drive.google.com/file/d/1VstC0zJwrWHqJXQcOBqqelSoYdsYy3Ou/view?usp=sharing)**

 
 

### Facades of Vienna, AT

Dataset Input

![Global Altar Image Dataset](/content/facades_dataset.jpg)

**[Altar DataSet](https://drive.google.com/file/d/1Zcs2XAS4YxJJEf3VHqFdR0E5Npr1wqXV/view?usp=sharing)**

Model Output

![Model Output](content/facade_model_output.gif)

**[Pretrained .plk Model](https://drive.google.com/file/d/1woaGw76VyJXyjbHZrT710yS5XHSgLq_K/view?usp=sharing)**
