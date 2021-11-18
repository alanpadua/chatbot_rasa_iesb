from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset

import datetime
import re

class ClearSlots(Action):

    def name(self) -> Text:
        return "action_clear_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # limpa slots do fazerpedido
        return [AllSlotsReset()]


class Submitfazerpedido(Action):

    def name(self) -> Text:
        return "action_submit_fazerpedido"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # recebe dados dos slots
        pedido = tracker.get_slot('pedido')
        endereco = tracker.get_slot('endereco')
        data = tracker.get_slot('data')
        valor = tracker.get_slot('valor')
        formapagamento = tracker.get_slot('formapagamento')

        d = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f%z')
        convert_data = d.strftime('%d/%m/%Y às %H:%M')
        # executa alguma coisa com os dados

        pedido, valor = self.somar_valores(pedido)

        pedido_formatado = ''
        for item in pedido: pedido_formatado += '\n - ' + item

        # limpa slots do fazerpedido
        return [
            # SlotSet('resultado_pedido', pedido),
            SlotSet('resultado_pedido', pedido_formatado),
            SlotSet('resultado_data', convert_data),
            SlotSet('resultado_endereco', endereco),
			SlotSet('resultado_valor', valor),
            SlotSet('resultado_formapagamento', formapagamento),
            SlotSet('pedido', None),
            SlotSet('data', None),
            SlotSet('endereco', None),
			SlotSet('valor', None),
            SlotSet('formapagamento', None)
        ]

    def somar_valores(self, pedido:str):
        pedido_formatado = ''
        valor_total = 5.0

        itens_pedido = re.split("; |, |\*|\n|e ", pedido)
        # print(len(pedido_formatado))

        for item in itens_pedido:
            if item == 'jantinha':
                valor_total += 14.0
            else:
                valor_total += 7.0
        
        return itens_pedido, valor_total

