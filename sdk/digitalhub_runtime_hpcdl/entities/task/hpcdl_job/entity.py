# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import typing

from digitalhub.entities.task._base.entity import Task

if typing.TYPE_CHECKING:
    from digitalhub.entities._base.entity.metadata import Metadata

    from digitalhub_runtime_hpcdl.entities.task.hpcdl_job.spec import TaskSpecHPCDLJob
    from digitalhub_runtime_hpcdl.entities.task.hpcdl_job.status import TaskStatusHPCDLJob


class TaskHPCDLJob(Task):
    """
    TaskHPCDLJob class.
    """

    def __init__(
        self,
        project: str,
        uuid: str,
        kind: str,
        metadata: Metadata,
        spec: TaskSpecHPCDLJob,
        status: TaskStatusHPCDLJob,
        user: str | None = None,
    ) -> None:
        super().__init__(project, uuid, kind, metadata, spec, status, user)

        self.spec: TaskSpecHPCDLJob
        self.status: TaskStatusHPCDLJob
