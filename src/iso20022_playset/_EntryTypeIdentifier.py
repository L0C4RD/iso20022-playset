# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class EntryTypeIdentifier(base_types._BaseDataType_String):

	_pattern = r"[BEOVW]{1,1}[0-9]{2,2}|DUM"