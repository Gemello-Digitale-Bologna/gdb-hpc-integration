# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.builder import RunBuilder

from digitalhub_runtime_hpcdl.entities._base.runtime_entity.builder import RuntimeEntityBuilderHPCDL
from digitalhub_runtime_hpcdl.entities._commons.enums import EntityKinds
from digitalhub_runtime_hpcdl.entities.run.hpcdl_run.entity import RunHPCDLRun
from digitalhub_runtime_hpcdl.entities.run.hpcdl_run.spec import RunSpecHPCDLRun, RunValidatorHPCDLRun
from digitalhub_runtime_hpcdl.entities.run.hpcdl_run.status import RunStatusHPCDLRun


class RunHPCDLRunBuilder(RunBuilder, RuntimeEntityBuilderHPCDL):
    """
    RunHPCDLRunBuilder runer.
    """

    ENTITY_CLASS = RunHPCDLRun
    ENTITY_SPEC_CLASS = RunSpecHPCDLRun
    ENTITY_SPEC_VALIDATOR = RunValidatorHPCDLRun
    ENTITY_STATUS_CLASS = RunStatusHPCDLRun
    ENTITY_KIND = EntityKinds.RUN_HPCDL.value
