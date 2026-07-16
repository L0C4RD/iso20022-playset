# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ActiveOrHistoricCurrencyCode
from . import BreakdownByCountry2
from . import BreakdownByCurrency2
from . import BreakdownByParty3
from . import BreakdownByUserDefinedParameter3
from . import CurrencyDesignation1
from . import DateAndDateTimeChoice
from . import FinancialInstrument9
from . import FinancialInstrumentQuantity1
from . import ForeignExchangeTerms19
from . import Max35Text
from . import NetCashForecast4
from . import PercentageRate
from . import UnitPrice19
from . import YesNoIndicator

class FundCashForecast6(base_types._BaseFieldType):

	__slots__ = ["_BrkdwnByCcy", "_BrkdwnByCtry", "_BrkdwnByPty", "_BrkdwnByUsrDfndParam", "_CcySts", "_FXRate", "_FinInstrmDtls", "_Id", "_InvstmtCcy", "_NetCshFcstDtls", "_PctgOfShrClssTtlNAV", "_Pric", "_PrvsTradDtTm", "_PrvsTtlNAV", "_PrvsTtlUnitsNb", "_TradDtTm", "_TtlNAV", "_TtlNAVChngRate", "_TtlUnitsNb", "_XcptnlNetCshFlowInd"]
	@property
	def BrkdwnByCcy(self):
		return self._BrkdwnByCcy

	@BrkdwnByCcy.setter
	def BrkdwnByCcy(self, value):
		self._BrkdwnByCcy = value if value is not None else base_types.UninitialisedField(self, 'BrkdwnByCcy', BreakdownByCurrency2, True)

	@BrkdwnByCcy.deleter
	def BrkdwnByCcy(self):
		del self._BrkdwnByCcy
		self._BrkdwnByCcy = base_types.UninitialisedField(self, 'BrkdwnByCcy', BreakdownByCurrency2, True)

	@property
	def BrkdwnByCtry(self):
		return self._BrkdwnByCtry

	@BrkdwnByCtry.setter
	def BrkdwnByCtry(self, value):
		self._BrkdwnByCtry = value if value is not None else base_types.UninitialisedField(self, 'BrkdwnByCtry', BreakdownByCountry2, True)

	@BrkdwnByCtry.deleter
	def BrkdwnByCtry(self):
		del self._BrkdwnByCtry
		self._BrkdwnByCtry = base_types.UninitialisedField(self, 'BrkdwnByCtry', BreakdownByCountry2, True)

	@property
	def BrkdwnByPty(self):
		return self._BrkdwnByPty

	@BrkdwnByPty.setter
	def BrkdwnByPty(self, value):
		self._BrkdwnByPty = value if value is not None else base_types.UninitialisedField(self, 'BrkdwnByPty', BreakdownByParty3, True)

	@BrkdwnByPty.deleter
	def BrkdwnByPty(self):
		del self._BrkdwnByPty
		self._BrkdwnByPty = base_types.UninitialisedField(self, 'BrkdwnByPty', BreakdownByParty3, True)

	@property
	def BrkdwnByUsrDfndParam(self):
		return self._BrkdwnByUsrDfndParam

	@BrkdwnByUsrDfndParam.setter
	def BrkdwnByUsrDfndParam(self, value):
		self._BrkdwnByUsrDfndParam = value if value is not None else base_types.UninitialisedField(self, 'BrkdwnByUsrDfndParam', BreakdownByUserDefinedParameter3, True)

	@BrkdwnByUsrDfndParam.deleter
	def BrkdwnByUsrDfndParam(self):
		del self._BrkdwnByUsrDfndParam
		self._BrkdwnByUsrDfndParam = base_types.UninitialisedField(self, 'BrkdwnByUsrDfndParam', BreakdownByUserDefinedParameter3, True)

	@property
	def CcySts(self):
		return self._CcySts

	@CcySts.setter
	def CcySts(self, value):
		self._CcySts = value if value is not None else base_types.UninitialisedField(self, 'CcySts', CurrencyDesignation1, False)

	@CcySts.deleter
	def CcySts(self):
		del self._CcySts
		self._CcySts = base_types.UninitialisedField(self, 'CcySts', CurrencyDesignation1, False)

	@property
	def FXRate(self):
		return self._FXRate

	@FXRate.setter
	def FXRate(self, value):
		self._FXRate = value if value is not None else base_types.UninitialisedField(self, 'FXRate', ForeignExchangeTerms19, False)

	@FXRate.deleter
	def FXRate(self):
		del self._FXRate
		self._FXRate = base_types.UninitialisedField(self, 'FXRate', ForeignExchangeTerms19, False)

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument9, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument9, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def InvstmtCcy(self):
		return self._InvstmtCcy

	@InvstmtCcy.setter
	def InvstmtCcy(self, value):
		self._InvstmtCcy = value if value is not None else base_types.UninitialisedField(self, 'InvstmtCcy', ActiveOrHistoricCurrencyCode, True)

	@InvstmtCcy.deleter
	def InvstmtCcy(self):
		del self._InvstmtCcy
		self._InvstmtCcy = base_types.UninitialisedField(self, 'InvstmtCcy', ActiveOrHistoricCurrencyCode, True)

	@property
	def NetCshFcstDtls(self):
		return self._NetCshFcstDtls

	@NetCshFcstDtls.setter
	def NetCshFcstDtls(self, value):
		self._NetCshFcstDtls = value if value is not None else base_types.UninitialisedField(self, 'NetCshFcstDtls', NetCashForecast4, True)

	@NetCshFcstDtls.deleter
	def NetCshFcstDtls(self):
		del self._NetCshFcstDtls
		self._NetCshFcstDtls = base_types.UninitialisedField(self, 'NetCshFcstDtls', NetCashForecast4, True)

	@property
	def PctgOfShrClssTtlNAV(self):
		return self._PctgOfShrClssTtlNAV

	@PctgOfShrClssTtlNAV.setter
	def PctgOfShrClssTtlNAV(self, value):
		self._PctgOfShrClssTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'PctgOfShrClssTtlNAV', PercentageRate, False)

	@PctgOfShrClssTtlNAV.deleter
	def PctgOfShrClssTtlNAV(self):
		del self._PctgOfShrClssTtlNAV
		self._PctgOfShrClssTtlNAV = base_types.UninitialisedField(self, 'PctgOfShrClssTtlNAV', PercentageRate, False)

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if value is not None else base_types.UninitialisedField(self, 'Pric', UnitPrice19, False)

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = base_types.UninitialisedField(self, 'Pric', UnitPrice19, False)

	@property
	def PrvsTradDtTm(self):
		return self._PrvsTradDtTm

	@PrvsTradDtTm.setter
	def PrvsTradDtTm(self, value):
		self._PrvsTradDtTm = value if value is not None else base_types.UninitialisedField(self, 'PrvsTradDtTm', DateAndDateTimeChoice, False)

	@PrvsTradDtTm.deleter
	def PrvsTradDtTm(self):
		del self._PrvsTradDtTm
		self._PrvsTradDtTm = base_types.UninitialisedField(self, 'PrvsTradDtTm', DateAndDateTimeChoice, False)

	@property
	def PrvsTtlNAV(self):
		return self._PrvsTtlNAV

	@PrvsTtlNAV.setter
	def PrvsTtlNAV(self, value):
		self._PrvsTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'PrvsTtlNAV', ActiveOrHistoricCurrencyAndAmount, True)

	@PrvsTtlNAV.deleter
	def PrvsTtlNAV(self):
		del self._PrvsTtlNAV
		self._PrvsTtlNAV = base_types.UninitialisedField(self, 'PrvsTtlNAV', ActiveOrHistoricCurrencyAndAmount, True)

	@property
	def PrvsTtlUnitsNb(self):
		return self._PrvsTtlUnitsNb

	@PrvsTtlUnitsNb.setter
	def PrvsTtlUnitsNb(self, value):
		self._PrvsTtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'PrvsTtlUnitsNb', FinancialInstrumentQuantity1, False)

	@PrvsTtlUnitsNb.deleter
	def PrvsTtlUnitsNb(self):
		del self._PrvsTtlUnitsNb
		self._PrvsTtlUnitsNb = base_types.UninitialisedField(self, 'PrvsTtlUnitsNb', FinancialInstrumentQuantity1, False)

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if value is not None else base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTimeChoice, False)

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTimeChoice, False)

	@property
	def TtlNAV(self):
		return self._TtlNAV

	@TtlNAV.setter
	def TtlNAV(self, value):
		self._TtlNAV = value if value is not None else base_types.UninitialisedField(self, 'TtlNAV', ActiveOrHistoricCurrencyAndAmount, True)

	@TtlNAV.deleter
	def TtlNAV(self):
		del self._TtlNAV
		self._TtlNAV = base_types.UninitialisedField(self, 'TtlNAV', ActiveOrHistoricCurrencyAndAmount, True)

	@property
	def TtlNAVChngRate(self):
		return self._TtlNAVChngRate

	@TtlNAVChngRate.setter
	def TtlNAVChngRate(self, value):
		self._TtlNAVChngRate = value if value is not None else base_types.UninitialisedField(self, 'TtlNAVChngRate', PercentageRate, False)

	@TtlNAVChngRate.deleter
	def TtlNAVChngRate(self):
		del self._TtlNAVChngRate
		self._TtlNAVChngRate = base_types.UninitialisedField(self, 'TtlNAVChngRate', PercentageRate, False)

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsNb', FinancialInstrumentQuantity1, False)

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = base_types.UninitialisedField(self, 'TtlUnitsNb', FinancialInstrumentQuantity1, False)

	@property
	def XcptnlNetCshFlowInd(self):
		return self._XcptnlNetCshFlowInd

	@XcptnlNetCshFlowInd.setter
	def XcptnlNetCshFlowInd(self, value):
		self._XcptnlNetCshFlowInd = value if value is not None else base_types.UninitialisedField(self, 'XcptnlNetCshFlowInd', YesNoIndicator, False)

	@XcptnlNetCshFlowInd.deleter
	def XcptnlNetCshFlowInd(self):
		del self._XcptnlNetCshFlowInd
		self._XcptnlNetCshFlowInd = base_types.UninitialisedField(self, 'XcptnlNetCshFlowInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrkdwnByCcy', type=BreakdownByCurrency2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrkdwnByCtry', type=BreakdownByCountry2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrkdwnByPty', type=BreakdownByParty3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrkdwnByUsrDfndParam', type=BreakdownByUserDefinedParameter3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CcySts', type=CurrencyDesignation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXRate', type=ForeignExchangeTerms19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetCshFcstDtls', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PctgOfShrClssTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=UnitPrice19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNAVChngRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcptnlNetCshFlowInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))