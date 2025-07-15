# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Callable

from digitalhub.entities._commons.enums import EntityTypes
from digitalhub.entities.artifact.crud import get_artifact
from digitalhub.entities.dataitem.crud import get_dataitem
from digitalhub.entities.model.crud import get_model


def get_getter_for_material(entity_type: str) -> Callable:
    """
    Return appropriate getter function.

    Parameters
    ----------
    entity_type : str
        The entity type.

    Returns
    -------
    Callable
        The getter function.
    """
    if entity_type == EntityTypes.ARTIFACT.value:
        return get_artifact

    if entity_type == EntityTypes.DATAITEM.value:
        return get_dataitem

    if entity_type == EntityTypes.MODEL.value:
        return get_model

    raise ValueError(f"Unhandled entity type: {entity_type}")
