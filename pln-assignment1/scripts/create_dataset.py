from datasets import load_dataset

dataset = load_dataset("ADS509/full_experiment_labels")

for split in dataset.keys():
    file_name = f"{split}_data.csv"
    
    dataset[split].to_csv(f"data/{file_name}", index=False)
    
    print(f"Successfully saved: {file_name}")