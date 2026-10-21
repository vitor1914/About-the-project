
from pathlib import Path
import json

import pandas as pd
import matplotlib.pyplot as plt


# Diretórios do projeto
BASE_DIR = Path(__file__).resolve().parent
ARQUIVO_ENTRADA = BASE_DIR / "dados" / "clientes.csv"
PASTA_RELATORIOS = BASE_DIR / "relatorios"
PASTA_GRAFICOS = BASE_DIR / "graficos"


def carregar_dados(caminho):
    """Carrega o CSV e reconhece marcadores comuns de dados ausentes."""
    return pd.read_csv(
        caminho,
        na_values=["", " ", "NA", "N/A", "null", "NULL", "None"],
        skipinitialspace=True
    )


def analisar_valores_ausentes(df):
    """Calcula ausentes, preenchidos e percentuais para cada coluna."""
    total_linhas = len(df)

    quantidade = df.isna().sum()
    preenchidos = df.notna().sum()

    if total_linhas > 0:
        percentual = (quantidade / total_linhas * 100).round(2)
    else:
        percentual = quantidade.astype(float)

    resultado = pd.DataFrame({
        "coluna": df.columns,
        "total_registros": total_linhas,
        "valores_ausentes": quantidade.values,
        "valores_preenchidos": preenchidos.values,
        "percentual_ausente": percentual.values
    })

    return resultado.sort_values(
        by="valores_ausentes",
        ascending=False
    ).reset_index(drop=True)


def gerar_graficos(resultado):
    """Cria gráficos de quantidade e percentual de valores ausentes."""
    PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)

    # Gráfico de quantidade
    dados = resultado.sort_values(
        "valores_ausentes",
        ascending=True
    )

    plt.figure(figsize=(10, 6))
    plt.barh(dados["coluna"], dados["valores_ausentes"])
    plt.xlabel("Quantidade de valores ausentes")
    plt.ylabel("Coluna")
    plt.title("Valores ausentes por coluna")
    plt.tight_layout()
    plt.savefig(
        PASTA_GRAFICOS / "valores_ausentes.png",
        dpi=150
    )
    plt.close()

    # Gráfico de percentual
    dados = resultado.sort_values(
        "percentual_ausente",
        ascending=True
    )

    plt.figure(figsize=(10, 6))
    plt.barh(dados["coluna"], dados["percentual_ausente"])
    plt.xlabel("Valores ausentes (%)")
    plt.ylabel("Coluna")
    plt.title("Percentual de valores ausentes por coluna")
    plt.tight_layout()
    plt.savefig(
        PASTA_GRAFICOS / "percentual_valores_ausentes.png",
        dpi=150
    )
    plt.close()


def salvar_relatorios(df, resultado):
    """Salva os resultados da análise em CSV e JSON."""
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

    resultado.to_csv(
        PASTA_RELATORIOS / "valores_ausentes_por_coluna.csv",
        index=False,
        encoding="utf-8-sig"
    )

    # Exporta uma cópia dos dados, sem excluir linhas ou colunas.
    df.to_csv(
        PASTA_RELATORIOS / "base_analisada.csv",
        index=False,
        encoding="utf-8-sig"
    )

    total_celulas = int(df.shape[0] * df.shape[1])
    total_ausentes = int(df.isna().sum().sum())

    percentual_geral = (
        round(total_ausentes / total_celulas * 100, 2)
        if total_celulas > 0
        else 0.0
    )

    resumo = {
        "arquivo_analisado": ARQUIVO_ENTRADA.name,
        "quantidade_registros": int(df.shape[0]),
        "quantidade_colunas": int(df.shape[1]),
        "total_celulas": total_celulas,
        "total_valores_ausentes": total_ausentes,
        "percentual_geral_ausente": percentual_geral,
        "colunas_com_ausentes": resultado.loc[
            resultado["valores_ausentes"] > 0,
            "coluna"
        ].tolist(),
        "detalhamento": resultado.to_dict(orient="records")
    }

    with open(
        PASTA_RELATORIOS / "resumo_analise.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        json.dump(
            resumo,
            arquivo,
            ensure_ascii=False,
            indent=4
        )

    return total_celulas, total_ausentes, percentual_geral


def main():
    if not ARQUIVO_ENTRADA.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {ARQUIVO_ENTRADA}"
        )

    df = carregar_dados(ARQUIVO_ENTRADA)

    resultado = analisar_valores_ausentes(df)

    total_celulas, total_ausentes, percentual_geral = (
        salvar_relatorios(df, resultado)
    )

    gerar_graficos(resultado)

    print("=" * 55)
    print("ANÁLISE DE VALORES AUSENTES")
    print("=" * 55)
    print(f"Registros: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")
    print(f"Células analisadas: {total_celulas}")
    print(f"Valores ausentes: {total_ausentes}")
    print(f"Percentual geral ausente: {percentual_geral}%")

    print("\nDetalhamento por coluna:")
    print(resultado.to_string(index=False))

    print("\nArquivos gerados:")
    print("relatorios/valores_ausentes_por_coluna.csv")
    print("relatorios/base_analisada.csv")
    print("relatorios/resumo_analise.json")
    print("graficos/valores_ausentes.png")
    print("graficos/percentual_valores_ausentes.png")

    print("\nAnálise concluída!")


if __name__ == "__main__":
    main()
