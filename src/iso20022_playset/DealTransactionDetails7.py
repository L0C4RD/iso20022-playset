from . import base_types
from .CollateralAmount14 import CollateralAmount14
from .ClosingDate4Choice import ClosingDate4Choice

class DealTransactionDetails7(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_DealDtlsAmt"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != base_types.auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def DealDtlsAmt(self):
		return self._DealDtlsAmt

	@DealDtlsAmt.setter
	def DealDtlsAmt(self, value):
		self._DealDtlsAmt = value if type(value) != base_types.auto else self.make_default("DealDtlsAmt")

	@DealDtlsAmt.deleter
	def DealDtlsAmt(self):
		del self._DealDtlsAmt
		self._DealDtlsAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealDtlsAmt', type=CollateralAmount14, min=0, max=1, mutex_group=None, array=False),
	))

