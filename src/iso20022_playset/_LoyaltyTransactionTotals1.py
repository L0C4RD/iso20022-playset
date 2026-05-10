from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._Max35Text import Max35Text
from ._DetailedAmount15 import DetailedAmount15
from ._AmountUnit1Code import AmountUnit1Code
from ._LoyaltyTypeTransactionTotals1Code import LoyaltyTypeTransactionTotals1Code
from ._Number import Number
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class LoyaltyTransactionTotals1(base_types._BaseFieldType):

	__slots__ = ["_LltyUnit", "_TxTp", "_DtldAmt", "_POIGrpId", "_CardPdctPrfl", "_CmltvAmt", "_TtlNb", "_Ccy"]
	@property
	def CardPdctPrfl(self):
		return self._CardPdctPrfl

	@CardPdctPrfl.setter
	def CardPdctPrfl(self, value):
		self._CardPdctPrfl = value if type(value) != base_types.auto else self.make_default("CardPdctPrfl")

	@CardPdctPrfl.deleter
	def CardPdctPrfl(self):
		del self._CardPdctPrfl
		self._CardPdctPrfl = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CmltvAmt(self):
		return self._CmltvAmt

	@CmltvAmt.setter
	def CmltvAmt(self, value):
		self._CmltvAmt = value if type(value) != base_types.auto else self.make_default("CmltvAmt")

	@CmltvAmt.deleter
	def CmltvAmt(self):
		del self._CmltvAmt
		self._CmltvAmt = None

	@property
	def DtldAmt(self):
		return self._DtldAmt

	@DtldAmt.setter
	def DtldAmt(self, value):
		self._DtldAmt = value if type(value) != base_types.auto else self.make_default("DtldAmt")

	@DtldAmt.deleter
	def DtldAmt(self):
		del self._DtldAmt
		self._DtldAmt = None

	@property
	def LltyUnit(self):
		return self._LltyUnit

	@LltyUnit.setter
	def LltyUnit(self, value):
		self._LltyUnit = value if type(value) != base_types.auto else self.make_default("LltyUnit")

	@LltyUnit.deleter
	def LltyUnit(self):
		del self._LltyUnit
		self._LltyUnit = None

	@property
	def POIGrpId(self):
		return self._POIGrpId

	@POIGrpId.setter
	def POIGrpId(self, value):
		self._POIGrpId = value if type(value) != base_types.auto else self.make_default("POIGrpId")

	@POIGrpId.deleter
	def POIGrpId(self):
		del self._POIGrpId
		self._POIGrpId = None

	@property
	def TtlNb(self):
		return self._TtlNb

	@TtlNb.setter
	def TtlNb(self, value):
		self._TtlNb = value if type(value) != base_types.auto else self.make_default("TtlNb")

	@TtlNb.deleter
	def TtlNb(self):
		del self._TtlNb
		self._TtlNb = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != base_types.auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardPdctPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldAmt', type=DetailedAmount15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyUnit', type=AmountUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=LoyaltyTypeTransactionTotals1Code, min=1, max=1, mutex_group=None, array=False),
	))

