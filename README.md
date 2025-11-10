# Estrutura do projeto Banco de Dados

```bash
Atividade_Banco_Dados/
│
├─ venv/                      # Ambiente Virtual (ignorado pelo git)
├─ .gitignore
├─ requirements.txt
├─ livros_sqlite.py
├─ livraria.db                # (ignorado pelo git)
└─ README.md                  # Explicação + Questões respondidas
```
---

## 📝 Execute na pasta do projeto


---

## Parte 1: Explicação do Código
- Descrição resumida do que foi implementado
- Como executar o projeto
- Como rodar o script

### Clone o repositório
```bash
git clone https://github.com/MarceloRangelDev/atividade_bd_python.git

```


### 📝 Crie o ambiente virtual
```bash
python -m venv venv
```

### Ativar o ambiente virtual

- macOS / Linux (bash, zsh):
```bash
source venv/bin/activate
# ou
.venv/bin/activate
```

- Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

- Windows (Prompt de Comando - cmd.exe):
```cmd
venv\Scripts\activate.bat
```

- Git Bash / MSYS:
```bash
source venv/Scripts/activate
```
---

### Instale dependências (se houver)
```bash
pip install -r requirements.txt
```
---

### Execute o script
```bash
python livros_sqlite.py
```

---
## Parte 2: Questões Teóricas
Pesquise no Google e responda as seguintes questões. Importante: Cite a fonte
(link) de onde obteve a informação para cada resposta.

### Questões para Pesquisa
#### Fundamentos de Bancos de Dados

### 1. Por que os bancos de dados são essenciais em aplicações modernas?

Os bancos de dados são fundamentais em aplicações atuais porque: 
- Servem como repositório centralizado para armazenamento e recuperação de dados estruturados e não‑estruturados, garantindo consistência e integridade. 

- Suportam funcionalidades-chave de sistemas modernos, como gerenciamento de perfis de usuários, catálogo de produtos e transações. 

- Permitem escalabilidade, auditoria, segurança e análise de dados.

Fonte: 
https://medium.com/design-bootcamp/database-management-in-modern-applications-c89a11426ac
https://knowledgecom.tech/importance-and-demand-for-databases/

### 2. Quais são as duas principais categorias de bancos de dados existentes?

As duas principais categorias são: 
- **Relacionais (SQL)** --- usam tabelas e esquema rígido. 
- **Não-relacionais (NoSQL)** --- usam modelos como documentos, chave‑valor ou grafos.
- Diferenças incluem esquema, consistência e modelo de dados. 
Fonte: https://www.geeksforgeeks.org/dbms/difference-between-relational-database-and-nosql
https://www.mongodb.com/resources/compare/relational-vs-non-relational-databases 
https://aws.amazon.com/compare/the-difference-between-relational-and-non-relational-databases

### 3. Em quais cenários é recomendado utilizar um banco de dados relacional?

-   Quando os dados são estruturados e possuem relacionamentos complexos.
-   Quando transações ACID são necessárias.
-   Quando há necessidade de joins e consultas complexas.
Fonte: https://www.geeksforgeeks.org/dbms/acid-properties-in-dbms

### 4. De que forma os recursos de hardware afetam a performance do banco?

-   **CPU**: processa consultas e operações.
-   **RAM**: aumenta cache e reduz acessos ao disco.
-   **Disco/I/O**: é comumente o maior gargalo.
Fonte:
https://www.techmixing.com/2025/08/effect-of-cpu-ram-and-disk-i-o-on-database-performance.html
https://dzone.com/articles/decoding-database-speed-essential-server-resources
https://www.ibm.com/docs/en/informix-servers/14.10.0

### 5. O que significa escalabilidade?

Escalabilidade é a capacidade de um sistema (aplicação, banco de dados ou infraestrutura) de manter ou melhorar seu desempenho quando aumentam a carga ou volume de dados.

- Tipos:
    - Vertical (scale‑up): aumentar recursos de uma única máquina (CPU, RAM, disco). Simples, mas limitado por teto físico e possivelmente mais caro.
    - Horizontal (scale‑out): adicionar mais máquinas/instâncias ao sistema; melhora capacidade e tolerância a falhas, mas exige particionamento, balanceamento e coordenação entre nós.

- Métricas e trade‑offs:
    - Focar em throughput, latência e custo operacional.
    - Escalar horizontalmente melhora disponibilidade e capacidade, mas aumenta complexidade (consistência, sincronização).
    - Escalar verticalmente é mais fácil de implementar inicialmente, mas tem limites e pode causar downtime.

Fontes: https://www.cloudzero.com/blog/horizontal-vs-vertical-scaling/ 
https://www.pingcap.com/blog/horizontal-scaling-vs-vertical-scaling/


### 6. Qual a relevância de organizar corretamente os dados?

-   Reduz redundância e evita anomalias. 
-   Mantém integridade e facilita manutenção.
Fonte: https://en.wikipedia.org/wiki/Relational_database

### 7. Como escolher entre SQL e NoSQL?

-   Depende de estrutura do dado, consistência, escalabilidade e tipo de dados.
-   SQL é mais simples e mais fácil de usar, mas não é tão eficiente.
-   NoSQL é mais eficiente, mas não é tão simples.
-   SQL é mais fácil de entender e trabalhar, mas não é tão eficiente.
-   NoSQL é mais fácil de usar, mas não é tão eficiente.
Fonte: https://www.mongodb.com/resources/compare/relational-vs-non-relational-databases


---

#### Comandos SQL
1. **Qual é a finalidade do comando SELECT em SQL?**\
`(Descreva sua função e uso básico)`\
Ler/consultar dados de tabelas.

2. **O que significam as siglas DML e DDL em bancos de dados?**\
`(Defina e diferencie Data Manipulation Language e Data Definition Language)`
-   **DML**: manipula dados (SELECT, INSERT, UPDATE, DELETE).
-   **DDL**: estrutura do BD (CREATE, ALTER, DROP).

3. **Para que serve a cláusula WHERE em consultas SQL?**\
`(Explique seu papel na filtragem de dados)`\
Filtra registros com base em uma condição.

4. **Por que é fundamental estabelecer uma chave primária (PRIMARY KEY) em tabelas?**\
`(Importância da chave primária)`\
Garante unicidade, integridade referencial e melhora o desempenho.

5. **Como funciona o comando UPDATE e qual sua sintaxe básica?**\
`(Explique a atualização de registros)`\
Atualiza registros existentes.

6. **Qual a função do comando DELETE em SQL?**\
`(Diferença entre DELETE e DROP)`\
Remove dados; difere de DROP, que remove a tabela inteira.

7. **Como a cláusula ORDER BY organiza os resultados de uma consulta?**\
`(Ordenação ascendente e descendente)`\
Ordena resultados (ASC ou DESC).
Sendo: 
**ASC**: Ordena resultados de forma ascendente (A-Z).
**DESC**: Ordena resultados de forma descendente (Z-A).

8. **Para que serve o comando LIMIT em consultas SQL?**\
`(Controle de quantidade de registros retornados)`\
Restringe número de registros retornados.

---

#### Outros Conceitos

1. **Por que é importante integrar o banco de dados com a camada de backend da aplicação?**\
`(Relação entre BD e servidor)`\
É importante para permitir o controle de acesso, regras de negócio e segurança.

2. **O que são views (visões) em bancos de dados e quais suas vantagens?**\
`(Conceito e utilidade de views)`\
São consultas armazenadas que atuam como tabelas virtuais e permitem reutilizar consultas e otimizam a performance.

3. **Quais são as propriedades ACID e por que são cruciais para transações?**\
`(Atomicidade, Consistência, Isolamento, Durabilidade)`\
ACID é um conjunto de garantias que tornam as transações seguras e previsíveis:

- **Atomicidade**  
    A transação é atômica: ou todas as operações são aplicadas, ou nenhuma. Permite rollback em caso de falha, evitando estados parciais.

- **Consistência**  
    Cada transação leva o banco de dados de um estado válido para outro, respeitando restrições, chaves e regras de integridade.

- **Isolamento**  
    Transações concorrentes não devem interferir entre si; cada uma percebe o sistema como se fosse a única em execução. Controlado por níveis de isolamento (ex.: READ COMMITTED, SERIALIZABLE).

- **Durabilidade**  
    Uma vez feita o commit, os efeitos da transação persistem mesmo diante de falhas (uso de logs e armazenamento confiável).

Por que são cruciais: garantem correção, integridade e confiança nas operações — especialmente em cenários concorrentes e críticos (ex.: transferências financeiras), onde falhas, duplicações ou perda de dados seriam inaceitáveis.

4. **O que estabelece o Princípio do Privilégio Mínimo em segurança de bancos de dados?**\
`(Conceito de menor privilégio e suas aplicações)`\
Cada usuário deve ter apenas os acessos necessários.

Estabelece que cada usuário, processo ou componente do sistema deve receber somente os privilégios estritamente necessários para executar suas funções, nem mais nem menos. O objetivo é reduzir a superfície de ataque e limitar o impacto de erros ou comprometimentos.

Boas práticas:
- Conceder permissões por função (roles) em vez de a usuários individuais.
- Separação de deveres (separation of duties) para evitar concentrações de poder.
- Uso de contas temporárias/elevação just-in-time para operações administrativas.
- Revisões e revogações periódicas de permissões e auditoria de acessos.
- Aplicar o princípio também a serviços e conexões entre componentes (credenciais mínimas).

Exemplo prático: criar uma role com SELECT apenas para a aplicação de leitura e uma role separada, com privilégios de INSERT/UPDATE, só para processos autorizados.

Fonte: https://cheatsheetseries.owasp.org/cheatsheets/Principle_of_Least_Privilege_Cheat_Sheet.html
