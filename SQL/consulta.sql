# usanso banco de dados restaurante
use restaurante;

# selecionando nome e categoria filtrando pelo preço
select nome, categoria from produtos
where preco > 30;

# selecionando nome, telefone e data filtrando pelo ano de nascuimento
select nome, telefone, data_nascimento from clientes
where year(data_nascimento) < 1985;

# selecionando id e ingrediente filtrando se contem a palavra carne
select id_produto, ingredientes from informacoes
where ingredientes like '%arne%';

# selecionando tudo e ordenando por preço, limite de 5 resultados
select * from produtos
order by preco desc limit 5;

# selecionando tudo e filtrando pela categoria limite de 2 pulando 6
select * from produtos
where categoria = 'Prato Principal'
limit 2 offset 5;

# criando backup da tabela pedidos
create table backup_pedidos as select * from pedidos;
insert into backup_pedidos select * from pedidos;
select * from backup_pedidos;