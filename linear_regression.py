from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np




class RegLinear():
    def __init__(self):
        self.x = None
        self.y = None
        self.model = LinearRegression()
        self.xreg = np.arange(-3, 3, 1)
        self.test_size:float = 0.3

        #variable of work out
        self.x_train = None
        self.y_train = None
        
        #Variables of test
        self.x_test = None
        self.y_test = None

    def generate_x_y(self) -> dict:
        self.x,self.y = make_regression(n_samples=200, n_features=1, noise=30)
        return {"x":self.x,"y":self.y}

    def get_linear_angular(self)-> dict:
        resp = self.generate_x_y()
        self.x = resp["x"]
        self.y = resp["y"]
        self.model.fit(self.x,self.y) 
        #y = mx + b -> m=coef angular e b -> coef linear
        print("inside of method")
        print("intercep",self.model.intercept_)#coef linear 
        print("coef",self.model.coef_)#coef angular
        #n_samples = qntd de dados | n_features = qtd de vars (relação de x e y) | noise= ruido
        return {"coef_ang":self.model.coef_,"coef_linear":self.model.intercept_}
    
    def create_graphic(self):
        resp = self.get_linear_angular()
        coef_ang = resp["coef_ang"]
        coef_linear = resp["coef_linear"]


        plt.plot(self.xreg, coef_ang*self.xreg+coef_linear,color="red") ###plot faz grafico em linhas
        #eq_reta -> y = mx + b
        # y = coef_angular(m) * xreg(x) + coef linear(b)
        plt.show()

    def get_r2(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.3)#test_size=0.3 = 30% dos valores x e y como teste e os restante 70% serão de traino
        self.model.fit(self.x_train,self.y_train)

        print("coef",self.model.coef_)#coef angular
        print("intercep",self.model.intercept_)#coef linear 
        response = self.model.score(self.x_test,self.y_test) # Def o R2
        print("response:",response)
        return response





reg = RegLinear()
reg.get_linear_angular()
reg.create_graphic()
reg.get_r2()


"""
#Gerando dados aleatórios 
x, y = make_regression(n_samples=200, n_features=1, noise=30) 
#print(f"x:{x}\ny:{y}")
#n_samples = qntd de dados | n_features = qtd de vars (relação de x e y) | noise= ruido
plt.scatter(x,y) ### scatter faz graficos em bolinhas
# plt.show()

#Creating model
model = LinearRegression()
# model.fit(x,y) 
# #y = mx + b -> m=coef angular e b -> coef linear
# print("intercep",model.intercept_)#coef linear 
# print("coef",model.coef_)#coef angular
xreg = np.arange(-3, 3, 1)
# plt.plot(xreg, 51.61*xreg+3.05,color="red") ###plot faz grafico em linhas
#eq_reta -> y = mx + b
#y = coef_angular(m) * xreg(x) + coef linear(b)
# plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)#test_size=0.3 = 30% dos valores x e y como teste e os restante 70% serão de traino
model.fit(x_train,y_train)

print("coef",model.coef_)#coef angular
print("intercep",model.intercept_)#coef linear 

#model.fit(x_train,y_train)
response = model.score(x_test,y_test) # Def o R2
print("response:",response)
"""