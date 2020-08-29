# Relatório

Um agente inteligente é uma entidade autônoma que é capaz de observar um ambiente através de sensores e atuar sobre este através de atuadores. Para tomar suas decisões ele pode atuar reativamente, realizar raciocínio por algoritmos simbólicos, procurando atingir metas. Agentes Inteligentes podem também ser capazes de aprender e usar estes conhecimentos para melhorar o seu desempenho.

Com isso, foi desenvolvido um programa para implementar o agente aspirador de pó, na linguagem **Python**. Para implementar o ambiente em que o agente será utilizado foi usada a biblioteca [tkinter](https://docs.python.org/3/library/tkinter.html), pois permite criar uma interface gráfica mais facilmente, e é possível determinar seu tamanho através de um parâmetro. O agente recebe o ambiente por parâmetro e possui funções para se movimentar e limpar os quadrados. Para a medida de desempenho foi implementada uma função que retorna o número de quadrados que foram limpos.

Portanto, foi possível implementar o agente aspirador de pó para ser usado em um ambiente e reagir às percepções através de ações, bem como medir seu desempenho através de uma função.