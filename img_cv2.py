#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:37:38 2021

@author: hassan
"""
#/home/hassan/Documents/2020-07/IMG_1504.JPG

import cv2
import numpy as np
from matplotlib import pyplot as plt
# Load image as grayscale
image = cv2.imread("/home/hassan/Documents/2020-07/IMG_1504.JPG", cv2.IMREAD_GRAYSCALE)
# Blur image
# image_blurry = cv2.blur(image, (5,5))
# # Show image
# plt.imshow(image_blurry, cmap="gray"), plt.axis("off")
# plt.show()
# image_very_blurry = cv2.blur(image, (100,100))
# # Show image
# # plt.imshow(image_very_blurry, cmap="winter"), plt.xticks([]), plt.yticks([])
# kernel = np.ones((5,5)) / 25.0
# image_kernel = cv2.filter2D(image, -1, kernel)

# plt.imshow(image_kernel, cmap="gray"), plt.xticks([]), plt.yticks([])
# image_enhanced = cv2.equalizeHist(image)
# plt.imshow(image_enhanced, cmap="gray"), plt.axis("off")
# plt.show

median_intensity = np.median(image)
lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
# Apply canny edge detector
image_canny = cv2.Canny(image, lower_threshold, upper_threshold)
# Show image
plt.imshow(image_canny, cmap="gray"), plt.axis("off")
plt.show()

