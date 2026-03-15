import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln

# Bir dakikada geçen araç sayıları (örnek veri)
data = np.array([8, 10, 12, 11, 13, 15, 14, 16, 9, 12, 11, 13, 14, 12])

# Negatif log-likelihood fonksiyonu
def negative_log_likelihood(lmbda):
    if lmbda <= 0:
        return np.inf
    
    
    n = len(data)
    sum_k = np.sum(data)
    
    
    nll = - (sum_k * np.log(lmbda) - n * lmbda)
    return nll

# başlangıç tahmini
initial_guess = 10

# sayısal optimizasyon
result = minimize(negative_log_likelihood, initial_guess)

lambda_numeric = result.x[0]

print("Sayısal MLE tahmini:", lambda_numeric)

# Analitik çözüm (ortalama)
lambda_analytic = np.mean(data)

print("Analitik çözüm:", lambda_analytic)