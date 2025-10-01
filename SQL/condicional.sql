# usando o banco de dados
use restaurante;

# filtrando pedidos por id_funcionario e status
select * from pedidos
where id_funcionario = 4 and status = 'Pendente';

# filtrando pedidos por status difrente de Concluido
select * from pedidos
where not status = 'Concluido';

# filtrando pedidos por id_produto
select * from pedidos
where id_produto in (1, 3, 5, 7, 8);

# filtrando por nnome dos clientes que começam com a letra C
select * from clientes
where nome like 'C%' or nome like 'c%';

# filtrando pratos que contenham carne ou frango
select * from informacoes
where ingredientes like '%arne%' or ingredientes like '%rango%';

# filtrando produtos por faixa de preço
select * from produtos
where preco between 20 and 30;

# alterando o status do pedido 6 para nulo
update pedidos
set status = null
where id_pedido = 6;

# selecionando pedidos com status nulo
select * from pedidos 
where status is null;

# selecionando pedidos e caso status nulo setando visualmente para cancelado
select id_pedido, status,
ifnull (status, 'Cancelado') as pedidos_nulos from pedidos;


select nome, cargo, salario,
case
	when salario > 3000 then 'Acima da Media'
    else 'Abaixo da Media'
end as media_salario
from funcionarios;
