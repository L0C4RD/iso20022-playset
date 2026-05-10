from . import base_types
import YesNoIndicator
import CurrencyDesignation1
import BreakdownByCountry2
import DateAndDateTimeChoice
import Max35Text
import NetCashForecast4
import UnitPrice19
import ForeignExchangeTerms19
import PercentageRate
import BreakdownByParty3
import FinancialInstrument9
import BreakdownByCurrency2
import FinancialInstrumentQuantity1
import BreakdownByUserDefinedParameter3
import ActiveOrHistoricCurrencyCode
import ActiveOrHistoricCurrencyAndAmount

class EstimatedFundCashForecast5(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmDtls", "_BrkdwnByCcy", "_XcptnlNetCshFlowInd", "_EstmtdTtlUnitsNb", "_InvstmtCcy", "_Pric", "_FXRate", "_CcySts", "_BrkdwnByCtry", "_EstmtdTtlNAV", "_PrvsTradDtTm", "_PrvsTtlUnitsNb", "_EstmtdTtlNAVChngRate", "_EstmtdPctgOfShrClssTtlNAV", "_BrkdwnByUsrDfndParam", "_EstmtdNetCshFcstDtls", "_Id", "_TradDtTm", "_PrvsTtlNAV", "_BrkdwnByPty"]
	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def BrkdwnByCcy(self):
		return self._BrkdwnByCcy

	@BrkdwnByCcy.setter
	def BrkdwnByCcy(self, value):
		self._BrkdwnByCcy = value if type(value) != auto else self.make_default("BrkdwnByCcy")

	@BrkdwnByCcy.deleter
	def BrkdwnByCcy(self):
		del self._BrkdwnByCcy
		self._BrkdwnByCcy = None

	@property
	def XcptnlNetCshFlowInd(self):
		return self._XcptnlNetCshFlowInd

	@XcptnlNetCshFlowInd.setter
	def XcptnlNetCshFlowInd(self, value):
		self._XcptnlNetCshFlowInd = value if type(value) != auto else self.make_default("XcptnlNetCshFlowInd")

	@XcptnlNetCshFlowInd.deleter
	def XcptnlNetCshFlowInd(self):
		del self._XcptnlNetCshFlowInd
		self._XcptnlNetCshFlowInd = None

	@property
	def EstmtdTtlUnitsNb(self):
		return self._EstmtdTtlUnitsNb

	@EstmtdTtlUnitsNb.setter
	def EstmtdTtlUnitsNb(self, value):
		self._EstmtdTtlUnitsNb = value if type(value) != auto else self.make_default("EstmtdTtlUnitsNb")

	@EstmtdTtlUnitsNb.deleter
	def EstmtdTtlUnitsNb(self):
		del self._EstmtdTtlUnitsNb
		self._EstmtdTtlUnitsNb = None

	@property
	def InvstmtCcy(self):
		return self._InvstmtCcy

	@InvstmtCcy.setter
	def InvstmtCcy(self, value):
		self._InvstmtCcy = value if type(value) != auto else self.make_default("InvstmtCcy")

	@InvstmtCcy.deleter
	def InvstmtCcy(self):
		del self._InvstmtCcy
		self._InvstmtCcy = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	@property
	def FXRate(self):
		return self._FXRate

	@FXRate.setter
	def FXRate(self, value):
		self._FXRate = value if type(value) != auto else self.make_default("FXRate")

	@FXRate.deleter
	def FXRate(self):
		del self._FXRate
		self._FXRate = None

	@property
	def CcySts(self):
		return self._CcySts

	@CcySts.setter
	def CcySts(self, value):
		self._CcySts = value if type(value) != auto else self.make_default("CcySts")

	@CcySts.deleter
	def CcySts(self):
		del self._CcySts
		self._CcySts = None

	@property
	def BrkdwnByCtry(self):
		return self._BrkdwnByCtry

	@BrkdwnByCtry.setter
	def BrkdwnByCtry(self, value):
		self._BrkdwnByCtry = value if type(value) != auto else self.make_default("BrkdwnByCtry")

	@BrkdwnByCtry.deleter
	def BrkdwnByCtry(self):
		del self._BrkdwnByCtry
		self._BrkdwnByCtry = None

	@property
	def EstmtdTtlNAV(self):
		return self._EstmtdTtlNAV

	@EstmtdTtlNAV.setter
	def EstmtdTtlNAV(self, value):
		self._EstmtdTtlNAV = value if type(value) != auto else self.make_default("EstmtdTtlNAV")

	@EstmtdTtlNAV.deleter
	def EstmtdTtlNAV(self):
		del self._EstmtdTtlNAV
		self._EstmtdTtlNAV = None

	@property
	def PrvsTradDtTm(self):
		return self._PrvsTradDtTm

	@PrvsTradDtTm.setter
	def PrvsTradDtTm(self, value):
		self._PrvsTradDtTm = value if type(value) != auto else self.make_default("PrvsTradDtTm")

	@PrvsTradDtTm.deleter
	def PrvsTradDtTm(self):
		del self._PrvsTradDtTm
		self._PrvsTradDtTm = None

	@property
	def PrvsTtlUnitsNb(self):
		return self._PrvsTtlUnitsNb

	@PrvsTtlUnitsNb.setter
	def PrvsTtlUnitsNb(self, value):
		self._PrvsTtlUnitsNb = value if type(value) != auto else self.make_default("PrvsTtlUnitsNb")

	@PrvsTtlUnitsNb.deleter
	def PrvsTtlUnitsNb(self):
		del self._PrvsTtlUnitsNb
		self._PrvsTtlUnitsNb = None

	@property
	def EstmtdTtlNAVChngRate(self):
		return self._EstmtdTtlNAVChngRate

	@EstmtdTtlNAVChngRate.setter
	def EstmtdTtlNAVChngRate(self, value):
		self._EstmtdTtlNAVChngRate = value if type(value) != auto else self.make_default("EstmtdTtlNAVChngRate")

	@EstmtdTtlNAVChngRate.deleter
	def EstmtdTtlNAVChngRate(self):
		del self._EstmtdTtlNAVChngRate
		self._EstmtdTtlNAVChngRate = None

	@property
	def EstmtdPctgOfShrClssTtlNAV(self):
		return self._EstmtdPctgOfShrClssTtlNAV

	@EstmtdPctgOfShrClssTtlNAV.setter
	def EstmtdPctgOfShrClssTtlNAV(self, value):
		self._EstmtdPctgOfShrClssTtlNAV = value if type(value) != auto else self.make_default("EstmtdPctgOfShrClssTtlNAV")

	@EstmtdPctgOfShrClssTtlNAV.deleter
	def EstmtdPctgOfShrClssTtlNAV(self):
		del self._EstmtdPctgOfShrClssTtlNAV
		self._EstmtdPctgOfShrClssTtlNAV = None

	@property
	def BrkdwnByUsrDfndParam(self):
		return self._BrkdwnByUsrDfndParam

	@BrkdwnByUsrDfndParam.setter
	def BrkdwnByUsrDfndParam(self, value):
		self._BrkdwnByUsrDfndParam = value if type(value) != auto else self.make_default("BrkdwnByUsrDfndParam")

	@BrkdwnByUsrDfndParam.deleter
	def BrkdwnByUsrDfndParam(self):
		del self._BrkdwnByUsrDfndParam
		self._BrkdwnByUsrDfndParam = None

	@property
	def EstmtdNetCshFcstDtls(self):
		return self._EstmtdNetCshFcstDtls

	@EstmtdNetCshFcstDtls.setter
	def EstmtdNetCshFcstDtls(self, value):
		self._EstmtdNetCshFcstDtls = value if type(value) != auto else self.make_default("EstmtdNetCshFcstDtls")

	@EstmtdNetCshFcstDtls.deleter
	def EstmtdNetCshFcstDtls(self):
		del self._EstmtdNetCshFcstDtls
		self._EstmtdNetCshFcstDtls = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if type(value) != auto else self.make_default("TradDtTm")

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = None

	@property
	def PrvsTtlNAV(self):
		return self._PrvsTtlNAV

	@PrvsTtlNAV.setter
	def PrvsTtlNAV(self, value):
		self._PrvsTtlNAV = value if type(value) != auto else self.make_default("PrvsTtlNAV")

	@PrvsTtlNAV.deleter
	def PrvsTtlNAV(self):
		del self._PrvsTtlNAV
		self._PrvsTtlNAV = None

	@property
	def BrkdwnByPty(self):
		return self._BrkdwnByPty

	@BrkdwnByPty.setter
	def BrkdwnByPty(self, value):
		self._BrkdwnByPty = value if type(value) != auto else self.make_default("BrkdwnByPty")

	@BrkdwnByPty.deleter
	def BrkdwnByPty(self):
		del self._BrkdwnByPty
		self._BrkdwnByPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkdwnByCcy', type=BreakdownByCurrency2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='XcptnlNetCshFlowInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pric', type=UnitPrice19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXRate', type=ForeignExchangeTerms19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcySts', type=CurrencyDesignation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkdwnByCtry', type=BreakdownByCountry2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlNAVChngRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdPctgOfShrClssTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkdwnByUsrDfndParam', type=BreakdownByUserDefinedParameter3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdNetCshFcstDtls', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrkdwnByPty', type=BreakdownByParty3, min=0, max=None, mutex_group=None, array=True),
	))

