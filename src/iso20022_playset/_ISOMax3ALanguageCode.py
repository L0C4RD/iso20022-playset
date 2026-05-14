# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ISOMax3ALanguageCode(base_types._BaseDataType_String):

	_pattern = r"[a-z]{2,3}"