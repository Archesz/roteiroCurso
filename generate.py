import streamlit as st

disciplinas_dict = {
    "Matemática": {
        "Conhecimentos Numéricos": [
            "Operações com Números Naturais",
            "Operações com Números Inteiros",
            "Expressões Numéricas",
            "Frações, Decimais e Dízimas",
            "Potenciação e Radiciação",
            "Notação Científica",
            "Operações Básicas ",
            "Teoria dos Conjuntos",
            "Conjuntos Numéricos",
            "Intervalos Reais",
            "Divisibilidade e Fatoração",
            "Regra de Três",
            "Revisão",
        ],
        "Geometria": [
            "Grandezas e Unidades de Medida",
            "Ângulos",
            "Triângulos",
            "Quadriláteros Notáveis",
            "Polígonos Regulares",
            "Círculo e Circunferência",
            "Teorema de Tales",
            "Congruência e Semelhança de Triângulos",
            "Trigonometria no Triângulo Retângulo",
            "Posições de Retas e Planos no Espaço",
            "Poliedros",
            "Prismas",
            "Pirâmides",
            "Cilindros",
            "Cones",
            "Esferas",
            "Troncos de Pirâmides e de Cones",
            "Simestrias",
            "Revisão",
        ],
        "Álgebra": [
            "Equação do 1º Grau",
            "Equação do 2º Grau",
            "Sistemas de Equações",
            "Gráficos",
            "Equações Irracionais",
            "Funções do 1º Grau",
            "Funções do 2º Grau",
            "Binômio de Newton",
            "Função Exponencial",
            "Função Modular",
            "Lógica",
            "Inequação do 1º Grau",
            "Inequação do 2º Grau",
            "Logaritmo",
            "Funções Logarítmicas",
            "Funções Polinomiais",
            "Equações Trigonométricas",
            "Inequações Trigonométricas",
            "Sistemas Lineares",
            "Matrizes (Opcional)",
            "Progressão Aritmética",
            "Progressão Geométrica"
        ],
        "Estatística": [
            "Análise Combinatória",
            "Noções de Probabilidade",
            "Representação e Análise de Dados",
            "Interpretação de Gráficos"
        ]
    },
    "Física": {
        "Fundamentos": [
            "Ordem de Grandeza",
            "Sistema Internacional de Unidades (SI)",
            "Vetores"
        ],
        "Mecânica - Cinemática": [
            "Fundamentos da Cinemática",
            "Movimento Uniforme",
            "Movimento Uniformemente Variado",
            "Movimento Circular Uniforme",
            "Cinemática Vetorial",
            "Lançamentos de Projéteis"
        ],
        "Mecânica - Dinâmica": [
            "Introdução à Dinâmica",
            "Leis de Newton",
            "Principais Forças da Mecânica",
            "Força de Atrito",
            "Dinâmica do Movimento Circular"
        ],
        "Mecânica - Energia e Impulso": [
            "Trabalho",
            "Energia Cinética",
            "Energia Potencial Gravitacional e Elástica",
            "Sistemas Conservativos",
            "Impulso, Quantidade de Movimento e Colisões"
        ],
        "Mecânica - Outros": [
            "Estatíca",
            "Hidrostática",
            "Gravitação"
        ],
        "Fenômenos Elétricos e Magnéticos": [
            "Eletrostática",
            "Eletrodinâmica: Corrente, Potência e Resistores",
            "Eletrodinâmica: Capacitores",
            "Eletromagnetismo: Campo Magnético",
            "Eletromagnetismo: Força e Induçã"
        ],
        "Termodinâmica": [
            "Termometria",
            "Calorimetria",
            "Propagação do Calor",
            "Dilatação Térmica",
            "Leis da Termodinâmica"
        ],
        "Óptica": [
            "Óptica Geométrica", "Reflexão e Espelhos Planos", "Espelhos Esféricos", "Refração", "Lentes Esféricas"
        ],
        "Oscilações e Ondas": ["Movimento Harmônica Simples", "Ondas", "Reflexão, Refração e Difração", "Ressonância, Polarização e Efeito Doppler", "Interferência", "Acústica", "Radiação"],
        "Relatividade": ["Dilatação do Tempo", "Contração do Espaço"]
    },
    "Biologia": {
        "Citologia": [
            "Célula",
            "Envoltórios Celulares",
            "Citoplasma",
            "Estudo do Núcleo",
            "Ciclo Celular e Divisão Celular"
        ],
        "Bioenergética": [
            "Aspectos Gerais do Metabolismo Celular",
            "Fermentação e Respiração Celular",
            "Fotossíntese e Quimiossíntese"
        ],
        "Histologia Animal e Humana": [
            "Tecido Epitelial", "Tecido Conjutivo", "Tecido Muscular", "Tecido Nervoso",
        ],
        "Fisiologia": [
            "Introdução a Fisiologia", "Sistema Digestório", "Sistema Respiratórios", "Sistemas Cardiovascular ou Circulatório", "Sistema Imunológico", "Sistema Excretor", "Sistema Nervoso", "Sistema Tegumentar", "Sistema Motor", "Sistema Sensorial", "Sistema Endócrino", "Sistema Reprodutor", "Nutrição"            
        ],
        "Classificação": [
            "Níveis de Organização dos Seres Vivos", "Classificação dos Seres Vivos", "Vírus e Príons", "Reino Monera: Bactéricas", "Reino Protoctista: Algas e Protozoários", "Reino Fungi"
        ],
        "Zoologia": [
            "Poríferos", "Cnidários", "Platelmintos", "Nematelmintos", "Moluscos", "Anelídeos", "Artrópodes", "Equinodermos", "Cordados"
        ],
        "Botânica": [
            "Briófitas", "Pteridófitas", "Gimnospermas", "Angiosperma", "Tecidos Vegetais", "Nutrição Vegetal", "Transporte Vegetal", "Fotoperiodismo", "Germinação"
        ],
        "Genética": [
            "Herança", "Concepções Pré-Mendelianas", "Leis de Mendel", "Polialelia", "Herança e Sexo", "Linkage", "Interação Gênica", "Citogenética", "Genética de Populações"
        ],
        "Origem da Vida": [
            "Explicações Pré-Darwinistas", "Origem da vida", "Evolução", "Teoria Sintética da Evolução"
        ],
        "Ecologia": [
            "Conceitos Básicos da Ecologia", "Comunidade Biológica", "Matéria e Energia no Ecossistema", "Dinâmica das Populações", "Biomas Terrestres", "Impactos e Problemas Ambientais"
        ]
    },
    "Química": {
        "Materiais": [
            "Propriedades dos Materiais", "Substâncias e Misturas", "Separação de Misturas"
        ],
        "Transformações Químicas": [
            "Evolução dos modelos atômicos", "Atomística", "Eletrosfera", "Tabela Periódica", "Átomo", "Ligações Químicas", "Estrutura e Propriedade", "Propriedades Periódicas"
        ],
        "Água": [
            "Funções Inorgânicas", "Química Descritiva", "Grandezas Química", "Sistemas Aquosos", "Cálculo de Concentração", "Mistura de Soluções"
        ],
        "Representações das Transformações": [
            "Reações Inorgânicas", "Fórmulas Químicas", "Estudo dos Gases", "Cálculo Estequiométricos", "Poluição", "Teoria Atômico Molecular"
        ],
        "Transformações Químicas e Energia": [
            "Termoquímica", "Eletroquímica", "Pilhas Eletroquímicas", "Eletrólise", "Transformações Nucleares", "Radioatividade"
        ],
        "Dinâmica e Equilíbrio": [
            "Cinética Química", "Equilíbrio Químico"
        ],
        "Compostos de Carbono": [
            "Introdução", "Hibrocarbonetos", "Compostos Orgânicos Oxigenados", "Funções Orgânicas Nitrogenadas", "Caracteristicas dos Compostos Orgânicos",
            "Isomeria Plana", "Isomeria Espacial", "Reações de Substituição", "Reações de Adição", "Reações de Eliminação", "Reações Orgânicas de Oxidação",
            "Esterificação e Hidrólise", "Polímeros", "Biomoléculas"
        ]
    },
    "Geografia": {
        "Representações": ["Astronomia", "Cartografia"],
        "Natureza": ["Geosfera", "Atmosfera", "Hidrosfera", "Biosfera", "Recursos Minerais", "Energia", "Políticas e Desafios Ambientais"],
        "Estruturas Produtivas": ["Indústria", "Agropecuária", "Comércio", "Transporte"],
        "Organizações e Movimentos": ["Urbanização", "População", "Migrações", "Capitalismo e Globalização", "Órgão Internacionais", "Blocos Supranacionais", "Brasil no Mundo", "EUA", "Israel x Palestina", "Primavera Árabe", "China", "Tensões nas Coreias"],
        "Regionalização": ["Amazônia e Região Norte", "Região Nordeste", "Região Centro-Oeste", "Região Sudeste", "Região Sul", "América Central e Caribe", "EUA", "África", "Europa", "China"]
    },
    "História": {
        "Geral": ["Pré-História", "Linha do Tempo", "Contagem do Tempo"],
        "Idade Antiga": ["Antiguidade Oriental", "Antiguidade Clássica - Grécia", "Antiguidade Clássica - Roma"],
        "Idade Média": ["Império Bizantino", "Reinos Bárbaros", "Império dos Francos", "Civilização Islâmica", "Feudalismo", "Cruzadas", "Crise do Século XIV", "Monarquias Nacionais", "Igreja Medieval"],
        "Idade Moderna": ["Renascimento Cultural", "Reforma Protestante", "Absolutismo", "Mercantilismo", "Expansão Marítima", "Civilizações Pré-Colombianas", "Colonização Espanhola na América", "Colonização Inglesa na América", "Expansão e Colonização Francesa", "Expansão e Colonização Holandesa", "Iluminismo", "Revolução Inglesa do Século XVII", "Revolução Industrial", "EUA - Independência"],
        "Idade Contemporânea": ["Revolução Francesa", "Era Napoleônica", "Independência do Haiti", "Congresso de Viena", "EUA - Expansão Territorial", "Independência da América Espanhola", "Unificações", "Segunda Revolução Industrial", "Neocolonialismo", "1ª Guerra Mundial", "Revolução Russa", "Guerra Fria", "2ª Guerra Mundial", "Revolução Chinesa"],
        "História do Brasil - Brasil Colônia": ["Povos Indígenas", "Período Pré-colonial", "Colonização", "Economia Açucareira", "Pecuária", "Expansão Territorial", "A Família Real Portuguesa no Brasil", "Independência do Brasil", "Movimentos Emancipacionistas"],
        "História do Brasil - Império": ["Primeiro Reinado", "Período Regencial","Segundo Reinado", "Expansão Cafeeira"],
        "História do Brasil - República": ["República da Espada", "República das Oligarquias", "Economia na República das Oligarquias", "Era Vargas", "Governo Dutra", "Segundo Governo Vargas", "Governo JK"]
    },
    "Gramática": {
        "Interpretação": ["Modos de Organização", "Interpretação das Esferas Sociais", "Estudos dos Gêneros Digitais", "Funções da Linguagem", "Relação entre textos"],
        "Aspectos Linguísticos": ["Substantivo", "Artigo", "Adjetivo", "Numeral", "Verbos", "Advérbio", "Pronomes", "Conectivos", "Pontuações", "Interjeição", "Regência", "Formação de palavras", "Sujeito e predicado", "Concordância Verbal", "Concordância Nominal"], 
        "Orações": ["Orações", "Orações Subordinadas Substantivas", "Orações Subordinadas Adjetivas", "Orações Subordinadas Adverbiais", "Orações Subordinadas Reduzidas", "Orações Coordenadas"]
    },
    "Literatura": {
        "Teoria": ["Literatura e Processo Social", "Gêneros Literários", "História Literária"],
        "Escola Literárias": ["Trovadorismo", "Humanismo", "Renascimento", "Quinhentismo", "Barroco", "Arcadismo", "Romantismo", "Realismo e Naturalismo", "Parnasianismo", "Simbolismo", "Pré-modernismo"]
    },
    "Sociologia": {
        "Natureza": ["Sociedade", "O que é o homem?", "Natureza e Cultura", "Conhecimento o Brasil", "As Desigualdades"],
        "Diversidade Cultural": ["Antropologia", "Cara do Brasil", "Religião no Brasil", "Tribos Urbanas", "Consumo", "Violência"],
        "Movimentos Sociais": ["Modernidade", "Instituições Sociais", "O estado", "Democracia", "Max Weber", "Poder da Política", "Direito Humano", "Movimentos Sociais"],
        "Estruturas Produtivas": ["Karl Marx", "Trabalho", "Produção e Dominação", "Émile Durkheim", "Trabalhadores do Brasil", "Georg Simmel", "Mídia e Tecnologia", "Sociólogos Contemporâneos"]
    }
}


def getAssuntos(disciplina):
    areas = disciplinas_dict[disciplina].keys()
    all_assuntos = []
    for area in areas:
        all_assuntos.append(list(disciplinas_dict[disciplina][area]))

    return all_assuntos, list(areas)


def generate(disciplinas):

    for disciplina in disciplinas:
        st.subheader(disciplina)
        try:
            assuntos, areas = getAssuntos(disciplina)

            for i in range(0, len(areas)):
                st.markdown(f"#### {areas[i]}")
                for a in assuntos[i]:
                    st.markdown(f"- [ ] {a}")

        except:
            continue

        st.divider()

def header(area):
    if area == "Exatas e Tecnologia":
        
        st.write(f"""
                 Disciplinas Prioritárias: 
                 1. Matemática.
                 2. Física.
                 3. Química.
                 4. Lingua Portuguesa e Literatura.
                 5. Humanidades.
                 """)

    elif area == "Artes e Humanidades":
        st.write(f"""
                 Disciplinas Prioritárias: 
                 1. História.
                 2. Matemática.
                 3. Geografia.
                 4. Lingua Portuguesa e Literatura.
                 5. Filosofia e Sociologia.
                 """)

    elif area == "Biológicas e Saúde":
        st.write(f"""
                 Disciplinas Prioritárias: 
                 1. Biologia.
                 2. Matemática.
                 3. Química.
                 4. Lingua Portuguesa.
                 5. Humanidades.
                 """)
