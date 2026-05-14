# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Min2Max3AlphaText(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z]{2,3}"