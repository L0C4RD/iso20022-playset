from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._TypeTransactionTotals2Code import TypeTransactionTotals2Code
from ._Max35Text import Max35Text
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Number import Number

class TransactionTotals12(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_POIGrpId", "_CardPdctPrfl", "_CardBrnd", "_CmltvAmt", "_TtlNb", "_Ccy"]
	@property
	def CardBrnd(self):
		return self._CardBrnd

	@CardBrnd.setter
	def CardBrnd(self, value):
		self._CardBrnd = value if type(value) != base_types.auto else self.make_default("CardBrnd")

	@CardBrnd.deleter
	def CardBrnd(self):
		del self._CardBrnd
		self._CardBrnd = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardBrnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPdctPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeTransactionTotals2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

