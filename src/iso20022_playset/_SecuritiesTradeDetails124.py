from . import base_types
from ._Price11 import Price11
from ._PlaceOfClearingIdentification2 import PlaceOfClearingIdentification2
from ._TradeTransactionCondition6Choice import TradeTransactionCondition6Choice
from ._SettlementDate22Choice import SettlementDate22Choice
from ._PlaceOfTradeIdentification2 import PlaceOfTradeIdentification2
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text
from ._Reporting9Choice import Reporting9Choice
from ._InvestorCapacity5Choice import InvestorCapacity5Choice
from ._TradeDate9Choice import TradeDate9Choice
from ._TradeOriginator4Choice import TradeOriginator4Choice
from ._Max3Number import Max3Number
from ._SettlementDate20Choice import SettlementDate20Choice

class SecuritiesTradeDetails124(base_types._BaseFieldType):

	__slots__ = ["_NbOfDaysAcrd", "_DealPric", "_FctvSttlmDt", "_SttlmInstrPrcgAddtlDtls", "_TradOrgtrRole", "_SttlmDt", "_TradDt", "_TradTxCond", "_Rptg", "_PlcOfClr", "_PlcOfTrad", "_InvstrCpcty", "_FxAddtlDtls"]
	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != base_types.auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if type(value) != base_types.auto else self.make_default("DealPric")

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = None

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if type(value) != base_types.auto else self.make_default("FctvSttlmDt")

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = None

	@property
	def SttlmInstrPrcgAddtlDtls(self):
		return self._SttlmInstrPrcgAddtlDtls

	@SttlmInstrPrcgAddtlDtls.setter
	def SttlmInstrPrcgAddtlDtls(self, value):
		self._SttlmInstrPrcgAddtlDtls = value if type(value) != base_types.auto else self.make_default("SttlmInstrPrcgAddtlDtls")

	@SttlmInstrPrcgAddtlDtls.deleter
	def SttlmInstrPrcgAddtlDtls(self):
		del self._SttlmInstrPrcgAddtlDtls
		self._SttlmInstrPrcgAddtlDtls = None

	@property
	def TradOrgtrRole(self):
		return self._TradOrgtrRole

	@TradOrgtrRole.setter
	def TradOrgtrRole(self, value):
		self._TradOrgtrRole = value if type(value) != base_types.auto else self.make_default("TradOrgtrRole")

	@TradOrgtrRole.deleter
	def TradOrgtrRole(self):
		del self._TradOrgtrRole
		self._TradOrgtrRole = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if type(value) != base_types.auto else self.make_default("TradTxCond")

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = None

	@property
	def Rptg(self):
		return self._Rptg

	@Rptg.setter
	def Rptg(self, value):
		self._Rptg = value if type(value) != base_types.auto else self.make_default("Rptg")

	@Rptg.deleter
	def Rptg(self):
		del self._Rptg
		self._Rptg = None

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if type(value) != base_types.auto else self.make_default("PlcOfClr")

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != base_types.auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def InvstrCpcty(self):
		return self._InvstrCpcty

	@InvstrCpcty.setter
	def InvstrCpcty(self, value):
		self._InvstrCpcty = value if type(value) != base_types.auto else self.make_default("InvstrCpcty")

	@InvstrCpcty.deleter
	def InvstrCpcty(self):
		del self._InvstrCpcty
		self._InvstrCpcty = None

	@property
	def FxAddtlDtls(self):
		return self._FxAddtlDtls

	@FxAddtlDtls.setter
	def FxAddtlDtls(self, value):
		self._FxAddtlDtls = value if type(value) != base_types.auto else self.make_default("FxAddtlDtls")

	@FxAddtlDtls.deleter
	def FxAddtlDtls(self):
		del self._FxAddtlDtls
		self._FxAddtlDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=SettlementDate22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrPrcgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradOrgtrRole', type=TradeOriginator4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate20Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rptg', type=Reporting9Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCpcty', type=InvestorCapacity5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
	))

