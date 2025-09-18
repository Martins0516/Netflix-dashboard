import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Código para carregar a página
st.set_page_config(page_title="Netflix Dashboard", layout="wide")
st.title("📊 Netflix Dashboard - Análise de Dados")



# Código para carregar os dados
@st.cache_data
def load_data():
    return pd.read_csv("data/netflix_titles.csv")

df = load_data()



# Código para criar o dashboard
st.sidebar.header("Filtros")
tipo = st.sidebar.multiselect("Selecione o tipo:", df['type'].unique(), default=df['type'].unique())
anos = st.sidebar.slider("Selecione o intervalo de anos:", int(df['release_year'].min()), 2025, (2000, 2020))

df_filtered = df[(df['type'].isin(tipo)) & (df['release_year'].between(anos[0], anos[1]))]

st.write(f"### Total de títulos filtrados: {df_filtered.shape[0]}")




# Gráfico 1: Distribuição por tipo
st.subheader("Distribuição de Filmes e Séries")
fig1, ax1 = plt.subplots()
sns.countplot(data=df_filtered, x="type", ax=ax1, palette="viridis")
st.pyplot(fig1)




# Gráfico 2: Títulos por ano
st.subheader("Lançamentos por Ano")
fig2, ax2 = plt.subplots(figsize=(10, 4))
df_filtered['release_year'].value_counts().sort_index().plot(ax=ax2, color="red")
ax2.set_ylabel("Quantidade de títulos")
st.pyplot(fig2)




# Gráfico 3: Principais países
st.subheader("Top 10 Países com mais títulos")
top_countries = df_filtered['country'].dropna().str.split(",").explode().str.strip().value_counts().head(10)
fig3, ax3 = plt.subplots()
top_countries.plot(kind="bar", ax=ax3, color="green")
st.pyplot(fig3)




# Gráfico 4: Principais gêneros
st.subheader("Top 10 Gêneros mais comuns")
top_genres = df_filtered['listed_in'].dropna().str.split(",").explode().str.strip().value_counts().head(10)
fig4, ax4 = plt.subplots()
top_genres.plot(kind="bar", ax=ax4, color="purple")
st.pyplot(fig4)

st.success("✅ Dashboard carregado com sucesso!")
