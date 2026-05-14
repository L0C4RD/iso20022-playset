# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max10DateText(base_types._BaseDataType_String):

	_pattern = r"([0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2})|([0-9]{2,2}-[0-9]{2,2})|([0-9]{4,4}-[0-9]{2,2})"