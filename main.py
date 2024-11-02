import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import poisson

st.set_page_config(page_title="Probabilidade de Falhas")
st.title("Probabilidade de Falhas de Equipamentos")

with st.sidebar:
    st.header("Configurações")
    tipo = st.radio("Selecione o cálculo", options=["Probab. Exata", "Menos que", "Mais que"])
    ocorrencia = st.number_input("Média de manutenções", min_value=1, max_value=99, value=2, step=1)
    processar = st.button("Processar")

if processar:
    lamb = ocorrencia
    inic = lamb - 2
    fim = lamb + 2
    x_vals = np.arange(inic, fim + 1)

    if tipo == "Probab. Exata":
        probs = poisson.pmf(x_vals, lamb)
        tit = "Probabilidade de ocorrência exata"
    elif tipo == "Menos que":
        probs = poisson.cdf(x_vals, lamb)
        tit = "Probabilidade de ocorrência igual ou menor que"
    else:
        probs = poisson.sf(x_vals, lamb)
        tit = "Probabilidade de ocorrência maior que"
        
    z_vals = np.round(probs, 4)
    labels = [f"{i} prob.: {p}" for i, p in zip(x_vals, z_vals)]

    fig, ax = plt.subplots()  # Corrigido aqui para plt.subplots()
    ax.bar(x_vals, probs, tick_label=labels, color=plt.cm.gray(np.linspace(0.4, 0.8, len(x_vals))))
    ax.set_title(tit)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)