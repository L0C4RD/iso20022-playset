from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._CashInOutForecast7 import CashInOutForecast7
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from ._LEIIdentifier import LEIIdentifier
from ._Max350Text import Max350Text
from ._NetCashForecast5 import NetCashForecast5
from ._OtherIdentification4 import OtherIdentification4
from ._PercentageRate import PercentageRate

class Fund1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_EstmtdCshInFcstDtls", "_EstmtdCshOutFcstDtls", "_EstmtdNetCshFcstDtls", "_EstmtdPctgOfFndTtlNAV", "_EstmtdTtlNAV", "_EstmtdTtlUnitsNb", "_Id", "_LglNttyIdr", "_Nm", "_PrvsTradDtTm", "_PrvsTtlNAV", "_PrvsTtlUnitsNb", "_TradDtTm"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

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
	def EstmtdPctgOfFndTtlNAV(self):
		return self._EstmtdPctgOfFndTtlNAV

	@EstmtdPctgOfFndTtlNAV.setter
	def EstmtdPctgOfFndTtlNAV(self, value):
		self._EstmtdPctgOfFndTtlNAV = value if type(value) != base_types.auto else self.make_default("EstmtdPctgOfFndTtlNAV")

	@EstmtdPctgOfFndTtlNAV.deleter
	def EstmtdPctgOfFndTtlNAV(self):
		del self._EstmtdPctgOfFndTtlNAV
		self._EstmtdPctgOfFndTtlNAV = None

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
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if type(value) != base_types.auto else self.make_default("LglNttyIdr")

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdCshInFcstDtls', type=CashInOutForecast7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdCshOutFcstDtls', type=CashInOutForecast7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdNetCshFcstDtls', type=NetCashForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EstmtdPctgOfFndTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=OtherIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
	))

