# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class NACEDomain2025Identifier(base_types._BaseDataType_String):

	_pattern = r"[A-V]{1,1}"