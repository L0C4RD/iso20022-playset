# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._EventFrequency1Code import EventFrequency1Code
from ._FinancialInstrument106 import FinancialInstrument106
from ._FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from ._Max35Text import Max35Text
from ._PartyIdentification125Choice import PartyIdentification125Choice
from ._PerformanceFactors5 import PerformanceFactors5
from ._UnitPrice24 import UnitPrice24
from ._ValuationStatistics4 import ValuationStatistics4
from ._ValuationTiming1Code import ValuationTiming1Code
from ._YesNoIndicator import YesNoIndicator

class PriceValuation5(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmDtls", "_FndMgmtCpny", "_Id", "_NAVDtTm", "_NxtValtnDtTm", "_OffclValtnInd", "_PrfrmncDtls", "_PricDtls", "_PrvsValtnDtTm", "_SspdInd", "_TtlNAV", "_TtlUnitsNb", "_ValtnDtTm", "_ValtnFrqcy", "_ValtnSttstcs", "_ValtnTp"]
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
	def FndMgmtCpny(self):
		return self._FndMgmtCpny

	@FndMgmtCpny.setter
	def FndMgmtCpny(self, value):
		self._FndMgmtCpny = value if type(value) != base_types.auto else self.make_default("FndMgmtCpny")

	@FndMgmtCpny.deleter
	def FndMgmtCpny(self):
		del self._FndMgmtCpny
		self._FndMgmtCpny = None

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
	def NAVDtTm(self):
		return self._NAVDtTm

	@NAVDtTm.setter
	def NAVDtTm(self, value):
		self._NAVDtTm = value if type(value) != base_types.auto else self.make_default("NAVDtTm")

	@NAVDtTm.deleter
	def NAVDtTm(self):
		del self._NAVDtTm
		self._NAVDtTm = None

	@property
	def NxtValtnDtTm(self):
		return self._NxtValtnDtTm

	@NxtValtnDtTm.setter
	def NxtValtnDtTm(self, value):
		self._NxtValtnDtTm = value if type(value) != base_types.auto else self.make_default("NxtValtnDtTm")

	@NxtValtnDtTm.deleter
	def NxtValtnDtTm(self):
		del self._NxtValtnDtTm
		self._NxtValtnDtTm = None

	@property
	def OffclValtnInd(self):
		return self._OffclValtnInd

	@OffclValtnInd.setter
	def OffclValtnInd(self, value):
		self._OffclValtnInd = value if type(value) != base_types.auto else self.make_default("OffclValtnInd")

	@OffclValtnInd.deleter
	def OffclValtnInd(self):
		del self._OffclValtnInd
		self._OffclValtnInd = None

	@property
	def PrfrmncDtls(self):
		return self._PrfrmncDtls

	@PrfrmncDtls.setter
	def PrfrmncDtls(self, value):
		self._PrfrmncDtls = value if type(value) != base_types.auto else self.make_default("PrfrmncDtls")

	@PrfrmncDtls.deleter
	def PrfrmncDtls(self):
		del self._PrfrmncDtls
		self._PrfrmncDtls = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != base_types.auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def PrvsValtnDtTm(self):
		return self._PrvsValtnDtTm

	@PrvsValtnDtTm.setter
	def PrvsValtnDtTm(self, value):
		self._PrvsValtnDtTm = value if type(value) != base_types.auto else self.make_default("PrvsValtnDtTm")

	@PrvsValtnDtTm.deleter
	def PrvsValtnDtTm(self):
		del self._PrvsValtnDtTm
		self._PrvsValtnDtTm = None

	@property
	def SspdInd(self):
		return self._SspdInd

	@SspdInd.setter
	def SspdInd(self, value):
		self._SspdInd = value if type(value) != base_types.auto else self.make_default("SspdInd")

	@SspdInd.deleter
	def SspdInd(self):
		del self._SspdInd
		self._SspdInd = None

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

	@property
	def ValtnDtTm(self):
		return self._ValtnDtTm

	@ValtnDtTm.setter
	def ValtnDtTm(self, value):
		self._ValtnDtTm = value if type(value) != base_types.auto else self.make_default("ValtnDtTm")

	@ValtnDtTm.deleter
	def ValtnDtTm(self):
		del self._ValtnDtTm
		self._ValtnDtTm = None

	@property
	def ValtnFrqcy(self):
		return self._ValtnFrqcy

	@ValtnFrqcy.setter
	def ValtnFrqcy(self, value):
		self._ValtnFrqcy = value if type(value) != base_types.auto else self.make_default("ValtnFrqcy")

	@ValtnFrqcy.deleter
	def ValtnFrqcy(self):
		del self._ValtnFrqcy
		self._ValtnFrqcy = None

	@property
	def ValtnSttstcs(self):
		return self._ValtnSttstcs

	@ValtnSttstcs.setter
	def ValtnSttstcs(self, value):
		self._ValtnSttstcs = value if type(value) != base_types.auto else self.make_default("ValtnSttstcs")

	@ValtnSttstcs.deleter
	def ValtnSttstcs(self):
		del self._ValtnSttstcs
		self._ValtnSttstcs = None

	@property
	def ValtnTp(self):
		return self._ValtnTp

	@ValtnTp.setter
	def ValtnTp(self, value):
		self._ValtnTp = value if type(value) != base_types.auto else self.make_default("ValtnTp")

	@ValtnTp.deleter
	def ValtnTp(self):
		del self._ValtnTp
		self._ValtnTp = None

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