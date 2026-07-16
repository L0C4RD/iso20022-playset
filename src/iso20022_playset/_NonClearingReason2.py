# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingExemptionException1Code
from . import Max350Text

class NonClearingReason2(base_types._BaseFieldType):

	__slots__ = ["_ClrXmptnXcptn", "_NonClrRsnInf"]
	@property
	def ClrXmptnXcptn(self):
		return self._ClrXmptnXcptn

	@ClrXmptnXcptn.setter
	def ClrXmptnXcptn(self, value):
		self._ClrXmptnXcptn = value if value is not None else base_types.UninitialisedField(self, 'ClrXmptnXcptn', ClearingExemptionException1Code, True)

	@ClrXmptnXcptn.deleter
	def ClrXmptnXcptn(self):
		del self._ClrXmptnXcptn
		self._ClrXmptnXcptn = base_types.UninitialisedField(self, 'ClrXmptnXcptn', ClearingExemptionException1Code, True)

	@property
	def NonClrRsnInf(self):
		return self._NonClrRsnInf

	@NonClrRsnInf.setter
	def NonClrRsnInf(self, value):
		self._NonClrRsnInf = value if value is not None else base_types.UninitialisedField(self, 'NonClrRsnInf', Max350Text, False)

	@NonClrRsnInf.deleter
	def NonClrRsnInf(self):
		del self._NonClrRsnInf
		self._NonClrRsnInf = base_types.UninitialisedField(self, 'NonClrRsnInf', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrXmptnXcptn', type=ClearingExemptionException1Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonClrRsnInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))