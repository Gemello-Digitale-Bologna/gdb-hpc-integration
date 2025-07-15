# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0
from digitalhub_runtime_hpcdl.entities._commons.enums import EntityKinds
from digitalhub_runtime_hpcdl.entities.function.hpcdl.builder import FunctionHPCDLBuilder
from digitalhub_runtime_hpcdl.entities.run.hpcdl_run.builder import RunHPCDLRunBuilder
from digitalhub_runtime_hpcdl.entities.task.hpcdl_job.builder import TaskHPCDLJobBuilder

entity_builders = (
    (EntityKinds.FUNCTION_HPCDL.value, FunctionHPCDLBuilder),
    (EntityKinds.RUN_HPCDL.value, RunHPCDLRunBuilder),
    (EntityKinds.TASK_HPCDL_JOB.value, TaskHPCDLTransformBuilder),
)

try:
    from digitalhub_runtime_hpcdl.runtimes.builder import RuntimeHPCDLBuilder

    runtime_builders = ((kind, RuntimeHPCDLBuilder) for kind in [e.value for e in EntityKinds])
except ImportError:
    runtime_builders = tuple()
