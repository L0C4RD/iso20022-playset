# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max9999HexBinaryText(base_types._BaseDataType_String):

	_pattern = r"([0-9A-F][0-9A-F]){1,9999}"