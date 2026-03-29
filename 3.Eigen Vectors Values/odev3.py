import numpy as np

# Analiz edilecek karesel matris
A = np.array([[4, 2], 
              [1, 3]])

# NumPy ile hesaplama
ozdegerler_np, ozvektorler_np = np.linalg.eig(A)

print("--- NumPy Sonuçları ---")
print(f"Özdeğerler:\n{ozdegerler_np}")
print(f"Özvektörler:\n{ozvektorler_np}")


# Manuel özdeğer hesaplama (2x2)
def manuel_hesapla_2x2(matris):
    trace_A = matris[0, 0] + matris[1, 1]
    det_A = (matris[0, 0] * matris[1, 1]) - (matris[0, 1] * matris[1, 0])
    
    delta = trace_A**2 - 4 * det_A
    
    lambda1 = (trace_A + np.sqrt(delta)) / 2
    lambda2 = (trace_A - np.sqrt(delta)) / 2
    
    return np.array([lambda1, lambda2])


# Manuel özvektör hesaplama (2x2)
def manuel_ozvektor_2x2(A, lambd):
    mat = A - lambd * np.eye(2)
    
    # ax + by = 0 çözümü
    if abs(mat[0,1]) > 1e-8:
        x = 1
        y = -mat[0,0] / mat[0,1]
    else:
        y = 1
        x = -mat[1,1] / mat[1,0]
    
    v = np.array([x, y])
    
    # normalize (daha düzgün çıktı için)
    return v / np.linalg.norm(v)


# Manuel sonuçları alalım
ozdegerler_manuel = manuel_hesapla_2x2(A)

print("\n--- Manuel Hesaplama Sonuçları (2x2) ---")
print(f"Özdeğerler: {ozdegerler_manuel}")


# Manuel özvektörleri hesapla
ozvektorler_manuel = np.array([manuel_ozvektor_2x2(A, l) for l in ozdegerler_manuel])

print("\n--- Manuel Özvektörler ---")
print(ozvektorler_manuel)


# Karşılaştırma
print("\n--- Karşılaştırma Analizi ---")
print(f"NumPy Özdeğerleri : {np.sort(ozdegerler_np)}")
print(f"Manuel Özdeğerler: {np.sort(ozdegerler_manuel)}")

# Fark kontrolü
fark = np.sort(ozdegerler_np) - np.sort(ozdegerler_manuel)
print(f"Toplam mutlak hata: {np.sum(np.abs(fark)):.6f}")