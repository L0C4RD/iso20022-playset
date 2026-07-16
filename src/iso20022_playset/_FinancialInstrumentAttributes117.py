# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountPrice4
from . import BalanceFormat14Choice
from . import DateFormat41Choice
from . import FractionDispositionType32Choice
from . import Period11
from . import QuantityToQuantityRatio2
from . import RenounceableEntitlementStatusTypeFormat4Choice
from . import RestrictedFINDecimalNumber
from . import SecurityIdentification20

class FinancialInstrumentAttributes117(base_types._BaseFieldType):

	__slots__ = ["_FrctnDspstn", "_InstdBal", "_IntrmdtSctiesToUndrlygRatio", "_MktPric", "_PstngDt", "_Qty", "_RnncblEntitlmntStsTp", "_SctyId", "_TradgPrd", "_UinstdBal", "_XpryDt"]
	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if value is not None else base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType32Choice, False)

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = base_types.UninitialisedField(self, 'FrctnDspstn', FractionDispositionType32Choice, False)

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if value is not None else base_types.UninitialisedField(self, 'InstdBal', BalanceFormat14Choice, False)

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = base_types.UninitialisedField(self, 'InstdBal', BalanceFormat14Choice, False)

	@property
	def IntrmdtSctiesToUndrlygRatio(self):
		return self._IntrmdtSctiesToUndrlygRatio

	@IntrmdtSctiesToUndrlygRatio.setter
	def IntrmdtSctiesToUndrlygRatio(self, value):
		self._IntrmdtSctiesToUndrlygRatio = value if value is not None else base_types.UninitialisedField(self, 'IntrmdtSctiesToUndrlygRatio', QuantityToQuantityRatio2, False)

	@IntrmdtSctiesToUndrlygRatio.deleter
	def IntrmdtSctiesToUndrlygRatio(self):
		del self._IntrmdtSctiesToUndrlygRatio
		self._IntrmdtSctiesToUndrlygRatio = base_types.UninitialisedField(self, 'IntrmdtSctiesToUndrlygRatio', QuantityToQuantityRatio2, False)

	@property
	def MktPric(self):
		return self._MktPric

	@MktPric.setter
	def MktPric(self, value):
		self._MktPric = value if value is not None else base_types.UninitialisedField(self, 'MktPric', AmountPrice4, False)

	@MktPric.deleter
	def MktPric(self):
		del self._MktPric
		self._MktPric = base_types.UninitialisedField(self, 'MktPric', AmountPrice4, False)

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if value is not None else base_types.UninitialisedField(self, 'PstngDt', DateFormat41Choice, False)

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = base_types.UninitialisedField(self, 'PstngDt', DateFormat41Choice, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', RestrictedFINDecimalNumber, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', RestrictedFINDecimalNumber, False)

	@property
	def RnncblEntitlmntStsTp(self):
		return self._RnncblEntitlmntStsTp

	@RnncblEntitlmntStsTp.setter
	def RnncblEntitlmntStsTp(self, value):
		self._RnncblEntitlmntStsTp = value if value is not None else base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableEntitlementStatusTypeFormat4Choice, False)

	@RnncblEntitlmntStsTp.deleter
	def RnncblEntitlmntStsTp(self):
		del self._RnncblEntitlmntStsTp
		self._RnncblEntitlmntStsTp = base_types.UninitialisedField(self, 'RnncblEntitlmntStsTp', RenounceableEntitlementStatusTypeFormat4Choice, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification20, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification20, False)

	@property
	def TradgPrd(self):
		return self._TradgPrd

	@TradgPrd.setter
	def TradgPrd(self, value):
		self._TradgPrd = value if value is not None else base_types.UninitialisedField(self, 'TradgPrd', Period11, False)

	@TradgPrd.deleter
	def TradgPrd(self):
		del self._TradgPrd
		self._TradgPrd = base_types.UninitialisedField(self, 'TradgPrd', Period11, False)

	@property
	def UinstdBal(self):
		return self._UinstdBal

	@UinstdBal.setter
	def UinstdBal(self, value):
		self._UinstdBal = value if value is not None else base_types.UninitialisedField(self, 'UinstdBal', BalanceFormat14Choice, False)

	@UinstdBal.deleter
	def UinstdBal(self):
		del self._UinstdBal
		self._UinstdBal = base_types.UninitialisedField(self, 'UinstdBal', BalanceFormat14Choice, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', DateFormat41Choice, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', DateFormat41Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesToUndrlygRatio', type=QuantityToQuantityRatio2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPric', type=AmountPrice4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableEntitlementStatusTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
	))