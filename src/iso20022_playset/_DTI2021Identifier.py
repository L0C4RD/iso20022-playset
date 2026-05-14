# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class DTI2021Identifier(base_types._BaseDataType_String):

	_pattern = r"[1-9B-DF-HJ-NP-XZ][0-9B-DF-HJ-NP-XZ]{8,8}"