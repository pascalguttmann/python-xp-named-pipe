from __future__ import annotations

import sys

if sys.platform == "win32":
    import win_named_pipe as xpnp
else:
    raise NotImplementedError

NamedPipe = xpnp.NamedPipe
# PipeEnd = xpnp.PipeEnd
WritePipeEnd = xpnp.WritePipeEnd
ReadPipeEnd = xpnp.ReadPipeEnd