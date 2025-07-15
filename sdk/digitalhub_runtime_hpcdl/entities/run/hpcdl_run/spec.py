# SPDX-FileCopyrightText: © 2025 DSLab - Fondazione Bruno Kessler
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from digitalhub.entities.run._base.spec import RunSpec, RunValidator


class RunSpecHPCDLRun(RunSpec):
    """
    RunSpecHPCDLRun specifications.
    """

    def __init__(
        self,
        task: str,
        local_execution: bool = False,
        function: str | None = None,
        workflow: str | None = None,
        node_selector: list[dict] | None = None,
        volumes: list[dict] | None = None,
        resources: dict | None = None,
        affinity: dict | None = None,
        tolerations: list[dict] | None = None,
        envs: list[dict] | None = None,
        secrets: list[str] | None = None,
        profile: str | None = None,
        runtime_class: str | None = None,
        priority_class: str | None = None,

        image: str | None = None,
        command: str | None = None,
        args: list[str] | None = None,
        inputs: dict | None = None,
        outputs: dict | None = None,
        walltime: str | None = None,
        nodes: int | None = None,
        tasks_per_node: int | None = None,
        cpus_per_task: int | None = None,
        gpus: int | None = None,
        qos: str | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            task,
            local_execution,
            function,
            workflow,
            node_selector,
            volumes,
            resources,
            affinity,
            tolerations,
            envs,
            secrets,
            profile,
            runtime_class,
            priority_class,
            **kwargs,
        )
        self.args = args
        self.image = image
        self.command = command
        self.inputs = inputs
        self.outputs = outputs
        self.walltime = walltime
        self.nodes = nodes
        self.tasks_per_node = tasks_per_node
        self.cpus_per_task = cpus_per_task
        self.gpus = gpus
        self.qos = qos


class RunValidatorHPCDLRun(RunValidator):
    """
    RunValidatorHPCDLRun validator.
    """

    # Run parameters
    args: list[str] = None
    """Arguments to pass to the entrypoint."""

    # Function parameters
    image: str = None
    command: str = None

    inputs: dict = None
    """Inputs to the run."""

    outputs: dict = None
    """Outputs of the run."""

    walltime: str = None
    """Walltime for the run."""

    nodes: int = None
    """Number of nodes to use for the run."""

    tasks_per_node: int = None
    """Number of tasks per node."""

    cpus_per_task: int = None
    """CPUs per task."""

    gpus: int = None
    """GPUs to use for the run."""

    qos: str = None
    """Quality of Service for the run."""