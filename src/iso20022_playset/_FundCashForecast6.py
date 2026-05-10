from . import base_types
from .FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from .CurrencyDesignation1 import CurrencyDesignation1
from .YesNoIndicator import YesNoIndicator
from .FinancialInstrument9 import FinancialInstrument9
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .UnitPrice19 import UnitPrice19
from .BreakdownByCountry2 import BreakdownByCountry2
from .BreakdownByUserDefinedParameter3 import BreakdownByUserDefinedParameter3
from .BreakdownByCurrency2 import BreakdownByCurrency2
from .NetCashForecast4 import NetCashForecast4
from .Max35Text import Max35Text
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .PercentageRate import PercentageRate
from .ForeignExchangeTerms19 import ForeignExchangeTerms19
from .BreakdownByParty3 import BreakdownByParty3

class FundCashForecast6(base_types._BaseFieldType):

	__slots__ = ["_InvstmtCcy", "_PrvsTtlNAV", "_FXRate", "_XcptnlNetCshFlowInd", "_BrkdwnByCtry", "_FinInstrmDtls", "_NetCshFcstDtls", "_Id", "_BrkdwnByCcy", "_TtlNAVChngRate", "_PctgOfShrClssTtlNAV", "_TradDtTm", "_PrvsTradDtTm", "_PrvsTtlUnitsNb", "_Pric", "_TtlNAV", "_BrkdwnByUsrDfndParam", "_BrkdwnByPty", "_CcySts", "_TtlUnitsNb"]
	@property
	def InvstmtCcy(self):
		return self._InvstmtCcy

	@InvstmtCcy.setter
	def InvstmtCcy(self, value):
		self._InvstmtCcy = value if type(value) != base_types.auto else self.make_default("InvstmtCcy")

	@InvstmtCcy.deleter
	def InvstmtCcy(self):
		del self._InvstmtCcy
		self._InvstmtCcy = None

	@property
	def PrvsTtlNAV(self):
		return self._PrvsTtlNAV

	@PrvsTtlNAV.setter
	def PrvsTtlNAV(self, value):
		self._PrvsTtlNAV = value if type(value) != base_types.auto else self.make_default("PrvsTtlNAV")

	@PrvsTtlNAV.deleter
	def PrvsTtlNAV(self):
		del self._PrvsTtlNAV
		self._PrvsTtlNAV = None

	@property
	def FXRate(self):
		return self._FXRate

	@FXRate.setter
	def FXRate(self, value):
		self._FXRate = value if type(value) != base_types.auto else self.make_default("FXRate")

	@FXRate.deleter
	def FXRate(self):
		del self._FXRate
		self._FXRate = None

	@property
	def XcptnlNetCshFlowInd(self):
		return self._XcptnlNetCshFlowInd

	@XcptnlNetCshFlowInd.setter
	def XcptnlNetCshFlowInd(self, value):
		self._XcptnlNetCshFlowInd = value if type(value) != base_types.auto else self.make_default("XcptnlNetCshFlowInd")

	@XcptnlNetCshFlowInd.deleter
	def XcptnlNetCshFlowInd(self):
		del self._XcptnlNetCshFlowInd
		self._XcptnlNetCshFlowInd = None

	@property
	def BrkdwnByCtry(self):
		return self._BrkdwnByCtry

	@BrkdwnByCtry.setter
	def BrkdwnByCtry(self, value):
		self._BrkdwnByCtry = value if type(value) != base_types.auto else self.make_default("BrkdwnByCtry")

	@BrkdwnByCtry.deleter
	def BrkdwnByCtry(self):
		del self._BrkdwnByCtry
		self._BrkdwnByCtry = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != base_types.auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def NetCshFcstDtls(self):
		return self._NetCshFcstDtls

	@NetCshFcstDtls.setter
	def NetCshFcstDtls(self, value):
		self._NetCshFcstDtls = value if type(value) != base_types.auto else self.make_default("NetCshFcstDtls")

	@NetCshFcstDtls.deleter
	def NetCshFcstDtls(self):
		del self._NetCshFcstDtls
		self._NetCshFcstDtls = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def BrkdwnByCcy(self):
		return self._BrkdwnByCcy

	@BrkdwnByCcy.setter
	def BrkdwnByCcy(self, value):
		self._BrkdwnByCcy = value if type(value) != base_types.auto else self.make_default("BrkdwnByCcy")

	@BrkdwnByCcy.deleter
	def BrkdwnByCcy(self):
		del self._BrkdwnByCcy
		self._BrkdwnByCcy = None

	@property
	def TtlNAVChngRate(self):
		return self._TtlNAVChngRate

	@TtlNAVChngRate.setter
	def TtlNAVChngRate(self, value):
		self._TtlNAVChngRate = value if type(value) != base_types.auto else self.make_default("TtlNAVChngRate")

	@TtlNAVChngRate.deleter
	def TtlNAVChngRate(self):
		del self._TtlNAVChngRate
		self._TtlNAVChngRate = None

	@property
	def PctgOfShrClssTtlNAV(self):
		return self._PctgOfShrClssTtlNAV

	@PctgOfShrClssTtlNAV.setter
	def PctgOfShrClssTtlNAV(self, value):
		self._PctgOfShrClssTtlNAV = value if type(value) != base_types.auto else self.make_default("PctgOfShrClssTtlNAV")

	@PctgOfShrClssTtlNAV.deleter
	def PctgOfShrClssTtlNAV(self):
		del self._PctgOfShrClssTtlNAV
		self._PctgOfShrClssTtlNAV = None

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if type(value) != base_types.auto else self.make_default("TradDtTm")

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = None

	@property
	def PrvsTradDtTm(self):
		return self._PrvsTradDtTm

	@PrvsTradDtTm.setter
	def PrvsTradDtTm(self, value):
		self._PrvsTradDtTm = value if type(value) != base_types.auto else self.make_default("PrvsTradDtTm")

	@PrvsTradDtTm.deleter
	def PrvsTradDtTm(self):
		del self._PrvsTradDtTm
		self._PrvsTradDtTm = None

	@property
	def PrvsTtlUnitsNb(self):
		return self._PrvsTtlUnitsNb

	@PrvsTtlUnitsNb.setter
	def PrvsTtlUnitsNb(self, value):
		self._PrvsTtlUnitsNb = value if type(value) != base_types.auto else self.make_default("PrvsTtlUnitsNb")

	@PrvsTtlUnitsNb.deleter
	def PrvsTtlUnitsNb(self):
		del self._PrvsTtlUnitsNb
		self._PrvsTtlUnitsNb = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def TtlNAV(self):
		return self._TtlNAV

	@TtlNAV.setter
	def TtlNAV(self, value):
		self._TtlNAV = value if type(value) != base_types.auto else self.make_default("TtlNAV")

	@TtlNAV.deleter
	def TtlNAV(self):
		del self._TtlNAV
		self._TtlNAV = None

	@property
	def BrkdwnByUsrDfndParam(self):
		return self._BrkdwnByUsrDfndParam

	@BrkdwnByUsrDfndParam.setter
	def BrkdwnByUsrDfndParam(self, value):
		self._BrkdwnByUsrDfndParam = value if type(value) != base_types.auto else self.make_default("BrkdwnByUsrDfndParam")

	@BrkdwnByUsrDfndParam.deleter
	def BrkdwnByUsrDfndParam(self):
		del self._BrkdwnByUsrDfndParam
		self._BrkdwnByUsrDfndParam = None

	@property
	def BrkdwnByPty(self):
		return self._BrkdwnByPty

	@BrkdwnByPty.setter
	def BrkdwnByPty(self, value):
		self._BrkdwnByPty = value if type(value) != base_types.auto else self.make_default("BrkdwnByPty")

	@BrkdwnByPty.deleter
	def BrkdwnByPty(self):
		del self._BrkdwnByPty
		self._BrkdwnByPty = None

	@property
	def CcySts(self):
		return self._CcySts

	@CcySts.setter
	def CcySts(self, value):
		self._CcySts = value if type(value) != base_types.auto else self.make_default("CcySts")

	@CcySts.deleter
	def CcySts(self):
		del self._CcySts
		self._CcySts = None

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if type(value) != base_types.auto else self.make_default("TtlUnitsNb")

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FXRate', type=ForeignExchangeTerms19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcptnlNetCshFlowInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkdwnByCtry', type=BreakdownByCountry2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetCshFcstDtls', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkdwnByCcy', type=BreakdownByCurrency2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNAVChngRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfShrClssTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=UnitPrice19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrkdwnByUsrDfndParam', type=BreakdownByUserDefinedParameter3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrkdwnByPty', type=BreakdownByParty3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcySts', type=CurrencyDesignation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))

