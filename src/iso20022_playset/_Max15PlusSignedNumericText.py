# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max15PlusSignedNumericText(base_types._BaseDataType_String):

	_pattern = r"[\+]{0,1}[0-9]{1,15}"