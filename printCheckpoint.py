import numpy as np
import torch
import matplotlib.pyplot as plt

Files_num = [20]
# Files_num = list(range(1,6))

results_path = []
for num in Files_num:
    file = f'Data/checkpoint{num}.pth'
    results_path.append(file)

checkpoints = []
for path in results_path:
    checkpoints.append(torch.load(path))


for i in range(len(checkpoints)):
    fig, ax_list = plt.subplots(2,1, figsize = (10,6))
    fig.suptitle(f'{results_path[i]} epochs: {checkpoints[i]["epoch"]}')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    ax_list[0].plot(checkpoints[i]['avglosses'])
    ax_list[0].title.set_text("avg losses")
    ax_list[1].plot(checkpoints[i]['results'])
    ax_list[1].title.set_text("results")
    plt.tight_layout()

plt.show()