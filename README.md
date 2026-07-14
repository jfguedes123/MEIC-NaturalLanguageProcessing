# Natural Language Processing Assignments

This repository contains the material developed for the **Natural Language Processing** course assignments. It is organized into two main projects:

- **Assignment 1** focuses on classical machine learning approaches for text classification.
- **Assignment 2** extends the work with transformer-based models and fine-tuning experiments.

Each assignment lives in its own folder and includes the code, datasets, notebooks, and generated outputs used during experimentation.

## Repository Structure

```text
pln-assignment1/
  README.md
  data/
  notebooks/
  scripts/

pln-assignment2/
  README.md
  requirements.txt
  data/
  models/
  notebooks/
```

## Assignment 1

The first assignment explores traditional NLP pipelines for text classification. The goal is to compare different preprocessing strategies, feature extraction techniques, and classical models such as Logistic Regression, SVMs, Naive Bayes, Random Forests, and other standard machine learning approaches.

The assignment includes:

- dataset files for training, validation, and testing;
- notebooks with the experimental workflow and results;
- scripts for dataset preparation and preprocessing;
- plots and output files generated during analysis.

The detailed notes for this assignment are available in [pln-assignment1/README.md](pln-assignment1/README.md).

## Assignment 2

The second assignment builds on the previous one by using pretrained transformer models from the Hugging Face ecosystem. The main focus is on selecting a suitable language model, fine-tuning it for the classification task, and comparing its performance against the baseline models from Assignment 1.

This assignment also includes experiments with more advanced approaches such as parameter-efficient fine-tuning and alternative training setups. Trained models and checkpoints are stored under the `models/` directory.

The full setup instructions and experimental notes are available in [pln-assignment2/README.md](pln-assignment2/README.md).

## Datasets

Both assignments use the same dataset split structure:

- `train_data.csv`
- `valid_data.csv`
- `test_data.csv`

These files are stored inside each assignment’s `data/` folder so that experiments remain self-contained.

## How to Run the Projects

### Assignment 1

1. Open the `pln-assignment1/` folder in VS Code or Jupyter.
2. Inspect the notebook in `notebooks/`.
3. Run the preprocessing or dataset creation script if needed.
4. Execute the notebook cells to reproduce the experiments and outputs.

### Assignment 2

1. Open the `pln-assignment2/` folder.
2. Create a Python virtual environment.
3. Install the dependencies listed in `requirements.txt`.
4. Open the notebook in `notebooks/` and run the fine-tuning workflow.

More specific setup commands are documented in the assignment-level README files.

## Results and Outputs

Generated artifacts are stored alongside each assignment so the experiments can be reviewed without rerunning everything from scratch. This includes:

- notebook outputs and analysis cells;
- CSV files with pipeline results;
- trained model checkpoints and best-performing model snapshots;
- graphs and other visual summaries.

## Group Members

This project was developed by **Group 20**:

- João Guedes (202108711)
- Luís Fiunte (202208819)

## Notes

- The repository is organized to keep each assignment independent and reproducible.
- For implementation details, always consult the README inside the relevant assignment folder.