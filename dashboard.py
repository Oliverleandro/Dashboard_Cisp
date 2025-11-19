
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Segurança Pública", layout="wide")

st.title("📊 Dashboard de Segurança Pública – RJ")
st.markdown("Análise baseada na base do CISP.")

@st.cache_data
def load_data():
    df = pd.read_excel("BaseDadosCisp.xlsx")
    df.columns = ["ano", "regiao", "hom_doloso", 
                  "total_roubos", "total_furtos"]

    df["crime_total"] = df["hom_doloso"] + df["total_roubos"] + df["total_furtos"]

#linha temporaria para ver regioes
    st.write("Regiões no arquivos: ", df["regiao"].unique())

    coordenadas = {
        "Capital": (-22.9, -43.2),
        "Baixada Fluminense": (-22.7, -43.6),
        "Niteroi": (-22.88, -43.03),
        "Interior": (-21.5, -42.0),
    }

    df["lat"] = df["regiao"].map(lambda x: coordenadas[x][0])
    df["lon"] = df["regiao"].map(lambda x: coordenadas[x][1])
    return df

df = load_data()

st.sidebar.header("Filtros")
anos = st.sidebar.multiselect("Ano", sorted(df["ano"].unique()), default=sorted(df["ano"].unique()))
regioes = st.sidebar.multiselect("Região", sorted(df["regiao"].unique()), default=sorted(df["regiao"].unique()))
df_filtro = df[(df["ano"].isin(anos)) & (df["regiao"].isin(regioes))]

col1, col2, col3 = st.columns(3)
col1.metric("Total Homicídios", f"{df_filtro['hom_doloso'].sum():,}")
col2.metric("Total Roubos", f"{df_filtro['total_roubos'].sum():,}")
col3.metric("Total Furtos", f"{df_filtro['total_furtos'].sum():,}")

fig1 = px.line(df_filtro.groupby("ano")["hom_doloso"].sum().reset_index(),
               x="ano", y="hom_doloso", markers=True,
               title="Homicídios Dolosos por Ano")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(df_filtro.groupby("regiao")["crime_total"].sum().reset_index(),
              x="regiao", y="crime_total",
              title="Comparação Entre Regiões")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.area(df_filtro.groupby("ano")["total_roubos"].sum().reset_index(),
               x="ano", y="total_roubos",
               title="Total de Roubos por Ano")
st.plotly_chart(fig3, use_container_width=True)

ranking = df_filtro.groupby("regiao")["crime_total"].sum().sort_values(ascending=False)
st.subheader("Ranking Regiões Mais Perigosas")
st.dataframe(ranking)

fig_rank = px.bar(ranking.reset_index(), x="regiao", y="crime_total", color="crime_total",
                  title="Ranking de Regiões Mais Perigosas")
st.plotly_chart(fig_rank, use_container_width=True)

fig_mapa = px.scatter_mapbox(df_filtro, lat="lat", lon="lon",
                             size="crime_total", hover_name="regiao",
                             color="crime_total", zoom=6,
                             mapbox_style="carto-positron",
                             title="Mapa Interativo de Crimes")
st.plotly_chart(fig_mapa, use_container_width=True)

st.subheader("Tabela Resumo")
st.dataframe(df_filtro)
