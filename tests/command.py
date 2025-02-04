import subprocess
from typing import Union


class ExecutionError(Exception):
    def __init__(self, code: int, out: str, err: str) -> None:
        self.code = code
        self.out = out
        self.err = err

    def __str__(self):
        return f"Command failed with rc={self.code}. Stdout:\n{self.out}\nStderr:\n{self.err}\n"


class Command:

    def __init__(self, args: Union[str, list[str]], shell: bool = True) -> None:
        self.args = args
        self.shell = shell

    def run(self, **kwargs):
        process = subprocess.Popen(
            self.args,
            shell=self.shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            **kwargs,
        )
        out, err = process.communicate()

        out = out.decode("utf-8")
        err = err.decode("utf-8")

        if process.returncode != 0:
            raise ExecutionError(process.returncode, out, err)

        return out
