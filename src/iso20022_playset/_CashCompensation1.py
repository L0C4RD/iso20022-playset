from . import base_types
from ._AmountAndDirection20 import AmountAndDirection20
from ._ISODate import ISODate

class CashCompensation1(base_types._BaseFieldType):

	__slots__ = ["_ValDt", "_SttlmAmt", "_Fees"]
	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if type(value) != base_types.auto else self.make_default("Fees")

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fees', type=AmountAndDirection20, min=0, max=1, mutex_group=None, array=False),
	))

