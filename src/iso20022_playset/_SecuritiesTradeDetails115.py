# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestorCapacity4Choice
from . import Max350Text
from . import Max3Number
from . import PlaceOfClearingIdentification2
from . import PlaceOfTradeIdentification1
from . import Price10
from . import Reporting6Choice
from . import SettlementDate17Choice
from . import SettlementDate18Choice
from . import TradeDate8Choice
from . import TradeOriginator3Choice
from . import TradeTransactionCondition5Choice

class SecuritiesTradeDetails115(base_types._BaseFieldType):

	__slots__ = ["_DealPric", "_FctvSttlmDt", "_FxAddtlDtls", "_InvstrCpcty", "_NbOfDaysAcrd", "_PlcOfClr", "_PlcOfTrad", "_Rptg", "_SttlmDt", "_SttlmInstrPrcgAddtlDtls", "_TradDt", "_TradOrgtrRole", "_TradTxCond"]
	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if value is not None else base_types.UninitialisedField(self, 'DealPric', Price10, False)

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = base_types.UninitialisedField(self, 'DealPric', Price10, False)

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'FctvSttlmDt', SettlementDate18Choice, False)

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = base_types.UninitialisedField(self, 'FctvSttlmDt', SettlementDate18Choice, False)

	@property
	def FxAddtlDtls(self):
		return self._FxAddtlDtls

	@FxAddtlDtls.setter
	def FxAddtlDtls(self, value):
		self._FxAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'FxAddtlDtls', Max350Text, False)

	@FxAddtlDtls.deleter
	def FxAddtlDtls(self):
		del self._FxAddtlDtls
		self._FxAddtlDtls = base_types.UninitialisedField(self, 'FxAddtlDtls', Max350Text, False)

	@property
	def InvstrCpcty(self):
		return self._InvstrCpcty

	@InvstrCpcty.setter
	def InvstrCpcty(self, value):
		self._InvstrCpcty = value if value is not None else base_types.UninitialisedField(self, 'InvstrCpcty', InvestorCapacity4Choice, False)

	@InvstrCpcty.deleter
	def InvstrCpcty(self):
		del self._InvstrCpcty
		self._InvstrCpcty = base_types.UninitialisedField(self, 'InvstrCpcty', InvestorCapacity4Choice, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if value is not None else base_types.UninitialisedField(self, 'PlcOfClr', PlaceOfClearingIdentification2, False)

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = base_types.UninitialisedField(self, 'PlcOfClr', PlaceOfClearingIdentification2, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification1, False)

	@property
	def Rptg(self):
		return self._Rptg

	@Rptg.setter
	def Rptg(self, value):
		self._Rptg = value if value is not None else base_types.UninitialisedField(self, 'Rptg', Reporting6Choice, True)

	@Rptg.deleter
	def Rptg(self):
		del self._Rptg
		self._Rptg = base_types.UninitialisedField(self, 'Rptg', Reporting6Choice, True)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@property
	def SttlmInstrPrcgAddtlDtls(self):
		return self._SttlmInstrPrcgAddtlDtls

	@SttlmInstrPrcgAddtlDtls.setter
	def SttlmInstrPrcgAddtlDtls(self, value):
		self._SttlmInstrPrcgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmInstrPrcgAddtlDtls', Max350Text, False)

	@SttlmInstrPrcgAddtlDtls.deleter
	def SttlmInstrPrcgAddtlDtls(self):
		del self._SttlmInstrPrcgAddtlDtls
		self._SttlmInstrPrcgAddtlDtls = base_types.UninitialisedField(self, 'SttlmInstrPrcgAddtlDtls', Max350Text, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@property
	def TradOrgtrRole(self):
		return self._TradOrgtrRole

	@TradOrgtrRole.setter
	def TradOrgtrRole(self, value):
		self._TradOrgtrRole = value if value is not None else base_types.UninitialisedField(self, 'TradOrgtrRole', TradeOriginator3Choice, False)

	@TradOrgtrRole.deleter
	def TradOrgtrRole(self):
		del self._TradOrgtrRole
		self._TradOrgtrRole = base_types.UninitialisedField(self, 'TradOrgtrRole', TradeOriginator3Choice, False)

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if value is not None else base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition5Choice, True)

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition5Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DealPric', type=Price10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=SettlementDate18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCpcty', type=InvestorCapacity4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rptg', type=Reporting6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradOrgtrRole', type=TradeOriginator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition5Choice, min=0, max=None, mutex_group=None, array=True),
	))