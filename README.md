# Montando o Ambiente

## Install Rasa
    https://rasa.com/docs/rasa/installation/

**Ambiente:**

	conda create --name py38env python==3.8
	conda activate py38env
	
	conda install ujson
	conda install tensorflow
	
	pip install rasa --use-deprecated=legacy-resolver
	<!-- pip install rasa --no-deps -->


    
**Dependências do Rasa:**

    pip install -U spacy
    python -m spacy download en_core_web_sm
    python -m spacy download en_core_web_md
    pip install -U pip setuptools wheel
    python -m spacy download pt_core_news_md

**Conda INFO:**

	conda activate py38env
	conda info --envs
    
    <!-- conda deactivate -->

**Remove env conda:**
    
	conda env remove -n [enviroment]

**Iniciar o projeto**

	./iniciar.sh


# Trabalho 2 - Rasa Framework

Objetivo: Criar um chatbot utilizando o Rasa Framework com as mesmas características do primeiro trabalho.


### Requisitos:

- Estrutura básica: Saudação, Finalização, Ação, Outras perguntas (opcional) 5 pts
- Executar ao menos uma ação customizada dentro de um fluxo de formulário que conecte em um serviço externo (usando requests do python) 5 pts


**Requisito obrigatório:** a pipeline deve ser configurada permitindo o treinamento do chatbot em português. Não será cobrado excelência na configuração e treinamento, mas o treinamento deve ser suficiente para que os fluxos de diálogo sejam executados.


Não é necessário integrar com nenhum mensageiro de frontend, apenas entregar o projeto do Rasa Framework


**Entrega:**

Enviar a pasta do projeto do Rasa Framework sem os arquivos de modelo. Para entregar, apague os arquivos da pasta model, compacte e envie. Se desejar, podem versionar os arquivos no GitHub.