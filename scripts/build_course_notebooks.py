"""Gera a estrutura didática de Ajustamento Avançado para 2027/1."""

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/HumbertoDiego/AjustamentoAvancadoIME/blob/main"


def md(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


def header(filename: str, title: str, objectives: list[str]):
    badge = (
        f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        f"(https://colab.research.google.com/github/HumbertoDiego/"
        f"AjustamentoAvancadoIME/blob/main/{filename})"
    )
    goals = "\n".join(f"{i}. {goal}" for i, goal in enumerate(objectives, 1))
    return [
        md(badge),
        md(f"# {title}\n\n**Maj Diego - 1º Semestre / 2027**\n\n**Objetivos:**\n\n{goals}"),
    ]


def write(filename: str, title: str, objectives: list[str], cells):
    nb = nbf.v4.new_notebook(
        cells=header(filename, title, objectives) + cells,
        metadata={
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
    )
    nbf.write(nb, ROOT / filename)


write(
    "01_revisao_ajustamento_basico.ipynb",
    "Aula 1 — Revisão de Ajustamento Básico",
    [
        "Revisar o Método dos Mínimos Quadrados (MMQ) e suas hipóteses.",
        "Distinguir os modelos paramétrico, condicionado e combinado.",
        "Avaliar a qualidade do ajustamento por resíduos, variâncias e testes estatísticos.",
    ],
    [
        md("## 1. Método dos Mínimos Quadrados\n\nO MMQ estima os parâmetros que minimizam $\\Phi=V^TPV$, em que $V$ é o vetor dos resíduos e $P$ é a matriz dos pesos. Para o modelo linear $L_b=AX$, a solução é\n\n$$\\hat X=(A^TPA)^{-1}A^TPL_b.$$"),
        code("import numpy as np\n\nA = np.array([[1., 0.], [1., 1.], [1., 2.]])\nL = np.array([[1.0], [2.1], [2.9]])\nP = np.eye(3)\nX = np.linalg.solve(A.T @ P @ A, A.T @ P @ L)\nV = A @ X - L\nprint('Parâmetros ajustados:', X.ravel())\nprint('Resíduos:', V.ravel())"),
        md("## 2. Modelos de ajustamento\n\n- **Paramétrico:** $L_a=F(X_a)$; as observações dependem de parâmetros desconhecidos.\n- **Condicionado:** $F(L_a)=0$; as observações ajustadas devem satisfazer condições.\n- **Combinado (implícito):** $F(L_a,X_a)=0$; observações e parâmetros aparecem simultaneamente."),
        md("## 3. Qualidade pós-ajustamento\n\nVerifique os graus de liberdade $gl=m-n$, o fator de variância a posteriori $\\hat\\sigma_0^2=V^TPV/gl$, a matriz de covariância dos parâmetros e a compatibilidade dos resíduos com o modelo estocástico."),
        code("gl = len(L) - A.shape[1]\nsigma0_sq = (V.T @ P @ V).item() / gl\nSigma_X = sigma0_sq * np.linalg.inv(A.T @ P @ A)\nprint('Variância a posteriori:', sigma0_sq)\nprint('Desvios-padrão:', np.sqrt(np.diag(Sigma_X)))"),
        md("## Exercícios\n\n1. Refaça o exemplo atribuindo menor peso à segunda observação.\n2. Escreva duas condições para o fechamento angular de um triângulo.\n3. Explique por que resíduos pequenos, isoladamente, não garantem um bom ajustamento."),
    ],
)

write(
    "02_ajustamento_com_injuncoes.ipynb",
    "Aula 2 — Ajustamento com Injunções",
    [
        "Interpretar injunções como informação adicional ou definição de datum.",
        "Formular o modelo combinado com injunções.",
        "Aplicar injunções ao modelo paramétrico e analisar seu efeito na solução.",
        "Preparar a 1ª VE prática.",
    ],
    [
        md("## 1. Por que usar injunções?\n\nInjunções fixam graus de liberdade, incorporam controles conhecidos ou impõem relações físicas. Podem ser **fortes** (valor fixo) ou **estocásticas** (pseudo-observações com incerteza)."),
        md("## 2. Modelo paramétrico com injunções\n\nPara $AX\\approx L$ e $CX=W$, o sistema de Lagrange é\n\n$$\\begin{bmatrix}A^TPA&C^T\\\\C&0\\end{bmatrix}\\begin{bmatrix}X\\\\K\\end{bmatrix}=\\begin{bmatrix}A^TPL\\\\W\\end{bmatrix}.$$"),
        code("import numpy as np\n\nA = np.array([[1., 0.], [0., 1.], [-1., 1.]])\nL = np.array([[100.2], [101.0], [0.9]])\nP = np.eye(3)\nC = np.array([[1., 0.]])\nW = np.array([[100.]])\nN, U = A.T @ P @ A, A.T @ P @ L\nM = np.block([[N, C.T], [C, np.zeros((1, 1))]])\nrhs = np.vstack([U, W])\nsolution = np.linalg.solve(M, rhs)\nprint('Parâmetros:', solution[:2].ravel())\nprint('Multiplicador:', solution[2:].ravel())"),
        md("## 3. Modelo combinado com injunções\n\nNo modelo implícito $F(L_a,X_a)=0$, as injunções entram como novas equações sobre $X_a$ ou sobre observações e parâmetros. A linearização deve manter separadas as derivadas em relação às observações e aos parâmetros."),
        md("## 4. Injunção forte × estocástica\n\nUma injunção forte elimina a variância na direção restringida. Uma injunção estocástica preserva a incerteza do controle e entra no ajustamento como observação ponderada. Sempre documente origem, unidade e precisão da informação."),
        md("## 1ª VE prática\n\n**Tarefa:** ajustar uma pequena rede com e sem injunções, comparar parâmetros, resíduos, matriz de covariância e condicionamento.\n\n**Entregáveis:** notebook executável, formulação matricial, resultados comentados e conclusão técnica."),
    ],
)

write(
    "03_deteccao_de_outliers.ipynb",
    "Aula 3 — Detecção de Outliers e Ajustamento Robusto",
    [
        "Aplicar data snooping e o teste de Baarda.",
        "Distinguir detecção, identificação e mitigação de outliers.",
        "Implementar um ajuste robusto e comparar as normas L1 e L2.",
        "Preparar a 2ª VE prática.",
    ],
    [
        md("## 1. Data snooping e teste de Baarda\n\nApós o teste global, analisam-se resíduos padronizados $w_i=v_i/\\sigma_{v_i}$. Valores incompatíveis com o nível de significância indicam observações a investigar; a remoção nunca deve ser automática ou apenas numérica."),
        code("import numpy as np\n\nx = np.arange(6, dtype=float)\ny = np.array([1.0, 2.1, 3.0, 8.2, 5.1, 6.0])\nA = np.column_stack([np.ones_like(x), x])\nX = np.linalg.lstsq(A, y, rcond=None)[0]\nv = A @ X - y\nH = A @ np.linalg.inv(A.T @ A) @ A.T\nqv = np.diag(np.eye(len(y)) - H)\ns0 = np.sqrt((v @ v) / (len(y) - A.shape[1]))\nw = v / (s0 * np.sqrt(qv))\nprint(np.column_stack([x, y, v, w]))"),
        md("## 2. Ajustamento robusto\n\nEstimadores robustos limitam a influência de resíduos grandes. No IRLS, uma sequência de MMQs reponderados aproxima perdas como Huber. A robustez reduz o efeito do outlier, mas não substitui sua investigação."),
        md("## 3. Normas L1 e L2\n\nA norma **L2** minimiza $\\sum v_i^2$, é eficiente sob erros gaussianos e sensível a extremos. A norma **L1** minimiza $\\sum|v_i|$, tolera melhor outliers e produz um problema de otimização não diferenciável na origem."),
        code("from scipy.optimize import linprog\n\n# Regressão L1: variáveis [b0, b1, u_1,...,u_m]\nm = len(y)\nc = np.r_[0., 0., np.ones(m)]\nAub = np.vstack([np.c_[A, -np.eye(m)], np.c_[-A, -np.eye(m)]])\nbub = np.r_[y, -y]\nsol = linprog(c, A_ub=Aub, b_ub=bub, bounds=[(None,None)]*2 + [(0,None)]*m)\nprint('L2:', X, 'L1:', sol.x[:2])"),
        md("## 2ª VE prática\n\n**Tarefa:** contaminar um conjunto de observações, aplicar teste global, Baarda, L2 e L1/Huber e comparar as soluções. **Entregáveis:** código, tabela de resíduos, gráfico comparativo e decisão técnica justificada."),
    ],
)

write(
    "04_series_temporais.ipynb",
    "Aula 4 — Séries Temporais",
    ["Decompor uma série em tendência, sazonalidade e ruído.", "Construir um modelo linear harmônico.", "Diagnosticar resíduos temporais e preparar a 3ª VE prática."],
    [
        md("## 1. Componentes\n\nUma série pode ser representada por $y_t=T_t+S_t+e_t$: tendência $T_t$, sazonalidade $S_t$ e ruído $e_t$. Em dados geodésicos, descontinuidades e correlação temporal exigem atenção especial."),
        code("import numpy as np\nimport matplotlib.pyplot as plt\n\nrng = np.random.default_rng(7)\nt = np.arange(60)\ny = 10 + 0.03*t + 0.8*np.sin(2*np.pi*t/12) + rng.normal(0, .2, len(t))\nA = np.column_stack([np.ones_like(t), t, np.sin(2*np.pi*t/12), np.cos(2*np.pi*t/12)])\nbeta = np.linalg.lstsq(A, y, rcond=None)[0]\ny_hat = A @ beta\nplt.plot(t, y, '.', label='observado'); plt.plot(t, y_hat, label='modelo'); plt.legend(); plt.grid();"),
        md("## 2. Modelagem\n\nA matriz de projeto reúne intercepto, tendência e termos harmônicos. Frequência, fase e amplitude devem ter interpretação física. Inspecione resíduos, autocorrelação, mudanças de regime e observações faltantes."),
        code("residuos = y_hat - y\nprint('Parâmetros:', beta)\nprint('RMSE:', np.sqrt(np.mean(residuos**2)))\nprint('Correlação lag 1:', np.corrcoef(residuos[:-1], residuos[1:])[0,1])"),
        md("## 3ª VE prática\n\nModelar uma série geodésica, separar tendência e sazonalidade, avaliar resíduos e interpretar a taxa estimada. Entregar notebook, gráfico, parâmetros com unidades e discussão de limitações."),
    ],
)

write(
    "05_regularizacao.ipynb",
    "Aula 5 — Regularização de Problemas Inversos",
    ["Reconhecer problemas mal condicionados.", "Aplicar TSVD e regularização de Tikhonov.", "Comparar viés, variância e estabilidade e preparar a 4ª VE prática."],
    [
        md("## 1. Problemas mal postos\n\nValores singulares pequenos amplificam o ruído. A regularização troca parte da resolução por estabilidade, incorporando um corte espectral ou uma preferência sobre a solução."),
        md("## 2. TSVD\n\nSe $A=U\\Sigma V^T$, o TSVD mantém apenas $k$ valores singulares: $x_k=V_k\\Sigma_k^{-1}U_k^TL$."),
        code("import numpy as np\n\nA = np.array([[1., .99], [.99, .9802], [1.01, 1.]])\nL = np.array([2.01, 1.98, 2.02])\nU, s, Vt = np.linalg.svd(A, full_matrices=False)\nfor k in (1, 2):\n    x_tsvd = Vt[:k].T @ ((U[:, :k].T @ L) / s[:k])\n    print('k=', k, 'x=', x_tsvd)"),
        md("## 3. Tikhonov\n\nA solução $x_\\lambda=(A^TA+\\lambda^2R^TR)^{-1}A^TL$ penaliza soluções incompatíveis com $R$. O parâmetro $\\lambda$ controla o compromisso entre ajuste e estabilidade."),
        code("for lam in (0., .01, .1, 1.):\n    x = np.linalg.solve(A.T@A + lam**2*np.eye(2), A.T@L)\n    print(f'lambda={lam:>4}: x={x}, ||v||={np.linalg.norm(A@x-L):.4f}')"),
        md("## 4ª VE prática\n\nResolver um problema inverso sintético por solução direta, TSVD e Tikhonov; justificar $k$ e $\\lambda$ por diagnóstico gráfico ou validação e discutir estabilidade."),
    ],
)

write(
    "06_otimizacao.ipynb",
    "Aula 6 — Otimização",
    ["Formular função objetivo e função de custo.", "Comparar métodos diretos e métodos de gradiente.", "Implementar otimização em lotes e mini-batches e preparar a 5ª VE prática."],
    [
        md("## 1. Função objetivo e custo\n\nA função objetivo expressa matematicamente o problema; em estimação, a função de custo mede o desacordo entre modelo e dados. No MMQ, $J(X)=\\frac12\\|AX-L\\|_P^2$."),
        md("## 2. Métodos diretos e de gradiente\n\nMétodos diretos não exigem derivadas e são úteis com funções irregulares ou poucas variáveis. Métodos de gradiente exploram $\\nabla J$ e escalam melhor, mas dependem do passo e do condicionamento."),
        code("import numpy as np\n\nA = np.array([[1.,0.],[1.,1.],[1.,2.],[1.,3.]])\nL = np.array([1.,2.,2.8,4.2])\nx = np.zeros(2)\neta = 0.05\nfor _ in range(200):\n    grad = A.T @ (A @ x - L) / len(L)\n    x -= eta * grad\nprint('Gradiente:', x)\nprint('Solução direta:', np.linalg.lstsq(A, L, rcond=None)[0])"),
        md("## 3. Lotes, mini-batches e épocas\n\nNo *batch gradient descent*, todo o conjunto compõe o gradiente. No método estocástico ou por mini-batches, atualizações mais frequentes reduzem custo por passo e introduzem variabilidade. Em todos os casos, embaralhamento e reprodutibilidade devem ser controlados."),
        md("## 5ª VE prática\n\nComparar solução direta, método sem derivadas e gradiente em um mesmo problema. Relatar custo por iteração, critério de parada, sensibilidade ao passo e resultado final."),
    ],
)

write(
    "07_avaliacao_escrita.ipynb",
    "Aula 7 — Avaliação Escrita (6ª VE)",
    ["Integrar os conceitos das Aulas 1 a 6.", "Formular modelos e interpretar resultados sem depender de código.", "Demonstrar domínio de hipóteses, diagnóstico e escolha de métodos."],
    [
        md("## Conteúdo avaliado\n\n1. MMQ e modelos paramétrico, condicionado e combinado.\n2. Injunções e datum.\n3. Outliers, Baarda, L1 e L2.\n4. Séries temporais.\n5. TSVD e Tikhonov.\n6. Otimização direta, por gradiente e em lotes."),
        md("## Orientações\n\nJustifique todas as escolhas, apresente unidades, identifique dimensões das matrizes e interprete os resultados. Respostas exclusivamente algébricas, sem conexão com o problema, serão consideradas incompletas."),
        md("## Roteiro de revisão\n\n- Quando uma matriz normal se torna singular?\n- Como uma injunção altera a solução e sua precisão?\n- Qual a diferença entre detectar e remover um outlier?\n- Como escolher a complexidade de um modelo temporal?\n- Por que regularizar?\n- Como condicionamento e taxa de aprendizagem se relacionam?"),
    ],
)


case_studies = [
    (8, "Rede de Nivelamento com Injunções", ["Formular e ajustar uma rede altimétrica.", "Comparar injunções fortes e estocásticas.", "Quantificar precisão e confiabilidade."], "Uma rede de nivelamento com ao menos cinco pontos, dois controles e observações redundantes.", "Modelo matricial, coordenadas ajustadas, resíduos, covariâncias e análise do datum."),
    (9, "Controle de Qualidade e Outliers em Rede", ["Aplicar teste global e data snooping.", "Comparar L2 e ajuste robusto.", "Justificar a decisão sobre observações suspeitas."], "Uma rede ou regressão geodésica contendo erros aleatórios e ao menos um outlier controlado.", "Tabela de testes, gráficos de resíduos, soluções comparadas e decisão técnica."),
    (10, "Série Temporal de Monitoramento", ["Estimar tendência e sazonalidade.", "Detectar descontinuidades ou valores anômalos.", "Interpretar taxas e incertezas."], "Série temporal GNSS, de recalque ou de deslocamento estrutural.", "Modelo temporal, diagnóstico dos resíduos, visualização e interpretação física."),
    (11, "Inversão Regularizada", ["Diagnosticar condicionamento.", "Aplicar TSVD e Tikhonov.", "Selecionar hiperparâmetros com critério explícito."], "Problema inverso de reconstrução, transformação ou estimação com matriz mal condicionada.", "Espectro singular, soluções regularizadas, curva de compromisso e análise de sensibilidade."),
    (12, "Projeto Integrador e Defesa Oral", ["Integrar modelagem, controle de qualidade e otimização.", "Produzir uma solução reproduzível.", "Defender escolhas e limitações na 7ª VE oral."], "Problema de Engenharia Cartográfica escolhido pela equipe e aprovado pelo docente.", "Notebook final, apresentação curta, dados e referências, resultados validados e defesa oral."),
]

for number, title, objectives, problem, deliverables in case_studies:
    filename = f"{number:02d}_estudo_de_caso_{number - 7}.ipynb"
    write(
        filename,
        f"Aula {number} — Estudo de Caso {number - 7}: {title}",
        objectives,
        [
            md(f"## Problema\n\n{problem}"),
            md("## Etapas sugeridas\n\n1. Definir hipótese, observações, parâmetros e unidades.\n2. Fazer análise exploratória e controle de qualidade.\n3. Implementar e validar o método.\n4. Comparar alternativas ou cenários.\n5. Comunicar conclusão, limitações e próximos passos."),
            md(f"## Entregáveis\n\n{deliverables}"),
            md("## Critérios da 7ª VE oral\n\n- Correção da formulação e da implementação.\n- Rastreabilidade e reprodutibilidade.\n- Qualidade das verificações e da interpretação.\n- Clareza da apresentação e domínio na arguição."),
            code("# Espaço inicial para parâmetros, importações e dados do estudo de caso.\nfrom pathlib import Path\nimport numpy as np\nimport matplotlib.pyplot as plt\n\nRNG = np.random.default_rng(2027)"),
        ],
    )


for obsolete in (
    "02_deteccao_erros_grosseiros.ipynb",
    "03_estimadores_robustos.ipynb",
    "04_filtragem_sequencial.ipynb",
    "05_redes_geodesicas.ipynb",
):
    path = ROOT / obsolete
    if path.exists():
        path.unlink()

print("Notebooks das Aulas 1–12 gerados com sucesso.")
