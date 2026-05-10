# Dicionário de Dados

Este documento apresenta a estrutura inicial prevista para a base analítica do projeto Rio API Indicadores Públicos.

## Objetivo

Registrar os principais campos que serão utilizados no projeto, indicando sua descrição, origem prevista e finalidade analítica.

## Base territorial

| Campo | Descrição | Origem prevista |
|---|---|---|
| municipio | Nome do município | DATA.RIO |
| bairro | Nome do bairro | DATA.RIO |
| regiao_administrativa | Região administrativa do bairro | DATA.RIO |
| area_planejamento | Área de planejamento do município | DATA.RIO |
| geometria | Informação geográfica do território | DATA.RIO |

## Educação

| Campo | Descrição | Origem prevista |
|---|---|---|
| qtd_escolas | Quantidade de escolas municipais no território | DATA.RIO |
| qtd_creches | Quantidade de creches no território | DATA.RIO |
| qtd_edis | Quantidade de Espaços de Desenvolvimento Infantil no território | DATA.RIO |
| qtd_unidades_educacao | Total de unidades educacionais identificadas | DATA.RIO |

## Saúde

| Campo | Descrição | Origem prevista |
|---|---|---|
| qtd_unidades_saude | Quantidade de unidades públicas de saúde no território | DATA.RIO |
| tipo_unidade_saude | Tipo da unidade de saúde | DATA.RIO |
| qtd_unidades_saude_por_tipo | Quantidade de unidades por tipo | DATA.RIO |

## Segurança pública

| Campo | Descrição | Origem prevista |
|---|---|---|
| ano | Ano de referência do indicador | ISP Dados Abertos |
| mes | Mês de referência do indicador | ISP Dados Abertos |
| roubo_rua | Quantidade de registros de roubo de rua | ISP Dados Abertos |
| roubo_veiculo | Quantidade de registros de roubo de veículo | ISP Dados Abertos |
| homicidio_doloso | Quantidade de registros de homicídio doloso | ISP Dados Abertos |
| letalidade_violenta | Indicador de letalidade violenta | ISP Dados Abertos |

## Indicadores derivados

| Campo | Descrição |
|---|---|
| total_equipamentos_publicos | Soma de unidades de saúde e educação no território |
| unidades_educacao_por_habitante | Indicador previsto para medir oferta educacional relativa à população |
| unidades_saude_por_habitante | Indicador previsto para medir oferta de saúde relativa à população |

## Observações

Este dicionário será atualizado conforme as APIs forem consumidas e os campos reais das bases forem identificados.

Os nomes finais das colunas poderão ser ajustados durante a etapa de tratamento e padronização dos dados.
