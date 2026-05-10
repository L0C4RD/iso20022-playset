from . import base_types
from .CashCollateral5 import CashCollateral5
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Max1025Text import Max1025Text

class ContractCollateral1(base_types._BaseFieldType):

	__slots__ = ["_CollDesc", "_TtlAmt", "_AddtlInf"]
	@property
	def CollDesc(self):
		return self._CollDesc

	@CollDesc.setter
	def CollDesc(self, value):
		self._CollDesc = value if type(value) != auto else self.make_default("CollDesc")

	@CollDesc.deleter
	def CollDesc(self):
		del self._CollDesc
		self._CollDesc = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollDesc', type=CashCollateral5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
	))

