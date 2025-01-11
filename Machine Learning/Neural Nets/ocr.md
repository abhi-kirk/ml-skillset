# Optical Character Recognition (OCR)
Converts visual text into machine-readable and editable formats. 
- TesseractOCR provides a fast and less-complex method relying on traditional image processing techniques (best for structured documents). 
- EasyOCR is a compute-heavy but more advanced method relying on deep learning algorithms (more robust to handwritten documents). 

## Core steps:
- *Preprocessing*:
  - TesseractOCR: Binarization, deskewing and noise removal using traditional image processing. 
  - EasyOCR: Minimal preprocessing. 
- *Text Detection*: 
  - TesseractOCR: Connected component analysis (using Union-Find data structure). 
  - EasyOCR: Deep learning based CRAFT (Character Region Awareness for Text Detection) algorithm which uses a CNN (VGG16) as the backbone for character feature extraction. 
- *Text Recognition*
  - TesseractOCR: Handcrafted features, and LSTM for sequence modeling. 
  - EasyOCR: CNN for feature extraction, and RNN for sequence modeling. 
- *Post processing*
  - TesseractOCR: Dictionaries (of valid recognized words) and rule-based language models (hte->the) to refine recognition outputs. 
  - EasyOCR: Same as TesseractOCR. 

## Why Sequence Modeling is needed?
It may be more intuitive to simply classify all alphanumeric characters using a CNN without sequence modeling. 

Challenges with character-level classification:
- Some languages have overlapping characters (e.g., hindi). 
- Real-world text may be distorted. 
- Context is not captured, e.g. 0 vs O or I vs 1 vs l. 
- Computationally expensive. 