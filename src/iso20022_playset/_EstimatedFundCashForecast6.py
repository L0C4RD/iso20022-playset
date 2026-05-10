from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._CashInForecast6 import CashInForecast6
from ._CashOutForecast6 import CashOutForecast6
from ._CurrencyDesignation1 import CurrencyDesignation1
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._FinancialInstrument9 import FinancialInstrument9
from ._FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from ._ForeignExchangeTerms19 import ForeignExchangeTerms19
from ._Max35Text import Max35Text
from ._NetCashForecast4 import NetCashForecast4
from ._PercentageRate import PercentageRate
from ._UnitPrice19 import UnitPrice19
from ._YesNoIndicator import YesNoIndicator

class EstimatedFundCashForecast6(base_types._BaseFieldType):

	__slots__ = ["_CcySts", "_EstmtdCshInFcstDtls", "_EstmtdCshOutFcstDtls", "_EstmtdNetCshFcstDtls", "_EstmtdPctgOfShrClssTtlNAV", "_EstmtdTtlNAV", "_EstmtdTtlNAVChngRate", "_EstmtdTtlUnitsNb", "_FXRate", "_FinInstrmDtls", "_Id", "_InvstmtCcy", "_Pric", "_PrvsTradDtTm", "_PrvsTtlNAV", "_PrvsTtlUnitsNb", "_TradDtTm", "_XcptnlNetCshFlowInd"]
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
	def EstmtdCshInFcstDtls(self):
		return self._EstmtdCshInFcstDtls

	@EstmtdCshInFcstDtls.setter
	def EstmtdCshInFcstDtls(self, value):
		self._EstmtdCshInFcstDtls = value if type(value) != base_types.auto else self.make_default("EstmtdCshInFcstDtls")

	@EstmtdCshInFcstDtls.deleter
	def EstmtdCshInFcstDtls(self):
		del self._EstmtdCshInFcstDtls
		self._EstmtdCshInFcstDtls = None

	@property
	def EstmtdCshOutFcstDtls(self):
		return self._EstmtdCshOutFcstDtls

	@EstmtdCshOutFcstDtls.setter
	def EstmtdCshOutFcstDtls(self, value):
		self._EstmtdCshOutFcstDtls = value if type(value) != base_types.auto else self.make_default("EstmtdCshOutFcstDtls")

	@EstmtdCshOutFcstDtls.deleter
	def EstmtdCshOutFcstDtls(self):
		del self._EstmtdCshOutFcstDtls
		self._EstmtdCshOutFcstDtls = None

	@property
	def EstmtdNetCshFcstDtls(self):
		return self._EstmtdNetCshFcstDtls

	@EstmtdNetCshFcstDtls.setter
	def EstmtdNetCshFcstDtls(self, value):
		self._EstmtdNetCshFcstDtls = value if type(value) != base_types.auto else self.make_default("EstmtdNetCshFcstDtls")

	@EstmtdNetCshFcstDtls.deleter
	def EstmtdNetCshFcstDtls(self):
		del self._EstmtdNetCshFcstDtls
		self._EstmtdNetCshFcstDtls = None

	@property
	def EstmtdPctgOfShrClssTtlNAV(self):
		return self._EstmtdPctgOfShrClssTtlNAV

	@EstmtdPctgOfShrClssTtlNAV.setter
	def EstmtdPctgOfShrClssTtlNAV(self, value):
		self._EstmtdPctgOfShrClssTtlNAV = value if type(value) != base_types.auto else self.make_default("EstmtdPctgOfShrClssTtlNAV")

	@EstmtdPctgOfShrClssTtlNAV.deleter
	def EstmtdPctgOfShrClssTtlNAV(self):
		del self._EstmtdPctgOfShrClssTtlNAV
		self._EstmtdPctgOfShrClssTtlNAV = None

	@property
	def EstmtdTtlNAV(self):
		return self._EstmtdTtlNAV

	@EstmtdTtlNAV.setter
	def EstmtdTtlNAV(self, value):
		self._EstmtdTtlNAV = value if type(value) != base_types.auto else self.make_default("EstmtdTtlNAV")

	@EstmtdTtlNAV.deleter
	def EstmtdTtlNAV(self):
		del self._EstmtdTtlNAV
		self._EstmtdTtlNAV = None

	@property
	def EstmtdTtlNAVChngRate(self):
		return self._EstmtdTtlNAVChngRate

	@EstmtdTtlNAVChngRate.setter
	def EstmtdTtlNAVChngRate(self, value):
		self._EstmtdTtlNAVChngRate = value if type(value) != base_types.auto else self.make_default("EstmtdTtlNAVChngRate")

	@EstmtdTtlNAVChngRate.deleter
	def EstmtdTtlNAVChngRate(self):
		del self._EstmtdTtlNAVChngRate
		self._EstmtdTtlNAVChngRate = None

	@property
	def EstmtdTtlUnitsNb(self):
		return self._EstmtdTtlUnitsNb

	@EstmtdTtlUnitsNb.setter
	def EstmtdTtlUnitsNb(self, value):
		self._EstmtdTtlUnitsNb = value if type(value) != base_types.auto else self.make_default("EstmtdTtlUnitsNb")

	@EstmtdTtlUnitsNb.deleter
	def EstmtdTtlUnitsNb(self):
		del self._EstmtdTtlUnitsNb
		self._EstmtdTtlUnitsNb = None

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
	def XcptnlNetCshFlowInd(self):
		return self._XcptnlNetCshFlowInd

	@XcptnlNetCshFlowInd.setter
	def XcptnlNetCshFlowInd(self, value):
		self._XcptnlNetCshFlowInd = value if type(value) != base_types.auto else self.make_default("XcptnlNetCshFlowInd")

	@XcptnlNetCshFlowInd.deleter
	def XcptnlNetCshFlowInd(self):
		del self._XcptnlNetCshFlowInd
		self._XcptnlNetCshFlowInd = None

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

