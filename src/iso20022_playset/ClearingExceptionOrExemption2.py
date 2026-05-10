from . import base_types
from .NonClearingReason2 import NonClearingReason2

class ClearingExceptionOrExemption2(base_types._BaseFieldType):

	__slots__ = ["_RptgCtrPty", "_OthrCtrPty"]
	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgCtrPty', type=NonClearingReason2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=NonClearingReason2, min=0, max=1, mutex_group=None, array=False),
	))

