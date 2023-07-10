import torch

from .huggingface import Huggingface

class MPTDolphin(Huggingface):
    def __init__(self, model_path, **kwargs):
        super().__init__(
            model_path,
            user='<human>: ',
            assistant='<bot>:',
            system='<system>: ',
            default_system='You are a helpful assistant',
            end='\n\n',
            **kwargs,
        )
