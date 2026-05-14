# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ISINOct2015Identifier(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}"