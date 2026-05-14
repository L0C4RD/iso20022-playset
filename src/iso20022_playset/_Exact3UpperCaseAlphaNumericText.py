# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Exact3UpperCaseAlphaNumericText(base_types._BaseDataType_String):

	_pattern = r"[A-Z0-9]{3}"