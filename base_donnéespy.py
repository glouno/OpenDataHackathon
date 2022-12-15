#BASE DONNEES
import pandas as pd
AUCHAN = pd.DataFrame()

AUCHAN['produit'] = ['œufs','beurre','lait', 'yaourt','riz','thon','eau','cheddar', 'SPAGHETTI','sauce tomate','poivre noire','moutarde','mayonnaise','ketchup','nutella','café', 'thé','biscuit','cookie','madeleine','brioche','pain de mie ','shampoing','dentifrice','savon','coton-tige', 'gel douche', 'demaquillant','déodorant','lave-sol','adoucissant','desodorisant','lessive','compote','pomme','clémentine','orange','poire','pomme de terre','oignon','ail','courgette','poivron','raisin','choux de bruxelle','créme fraiche','huile tournesol','tomate cerise','emmental','liquide vaiselle','jus orange','glace caramel','Confiture bio fraises','chocolat noir']
AUCHAN['prix'] = [4.05,2.45,6.99,4.59,2.25,2.39,3.15,1.29,1.99,2.75,4.05,3.29,2.65,2.15,5.79,3.99,2.05,1.59,2.75,2.39,3.05,1.29,5.65,5.50,4.60,3.20,9.23,1.70,4.29,5.49,4.62,5.34,8.50,2.65,4.49,2.99,2.69,2.89,1.48,1.34,16.62,2.69,2.76,4.19,1.85,2.95,3.39,1.50,2.39,1.99,3.05,5.35,1.69,4.99] 
AUCHAN['unité']=['unite','kg','litre','unite','kg','g','litre','g','kg','unite','g','g','unite','unite','kg','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','litre','unite','unite','unite','unite','kg','kg','kg','kg','kg','kg','kg','kg','kg','kg','unite','litre','kg','kg','litre','litre','unite','kg','unite','unite']




MONOPRIX=pd.DataFrame()
MONOPRIX['produit']= ['œufs','beurre','lait', 'yaourt','riz','thon','eau','cheddar', 'SPAGHETTI','sauce tomate','poivre noire','moutarde','mayonnaise','ketchup','nutella','café', 'thé','biscuit','cookie','madeleine','brioche','pain de mie ','shampoing','dentifrice','savon','coton-tige', 'gel douche', 'demaquillant','déodorant','lave-sol','adoucissant','desodorisant','lessive','compote','pomme','clémentine','orange','poire','pomme de terre','oignon','ail','courgette','poivron','raisin','choux de bruxelle','créme fraiche','huile tournesol','tomate cerise','emmental','liquide vaiselle','jus orange','glace caramel','Confiture bio fraises','chocolat noir']
MONOPRIX['prix']=[3.99,2.59,5.29,3.29,2.79,2.14,3.49,1.75,2.15,1.65,4.39,2.69,2.09,2.45,5.98,4.69,1.95,1.39,1.99,2.19,3.19,1.39,3.29,4.49,2.25,1.79,4.69,2.99,3.19,3.79,4.39,3.90,12.50,7.79,3.49,2.99,3.49,2.53,4.99,1.50,3.20,6.99,1.97,4.62,2.00,3.99,3.69,1.99,3.29,1.99,1.65,7.29,1.95,2.19]
MONOPRIX['unité']=['unite','kg','litre','unite','kg','g','litre','g','kg','unite','g','g','unite','unite','kg','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','litre','unite','unite','unite','unite','kg','kg','kg','kg','kg','kg','kg','kg','kg','kg','unite','litre','kg','kg','litre','litre','unite','kg','unite','unite']




FRANPRIX=pd.DataFrame()
FRANPRIX['produit']=['œufs','beurre','lait', 'yaourt','riz','thon','eau','cheddar', 'SPAGHETTI','sauce tomate','poivre noire','moutarde','mayonnaise','ketchup','nutella','café', 'thé','biscuit','cookie','madeleine','brioche','pain de mie ','shampoing','dentifrice','savon','coton-tige', 'gel douche', 'demaquillant','déodorant','lave-sol','adoucissant','desodorisant','lessive','compote','pomme','clémentine','orange','poire','pomme de terre','oignon','ail','courgette','poivron','raisin','choux de bruxelle','créme fraiche','huile tournesol','tomate cerise','emmental','liquide vaiselle','jus orange','glace caramel','Confiture bio fraises','chocolat noir']
FRANPRIX['prix']=[3.50,3.20,6.30,5.90,6.00,4.50,4.00,2.10,2.40,2.50,4.05,3.25,2.35,2.90,6.55,4.65,2.35,1.80,2.75,2.20,4.80,1.85,3.55,5.40,2.63,1.80,5.90,2.68,3.93,3.94,6.65,6.90,12.82,2.10,3.49,3.99,3.69,3.59,6.25,1.89,5.59,5.99,1.49,4.69,1.89,4.09,3.65,0.99,3.94,2.95,1.95,8.00,2.05,3.95]
FRANPRIX['unité']=['unite','kg','litre','unite','kg','g','litre','g','kg','unite','g','g','unite','unite','kg','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','litre','unite','unite','unite','unite','kg','kg','kg','kg','kg','kg','kg','kg','kg','kg','unite','litre','kg','kg','litre','litre','unite','kg','unite','unite']



LECLERC=pd.DataFrame()
LECLERC['produit']= ['œufs','beurre','lait', 'yaourt','riz','thon','eau','cheddar', 'SPAGHETTI','sauce tomate','poivre noire','moutarde','mayonnaise','ketchup','nutella','café', 'thé','biscuit','cookie','madeleine','brioche','pain de mie ','shampoing','dentifrice','savon','coton-tige', 'gel douche', 'demaquillant','déodorant','lave-sol','adoucissant','desodorisant','lessive','compote','pomme','clémentine','orange','poire','pomme de terre','oignon','ail','courgette','poivron','raisin','choux de bruxelle','créme fraiche','huile tournesol','tomate cerise','emmental','liquide vaiselle','jus orange','glace caramel','Confiture bio fraises','chocolat noir']
LECLERC['prix']=[1.83,2.28,4.99,2.42,3.58,2.21,2.72,1.09,1.19,1.33,4.01,3.40,1.37,1.85,5.49,3.68,1.54,1.33,1.46,1.66,2.76,1.19,3.52,5.64,1.99,1.09,3.75,2.25,3.45,3.61,2.99,3.62,12.07,7.38,2.99,2.49,2.77,2.29,2.30,2.49,3.49,2.79,1.97,4.99,1.65,3.45,3.63,1.79,2.64,1.78,2.11,5.49,1.95,1.84]
LECLERC['unité']=['unite','kg','litre','unite','kg','g','litre','g','kg','unite','g','g','unite','unite','kg','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','litre','unite','unite','unite','unite','kg','kg','kg','kg','kg','kg','kg','kg','kg','kg','unite','litre','kg','kg','litre','litre','unite','kg','unite','unite']


CARREFOUR=pd.DataFrame()
CARREFOUR['produit']= ['œufs','beurre','lait', 'yaourt','riz','thon','eau','cheddar', 'SPAGHETTI','sauce tomate','poivre noire','moutarde','mayonnaise','ketchup','nutella','café', 'thé','biscuit','cookie','madeleine','brioche','pain de mie ','shampoing','dentifrice','savon','coton-tige', 'gel douche', 'demaquillant','déodorant','lave-sol','adoucissant','desodorisant','lessive','compote','pomme','clémentine','orange','poire','pomme de terre','oignon','ail','courgette','poivron','raisin','choux de bruxelle','créme fraiche','huile tournesol','tomate cerise','emmental','liquide vaiselle','jus orange','glace caramel','Confiture bio fraises','chocolat noir']
CARREFOUR['prix']=[2.99,2.29,5.88,4.35,3.95,2.82,3.00,1.45,1.99,1.49,3.45,2.79,2.37,2.15,5.62,3.79,1.55,1.39,2.05,2.49,2.89,1.75,2.65,8.35,2.09,1.85,3.73,4.2,2.41,2.95,3.59,3.99,12.35,7.38,2.98,3.9,2.69,1.85,3.49,2.89,3.49,2.69,2.99,3.5,1.62,3.44,3.39,2.29,2.39,1.99,1.49,5.35,1.68,1.89]
CARREFOUR['unité']=['unite','kg','litre','unite','kg','g','litre','g','kg','unite','g','g','unite','unite','kg','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','unite','litre','unite','unite','unite','unite','kg','kg','kg','kg','kg','kg','kg','kg','kg','kg','unite','litre','kg','kg','litre','litre','unite','kg','unite','unite']