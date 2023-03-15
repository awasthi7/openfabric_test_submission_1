import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here

    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    #import ChatterBot as cb
    from chatterbot import ChatBot
    from chatterbot.trainers import ChatterBotCorpusTrainer
    cb = ChatBot('openfabric_science_bot')
    trainer = ChatterBotCorpusTrainer(cb)
    trainer.train("chatterbot.corpus.english.science")
    for text in request.text:
        # TODO Add code here
    #x=request.text
     response = cb.get_response(text)
     output.append(response)

    return SimpleText(dict(text=output))
