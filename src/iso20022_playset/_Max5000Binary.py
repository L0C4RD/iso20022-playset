# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max5000Binary(base_types._BaseDataType_B64Binary):

	_max = 5000
	_min = 1