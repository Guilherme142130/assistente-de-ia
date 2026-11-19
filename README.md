# Alfred Jovem – Sistema Inteligente de Orientação e Apoio aos Jovens

## 1. Sobre o projeto

O Alfred Jovem é um assistente virtual desenvolvido em Python com o objetivo de oferecer orientações e informações úteis para jovens. O sistema funciona pelo terminal e permite que o usuário faça perguntas, consulte orientações por categorias e encontre informações relacionadas a diferentes assuntos do cotidiano.

O projeto busca facilitar o acesso à informação por meio de respostas simples e de uma base de conhecimento organizada.

## 2. Público-alvo

O sistema é destinado principalmente a jovens que buscam orientações e informações sobre assuntos como trabalho, documentação e serviços importantes para sua vida pessoal e profissional.

## 3. Objetivo do projeto

O objetivo é desenvolver uma ferramenta acessível que ajude os jovens a encontrar informações confiáveis, contribuindo para sua autonomia e para o acesso ao conhecimento.

## 4. Tecnologias utilizadas

- Python
- JSON para armazenamento da base de conhecimento
- CSV para exportação dos registros de atendimento
- Programação Orientada a Objetos
- Git e GitHub para versionamento e disponibilização do projeto

## 5. Funcionalidades

- Responder perguntas escritas pelo usuário.
- Pesquisar orientações na base de conhecimento.
- Organizar informações por categorias.
- Utilizar normalização de texto para facilitar a busca.
- Calcular pontuações para identificar orientações relacionadas à pergunta.
- Apresentar o nível de confiança da resposta.
- Bloquear entradas que aparentem conter dados pessoais.
- Registrar os atendimentos realizados.
- Apresentar indicadores de utilização.
- Exportar os registros para um arquivo CSV.

## 6. Base de conhecimento

As orientações são armazenadas em um arquivo JSON, permitindo organizar os conteúdos por identificador, categoria, título, palavras-chave, resposta, documentos necessários, local de consulta, fonte e data de verificação.

Atualmente, a base contém 10 orientações distribuídas em 3 categorias.

## 7. Como executar o projeto

1. Instale o Python em seu computador.
2. Baixe ou clone o repositório.
3. Abra a pasta do projeto no terminal.
4. Execute o comando:

```bash
python main.py
```

5. Siga as instruções apresentadas pelo assistente.

## 8. Sistema de busca

O Alfred utiliza uma busca por pontuação para relacionar a pergunta do usuário às orientações cadastradas.

A pontuação considera:
- Correspondência entre os termos digitados e as palavras-chave cadastradas.
- Correspondência entre os termos da pergunta e o título da orientação.

Os resultados são organizados conforme a pontuação obtida. Isso ajuda o sistema a selecionar conteúdos relacionados à dúvida apresentada.

## 9. Fontes de informação

As orientações utilizam fontes oficiais, incluindo:

- Portal Gov.br: https://www.gov.br/
- Tribunal Superior Eleitoral: https://www.tse.jus.br/

As informações possuem uma data de verificação registrada na base de conhecimento.

## 10. Testes com usuários

Esta seção deve ser preenchida após a realização dos testes com pessoas externas à equipe.

Devem ser registrados:
- Quantidade de pessoas participantes.
- Quantidade total de atendimentos.
- Dúvidas apresentadas pelos participantes.
- Resultados obtidos.
- Melhorias realizadas a partir das sugestões recebidas.

## 11. Limitações do sistema

O Alfred depende das informações cadastradas em sua base de conhecimento. Portanto, perguntas sobre assuntos que ainda não foram adicionados podem não apresentar resultados.

O sistema não substitui orientações profissionais ou atendimento de órgãos oficiais. É importante consultar as fontes indicadas para confirmar informações que possam sofrer alterações.

## 12. Vídeo de apresentação

Link do vídeo: (https://youtu.be/_oNcATzyURc)

## 13. Integrantes da equipe

- Nome: Guilherme de Lucena Fontes – RM: 569658
- Nome: Ricardo Tunes Vaca – RM: 555919
- Nome: Matheus Levi Dagel – RM: 571961