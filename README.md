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

