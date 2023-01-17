from .adaptor import Adaptor
from .berts import RobertaAdaptor, AlbertAdaptor

ADAPTORS = {
    'ALBERT': AlbertAdaptor(),
    'ROBERTA': RobertaAdaptor(),

}

def get_adaptor(model_type:str) -> Adaptor:
    return ADAPTORS[model_type] if model_type in ADAPTORS else Adaptor()
