# AbstractArt-by-GAN
The code is from Engineer Thesis: Creating abstract images using Generative Adversarial Network

Polish title: Tworzenie obrazów abstrakcyjnych zużyciem Generatywnej Sieci Przeciwstawnej

Author: Maciej Ołdakowski

University: PJATK

Student id: s21348

Abstract:

  The paper presents a proposal for using Generative Adversarial Networks (GAN) in the creation of abstract images. The paper is based on available research and scientific articles on Generative Adversarial Networks. The presented method involves the use of two rival neural networks: a generator and a discriminator. The task of the generator is to create images as close in appearance as possible to the real images in the training set, while the discriminator compares the data and evaluates which images are true and which are false (generated).
  During the creation of the network, convolution layers, normalizing layers and activation functions (ReLu and Tanh), which were used to improve the quality of the generated images. The model was trained using two sets of abstract images: Delaunay and abstract images from the WikiArt (Improved) dataset. The quality of the images was evaluated using the loss function, prediction accuracy and visual representation of the model. The Python language and libraries were used in the process: NumPy, PIL, Keras and Matplotlib. The results of the work show the advantages and disadvantages of using the GAN structure in the process of generating abstract images.

# Description
Using Delaunay and WikiArt dataset for traing. The aim is to generate a real-like 64x64 pixels images of abstract art, similar to those in training data set.
The model is build using GAN architecture. 
<p align="center">
<img src=https://github.com/Maciej-Ol/AbstractArt-by-GAN/blob/main/output/examples/training.gif/>
</p>

# Examples
Here you can check the generating images app that uses different models from the paper:
[Abstract Art by GAN](https://maciej-ol-abstractart-by-gan-app-mpt1bi.streamlit.app/)


# License and Citations
This is an open source project under license (see the LICENSE file). 

Please cite the following paper:
M. Ołdakowski, Creating abstract images using Generative Adversarial Network, 2023, PJATK.

or

M. Ołdakowski, Tworzenie obrazów abstrakcyjnych zużyciem Generatywnej Sieci Przeciwstawnej, 2023, PJATK.
