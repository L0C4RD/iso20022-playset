# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max10KBinary(base_types._BaseDataType_B64Binary):

	_max = 10240
	_min = 1