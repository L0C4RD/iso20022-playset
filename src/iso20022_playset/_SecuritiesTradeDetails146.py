from . import base_types
from .MatchingStatus27Choice import MatchingStatus27Choice
from .Price10 import Price10
from .TradeDate8Choice import TradeDate8Choice
from .AffirmationStatus8Choice import AffirmationStatus8Choice
from .TradeTransactionCondition5Choice import TradeTransactionCondition5Choice
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .Max3Number import Max3Number
from .OpeningClosing3Choice import OpeningClosing3Choice
from .CurrencyToBuyOrSell1Choice import CurrencyToBuyOrSell1Choice
from .PlaceOfTradeIdentification1 import PlaceOfTradeIdentification1
from .InvestorCapacity4Choice import InvestorCapacity4Choice
from .PlaceOfClearingIdentification2 import PlaceOfClearingIdentification2
from .TradeOriginator3Choice import TradeOriginator3Choice
from .Max350Text import Max350Text
from .UTIIdentifier import UTIIdentifier
from .Max35Text import Max35Text
from .TypeOfPrice29Choice import TypeOfPrice29Choice
from .Reporting6Choice import Reporting6Choice

class SecuritiesTradeDetails146(base_types._BaseFieldType):

	__slots__ = ["_FxAddtlDtls", "_NbOfDaysAcrd", "_TradId", "_PlcOfTrad", "_TradTxCond", "_CcyToBuyOrSell", "_OpngClsg", "_TradDt", "_SttlmInstrPrcgAddtlDtls", "_MtchgSts", "_TpOfPric", "_UnqTxIdr", "_AffirmSts", "_TradOrgtrRole", "_Rptg", "_LateDlvryDt", "_InvstrCpcty", "_DealPric", "_CollTxId", "_PlcOfClr"]
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
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != base_types.auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

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
	def CcyToBuyOrSell(self):
		return self._CcyToBuyOrSell

	@CcyToBuyOrSell.setter
	def CcyToBuyOrSell(self, value):
		self._CcyToBuyOrSell = value if type(value) != base_types.auto else self.make_default("CcyToBuyOrSell")

	@CcyToBuyOrSell.deleter
	def CcyToBuyOrSell(self):
		del self._CcyToBuyOrSell
		self._CcyToBuyOrSell = None

	@property
	def OpngClsg(self):
		return self._OpngClsg

	@OpngClsg.setter
	def OpngClsg(self, value):
		self._OpngClsg = value if type(value) != base_types.auto else self.make_default("OpngClsg")

	@OpngClsg.deleter
	def OpngClsg(self):
		del self._OpngClsg
		self._OpngClsg = None

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
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != base_types.auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	@property
	def TpOfPric(self):
		return self._TpOfPric

	@TpOfPric.setter
	def TpOfPric(self, value):
		self._TpOfPric = value if type(value) != base_types.auto else self.make_default("TpOfPric")

	@TpOfPric.deleter
	def TpOfPric(self):
		del self._TpOfPric
		self._TpOfPric = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != base_types.auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if type(value) != base_types.auto else self.make_default("AffirmSts")

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = None

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
	def LateDlvryDt(self):
		return self._LateDlvryDt

	@LateDlvryDt.setter
	def LateDlvryDt(self, value):
		self._LateDlvryDt = value if type(value) != base_types.auto else self.make_default("LateDlvryDt")

	@LateDlvryDt.deleter
	def LateDlvryDt(self):
		del self._LateDlvryDt
		self._LateDlvryDt = None

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
	def CollTxId(self):
		return self._CollTxId

	@CollTxId.setter
	def CollTxId(self, value):
		self._CollTxId = value if type(value) != base_types.auto else self.make_default("CollTxId")

	@CollTxId.deleter
	def CollTxId(self):
		del self._CollTxId
		self._CollTxId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FxAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition5Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcyToBuyOrSell', type=CurrencyToBuyOrSell1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngClsg', type=OpeningClosing3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus27Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpOfPric', type=TypeOfPrice29Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradOrgtrRole', type=TradeOriginator3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rptg', type=Reporting6Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LateDlvryDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCpcty', type=InvestorCapacity4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollTxId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PlcOfClr', type=PlaceOfClearingIdentification2, min=0, max=1, mutex_group=None, array=False),
	))

