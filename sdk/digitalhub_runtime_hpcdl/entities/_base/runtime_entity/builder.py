# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities._base.runtime_entity.builder import RuntimeEntityBuilder
from digitalhub.entities.task._base.utils import build_task_actions

from digitalhub_runtime_hpcdl.entities._commons.enums import EntityKinds, TaskActions


class RuntimeEntityBuilderHPCDL(RuntimeEntityBuilder):
    EXECUTABLE_KIND = EntityKinds.FUNCTION_HPCDL.value
    TASKS_KINDS = build_task_actions(
        [
            (
                EntityKinds.TASK_HPCDL_JOB.value,
                TaskActions.JOB.value,
            )
        ]
    )
    RUN_KIND = EntityKinds.RUN_HPCDL.value
