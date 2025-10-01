#Use o banco de dados restaurante
use restaurante;

#Crie uma view chamada resumo_pedido do join entre essas tabelas:
#pedidos: id, quantidade e data
#clientes: nome e email
#funcionarios: nome
#produtos: nome, preco
create view resumo_pedido as
select pe.id_pedido, pe.quantidade, pe.data_pedido,
    c.nome as cliente, c.email,
    p.nome as produto, p.preco
from pedidos pe
join clientes c on c.id_cliente = pe.id_cliente
join produtos p on p.id_produto = pe.id_produto;

#Selecione o id do pedido, nome do cliente e o total (quantidade * preco) de cada pedido da view resumo_pedido
select id_pedido, cliente, quantidade*preco as total 
from resumo_pedido;

#Atualiza o view resumo pedido, adicionando campo total
alter view resumo_pedido as
select pe.id_pedido, pe.quantidade, pe.data_pedido,
    c.nome as cliente, c.email,
    p.nome as produto, p.preco, pe.quantidade*p.preco as total
from pedidos pe
join clientes c on c.id_cliente = pe.id_cliente
join produtos p on p.id_produto = pe.id_produto;

#Repita a consulta da questão 3, utilizando o campo total adicionado
select id_pedido, cliente, total 
from resumo_pedido;

#Repita a consulta da pergunta anterior, com uso do EXPLAIN para verificar e compreender o JOIN que está oculto na nossa query
explain
select id_pedido, cliente, total 
from resumo_pedido;

#Crie uma função chamada ‘BuscaIngredientesProduto’, que irá retornar os ingredientes da tabela info produtos, 
#passar o id de produto como argumento (entrada) da função.
DELIMITER //
create function BuscaIngredientesProduto(idProduto int)
returns varchar(200)
reads sql data
begin
    declare ingredientes varchar(200);
    select descricao into ingredientes from produtos where id_produto = idProduto;
    return ingredientes;
end //
DELIMITER ;

#Execute a função ‘BuscaIngredientesProduto’ com o id de produto 10
select BuscaIngredientesProduto(10);

#Crie uma função chamada ‘mediaPedido’ que irá retornar uma mensagem dizendo que o total do pedido é acima, 
#abaixo ou igual a média de todos os pedidos, quando passar o id do pedido como argumento da função
DELIMITER //
create function mediaPedido (idPedido int)
returns varchar (50)
reads sql data
begin
    declare resultado varchar (50);
    declare media decimal(10,2);
    declare pedidoTotal DECIMAL(10,2);

    select preco into pedidoTotal from pedidos where id_pedido = idPedido;
    
    if pedidoTotal is null then
        set resultado = 'Pedido Não Encontrado';
    else
        select avg(preco) into media from pedidos;

        if pedidoTotal > media then
            set resultado = 'Maior que a Media';
        elseif pedidoTotal < media then
            set resultado = 'Menor que a Media';
        else 
            set resultado = 'Igual a Media';
        end if;
    end if;

    return resultado;

end //
DELIMITER ;

#Execute a função ‘mediaPedido’ com o id de pedido 5 e depois 6.
select mediaPedido(5);
select mediaPedido(6);
