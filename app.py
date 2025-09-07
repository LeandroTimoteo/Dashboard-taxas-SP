import streamlit as st
import pandas as pd
import plotly.express as px

# Função para carregar os dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados.csv")

# Carregar os dados uma única vez
df = carregar_dados()

# Abas do dashboard
tab1, tab2, tab3 = st.tabs(["Tabela e Gráfico", "Detalhes por Cidade", "Comparação de Impostos"])

with tab1:
    st.subheader("Tabela de Dados")
    st.dataframe(df)

    st.subheader("Total de Impostos por Cidade")
    fig = px.bar(df, x="Cidade", y="Total_Impostos_RS", color="Cidade",
                 labels={"Total_Impostos_RS": "Total de Impostos (R$)", "Cidade": "Cidade"},
                 title="Total de Impostos por Cidade (Simulado)")
    st.plotly_chart(fig)

with tab2:
    st.subheader("Detalhes por Cidade")
    cidade_selecionada = st.selectbox("Selecione uma cidade:", df["Cidade"].unique())
    dados_cidade = df[df["Cidade"] == cidade_selecionada]

    st.metric(label="IPTU Médio", value=f"R$ {dados_cidade['IPTU_Medio_RS'].values[0]}")
    st.metric(label="Taxa de Serviços", value=f"R$ {dados_cidade['Taxa_Servicos_RS'].values[0]}")
    st.metric(label="Total de Impostos", value=f"R$ {dados_cidade['Total_Impostos_RS'].values[0]}")

with tab3:
    st.subheader("Comparação entre IPTU e Taxa de Serviços")

    df_melted = df.melt(id_vars="Cidade", value_vars=["IPTU_Medio_RS", "Taxa_Servicos_RS"],
                        var_name="Tipo de Imposto", value_name="Valor (R$)")

    fig_comparacao = px.bar(df_melted, x="Cidade", y="Valor (R$)", color="Tipo de Imposto",
                            barmode="group", title="IPTU vs Taxa de Serviços por Cidade")
    st.plotly_chart(fig_comparacao)

# Menu lateral
st.sidebar.title("🧭 Navegação")
pagina_selecionada = st.sidebar.selectbox(
    "Escolha uma página:",
    ["Dashboard", "Cidades com Maiores Impostos", "Perfil", "Estatísticas"]
)

# Carregar página selecionada
if pagina_selecionada == "Dashboard":
    # Código da Dashboard com abas
    pass  # Deixe isso aqui, pois já temos o código das abas acima

elif pagina_selecionada == "Cidades com Maiores Impostos":
    from paginas import cidades_altas
    cidades_altas.mostrar(df)  # Passando o df carregado

elif pagina_selecionada == "Perfil":
    from paginas import perfil
    perfil.mostrar()  # Se não usa df na página perfil, pode deixar sem

elif pagina_selecionada == "Estatísticas":
    from paginas import estatisticas
    estatisticas.mostrar(df)  # Passando o df carregado
    
    