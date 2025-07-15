# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.task._base.builder import TaskBuilder

from digitalhub_runtime_hpcdl.entities._base.runtime_entity.builder import RuntimeEntityBuilderHPCDL
from digitalhub_runtime_hpcdl.entities._commons.enums import EntityKinds
from digitalhub_runtime_hpcdl.entities.task.hpcdl_job.entity import TaskHPCDLJob
from digitalhub_runtime_hpcdl.entities.task.hpcdl_job.spec import TaskSpecHPCDLJob, TaskValidatorHPCDLJob
from digitalhub_runtime_hpcdl.entities.task.hpcdl_job.status import TaskStatusHPCDLJob


class TaskHCPDLJobBuilder(TaskBuilder, RuntimeEntityBuilderHPCDL):
    """
    TaskHCPDLJobBuilder transformer.
    """

    ENTITY_CLASS = TaskHPCDLJob
    ENTITY_SPEC_CLASS = TaskSpecHPCDLJob
    ENTITY_SPEC_VALIDATOR = TaskValidatorHPCDLJob
    ENTITY_STATUS_CLASS = TaskStatusHPCDLJob
    ENTITY_KIND = EntityKinds.TASK_HPCDL_JOB.value
