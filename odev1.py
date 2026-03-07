import numpy as np

# -----------------------------
# EV kelimesi için HMM parametreleri
# -----------------------------
startprob_ev = np.array([1.0, 0.0])
transmat_ev = np.array([
    [0.6, 0.4],
    [0.2, 0.8]
])
emissionprob_ev = np.array([
    [0.7, 0.3],   # e
    [0.1, 0.9]    # v
])

# -----------------------------
# OKUL kelimesi için HMM parametreleri
# -----------------------------
startprob_okul = np.array([1.0, 0.0])
transmat_okul = np.array([
    [0.5, 0.5],
    [0.4, 0.6]
])
emissionprob_okul = np.array([
    [0.6, 0.4],
    [0.3, 0.7]
])

# -----------------------------
# Test gözlem dizisi
# High = 0
# Low = 1
# -----------------------------
test = [0, 1]  # iki gözlem

# -----------------------------
# Log-likelihood hesaplamak için Viterbi gibi basit bir forward fonksiyonu
# -----------------------------
def hmm_log_likelihood(startprob, transmat, emissionprob, obs):
    n_states = len(startprob)
    T = len(obs)

    # forward matrisini oluştur
    fwd = np.zeros((T, n_states))

    # t=0 için
    fwd[0, :] = startprob * emissionprob[:, obs[0]]

    # t>0 için
    for t in range(1, T):
        for j in range(n_states):
            fwd[t, j] = emissionprob[j, obs[t]] * np.sum(fwd[t-1, :] * transmat[:, j])

    # log-likelihood
    return np.log(np.sum(fwd[T-1, :]))

# -----------------------------
# Skorları hesapla
# -----------------------------
score_ev = hmm_log_likelihood(startprob_ev, transmat_ev, emissionprob_ev, test)
score_okul = hmm_log_likelihood(startprob_okul, transmat_okul, emissionprob_okul, test)

print("EV modeli skoru:", score_ev)
print("OKUL modeli skoru:", score_okul)

# Karar
if score_ev > score_okul:
    print("Tahmin edilen kelime: EV")
else:
    print("Tahmin edilen kelime: OKUL")