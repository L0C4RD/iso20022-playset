# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import DateAndDateTime2Choice
from . import EventFrequency1Code
from . import FinancialInstrument106
from . import FinancialInstrumentQuantity1
from . import Max35Text
from . import PartyIdentification125Choice
from . import PerformanceFactors5
from . import UnitPrice24
from . import ValuationStatistics4
from . import ValuationTiming1Code
from . import YesNoIndicator

class PriceValuation5(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmDtls", "_FndMgmtCpny", "_Id", "_NAVDtTm", "_NxtValtnDtTm", "_OffclValtnInd", "_PrfrmncDtls", "_PricDtls", "_PrvsValtnDtTm", "_SspdInd", "_TtlNAV", "_TtlUnitsNb", "_ValtnDtTm", "_ValtnFrqcy", "_ValtnSttstcs", "_ValtnTp"]
	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument106, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument106, False)

	@property
	def FndMgmtCpny(self):
		return self._FndMgmtCpny

	@FndMgmtCpny.setter
	def FndMgmtCpny(self, value):
		self._FndMgmtCpny = value if value is not None else base_types.UninitialisedField(self, 'FndMgmtCpny', PartyIdentification125Choice, False)

	@FndMgmtCpny.deleter
	def FndMgmtCpny(self):
		del self._FndMgmtCpny
		self._FndMgmtCpny = base_types.UninitialisedField(self, 'FndMgmtCpny', PartyIdentification125Choice, False)

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
	def NAVDtTm(self):
		return self._NAVDtTm

	@NAVDtTm.setter
	def NAVDtTm(self, value):
		self._NAVDtTm = value if value is not None else base_types.UninitialisedField(self, 'NAVDtTm', DateAndDateTime2Choice, False)

	@NAVDtTm.deleter
	def NAVDtTm(self):
		del self._NAVDtTm
		self._NAVDtTm = base_types.UninitialisedField(self, 'NAVDtTm', DateAndDateTime2Choice, False)

	@property
	def NxtValtnDtTm(self):
		return self._NxtValtnDtTm

	@NxtValtnDtTm.setter
	def NxtValtnDtTm(self, value):
		self._NxtValtnDtTm = value if value is not None else base_types.UninitialisedField(self, 'NxtValtnDtTm', DateAndDateTime2Choice, False)

	@NxtValtnDtTm.deleter
	def NxtValtnDtTm(self):
		del self._NxtValtnDtTm
		self._NxtValtnDtTm = base_types.UninitialisedField(self, 'NxtValtnDtTm', DateAndDateTime2Choice, False)

	@property
	def OffclValtnInd(self):
		return self._OffclValtnInd

	@OffclValtnInd.setter
	def OffclValtnInd(self, value):
		self._OffclValtnInd = value if value is not None else base_types.UninitialisedField(self, 'OffclValtnInd', YesNoIndicator, False)

	@OffclValtnInd.deleter
	def OffclValtnInd(self):
		del self._OffclValtnInd
		self._OffclValtnInd = base_types.UninitialisedField(self, 'OffclValtnInd', YesNoIndicator, False)

	@property
	def PrfrmncDtls(self):
		return self._PrfrmncDtls

	@PrfrmncDtls.setter
	def PrfrmncDtls(self, value):
		self._PrfrmncDtls = value if value is not None else base_types.UninitialisedField(self, 'PrfrmncDtls', PerformanceFactors5, False)

	@PrfrmncDtls.deleter
	def PrfrmncDtls(self):
		del self._PrfrmncDtls
		self._PrfrmncDtls = base_types.UninitialisedField(self, 'PrfrmncDtls', PerformanceFactors5, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', UnitPrice24, True)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', UnitPrice24, True)

	@property
	def PrvsValtnDtTm(self):
		return self._PrvsValtnDtTm

	@PrvsValtnDtTm.setter
	def PrvsValtnDtTm(self, value):
		self._PrvsValtnDtTm = value if value is not None else base_types.UninitialisedField(self, 'PrvsValtnDtTm', DateAndDateTime2Choice, False)

	@PrvsValtnDtTm.deleter
	def PrvsValtnDtTm(self):
		del self._PrvsValtnDtTm
		self._PrvsValtnDtTm = base_types.UninitialisedField(self, 'PrvsValtnDtTm', DateAndDateTime2Choice, False)

	@property
	def SspdInd(self):
		return self._SspdInd

	@SspdInd.setter
	def SspdInd(self, value):
		self._SspdInd = value if value is not None else base_types.UninitialisedField(self, 'SspdInd', YesNoIndicator, False)

	@SspdInd.deleter
	def SspdInd(self):
		del self._SspdInd
		self._SspdInd = base_types.UninitialisedField(self, 'SspdInd', YesNoIndicator, False)

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
	def ValtnDtTm(self):
		return self._ValtnDtTm

	@ValtnDtTm.setter
	def ValtnDtTm(self, value):
		self._ValtnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ValtnDtTm', DateAndDateTime2Choice, False)

	@ValtnDtTm.deleter
	def ValtnDtTm(self):
		del self._ValtnDtTm
		self._ValtnDtTm = base_types.UninitialisedField(self, 'ValtnDtTm', DateAndDateTime2Choice, False)

	@property
	def ValtnFrqcy(self):
		return self._ValtnFrqcy

	@ValtnFrqcy.setter
	def ValtnFrqcy(self, value):
		self._ValtnFrqcy = value if value is not None else base_types.UninitialisedField(self, 'ValtnFrqcy', EventFrequency1Code, False)

	@ValtnFrqcy.deleter
	def ValtnFrqcy(self):
		del self._ValtnFrqcy
		self._ValtnFrqcy = base_types.UninitialisedField(self, 'ValtnFrqcy', EventFrequency1Code, False)

	@property
	def ValtnSttstcs(self):
		return self._ValtnSttstcs

	@ValtnSttstcs.setter
	def ValtnSttstcs(self, value):
		self._ValtnSttstcs = value if value is not None else base_types.UninitialisedField(self, 'ValtnSttstcs', ValuationStatistics4, True)

	@ValtnSttstcs.deleter
	def ValtnSttstcs(self):
		del self._ValtnSttstcs
		self._ValtnSttstcs = base_types.UninitialisedField(self, 'ValtnSttstcs', ValuationStatistics4, True)

	@property
	def ValtnTp(self):
		return self._ValtnTp

	@ValtnTp.setter
	def ValtnTp(self, value):
		self._ValtnTp = value if value is not None else base_types.UninitialisedField(self, 'ValtnTp', ValuationTiming1Code, False)

	@ValtnTp.deleter
	def ValtnTp(self):
		del self._ValtnTp
		self._ValtnTp = base_types.UninitialisedField(self, 'ValtnTp', ValuationTiming1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument106, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FndMgmtCpny', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NAVDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtValtnDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclValtnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrfrmncDtls', type=PerformanceFactors5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice24, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsValtnDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SspdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnFrqcy', type=EventFrequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnSttstcs', type=ValuationStatistics4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValtnTp', type=ValuationTiming1Code, min=1, max=1, mutex_group=None, array=False),
	))