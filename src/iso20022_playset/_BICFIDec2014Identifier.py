# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class BICFIDec2014Identifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}"