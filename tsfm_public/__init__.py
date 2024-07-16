# Copyright contributors to the TSFM project
#

from .version import __version__, __version_tuple__

from pathlib import Path
from typing import TYPE_CHECKING


# Check the dependencies satisfy the minimal versions required.
from transformers.utils import _LazyModule, logging


logger = logging.get_logger(__name__)  # pylint: disable=invalid-name

# Base objects, independent of any specific backend
_import_structure = {
    "models": [],
    "models.tinytimemixer": ["TINYTIMEMIXER_PRETRAINED_CONFIG_ARCHIVE_MAP", "TinyTimeMixerConfig"],
    "toolkit": [],
}


# PyTorch-backed objects
_import_structure["models.tinytimemixer"].extend(
    [
        "TINYTIMEMIXER_PRETRAINED_MODEL_ARCHIVE_LIST",
        "TinyTimeMixerPreTrainedModel",
        "TinyTimeMixerModel",
        "TinyTimeMixerForPrediction",
    ]
)

# Direct imports for type-checking
if TYPE_CHECKING:
    from .models.tinytimemixer import (
        TINYTIMEMIXER_PRETRAINED_CONFIG_ARCHIVE_MAP,
        TINYTIMEMIXER_PRETRAINED_MODEL_ARCHIVE_LIST,
        TinyTimeMixerConfig,
        TinyTimeMixerForPrediction,
        TinyTimeMixerModel,
        TinyTimeMixerPreTrainedModel,
    )
else:
    # Standard
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )
