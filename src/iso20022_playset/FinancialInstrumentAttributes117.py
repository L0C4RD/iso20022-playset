from . import base_types
from .Period11 import Period11
from .BalanceFormat14Choice import BalanceFormat14Choice
from .FractionDispositionType32Choice import FractionDispositionType32Choice
from .RenounceableEntitlementStatusTypeFormat4Choice import RenounceableEntitlementStatusTypeFormat4Choice
from .RestrictedFINDecimalNumber import RestrictedFINDecimalNumber
from .QuantityToQuantityRatio2 import QuantityToQuantityRatio2
from .AmountPrice4 import AmountPrice4
from .DateFormat41Choice import DateFormat41Choice
from .SecurityIdentification20 import SecurityIdentification20

class FinancialInstrumentAttributes117(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_IntrmdtSctiesToUndrlygRatio", "_MktPric", "_RnncblEntitlmntStsTp", "_XpryDt", "_InstdBal", "_TradgPrd", "_PstngDt", "_SctyId", "_UinstdBal", "_FrctnDspstn"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def IntrmdtSctiesToUndrlygRatio(self):
		return self._IntrmdtSctiesToUndrlygRatio

	@IntrmdtSctiesToUndrlygRatio.setter
	def IntrmdtSctiesToUndrlygRatio(self, value):
		self._IntrmdtSctiesToUndrlygRatio = value if type(value) != base_types.auto else self.make_default("IntrmdtSctiesToUndrlygRatio")

	@IntrmdtSctiesToUndrlygRatio.deleter
	def IntrmdtSctiesToUndrlygRatio(self):
		del self._IntrmdtSctiesToUndrlygRatio
		self._IntrmdtSctiesToUndrlygRatio = None

	@property
	def MktPric(self):
		return self._MktPric

	@MktPric.setter
	def MktPric(self, value):
		self._MktPric = value if type(value) != base_types.auto else self.make_default("MktPric")

	@MktPric.deleter
	def MktPric(self):
		del self._MktPric
		self._MktPric = None

	@property
	def RnncblEntitlmntStsTp(self):
		return self._RnncblEntitlmntStsTp

	@RnncblEntitlmntStsTp.setter
	def RnncblEntitlmntStsTp(self, value):
		self._RnncblEntitlmntStsTp = value if type(value) != base_types.auto else self.make_default("RnncblEntitlmntStsTp")

	@RnncblEntitlmntStsTp.deleter
	def RnncblEntitlmntStsTp(self):
		del self._RnncblEntitlmntStsTp
		self._RnncblEntitlmntStsTp = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def InstdBal(self):
		return self._InstdBal

	@InstdBal.setter
	def InstdBal(self, value):
		self._InstdBal = value if type(value) != base_types.auto else self.make_default("InstdBal")

	@InstdBal.deleter
	def InstdBal(self):
		del self._InstdBal
		self._InstdBal = None

	@property
	def TradgPrd(self):
		return self._TradgPrd

	@TradgPrd.setter
	def TradgPrd(self, value):
		self._TradgPrd = value if type(value) != base_types.auto else self.make_default("TradgPrd")

	@TradgPrd.deleter
	def TradgPrd(self):
		del self._TradgPrd
		self._TradgPrd = None

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if type(value) != base_types.auto else self.make_default("PstngDt")

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def UinstdBal(self):
		return self._UinstdBal

	@UinstdBal.setter
	def UinstdBal(self, value):
		self._UinstdBal = value if type(value) != base_types.auto else self.make_default("UinstdBal")

	@UinstdBal.deleter
	def UinstdBal(self):
		del self._UinstdBal
		self._UinstdBal = None

	@property
	def FrctnDspstn(self):
		return self._FrctnDspstn

	@FrctnDspstn.setter
	def FrctnDspstn(self, value):
		self._FrctnDspstn = value if type(value) != base_types.auto else self.make_default("FrctnDspstn")

	@FrctnDspstn.deleter
	def FrctnDspstn(self):
		del self._FrctnDspstn
		self._FrctnDspstn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesToUndrlygRatio', type=QuantityToQuantityRatio2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPric', type=AmountPrice4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RnncblEntitlmntStsTp', type=RenounceableEntitlementStatusTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPrd', type=Period11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=DateFormat41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UinstdBal', type=BalanceFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrctnDspstn', type=FractionDispositionType32Choice, min=0, max=1, mutex_group=None, array=False),
	))

