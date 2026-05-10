import base_types
import TradeDate8Choice
import MatchingStatus27Choice
import PlaceOfClearingIdentification2
import AffirmationStatus8Choice
import DateAndDateTime2Choice
import Max3Number
import InvestorCapacity4Choice
import Price10
import Max350Text
import Reporting6Choice
import CurrencyToBuyOrSell1Choice
import TradeTransactionCondition5Choice
import PlaceOfTradeIdentification1
import TradeOriginator3Choice

class SecuritiesTradeDetails116(base_types._BaseFieldType):

	__slots__ = ["_OpngSttlmDt", "_NbOfDaysAcrd", "_MtchgSts", "_PlcOfClr", "_CcyToBuyOrSell", "_Rptg", "_TradTxCond", "_InvstrCpcty", "_AffirmSts", "_TradDt", "_PlcOfTrad", "_DealPric", "_FxAddtlDtls", "_TradOrgtrRole", "_SttlmInstrPrcgAddtlDtls"]
	@property
	def OpngSttlmDt(self):
		return self._OpngSttlmDt

	@OpngSttlmDt.setter
	def OpngSttlmDt(self, value):
		self._OpngSttlmDt = value if type(value) != auto else self.make_default("OpngSttlmDt")

	@OpngSttlmDt.deleter
	def OpngSttlmDt(self):
		del self._OpngSttlmDt
		self._OpngSttlmDt = None

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if type(value) != auto else self.make_default("NbOfDaysAcrd")

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = None

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	@property
	def PlcOfClr(self):
		return self._PlcOfClr

	@PlcOfClr.setter
	def PlcOfClr(self, value):
		self._PlcOfClr = value if type(value) != auto else self.make_default("PlcOfClr")

	@PlcOfClr.deleter
	def PlcOfClr(self):
		del self._PlcOfClr
		self._PlcOfClr = None

	@property
	def CcyToBuyOrSell(self):
		return self._CcyToBuyOrSell

	@CcyToBuyOrSell.setter
	def CcyToBuyOrSell(self, value):
		self._CcyToBuyOrSell = value if type(value) != auto else self.make_default("CcyToBuyOrSell")

	@CcyToBuyOrSell.deleter
	def CcyToBuyOrSell(self):
		del self._CcyToBuyOrSell
		self._CcyToBuyOrSell = None

	@property
	def Rptg(self):
		return self._Rptg

	@Rptg.setter
	def Rptg(self, value):
		self._Rptg = value if type(value) != auto else self.make_default("Rptg")

	@Rptg.deleter
	def Rptg(self):
		del self._Rptg
		self._Rptg = None

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if type(value) != auto else self.make_default("TradTxCond")

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = None

	@property
	def InvstrCpcty(self):
		return self._InvstrCpcty

	@InvstrCpcty.setter
	def InvstrCpcty(self, value):
		self._InvstrCpcty = value if type(value) != auto else self.make_default("InvstrCpcty")

	@InvstrCpcty.deleter
	def InvstrCpcty(self):
		del self._InvstrCpcty
		self._InvstrCpcty = None

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if type(value) != auto else self.make_default("AffirmSts")

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if type(value) != auto else self.make_default("DealPric")

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = None

	@property
	def FxAddtlDtls(self):
		return self._FxAddtlDtls

	@FxAddtlDtls.setter
	def FxAddtlDtls(self, value):
		self._FxAddtlDtls = value if type(value) != auto else self.make_default("FxAddtlDtls")

	@FxAddtlDtls.deleter
	def FxAddtlDtls(self):
		del self._FxAddtlDtls
		self._FxAddtlDtls = None

	@property
	def TradOrgtrRole(self):
		return self._TradOrgtrRole

	@TradOrgtrRole.setter
	def TradOrgtrRole(self, value):
		self._TradOrgtrRole = value if type(value) != auto else self.make_default("TradOrgtrRole")

	@TradOrgtrRole.deleter
	def TradOrgtrRole(self):
		del self._TradOrgtrRole
		self._TradOrgtrRole = None

	@property
	def SttlmInstrPrcgAddtlDtls(self):
		return self._SttlmInstrPrcgAddtlDtls

	@SttlmInstrPrcgAddtlDtls.setter
	def SttlmInstrPrcgAddtlDtls(self, value):
		self._SttlmInstrPrcgAddtlDtls = value if type(value) != auto else self.make_default("SttlmInstrPrcgAddtlDtls")

	@SttlmInstrPrcgAddtlDtls.deleter
	def SttlmInstrPrcgAddtlDtls(self):
		del self._SttlmInstrPrcgAddtlDtls
		self._SttlmInstrPrcgAddtlDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngSttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyToBuyOrSell', type=CurrencyToBuyOrSell1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rptg', type=Reporting6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition5Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstrCpcty', type=InvestorCapacity4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradOrgtrRole', type=TradeOriginator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

