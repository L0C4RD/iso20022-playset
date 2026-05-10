import base_types
import DateAndDateTimeChoice
import ValuationStatistics3
import EventFrequency1Code
import YesNoIndicator
import ValuationTiming1Code
import UnitPrice15
import Max35Text
import PerformanceFactors1
import PartyIdentification2Choice
import ActiveOrHistoricCurrencyAndAmount
import FinancialInstrumentQuantity1
import FinancialInstrument8

class PriceValuation4(base_types._BaseFieldType):

	__slots__ = ["_FndMgmtCpny", "_FinInstrmDtls", "_TtlUnitsNb", "_OffclValtnInd", "_ValtnFrqcy", "_ValtnTp", "_NAVDtTm", "_Id", "_ValtnSttstcs", "_TtlNAV", "_PrfrmncDtls", "_NxtValtnDtTm", "_PrvsValtnDtTm", "_ValtnDtTm", "_PricDtls", "_SspdInd"]
	@property
	def FndMgmtCpny(self):
		return self._FndMgmtCpny

	@FndMgmtCpny.setter
	def FndMgmtCpny(self, value):
		self._FndMgmtCpny = value if type(value) != auto else self.make_default("FndMgmtCpny")

	@FndMgmtCpny.deleter
	def FndMgmtCpny(self):
		del self._FndMgmtCpny
		self._FndMgmtCpny = None

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
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if type(value) != auto else self.make_default("TtlUnitsNb")

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = None

	@property
	def OffclValtnInd(self):
		return self._OffclValtnInd

	@OffclValtnInd.setter
	def OffclValtnInd(self, value):
		self._OffclValtnInd = value if type(value) != auto else self.make_default("OffclValtnInd")

	@OffclValtnInd.deleter
	def OffclValtnInd(self):
		del self._OffclValtnInd
		self._OffclValtnInd = None

	@property
	def ValtnFrqcy(self):
		return self._ValtnFrqcy

	@ValtnFrqcy.setter
	def ValtnFrqcy(self, value):
		self._ValtnFrqcy = value if type(value) != auto else self.make_default("ValtnFrqcy")

	@ValtnFrqcy.deleter
	def ValtnFrqcy(self):
		del self._ValtnFrqcy
		self._ValtnFrqcy = None

	@property
	def ValtnTp(self):
		return self._ValtnTp

	@ValtnTp.setter
	def ValtnTp(self, value):
		self._ValtnTp = value if type(value) != auto else self.make_default("ValtnTp")

	@ValtnTp.deleter
	def ValtnTp(self):
		del self._ValtnTp
		self._ValtnTp = None

	@property
	def NAVDtTm(self):
		return self._NAVDtTm

	@NAVDtTm.setter
	def NAVDtTm(self, value):
		self._NAVDtTm = value if type(value) != auto else self.make_default("NAVDtTm")

	@NAVDtTm.deleter
	def NAVDtTm(self):
		del self._NAVDtTm
		self._NAVDtTm = None

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
	def ValtnSttstcs(self):
		return self._ValtnSttstcs

	@ValtnSttstcs.setter
	def ValtnSttstcs(self, value):
		self._ValtnSttstcs = value if type(value) != auto else self.make_default("ValtnSttstcs")

	@ValtnSttstcs.deleter
	def ValtnSttstcs(self):
		del self._ValtnSttstcs
		self._ValtnSttstcs = None

	@property
	def TtlNAV(self):
		return self._TtlNAV

	@TtlNAV.setter
	def TtlNAV(self, value):
		self._TtlNAV = value if type(value) != auto else self.make_default("TtlNAV")

	@TtlNAV.deleter
	def TtlNAV(self):
		del self._TtlNAV
		self._TtlNAV = None

	@property
	def PrfrmncDtls(self):
		return self._PrfrmncDtls

	@PrfrmncDtls.setter
	def PrfrmncDtls(self, value):
		self._PrfrmncDtls = value if type(value) != auto else self.make_default("PrfrmncDtls")

	@PrfrmncDtls.deleter
	def PrfrmncDtls(self):
		del self._PrfrmncDtls
		self._PrfrmncDtls = None

	@property
	def NxtValtnDtTm(self):
		return self._NxtValtnDtTm

	@NxtValtnDtTm.setter
	def NxtValtnDtTm(self, value):
		self._NxtValtnDtTm = value if type(value) != auto else self.make_default("NxtValtnDtTm")

	@NxtValtnDtTm.deleter
	def NxtValtnDtTm(self):
		del self._NxtValtnDtTm
		self._NxtValtnDtTm = None

	@property
	def PrvsValtnDtTm(self):
		return self._PrvsValtnDtTm

	@PrvsValtnDtTm.setter
	def PrvsValtnDtTm(self, value):
		self._PrvsValtnDtTm = value if type(value) != auto else self.make_default("PrvsValtnDtTm")

	@PrvsValtnDtTm.deleter
	def PrvsValtnDtTm(self):
		del self._PrvsValtnDtTm
		self._PrvsValtnDtTm = None

	@property
	def ValtnDtTm(self):
		return self._ValtnDtTm

	@ValtnDtTm.setter
	def ValtnDtTm(self, value):
		self._ValtnDtTm = value if type(value) != auto else self.make_default("ValtnDtTm")

	@ValtnDtTm.deleter
	def ValtnDtTm(self):
		del self._ValtnDtTm
		self._ValtnDtTm = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def SspdInd(self):
		return self._SspdInd

	@SspdInd.setter
	def SspdInd(self, value):
		self._SspdInd = value if type(value) != auto else self.make_default("SspdInd")

	@SspdInd.deleter
	def SspdInd(self):
		del self._SspdInd
		self._SspdInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FndMgmtCpny', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclValtnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFrqcy', type=EventFrequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnTp', type=ValuationTiming1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NAVDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnSttstcs', type=ValuationStatistics3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrfrmncDtls', type=PerformanceFactors1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtValtnDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsValtnDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SspdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

