from . import base_types
from ._ClearingExemptionException1Code import ClearingExemptionException1Code
from ._Max350Text import Max350Text

class NonClearingReason2(base_types._BaseFieldType):

	__slots__ = ["_ClrXmptnXcptn", "_NonClrRsnInf"]
	@property
	def ClrXmptnXcptn(self):
		return self._ClrXmptnXcptn

	@ClrXmptnXcptn.setter
	def ClrXmptnXcptn(self, value):
		self._ClrXmptnXcptn = value if type(value) != base_types.auto else self.make_default("ClrXmptnXcptn")

	@ClrXmptnXcptn.deleter
	def ClrXmptnXcptn(self):
		del self._ClrXmptnXcptn
		self._ClrXmptnXcptn = None

	@property
	def NonClrRsnInf(self):
		return self._NonClrRsnInf

	@NonClrRsnInf.setter
	def NonClrRsnInf(self, value):
		self._NonClrRsnInf = value if type(value) != base_types.auto else self.make_default("NonClrRsnInf")

	@NonClrRsnInf.deleter
	def NonClrRsnInf(self):
		del self._NonClrRsnInf
		self._NonClrRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrXmptnXcptn', type=ClearingExemptionException1Code, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonClrRsnInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

