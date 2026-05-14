# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class NewZealandNCCIdentifier(base_types._BaseDataType_String):

	_pattern = r"NZ[0-9]{6,6}"