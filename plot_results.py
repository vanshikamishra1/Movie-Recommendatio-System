import os
import pandas as pd
import matplotlib.pyplot as plt
import os
import pandas as pd
import matplotlib.pyplot as plt

directory = os.path.join(os.path.dirname(__file__), '../outputs')
data_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
metrics = ["Recall@10", "NDCG@10", "Precision@10", "HitRate@10", "Accuracy@10"]

for file in data_files:
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)
    model_name = file.replace('.csv', '')
    epochs = df['Epoch']
    for metric in metrics:
        plt.figure(figsize=(7, 4))
        plt.plot(epochs, df[metric], marker='o')
        plt.xlabel('Epoch')
        plt.ylabel(metric)
        plt.title(f'{model_name}: {metric} vs Epoch')
        plt.tight_layout()
        out_path = os.path.join(directory, f'trend_{model_name}_{metric}.png')
        plt.savefig(out_path)
        plt.close()
        print(f'Saved: {out_path}')


directory = os.path.join(os.path.dirname(__file__), '../outputs')
data_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

metrics = ["Recall@10", "NDCG@10", "Precision@10", "HitRate@10", "Accuracy@10"]
model_scores = {metric: {} for metric in metrics}

for file in data_files:
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path)
    model_name = file.replace('.csv', '')
    
    last_row = df.iloc[-1]
    for metric in metrics:
        model_scores[metric][model_name] = last_row[metric]


for metric in metrics:
    plt.figure(figsize=(7, 4))
    plt.bar(model_scores[metric].keys(), model_scores[metric].values(), color='skyblue')
    plt.ylabel(metric)
    plt.xlabel('Model')
    plt.title(f'Model Comparison: {metric}')
    plt.tight_layout()
    out_path = os.path.join(directory, f'comparison_{metric}.png')
    plt.savefig(out_path)
    plt.close()
    print(f'Saved: {out_path}')

print('All comparison plots saved in outputs folder.')