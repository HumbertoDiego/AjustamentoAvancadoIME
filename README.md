# Ajustamento Avançado IME

Aulas de Ajustamento Avançado (Inverse Problems) ministradas para o 3º ano do Curso de Engenharia Cartográfica do Instituto Militar de Engenharia - Rio de Janeiro/RJ

<img src="media/imgs/AjustAvançado.png">

## SUMÁRIO:

- [Aula 1](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/01_revisao_ajustamento_basico.ipynb): Revisão sobre Ajustamento Básico, Cálculo vetorial, Expansão de Taylor, Multiplicadores de Lagrange, MMQ Caso Geral (Combinado/Implícito)

- [Aula 2](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/02_deteccao_erros_grosseiros.ipynb): 

- [Aula 3](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/03_estimadores_robustos.ipynb): 

- [Aula 4](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/04_filtragem_sequencial.ipynb): 

- [Aula 5](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/05_redes_geodesicas.ipynb): 



## REQUISITOS:

- [Python 3.12](https://www.python.org/downloads/)
- [Colab]
- [VS Code](https://code.visualstudio.com/) e [Extensão Jupyter do VS Code](https://marketplace.visualstudio.com/search?term=jupyter&target=VSCode&category=All%20categories&sortBy=Relevance)

No Windows PowerShell, macOS e Linux (Colab):

```powershell
pip install -r requirements.txt
```

<!--
git pull ajustamento main
git add * ; git commit -m "aula update"; git push ajustamento main
jupyter nbconvert --to slides 05_cond_sistemas.ipynb --TagRemovePreprocessor.remove_input_tags="hide_input" --SlidesExporter.reveal_scroll=True --post serve

reset
git init
git remote add ajustamento https://github.com/HumbertoDiego/AjustamentoAvancadoIME
git add * ; git commit -m "aula update"; git push ajustamento main --force
-->
