# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class UTIIdentifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}"