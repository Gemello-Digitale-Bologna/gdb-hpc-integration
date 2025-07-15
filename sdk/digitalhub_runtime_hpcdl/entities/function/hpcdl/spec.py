# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.function._base.spec import FunctionSpec, FunctionValidator


class FunctionSpecHPCDL(FunctionSpec):
    """
    FunctionSpecHPCDL specifications.
    """

    def __init__(
        self,
        image: str | None = None,
        command: str | None = None,
    ) -> None:
        super().__init__()

        self.image = image
        self.command = command


class FunctionValidatorHPCDL(FunctionValidator):
    """
    FunctionValidatorHPCDL validator.
    """

    image: str = None
    """Name of the Function's HPCDL image."""

    command: str = None
    """Command to run inside the container."""
