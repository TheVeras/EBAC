#Use o banco de dados restaurante e crie os joins ou subconsultas
use restaurante;

#Selecionar:
#produtos: id, nome e descrição e info_produtos:  ingredientes
select p.id_produto, p.descricao, i.ingredientes
from produtos p
join informacoes i
on p.id_produto = i.id_produto;

#Selecionar:
#pedidos:  id, quantidade e data e clientes: nome e email
select pe.id_pedido, pe.quantidade, pe.data_pedido, cl.nome, cl.email
from pedidos pe
join clientes cl
on pe.id_cliente = cl.id_cliente;

#Selecionar:
#pedidos:  id, quantidade e data e clientes: nome e email e funcionarios: nome
select pe.id_pedido, pe.quantidade, pe.data_pedido, 
    cl.nome as cliente, cl.email, 
    f.nome as funcionario
from pedidos pe
join clientes cl
    on pe.id_cliente = cl.id_cliente
join funcionarios f
    on pe.id_funcionario = f.id_funcionario;

#Selecionar:
#pedidos:  id, quantidade e data e clientes: nome e email e funcionarios: nome e produtos: nome, preco
select pe.id_pedido, pe.quantidade, pe.data_pedido, 
    cl.nome as cliente, cl.email, 
    f.nome as funcionario,
    p.nome as produto, p.preco
from pedidos pe
join clientes cl
    on pe.id_cliente = cl.id_cliente
join funcionarios f
    on pe.id_funcionario = f.id_funcionario
join produtos p
    on pe.id_produto = p.id_produto;
    
#Selecionar o nome dos clientes com os pedidos com status ‘Pendente’ e exibir por ordem descendente de acordo com o id do pedido
select pe.id_pedido, pe.status,
    cl.nome as cliente
from pedidos pe
	join clientes cl
    on pe.id_cliente = cl.id_cliente
where pe.status = 'Pendente'
order by pe.id_pedido desc;

#Selecionar clientes sem pedidos
select cl.* 
from clientes cl
left join pedidos pe
    on cl.id_cliente = pe.id_cliente
where pe.id_cliente is null;

#Selecionar o nome do cliente e o total de pedidos cada cliente
select cl.nome as cliente,
    pedidos_agregados.total_pedidos
from clientes cl
join(
    select id_cliente, count(*) as total_pedidos
    from pedidos
    group by id_cliente
) as pedidos_agregados on
cl.id_cliente = pedidos_agregados.id_cliente;

#Selecionar o preço total (quantidade*preco) de cada pedido
select id_pedido, quantidade, preco, sum(quantidade*preco) as preco_total
from pedidos
group by id_pedido;
