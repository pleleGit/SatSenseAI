# Datasets Overview

This repository provides three datasets prepared for satellite imagery-based machine learning tasks.

## Datasets

### 1. `images.zip`
- **Description**:  
  This archive contains the original satellite images collected for the project using the VIIRS night-time satellite images.
- **Source**:  
  Images were manually downloaded and processed from **Google Earth Engine** and the VIIRS night-time satellite images.
- **Content**:  
  - Raw, unprocessed satellite images.
  - Organized into country-specific folders.

## 🔗 Download Link

 [Download `images.zip` via Google Drive](https://drive.google.com/file/d/1qoQVIcz8zIUmfJTQuUiJGPdvN6r23PYD/view?usp=sharing)

---

### 2. `bags.zip`
- **Description**:  
  This archive groups the original images into "bags" per year, for use in **Multiple Instance Learning (MIL)** frameworks. 
  Each bag consists of images from related areas grouped per year of capture.
- **Source**:  
  Created by programmatically grouping images from `images.zip`.
- **Content**:  
  - Each bag contains multiple related images.

## 🔗 Download Link

 [Download `bags.zip` via Google Drive](https://drive.google.com/file/d/1Ujgrjf1bV2gNtmXBsUfb40O2UMlhig_r/view?usp=sharing)

---

### 3. `bagsAugmented.zip`
- **Description**:  
  This archive contains **augmented** versions of the bags to expand training data and improve model generalization.
- **Source**:  
  Data augmentations (e.g., random rotations, flips, slight color adjustments) were applied to images in `bags.zip`.
- **Content**:  
  - Augmented images organized with the same bag structure as `bags.zip`.
  - Enhances model robustness by introducing data variability.

## 🔗 Download Link

 [Download `bagsAugmented.zip` via Google Drive](https://drive.google.com/file/d/1HW37TJRgiLF_nukB5NEOh2CxdugDq1K5/view?usp=sharing)

---

## 📑 Notes
- Unzip the archives before using them in your machine learning pipelines.

---
