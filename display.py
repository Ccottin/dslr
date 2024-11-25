import tkinter as tk
from tkinter import ttk


def display_data(data):
    # Créer une fenêtre Tkinter
    root = tk.Tk()
    root.title("Affichage DataFrame")

    # Créer une table dans une fenêtre déroulante
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    # Ajouter une barre de défilement
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Créer une liste de colonnes et de données
    tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=tree.yview)

    # Configurer les colonnes
    tree["columns"] = list(data.columns)
    tree["show"] = "headings"  # Masquer la colonne par défaut
    for col in data.columns:
        tree.heading(col, text=col)  # Ajouter les en-têtes
        tree.column(col, width=100)  # Largeur par défaut

    # Ajouter les données
    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))

    # Lancer la fenêtre
    root.mainloop()