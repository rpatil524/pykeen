# -*- coding: utf-8 -*-
from kg_embeddings_model.conv_e import ConvE
from kg_embeddings_model.trans_d import TransD
from kg_embeddings_model.trans_e import TransE
from kg_embeddings_model.trans_h import TransH
from kg_embeddings_model.trans_r import TransR
from utilities.constants import TRANS_E, TRANS_H, KG_EMBEDDING_MODEL, TRANS_D, TRANS_R, CONV_E


def get_kg_embedding_model(config):
    """

    :param config:
    :return:
    """
    model_name = config[KG_EMBEDDING_MODEL]

    if model_name == TRANS_E:
        return TransE(config=config)
    if model_name == TRANS_H:
        return TransH(config=config)
    if model_name == TRANS_D:
        return TransD(config=config)
    if model_name == TRANS_R:
        return TransR(config=config)
    if model_name == CONV_E:
        return ConvE(config=config)


