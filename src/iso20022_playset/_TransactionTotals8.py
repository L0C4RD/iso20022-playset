# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import DetailedAmount15
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Number
from . import TypeTransactionTotals3Code

class TransactionTotals8(base_types._BaseFieldType):

	__slots__ = ["_CardPdctPrfl", "_Ccy", "_CmltvAmt", "_DtldAmt", "_POIGrpId", "_Tp", "_TtlNb"]
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
	def DtldAmt(self):
		return self._DtldAmt

	@DtldAmt.setter
	def DtldAmt(self, value):
		self._DtldAmt = value if value is not None else base_types.UninitialisedField(self, 'DtldAmt', DetailedAmount15, False)

	@DtldAmt.deleter
	def DtldAmt(self):
		del self._DtldAmt
		self._DtldAmt = base_types.UninitialisedField(self, 'DtldAmt', DetailedAmount15, False)

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
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TypeTransactionTotals3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TypeTransactionTotals3Code, False)

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
		base_types.FieldEntry(name='CardPdctPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmltvAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtldAmt', type=DetailedAmount15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIGrpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TypeTransactionTotals3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNb', type=Number, min=1, max=1, mutex_group=None, array=False),
	))