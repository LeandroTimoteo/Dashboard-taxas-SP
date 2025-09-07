import streamlit as st
import pandas as pd
import plotly.express as px

def mostrar(df):
    st.title("🏆 Cidades com Maiores Impostos")

    # Ordenar pelo total de impostos
    df_sorted = df.sort_values(by="Total_Impostos_RS", ascending=False)

    # Pegar as top 5 cidades
    top_5 = df_sorted.head(5)

    # Mostrar subtítulo
    st.markdown("### Essas são as 5 cidades com maior carga tributária:")

    # Mostrar tabela com destaque no valor máximo
    st.dataframe(top_5[["Cidade", "Total_Impostos_RS"]].style.highlight_max(axis=0))

    # Gráfico de barras
    st.bar_chart(data=top_5.set_index("Cidade")["Total_Impostos_RS"])