# app_ferias
Projeto de aplicação para cálculo de férias com Python.
A empresa Coca-Cola Company requer um programa com interface gráfica de
usuário, o qual deve realizar o cálculo dos dias de férias a que o trabalhador tem
direito, dependendo do seu cargo e tempo de serviço na empresa. Para isso, a
empresa forneceu os seguintes requisitos:
Design e Funcionalidade
O programa deve conter três interfaces distintas, para navegação entre elas, sendo
as seguintes:
1. Tela de boas-vindas: A) A tela principal de inicialização deve conter: ▪
Logotipo e cores da marca. ▪ Imagem representativa no ícone da aplicação. ▪
Um campo de texto onde o usuário deve digitar seu nome. ▪ Um botão que
permita avançar para a próxima tela. ▪ No rodapé da interface, deve conter o
texto ©2022 The Coca-Cola Company.
B) Funcionalidade dessa interface: ▪ Capturar o nome do usuário. ▪ Não permitir
avançar para a próxima interface se o usuário não tiver escrito seu nome. ▪ Se o
usuário escrever seu nome, permitir avançar para a próxima interface.
2. Tela de Termos e Condições: A) A tela de termos e condições deve conter:
▪ Logotipo da marca. ▪ Imagem representativa no ícone da aplicação. ▪ Um
campo onde possam ser lidos os termos e condições. ▪ Implementar uma
forma para que o usuário aceite os termos e condições. ▪ Botão de continuar.
▪ Botão de Não aceitar.
B) Funcionalidade dessa interface: ▪ O nome do usuário que aceitará ou não os
termos e condições deve aparecer em alguma parte da interface, pois assim é
confirmado que é o mesmo usuário quem aceita os termos e condições. ▪ O botão
de “Continuar” deve estar desabilitado enquanto o usuário não aceitar os termos e
condições, enquanto o botão de “Não aceitar” deve estar habilitado. ▪ O botão “Não
aceitar” deve ser desabilitado quando o usuário aceitar os termos e condições,
enquanto o botão de “Continuar” deve ser habilitado. ▪ O botão “Continuar” deve
enviar para a próxima tela, enquanto o botão “Não aceitar” deve fechar a aplicação.
3. Tela principal: A) A tela principal deve conter: ▪ Logotipo da marca. ▪
Imagem representativa no ícone da aplicação. ▪ Menu superior com
diferentes funcionalidades (a critério do desenvolvedor). ▪ Campos de texto
para nome, sobrenome e resultado do cálculo das férias do trabalhador. ▪
Uma lista suspensa para selecionar o departamento e o tempo de serviço do
trabalhador. ▪ No rodapé da interface, deve conter o texto ©2022 The CocaCola Company.
B) Funcionalidade dessa interface: ▪ Em alguma parte da interface deve ser exibido
o nome do usuário que aceitou os termos e condições. ▪ O usuário deve ter a
liberdade de realizar ações de personalização na interface gráfica. ▪ Deve haver
uma opção para limpar os campos e realizar um novo cálculo. ▪ Deve haver uma
opção para retornar à tela de boas-vindas. ▪ Implementar uma maneira de realizar o
cálculo dos dias de férias com os dados solicitados do trabalhador. ▪ Adicionar os
dados do desenvolvedor de maneira que não interfiram na visibilidade do usuário
durante o uso do programa.
Tabela de dias a que um trabalhador tem direito:
Trabalhadores de atendimento ao cliente: • Com 1 ano de serviço, recebem 14
dias de férias. • Com 2 a 6 anos de serviço, recebem 18 dias de férias. • A partir de
7 anos de serviço, recebem 22 dias de férias.
Trabalhadores de Logística: • Com 1 ano de serviço, recebem 10 dias de férias. •
Com 2 a 6 anos de serviço, recebem 15 dias de férias. • A partir de 7 anos de
serviço, recebem 20 dias de férias.
Gerentes: • Com 1 ano de serviço, recebem 18 dias de férias. • Com 2 a 6 anos de
serviço, recebem 25 dias de férias. • A partir de 7 anos de serviço, recebem 30 dias
de férias.
