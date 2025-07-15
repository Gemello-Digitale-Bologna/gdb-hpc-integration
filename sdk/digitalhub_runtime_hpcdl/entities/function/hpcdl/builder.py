# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.builder import FunctionBuilder

from digitalhub_runtime_hpcdl.entities._base.runtime_entity.builder import RuntimeEntityBuilderHPCDL
from digitalhub_runtime_hpcdl.entities._commons.enums import EntityKinds
from digitalhub_runtime_hpcdl.entities.function.hpcdl.entity import FunctionHPCDL
from digitalhub_runtime_hpcdl.entities.function.hpcdl.spec import FunctionSpecHPCDL, FunctionValidatorHPCDL
from digitalhub_runtime_hpcdl.entities.function.hpcdl.status import FunctionStatusHPCDL


class FunctionHPCDLBuilder(FunctionBuilder, RuntimeEntityBuilderHPCDL):
    """
    FunctionHPCDL builder.
    """

    ENTITY_CLASS = FunctionHPCDL
    ENTITY_SPEC_CLASS = FunctionSpecHPCDL
    ENTITY_SPEC_VALIDATOR = FunctionValidatorHPCDL
    ENTITY_STATUS_CLASS = FunctionStatusHPCDL
    ENTITY_KIND = EntityKinds.FUNCTION_HPCDL.value

    def build(
        self,
        kind: str,
        project: str,
        name: str,
        uuid: str | None = None,
        description: str | None = None,
        labels: list[str] | None = None,
        embedded: bool = False,
        **kwargs,
    ) -> FunctionHPCDL:
        obj = super().build(
            kind,
            project,
            name,
            uuid,
            description,
            labels,
            embedded,
            **kwargs,
        )
        return obj

    def from_dict(self, obj: dict, validate: bool = True) -> FunctionHPCDL:
        """
        Create a new object from dictionary.

        Parameters
        ----------
        obj : dict
            Dictionary to create object from.
        validate : bool
            Flag to indicate if arguments must be validated.

        Returns
        -------
        FunctionHPCDL
            Object instance.
        """
        entity = super().from_dict(obj, validate=validate)
        return entity

    def _parse_dict(self, obj: dict, validate: bool = True) -> dict:
        """
        Get dictionary and parse it to a valid entity dictionary.

        Parameters
        ----------
        entity : str
            Entity type.
        obj : dict
            Dictionary to parse.

        Returns
        -------
        dict
            A dictionary containing the attributes of the entity instance.
        """
        return super()._parse_dict(obj, validate=validate)
