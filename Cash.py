import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Análise de Rentabilidade - Construtora Tenda", layout="wide")

# Logo redonda (substitua pelo caminho da sua imagem ou URL)
logo = "Logo.png"  # Exemplo de caminho local para a imagem

# Cria uma linha com duas colunas: uma para a logo e outra para o título
col1, col2 = st.columns([1, 4])  # Ajuste a proporção conforme necessário

# Coluna 1: Exibe a logo
with col1:
    st.image(logo, width=100)  # Exibe a logo com largura de 100px

# Coluna 2: Exibe o título
with col2:
    st.markdown(
    """
    <h1 style="text-align: center;">Posição de Caixa - Construtora Tenda</h1>
    """, 
    unsafe_allow_html=True
)

st.divider()

# Sidebar para menus e filtros
with st.sidebar:
    st.markdown(
    """
    <h1 style="text-align: center;">Menu de Navegação</h1>
    """, 
    unsafe_allow_html=True
)
    st.divider()
    menu_option = st.radio(
        "Selecione uma opção:",
        [
            "Visão Geral", 
            "Rentabilidade", 
            "Bancos e Ratings", 
            "Caixa Bloqueado", 
            "Bloqueio de Garantia por Bancos", 
            "Posição de Caixa por Empresa", 
            "Fluxo de Caixa", 
            "Indicadores Econômicos"
        ]
    )
    st.divider()
    st.header("Filtros")
    # Filtro por categoria de rentabilidade
    categoria_filtro = st.selectbox(
        "Selecione uma categoria de rentabilidade:",
        ["Todas", "Gestão Externa", "Fundo FI Tenda", "Fundo Itaú Corp Plus", "CDB", "Compromissada", "Dynamic", "LF"]
    )

    # Filtro por período
    periodo_filtro = st.selectbox(
        "Selecione o período:",
        ["Últimos 30 dias", "Últimos 90 dias", "Últimos 12 meses"]
    )
    st.divider()
    st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; height: 20vh;">
        <a href="http://www.google.com" target="_blank" style="font-size: 15px; text-decoration: none; color: white;">
            🌎 Pesquise no Google
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
    
# Dados de rentabilidade (extraídos do PDF)
data = {
    "Nome": ["Gestão Externa", "Fundo FI Tenda", "Fundo Itaú Corp Plus", "CDB", "Compromissada", "Dynamic", "LF"],
    "% CDI Ano": [105.78, 97.79, 104.97, 100.37, 88.00, 85.00, 102.00],
    "Valor (R$)": [1008, 28079, 4092, 266874, 19676, 33, 21058]
}

# Criando um DataFrame com os dados
df = pd.DataFrame(data)

# Dados de fluxo de caixa
fluxo_data = {
    "Categoria": ["Fluxo Operacional", "Liberação SFH", "Amortização/Juros SFH"],
    "Valor (R$)": [-54390, 18929, -35402]
}
fluxo_df = pd.DataFrame(fluxo_data)

# Dados de indicadores econômicos (exemplo fictício)
indicadores_economicos = {
    "Indicador": ["IPCA", "Selic", "PIB", "Câmbio (USD/BRL)"],
    "Valor": ["4.5%", "13.75%", "2.9%", "5.20"]
}
indicadores_df = pd.DataFrame(indicadores_economicos)

# Dados de bancos e ratings (extraídos do PDF)
bancos_data = {
    "Banco": ["CEF", "Bradesco", "Votorantim", "Banco do Brasil", "Itaú", "Santander", "Banco Original", "Daycoval", "Pine", "Mercantil", "Safra"],
    "Rating": ["AA", "AAA", "AAA", "AAA", "AAA", "AA", "BBB", "AA", "BBB", "B", "AAA"],
    "Total (R$)": [428779, 22743, 64, 2431, 30184, 10710, 1, 134, 19, 19, 10893],
    "Liquidez (R$)": [302138, 13898, 1, 815, 815, 206, 1, 98, 19, 19, 10814],
    "Bloqueado (R$)": [55335, 8843, 63, 0, 21058, 10734, 0, 36, 0, 0, 79]
}
bancos_df = pd.DataFrame(bancos_data)

# Dados de caixa bloqueado (extraídos do PDF)
caixa_bloqueado_data = {
    "Categoria": ["Bloqueio Garantia", "Patrimônio Afetado", "SPE Sócio (Tenda)", "Total"],
    "Valor (R$)": [79418, 11730, 15289, 106437]
}
caixa_bloqueado_df = pd.DataFrame(caixa_bloqueado_data)

# Dados de bloqueio de garantia por bancos (extraídos do PDF)
bloqueio_garantia_data = {
    "Banco": ["CEF", "Bradesco", "Votorantim", "Banco do Brasil", "Itaú", "Santander", "Banco Original", "Daycoval", "Pine", "Mercantil", "Safra"],
    "Bloqueio Garantia (R$)": [55335, 8843, 63, 0, 21058, 10734, 0, 36, 0, 0, 79]
}
bloqueio_garantia_df = pd.DataFrame(bloqueio_garantia_data)

# Dados de posição de caixa por empresa (extraídos do PDF)
posicao_caixa_data = {
    "Empresa": ["Tenda", "SPE Tenda", "Outras"],
    "Saldo Disponível (R$)": [60588, 275515, 100000],
    "Saldo Bloqueado (R$)": [53488, 45154, 50000],
    "Total (R$)": [114076, 320669, 150000]
}
posicao_caixa_df = pd.DataFrame(posicao_caixa_data)

# Página de Visão Geral
if menu_option == "Visão Geral":
    st.header("Visão Geral")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Caixa Líquido Efetivo", value="R$ 337.190", delta="-R$ 31.000")
    with col2:
        st.metric(label="Caixa Líquido Plano", value="R$ 668.840", delta="+R$ 153.334")
    with col3:
        st.metric(label="Rentabilidade Média", value="99.61%", delta="+0.5%")

    st.write("### Gráfico de Rentabilidade por Categoria")
    fig1 = px.bar(df, x="Nome", y="% CDI Ano", text="% CDI Ano", color="% CDI Ano",
                  color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig1, use_container_width=True)  # Ocupa toda a largura

# Página de Rentabilidade
elif menu_option == "Rentabilidade":
    st.header("Análise de Rentabilidade")

    # Aplicando filtro de categoria
    if categoria_filtro != "Todas":
        df_filtrado = df[df["Nome"] == categoria_filtro]
    else:
        df_filtrado = df

    st.write(f"### Rentabilidade - {categoria_filtro}")
    st.dataframe(df_filtrado, use_container_width=True)  # Tabela ocupa toda a largura

    st.divider()
    # Gráfico de pizza para a distribuição dos valores (R$)
    st.write("### Distribuição dos Valores (R$)")
    fig2 = px.pie(df_filtrado, values="Valor (R$)", names="Nome", title="Distribuição dos Valores",
                  color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig2, use_container_width=True)  # Ocupa toda a largura

# Página de Bancos e Ratings
elif menu_option == "Bancos e Ratings":
    st.header("Bancos e Ratings")

    st.write("### Dados dos Bancos e Ratings")
    st.dataframe(bancos_df, use_container_width=True)  # Tabela ocupa toda a largura

    st.divider()
    # Gráfico de ratings dos bancos
    st.write("### Distribuição de Ratings dos Bancos")
    fig3 = px.bar(bancos_df, x="Banco", y="Total (R$)", color="Total (R$)", text="Total (R$)",
                  color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig3, use_container_width=True)  # Ocupa toda a largura

# Página de Caixa Bloqueado
elif menu_option == "Caixa Bloqueado":
    st.header("Caixa Bloqueado")

    st.write("### Dados de Caixa Bloqueado")
    st.dataframe(caixa_bloqueado_df, use_container_width=True)  # Tabela ocupa toda a largura

    st.divider()
    # Gráfico de caixa bloqueado
    st.write("### Distribuição de Caixa Bloqueado")
    fig4 = px.bar(caixa_bloqueado_df, x="Categoria", y="Valor (R$)", text="Valor (R$)", color="Valor (R$)",
                  color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig4, use_container_width=True)  # Ocupa toda a largura

# Página de Bloqueio de Garantia por Bancos
elif menu_option == "Bloqueio de Garantia por Bancos":
    st.header("Bloqueio de Garantia por Bancos")

    st.write("### Dados de Bloqueio de Garantia por Bancos")
    st.dataframe(bloqueio_garantia_df, use_container_width=True)  # Tabela ocupa toda a largura

    st.divider()
    # Gráfico de bloqueio de garantia por bancos
    st.write("### Distribuição de Bloqueio de Garantia por Bancos")
    fig5 = px.bar(bloqueio_garantia_df, x="Banco", y="Bloqueio Garantia (R$)", text="Bloqueio Garantia (R$)", color="Bloqueio Garantia (R$)",
                  color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig5, use_container_width=True)  # Ocupa toda a largura

# Página de Posição de Caixa por Empresa
elif menu_option == "Posição de Caixa por Empresa":
    st.header("Posição de Caixa por Empresa")

    st.write("### Dados de Posição de Caixa por Empresa")
    st.dataframe(posicao_caixa_df, use_container_width=True)  # Tabela ocupa toda a largura

    st.divider()
    # Gráfico de posição de caixa por empresa
    st.write("### Distribuição de Saldo Disponível e Bloqueado por Empresa")
    fig6 = px.bar(posicao_caixa_df, x="Empresa", y=["Saldo Disponível (R$)", "Saldo Bloqueado (R$)"], barmode="group",
                  color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig6, use_container_width=True)  # Ocupa toda a largura

# Página de Fluxo de Caixa
elif menu_option == "Fluxo de Caixa":
    st.header("Fluxo de Caixa")

    st.write("### Fluxo de Caixa (R$)")
    fig7 = px.bar(fluxo_df, x="Categoria", y="Valor (R$)", text="Valor (R$)", color="Valor (R$)",
                  color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig7, use_container_width=True)  # Ocupa toda a largura

    # Métricas de fluxo de caixa
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Fluxo Operacional", value="R$ -54.390")
    with col2:
        st.metric(label="Liberação SFH", value="R$ 18.929")
    with col3:
        st.metric(label="Amortização/Juros SFH", value="R$ -35.402")

# Página de Indicadores Econômicos
elif menu_option == "Indicadores Econômicos":
    st.header("Indicadores Econômicos")

    st.write("### Principais Indicadores Econômicos")
    st.dataframe(indicadores_df, use_container_width=True)  # Tabela ocupa toda a largura

    st.divider()
    # Gráfico de indicadores econômicos (exemplo fictício)
    st.write("### Gráfico de Indicadores Econômicos")
    fig8 = go.Figure(data=[go.Bar(x=indicadores_df["Indicador"], y=[4.5, 13.75, 2.9, 5.2], marker_color=px.colors.sequential.Blues)])
    fig8.update_layout(title="Indicadores Econômicos", xaxis_title="Indicador", yaxis_title="Valor (%)")
    st.plotly_chart(fig8, use_container_width=True)  # Ocupa toda a largura
    
# Rodapé
st.write("---")
st.markdown(
    "<p style='text-align: center;'>By Ryan Costa Rangel - Analista Financeiro Jr</p>", 
    unsafe_allow_html=True
)
