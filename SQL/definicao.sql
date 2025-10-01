# criando o banco de dados
create database restaurante;
# utilizando o banco de dados
use restaurante;
# criando a tabela funcionarios
create table funcionarios(
	id_funcionario int auto_increment primary key,
    nome varchar(255),
    cpf varchar(14),
    data_nascimento date,
    enderecoi varchar(255),
    telefone varchar(15),
    email varchar(100),
    cargo varchar(100),
    salario decimal(10,2),
    data_admissao date
);
# criando tabela de cliente
create table clientes(
	id_cliente int primary key auto_increment,
    nome varchar(255),
    cpf varchar(14),
    data_nascimento date,
    endereco varchar(255),
    telefone varchar(15),
    email varchar(100),
    data_cadastro date
);
# criando tabelas de produtos
create table produtos(
	id_produto int primary key auto_increment,
    nome varchar(255),
    descricao text,
    preco decimal(10,2),
    categoria varchar(100)
);
# criando tabela de pedidos
create table pedidos(
	id_pedido int primary key auto_increment,
    id_cliente int,
    id_funcionario int,
    id_produto int,
    quantidade int,
    preco decimal(10,2),
    data_pedido date,
    status varchar(50)
);
#criando a tabela de informacoes
create table informacoes(
	id_info int primary key auto_increment,
    id_produto int,
    ingredientes text,
    fornecedor varchar(255)
);
# criando constraints para as FKs

# fk de id_cliente
alter table pedidos
add constraint FK_PEDIDO_CLIENTE
foreign key (id_cliente)
references clientes(id_cliente);

# fk de id_funcionario
alter table pedidos
add constraint FK_PEDIDO_FUNCIONARIO
foreign key (id_funcionario)
references funcionarios(id_funcionario);

# fk de id_produto
alter table pedidos
add constraint FK_PEDIDO_PRODUTO
foreign key (id_produto)
references produtos(id_produto);

# fk de produtos na tabela informacoes
alter table informacoes
add constraint FK_INFORMACOES_PRODUTO
foreign key (id_produto)
references produtos(id_produto);

