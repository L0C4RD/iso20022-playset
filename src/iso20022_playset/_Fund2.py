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

class Fund2(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_CshInFcstDtls", "_CshOutFcstDtls", "_Id", "_LglNttyIdr", "_NetCshFcstDtls", "_Nm", "_PctgOfFndTtlNAV", "_PrvsTradDtTm", "_PrvsTtlNAV", "_PrvsTtlUnitsNb", "_TradDtTm", "_TtlNAV", "_TtlUnitsNb"]
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
	def CshInFcstDtls(self):
		return self._CshInFcstDtls

	@CshInFcstDtls.setter
	def CshInFcstDtls(self, value):
		self._CshInFcstDtls = value if type(value) != base_types.auto else self.make_default("CshInFcstDtls")

	@CshInFcstDtls.deleter
	def CshInFcstDtls(self):
		del self._CshInFcstDtls
		self._CshInFcstDtls = None

	@property
	def CshOutFcstDtls(self):
		return self._CshOutFcstDtls

	@CshOutFcstDtls.setter
	def CshOutFcstDtls(self, value):
		self._CshOutFcstDtls = value if type(value) != base_types.auto else self.make_default("CshOutFcstDtls")

	@CshOutFcstDtls.deleter
	def CshOutFcstDtls(self):
		del self._CshOutFcstDtls
		self._CshOutFcstDtls = None

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
	def PctgOfFndTtlNAV(self):
		return self._PctgOfFndTtlNAV

	@PctgOfFndTtlNAV.setter
	def PctgOfFndTtlNAV(self, value):
		self._PctgOfFndTtlNAV = value if type(value) != base_types.auto else self.make_default("PctgOfFndTtlNAV")

	@PctgOfFndTtlNAV.deleter
	def PctgOfFndTtlNAV(self):
		del self._PctgOfFndTtlNAV
		self._PctgOfFndTtlNAV = None

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
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshInFcstDtls', type=CashInOutForecast7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshOutFcstDtls', type=CashInOutForecast7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=OtherIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetCshFcstDtls', type=NetCashForecast5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfFndTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))

