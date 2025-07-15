# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum


class EntityKinds(Enum):
    """
    Entity kinds.
    """

    FUNCTION_HPCDL = "hpcdl"
    TASK_HPCDL_JOB = "hpcdl+job"
    RUN_HPCDL = "hpcdl+run"


class TaskActions(Enum):
    """
    Task actions.
    """

    JOB = "job"
