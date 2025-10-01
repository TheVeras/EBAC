# usando o bando de dados restaurante	
use restaurante;

# calculando a quantidade de pedidos
select count(*) as quantidade_pedidos from pedidos;

# Calcule a quantidade de clientes únicos que realizaram pedidos
select count(distinct id_cliente) from pedidos;

# Calcule a média de preço dos produtos
select avg(preco) as media_preco from produtos;

# Calcule o mínimo e máximo do preço dos produtos
select min(preco) as valor_minino, max(preco) as valor_maximo
from produtos;

# Selecione o nome e o preço do produto e faça um rank dos 5 produtos mais caros
select nome, preco,
rank () over (order by preco desc) as produtos_mais_caros
from produtos
limit 5;

# Selecione a média dos preços dos produtos agrupados por categoria
select categoria, avg(preco) as media_valor from produtos
group by categoria;

# Selecionar o fornecedor e a quantidade de produtos que vieram daquele fornecedor da informações de produtos
select distinct fornecedor from informacoes;
select fornecedor, count(fornecedor) from informacoes
group by fornecedor;
-- aqui acredito que deveriamos fazer um tratamento melhor, pois, existem produtos que contem mais de um fornecedor

# Selecionar os fornecedores que possuem mais de um produto cadastrado
SELECT fornecedor, COUNT(fornecedor) AS total_produtos
FROM informacoes
GROUP BY fornecedor
HAVING COUNT(fornecedor) > 1;

# Selecionar os clientes que realizaram apenas 1 pedido
select id_cliente, count(id_cliente) as total_pedidos
from pedidos
group by id_cliente
having count(id_cliente) < 2;