#!/usr/bin/env bash

echo 'iniciando.....'
# cd chatbot_rasa/

# echo 'Conda habilitando ambiente.'
# conda info --envs
# conda activate py38env

echo 'Treinando o Rasa........'
rasa train 

echo 'Iniciando o duckling........'
gnome-terminal -- docker run -p 8000:8000 rasa/duckling &
#docker run -p 8000:8000 rasa/duckling &

echo 'Iniciando o Rasa action.....'
gnome-terminal -- rasa run actions &
#rasa run actions &

echo 'Iniciando o Rasa Shell.....'
# RASA_TELEMETRY_DEBUG=true rasa shell 
rasa shell 

echo 'Parando a imagem docker do Duckling.....'
docker ps -q --filter ancestor=rasa/duckling
docker stop $(docker ps -q --filter ancestor=rasa/duckling)
docker rm $(docker ps -aq --filter ancestor=rasa/duckling)

echo 'Parando o Rasa run actions.....'
ps -ef | grep "rasa run actions"
kill -9 $(ps -ef | grep "rasa run actions" | awk '{print $2}')


echo 'Serviços finalizados!'