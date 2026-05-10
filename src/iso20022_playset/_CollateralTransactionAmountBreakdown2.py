from . import base_types
from ._Period4Choice import Period4Choice
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._GenericIdentification178 import GenericIdentification178

class CollateralTransactionAmountBreakdown2(base_types._BaseFieldType):

	__slots__ = ["_TxAmt", "_LotNb", "_Prd"]
	@property
	def TxAmt(self):
		return self._TxAmt

	@TxAmt.setter
	def TxAmt(self, value):
		self._TxAmt = value if type(value) != base_types.auto else self.make_default("TxAmt")

	@TxAmt.deleter
	def TxAmt(self):
		del self._TxAmt
		self._TxAmt = None

	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if type(value) != base_types.auto else self.make_default("LotNb")

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotNb', type=GenericIdentification178, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
	))

