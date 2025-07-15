# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities._commons.enums import Relationship
from digitalhub.entities._commons.utils import get_entity_type_from_key
from digitalhub.entities.run._base.entity import Run
from digitalhub.factory.factory import factory

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata
    from digitalhub.entities._base.material.entity import MaterialEntity

    from digitalhub_runtime_hpcdl.entities.run.hpcdl_run.spec import RunSpecHPCDLRun
    from digitalhub_runtime_hpcdl.entities.run.hpcdl_run.status import RunStatusHPCDLRun


class RunHPCDLRun(Run):
    """
    RunHPCDLRun class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: RunSpecHPCDLRun,
        status: RunStatusHPCDLRun,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: RunSpecHPCDLRun
        self.status: RunStatusHPCDLRun

    def _setup_execution(self) -> None:
        """
        Setup run execution.

        Returns
        -------
        None
        """
        self.refresh()
        self.save(update=True)