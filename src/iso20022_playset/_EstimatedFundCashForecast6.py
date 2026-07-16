# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ActiveOrHistoricCurrencyCode
from . import CashInForecast6
from . import CashOutForecast6
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

class EstimatedFundCashForecast6(base_types._BaseFieldType):

	__slots__ = ["_CcySts", "_EstmtdCshInFcstDtls", "_EstmtdCshOutFcstDtls", "_EstmtdNetCshFcstDtls", "_EstmtdPctgOfShrClssTtlNAV", "_EstmtdTtlNAV", "_EstmtdTtlNAVChngRate", "_EstmtdTtlUnitsNb", "_FXRate", "_FinInstrmDtls", "_Id", "_InvstmtCcy", "_Pric", "_PrvsTradDtTm", "_PrvsTtlNAV", "_PrvsTtlUnitsNb", "_TradDtTm", "_XcptnlNetCshFlowInd"]
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
	def EstmtdCshInFcstDtls(self):
		return self._EstmtdCshInFcstDtls

	@EstmtdCshInFcstDtls.setter
	def EstmtdCshInFcstDtls(self, value):
		self._EstmtdCshInFcstDtls = value if value is not None else base_types.UninitialisedField(self, 'EstmtdCshInFcstDtls', CashInForecast6, True)

	@EstmtdCshInFcstDtls.deleter
	def EstmtdCshInFcstDtls(self):
		del self._EstmtdCshInFcstDtls
		self._EstmtdCshInFcstDtls = base_types.UninitialisedField(self, 'EstmtdCshInFcstDtls', CashInForecast6, True)

	@property
	def EstmtdCshOutFcstDtls(self):
		return self._EstmtdCshOutFcstDtls

	@EstmtdCshOutFcstDtls.setter
	def EstmtdCshOutFcstDtls(self, value):
		self._EstmtdCshOutFcstDtls = value if value is not None else base_types.UninitialisedField(self, 'EstmtdCshOutFcstDtls', CashOutForecast6, True)

	@EstmtdCshOutFcstDtls.deleter
	def EstmtdCshOutFcstDtls(self):
		del self._EstmtdCshOutFcstDtls
		self._EstmtdCshOutFcstDtls = base_types.UninitialisedField(self, 'EstmtdCshOutFcstDtls', CashOutForecast6, True)

	@property
	def EstmtdNetCshFcstDtls(self):
		return self._EstmtdNetCshFcstDtls

	@EstmtdNetCshFcstDtls.setter
	def EstmtdNetCshFcstDtls(self, value):
		self._EstmtdNetCshFcstDtls = value if value is not None else base_types.UninitialisedField(self, 'EstmtdNetCshFcstDtls', NetCashForecast4, True)

	@EstmtdNetCshFcstDtls.deleter
	def EstmtdNetCshFcstDtls(self):
		del self._EstmtdNetCshFcstDtls
		self._EstmtdNetCshFcstDtls = base_types.UninitialisedField(self, 'EstmtdNetCshFcstDtls', NetCashForecast4, True)

	@property
	def EstmtdPctgOfShrClssTtlNAV(self):
		return self._EstmtdPctgOfShrClssTtlNAV

	@EstmtdPctgOfShrClssTtlNAV.setter
	def EstmtdPctgOfShrClssTtlNAV(self, value):
		self._EstmtdPctgOfShrClssTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'EstmtdPctgOfShrClssTtlNAV', PercentageRate, False)

	@EstmtdPctgOfShrClssTtlNAV.deleter
	def EstmtdPctgOfShrClssTtlNAV(self):
		del self._EstmtdPctgOfShrClssTtlNAV
		self._EstmtdPctgOfShrClssTtlNAV = base_types.UninitialisedField(self, 'EstmtdPctgOfShrClssTtlNAV', PercentageRate, False)

	@property
	def EstmtdTtlNAV(self):
		return self._EstmtdTtlNAV

	@EstmtdTtlNAV.setter
	def EstmtdTtlNAV(self, value):
		self._EstmtdTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'EstmtdTtlNAV', ActiveOrHistoricCurrencyAndAmount, True)

	@EstmtdTtlNAV.deleter
	def EstmtdTtlNAV(self):
		del self._EstmtdTtlNAV
		self._EstmtdTtlNAV = base_types.UninitialisedField(self, 'EstmtdTtlNAV', ActiveOrHistoricCurrencyAndAmount, True)

	@property
	def EstmtdTtlNAVChngRate(self):
		return self._EstmtdTtlNAVChngRate

	@EstmtdTtlNAVChngRate.setter
	def EstmtdTtlNAVChngRate(self, value):
		self._EstmtdTtlNAVChngRate = value if value is not None else base_types.UninitialisedField(self, 'EstmtdTtlNAVChngRate', PercentageRate, False)

	@EstmtdTtlNAVChngRate.deleter
	def EstmtdTtlNAVChngRate(self):
		del self._EstmtdTtlNAVChngRate
		self._EstmtdTtlNAVChngRate = base_types.UninitialisedField(self, 'EstmtdTtlNAVChngRate', PercentageRate, False)

	@property
	def EstmtdTtlUnitsNb(self):
		return self._EstmtdTtlUnitsNb

	@EstmtdTtlUnitsNb.setter
	def EstmtdTtlUnitsNb(self, value):
		self._EstmtdTtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'EstmtdTtlUnitsNb', FinancialInstrumentQuantity1, False)

	@EstmtdTtlUnitsNb.deleter
	def EstmtdTtlUnitsNb(self):
		del self._EstmtdTtlUnitsNb
		self._EstmtdTtlUnitsNb = base_types.UninitialisedField(self, 'EstmtdTtlUnitsNb', FinancialInstrumentQuantity1, False)

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
		base_types.FieldEntry(name='CcySts', type=CurrencyDesignation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdCshInFcstDtls', type=CashInForecast6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdCshOutFcstDtls', type=CashOutForecast6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdNetCshFcstDtls', type=NetCashForecast4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdPctgOfShrClssTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdTtlNAVChngRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXRate', type=ForeignExchangeTerms19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pric', type=UnitPrice19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcptnlNetCshFlowInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))