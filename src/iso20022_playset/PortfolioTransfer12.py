import base_types
import Max35Text
import AdditionalInformation15
import FundPortfolio9Choice
import FinancialInstrument101

class PortfolioTransfer12(base_types._BaseFieldType):

	__slots__ = ["_Prtfl", "_FinInstrmAsstForTrf", "_TrfId", "_MstrRef", "_AddtlInf"]
	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if type(value) != auto else self.make_default("Prtfl")

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = None

	@property
	def FinInstrmAsstForTrf(self):
		return self._FinInstrmAsstForTrf

	@FinInstrmAsstForTrf.setter
	def FinInstrmAsstForTrf(self, value):
		self._FinInstrmAsstForTrf = value if type(value) != auto else self.make_default("FinInstrmAsstForTrf")

	@FinInstrmAsstForTrf.deleter
	def FinInstrmAsstForTrf(self):
		del self._FinInstrmAsstForTrf
		self._FinInstrmAsstForTrf = None

	@property
	def TrfId(self):
		return self._TrfId

	@TrfId.setter
	def TrfId(self, value):
		self._TrfId = value if type(value) != auto else self.make_default("TrfId")

	@TrfId.deleter
	def TrfId(self):
		del self._TrfId
		self._TrfId = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtfl', type=FundPortfolio9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAsstForTrf', type=FinancialInstrument101, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

