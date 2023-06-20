# webscraping-amazon-multpag
Webscraping no site da Amazon com base na paginação

Fazendo o webscraping com base no href que o botão de paginação oferece.

Ao tentar rodar o código, a partir de uma certa quantidade de requisições, a Amazon começa a barrar a requisição e assim dando erro 😢.

O codigo apenas retorna o link das paginas de produtos, e não cada produto e seu preço.
Ao tentar retornar o nome de cada produto e seu preço, apareceu um problema:
- O site carrega dinamicamente, ou seja, na unica requisição que é feita, ele não tem todos elementos HTML.
  
São 36 produtos por página, na requisição do código, retornam apenas 24. E os outros 12? Rolando a página, percebe-se uma requisição, e nessa requisição, é retornado um JSON,
que é onde está os outros 12 produtos(o HTML deles).

Pois é, ta ai um desafio.
