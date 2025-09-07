import streamlit as st
import pandas as pd
import plotly.express as px

def mostrar(df):
    st.title("📊 Estatísticas Descritivas dos Impostos")

    # Verificar se as colunas necessárias estão no DataFrame
    colunas_necessarias = ["IPTU_Medio_RS", "Taxa_Servicos_RS", "Total_Impostos_RS"]
    colunas_faltantes = [coluna for coluna in colunas_necessarias if coluna not in df.columns]

    if colunas_faltantes:
        st.error(f"As seguintes colunas não foram encontradas no DataFrame: {', '.join(colunas_faltantes)}")
        return

    # Mostrar estatísticas básicas
    total_cidades = len(df)
    media_iptu = df["IPTU_Medio_RS"].mean()
    media_taxa = df["Taxa_Servicos_RS"].mean()
    media_total = df["Total_Impostos_RS"].mean()

    st.markdown("### 📊 Visão Geral")
    col1, col2, col3 = st.columns(3)
    col1.metric("Cidades cadastradas", total_cidades)
    col2.metric("Média IPTU (R$)", f"{media_iptu:.2f}")
    col3.metric("Média Taxa Serviços (R$)", f"{media_taxa:.2f}")

    st.markdown(f"### Média Total de Impostos: R$ {media_total:.2f}")

    # Gráfico de boxplot
    st.markdown("### 📦 Distribuição do Total de Impostos")
    fig = px.box(df, y="Total_Impostos_RS", title="Distribuição do Total de Impostos por Cidade")
    st.plotly_chart(fig)