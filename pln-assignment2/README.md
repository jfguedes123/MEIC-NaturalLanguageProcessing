# PLN-Assignment 2

## Overview
This repository contains the code and findings for Assignment 2. The primary objective of this project is to advance from the traditional machine learning or baseline approaches developed in Assignment 1 by leveraging state-of-the-art deep learning models. Specifically, this project focuses on selecting, fine-tuning, and evaluating pre-trained language models from the **Hugging Face** ecosystem for text classification.

## Objectives
* **Model Selection:** Explore the Hugging Face Hub to identify and select a pre-trained transformer model optimized for the specific language and text genre of our dataset.
* **Fine-Tuning:** Adapt the chosen pre-trained model to our specific text classification task.
* **Comparative Analysis:** Benchmark the performance of the fine-tuned transformer model(s) against the baseline models developed in Assignment 1.

## Advanced Explorations (Bonus)
In addition to standard fine-tuning, this project also explores the following advanced techniques:
* **[ ] Domain Adaptation:** Adapting the language model specifically to the target domain before task-specific fine-tuning.
* **[ ] Parameter-Efficient Fine-Tuning (PEFT):** Implementing techniques like **LoRA** (Low-Rank Adaptation) to reduce computational costs while maintaining model performance.
* **[ ] LLM Prompting:** Experimenting with prompting strategies on larger language models to perform the classification task without extensive weight updates.
*(Note to self: Check the boxes above as these are implemented)*

## Setup

### Prerequisites
- Python 3.11+

### Create and activate the virtual environment

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Register the kernel with Jupyter

After activating the venv, register it as a Jupyter kernel:

```bash
python -m ipykernel install --user --name pln-assignment2 --display-name "PLN Assignment 2"
```

### Launch Jupyter

```bash
jupyter notebook
```

Select the **PLN Assignment 2** kernel when opening a notebook.

---

#### Group 20:
- João Guedes (202108711)
- Luís Fiunte (202208819)
