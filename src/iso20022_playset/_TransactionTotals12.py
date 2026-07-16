# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Number
from . import TypeTransactionTotals2Code

class TransactionTotals12(base_types._BaseFieldType):

	__slots__ = ["_CardBrnd", "_CardPdctPrfl", "_Ccy", "_CmltvAmt", "_POIGrpId", "_Tp", "_TtlNb"]
	@property
	def CardBrnd(self):
		return self._CardBrnd

	@CardBrnd.setter
	def CardBrnd(self, value):
		self._CardBrnd = value if value is not None else base_types.UninitialisedField(self, 'CardBrnd', Max35Text, False)

	@CardBrnd.deleter
	def CardBrnd(self):
		del self._CardBrnd
		self._CardBrnd = base_types.UninitialisedField(self, 'CardBrnd', Max35Text, False)

	@property
	def CardPdctPrfl(self):
		return self._CardPdctPrfl

	@CardPdctPrfl.setter
	def CardPdctPrfl(self, value):
		self._CardPdctPrfl = value if value is not None else base_types.UninitialisedField(self, 'CardPdctPrfl', Max35Text, False)

	@CardPdctPrfl.deleter
	def CardPdctPrfl(self):
		del self._CardPdctPrfl
		self._CardPdctPrfl = base_types.UninitialisedField(self, 'CardPdctPrfl', Max35Text, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CmltvAmt(self):
		return self._CmltvAmt

	@CmltvAmt.setter
	def CmltvAmt(self, value):
		self._CmltvAmt = value if value is not None else base_types.UninitialisedField(self, 'CmltvAmt', ImpliedCurrencyAndAmount, False)

	@CmltvAmt.deleter
	def CmltvAmt(self):
		del self._CmltvAmt
		self._CmltvAmt = base_types.UninitialisedField(self, 'CmltvAmt', ImpliedCurrencyAndAmount, False)

	@property
	def POIGrpId(self):
		return self._POIGrpId

	@POIGrpId.setter
	def POIGrpId(self, value):
		self._POIGrpId = value if value is not None else base_types.UninitialisedField(self, 'POIGrpId', Max35Text, False)

	@POIGrpId.deleter
	def POIGrpId(self):
		del self._POIGrpId
		self._POIGrpId = base_types.UninitialisedField(self, 'POIGrpId', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeTransactionTotals2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeTransactionTotals2Code, False)

	@property
	def TtlNb(self):
		return self._TtlNb

	@TtlNb.setter
	def TtlNb(self, value):
		self._TtlNb = value if value is not None else base_types.UninitialisedField(self, 'TtlNb', Number, False)

	@TtlNb.deleter
	def TtlNb(self):
		del self._TtlNb
		self._TtlNb = base_types.UninitialisedField(self, 'TtlNb', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardBrnd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardPdctPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeTransactionTotals2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))