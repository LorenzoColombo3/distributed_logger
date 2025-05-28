import matplotlib.pyplot as plt

pk_labels = ['ONE', 'QUORUM', 'ALL']
pk_3_nodi = [5.09, 15.19, 12.30]
pk_2_nodi = [1.26, 1.75, None] 

service_labels = ['ONE', 'QUORUM', 'ALL']
service_3_nodi = [3860.11, 5338.84, 6123.41]
service_2_nodi = [3583.05, 5241.89, None] 

x = range(len(pk_labels))
bar_width = 0.35

def plot_graph(title, labels, values_3, values_2, ylabel, filename):
    fig, ax = plt.subplots()
    
    bars1 = [v if v is not None else 0 for v in values_3]
    bars2 = [v if v is not None else 0 for v in values_2]

    b1 = ax.bar([i - bar_width/2 for i in x], bars1, bar_width, label='3 nodi', color='#4A90E2')
    b2 = ax.bar([i + bar_width/2 for i in x], bars2, bar_width, label='2 nodi', color='#50E3C2')

    for idx, v in enumerate(values_3):
        if v is None:
            ax.text(idx - bar_width/2, 10, "Errore", ha='center', va='bottom', color='red', rotation=90)
    for idx, v in enumerate(values_2):
        if v is None:
            ax.text(idx + bar_width/2, 10, "Errore", ha='center', va='bottom', color='red', rotation=90)

    ax.set_xlabel('Livello di consistenza')
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

plot_graph(
    "Query su chiave primaria (id)",
    pk_labels,
    pk_3_nodi,
    pk_2_nodi,
    "Tempo (ms)",
    "query_pk_tempo.png"
)

plot_graph(
    "Query con ALLOW FILTERING su service",
    service_labels,
    service_3_nodi,
    service_2_nodi,
    "Tempo (ms)",
    "query_service_tempo.png"
)
