# Copyright 2020 The TensorFlow Quantum Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Module functions for tensorflow_quantum.*"""

# Import basic ops and op getters.
from tensorflow_quantum.core import (append_circuit, get_expectation_op,
                                     get_sampled_expectation_op,
                                     get_sampling_op, get_state_op,
                                     padded_to_ragged)

# Re-label python module as layers module.
import tensorflow_quantum.python.layers as layers

# Import utility functions for tensor operations & conversions.
from tensorflow_quantum.python.util import (
    # Utility functions
    convert_to_tensor,
    from_tensor,
)

# Re-label python module as util module.
import tensorflow_quantum.python.util as util

# Import datasets.
import tensorflow_quantum.datasets as datasets

# Import differentiators.
import tensorflow_quantum.python.differentiators as differentiators

__version__ = "0.2.0"
