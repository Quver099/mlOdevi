import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln
import matplotlib.pyplot as plt # Grafikler için eklendi
from scipy.stats import poisson # Poisson dağılımı için eklendi

# Bir dakikada geçen araç sayıları (örnek veri)
data = np.array([8, 10, 12, 11, 13, 15, 14, 16, 9, 12, 11, 13, 14, 12])

# Negatif log-likelihood fonksiyonu
def negative_log_likelihood(lmbda):
    if lmbda <= 0:
        return np.inf
    
    n = len(data)
    sum_k = np.sum(data)
    
    # NLL hesaplama
    nll = - (sum_k * np.log(lmbda) - n * lmbda)
    return nll

# Başlangıç tahmini
initial_guess = 10

# Sayısal optimizasyon
result = minimize(negative_log_likelihood, initial_guess)
lambda_numeric = result.x[0]

print("Sayısal MLE tahmini:", lambda_numeric)

# Analitik çözüm (ortalama)
lambda_analytic = np.mean(data)
print("Analitik çözüm:", lambda_analytic)

# --- BÖLÜM 3: Görselleştirme ---
# Poisson PMF hesapla
x_range = np.arange(0, max(data) + 3)
poisson_pmf = poisson.pmf(x_range, lambda_numeric)

plt.figure(figsize=(10, 6))

# Histogram
plt.hist(data, bins=range(min(data), max(data) + 2), 
         density=True, alpha=0.6, color='blue', label='Gerçek Veri Histogramı', align='left')

# Poisson eğrisi
plt.plot(x_range, poisson_pmf, 'ro-', label=f'Poisson Dağılımı ($\lambda={lambda_numeric:.2f}$)')

plt.xlabel('Araç Sayısı (k)')
plt.ylabel('Olasılık')
plt.title('Trafik Verisi ve Poisson Dağılımı Karşılaştırması')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()