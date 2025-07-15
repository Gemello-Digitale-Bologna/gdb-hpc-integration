# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.runtimes.builder import RuntimeBuilder

from digitalhub_runtime_hpcdl.runtimes.runtime import RuntimeHPCDL


class RuntimeHPCDLBuilder(RuntimeBuilder):
    """RuntimeHPCDLBuilder class."""

    RUNTIME_CLASS = RuntimeHPCDL
