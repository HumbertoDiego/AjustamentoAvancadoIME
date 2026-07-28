# Ajustamento Avançado IME

Aulas de Ajustamento Avançado ministradas para o 4º ano do Curso de Engenharia Cartográfica do Instituto Militar de Engenharia - Rio de Janeiro/RJ

<img src="media/imgs/ajustavcd.png">

## SUMÁRIO:

- [Aula 1](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/01_revisao_ajustamento_basico.ipynb): Revisão de Ajustamento Básico — MMQ, modelos paramétrico, condicionado e combinado e qualidade pós-ajustamento.
- [Aula 2](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/02_ajustamento_com_injuncoes.ipynb): Ajustamento com Injunções — modelos combinado e paramétrico com injunções. **1ª VE prática.**
- [Aula 3](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/03_deteccao_de_outliers.ipynb): Detecção de Outliers — data snooping, teste de Baarda, ajuste robusto e comparação L1/L2. **2ª VE prática.**
- [Aula 4](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/04_series_temporais.ipynb): Séries Temporais — tendência, sazonalidade, ruído e modelagem. **3ª VE prática.**
- [Aula 5](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/05_regularizacao.ipynb): Regularização — TSVD e Tikhonov. **4ª VE prática.**
- [Aula 6](https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main/06_otimizacao.ipynb): Otimização — função objetivo, métodos diretos, gradiente e lotes. **5ª VE prática.**
- Aula 7: Avaliação escrita. **6ª VE escrita.**
- Aulas 8-12:  Problemas e estudos de caso. **7ª VE apresentação oral.**

## REQUISITOS:

- [Python 3.12](https://www.python.org/downloads/)
- [Colab](https://colab.research.google.com/notebooks/intro.ipynb)
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
git add * ; git commit -m "aula 01 update"; git push ajustamento main --force
-->

