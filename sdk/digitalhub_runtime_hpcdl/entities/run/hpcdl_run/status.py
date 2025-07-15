# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.status import RunStatus


class RunStatusHPCDLRun(RunStatus):
    """
    RunStatusHPCDLRun status.
    """

    def __init__(
        self,
        state: str,
        message: str | None = None,
        transitions: list[dict] | None = None,
        k8s: dict | None = None,
        metrics: dict | None = None,
        outputs: dict | None = None,
        job: dict | None = None,
        **kwargs,
    ) -> None:
        super().__init__(state, message, transitions, k8s, metrics, **kwargs)
        self.outputs = outputs
        self.job = job
