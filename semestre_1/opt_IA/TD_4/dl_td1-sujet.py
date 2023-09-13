# ### Présentation
# 
# Le but de ce premier TD est de vous familiariser avec les réseaux de neurones et leur entraînement. Nous allons passer en revue les éléments de base suivant :
# 
#  - données d'apprentissage, 
#  
#  - fonction de perte (loss function)
#  
#  - descente de gradient
#  
#  Pour cela, nous allons utiliser un réseau de neurone (composé d'un seul neurone en fait) pour deux tâches : 
#  
#   - une régression linéaire simple
#   
#   - une régression logistique.

# Commençons par importer quelques unes des bibliothèques usuelles :

from ast import Pass
import numpy as np
import random as rd
import matplotlib.pyplot as plt

import warnings
warnings.simplefilter('ignore')


# ### On génère les données 

#Data: 
def generate(m, sizeNoise, slope, intersect):    
    x = [rd.random()*50 + 5 for i in range(m)]
    noise = [rd.random() * sizeNoise for i in range(m)]#np.rand(m,1) * sizeNoise
    y = [intersect + slope*x[i] + noise[i] for i in range(m)] 
    return np.array([x]), np.array([y])

m = 100
sizeNoise = 10
a = 0.8
b =  20
    
X, Y = generate(m, sizeNoise, a, b)
plt.grid()
plt.scatter(X, Y)


# ### Exercice 1. Un neurone :

# 
# 2. Ecrivez une fonction <code>neuron(x, w, b, f)</code> permettant d'implémenter ce neurone

def neuron(x, w, b, f):
    pass


# 3. Définissez deux fonctions id et sigmoid.

def id(z):
    pass

def sigmoid(z):
    pass

# 4. Testez vos fonctions. Décommenter le code suivant et vérifiez que le résultat affiché est celui prévu.

#x = np.array([[1, 2, 3]])
# y = np.array([1, 0, 1])

# w = np.array([1])
# b = [1]
# y_hat = neuron(x, w, b, id)
# print('x: ', x)
# print('y_hat: ', y_hat)


# ### Exercice 2. Régression linéaire : 

# 1. Ecrivez le code de la fonction loss(y, y_hat) définie comme la moyenne des carrés des écarts : 

def loss(y, y_hat):
    pass

# 3. Ecrivez la focntion gradient(x, y_hat, y) retournant le gradient de la fonction L.

def gradient(x, y_hat, y):
    pass

# 4. Ecrivez une fonction train(x, y, nu, epochs) qui réalise une déscente du gradient de 
# la fonction $\cal L$ afin de trouver les paramètres $w$ et $b$ minimisant la valeur de L. 

def train(x, y, nu, epochs):
    pass

# 5. Entraînez votre neurone. Prenez $0.001$ comme valeur pour le pas d'apprentissage, et 10000 pour le nombre d'epochs.
# 6. Donnez l'équation de la droite de régression obtenue. Ecrivez l'instruction permettant de calculer les valeurs prédites.
# 7. Dessinez la droite de régression sur la même figure que le nuage de point.
# 8. Comparez le résultat obtenu avec la droite donnée par <code>linregress</code> du sous module <code>stats</code> du module <code>scipy</code>.


# ### Exercice 3. Régression logistique :
# 

# 1. Comment devons-nous appeler la "fonction" neuron pour que le fonction d'activation soit la sigmoid ?

# 2. Le code suivant est à décommenter pour faire la suite 

# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split

# X, y = make_classification(n_samples=1000, n_features=1, n_classes=2, 
#                            n_informative=1, n_redundant=0, n_repeated=0,
#                           n_clusters_per_class=1)

# X_train, X_test, y_train, y_test = train_test_split(X, y)
# print(X_train.shape)
# print(y_train.shape)
# print(np.unique(y))


# 3. Définissez la nouvelle fonction de perte. Nous allons utiliser la fonction *cross_entropy* vue en cours :

def loss_log(y, y_hat):
    pass

# 5. Calculez le gradient de $\cal L$ et écrivez la fonction correspondante

def gradient_log(x, y_hat, y):
    pass

# 6. Adaptez une fonction train(x, y, nu, epochs) pour réaliser une déscente du gradient de la fonction $\cal L$ afin de trouver les paramètres $w$ et $b$ minimisant la valeur de $\cal L$. 

def train_log(x, y, nu, epochs):
    pass
# 7. Décomentez et exécutez la cellule suivante pour que vos calculs matriciels puissent se faire et entraînez votre neurone.

# X_train = np.reshape(X_train, (X_train.shape[1], X_train.shape[0]))
# print(X_train.shape)
# print(y_train.shape)


# 8. Evaluez votre modèle. Pour cela : 

# 8.1. Exécutez la code suivant pour formater les données de test.

#X_test = np.reshape(X_test, (X_test.shape[1], X_test.shape[0]))


# 8.2. Appliquez votre neurone aux données de test et observez le résultat obtenu.

# 8.3. Transformez les sorties en 0 et 1 : 

# 8.4. Evaluez la qualité du modèle obtenu 


if __name__=='__main__':
    print('programme principal')
    #écivez ici les instructions à exécuter