# Blockchain Simulation - Exercice de Formation

Cette simulation démontre les concepts clés d'une blockchain :
- **Proof of Work (PoW)** : Mécanisme de consensus par résolution de puzzles cryptographiques
- **Intégrité de la chaîne** : Validation et détection de corruption des blocs
- **Calcul de Merkle Root** : Structure hiérarchique des hash pour l'intégrité des transactions
- **Système décentralisé** : Simulation d'interactions entre pairs (peers)

## Prérequis

- Python 3.6+
- Modules standard Python (hashlib, time, json)

## Structure du Projet

```
blockchain-simulation/
├── blockchain.py           # Code principal de la simulation
├── README.md              # Documentation
└── [autres fichiers]      # Fichiers de support
```

## Utilisation

### 1. Lancement de la simulation normale

```bash
python blockchain.py
```

### 2. Test avec corruption manuelle

```bash
python blockchain.py -corrupt
```

Cette option permet de tester la capacité de la blockchain à détecter les tentatives de modification malveillante.

## Fonctionnalités Implémentées

### ✅ Mining et Proof of Work
- Résolution de puzzles computationnels
- Validation des blocs par consensus

### ✅ Validation d'Intégrité
- Détection automatique des blocs corrompus
- Vérification de l'enchaînement des hash

### ✅ Merkle Root
- Calcul hiérarchique des hash de transactions
- Vérification de l'intégrité des données

### ✅ Simulation Multi-Peers
- Interaction entre plusieurs nœuds
- Démonstration de la décentralisation

## Personnalisation

Vous pouvez ajuster :
- **Difficulté du PoW** : Modifier la complexité des puzzles
- **Nombre de peers** : Étendre la simulation réseau
- **Taille des blocs** : Adapter selon vos besoins d'apprentissage

## Concepts Blockchain Démontrés

1. **Immutabilité** : Une fois ajouté, un bloc ne peut être modifié sans casser la chaîne
2. **Consensus** : Validation collective par Proof of Work
3. **Transparence** : Tous les participants peuvent vérifier la validité
4. **Décentralisation** : Aucun point de contrôle unique

## Commandes Utiles

```bash
# Simulation standard
python blockchain.py

# Test de résistance à la corruption
python blockchain.py -corrupt

# Vérification de l'intégrité
# (intégré dans la simulation)
```

