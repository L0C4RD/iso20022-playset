from . import base_types
from .Period4Choice import Period4Choice
from .SupplementaryData1 import SupplementaryData1
from .SecuritiesInvalidReferenceDataReport4 import SecuritiesInvalidReferenceDataReport4
from .Number import Number

class FinancialInstrumentReportingInvalidReferenceDataReportV02(base_types._BaseFieldType):

	__slots__ = ["_NbOfRcrds", "_SplmtryData", "_DtPrd", "_FinInstrms"]
	@property
	def NbOfRcrds(self):
		return self._NbOfRcrds

	@NbOfRcrds.setter
	def NbOfRcrds(self, value):
		self._NbOfRcrds = value if type(value) != auto else self.make_default("NbOfRcrds")

	@NbOfRcrds.deleter
	def NbOfRcrds(self):
		del self._NbOfRcrds
		self._NbOfRcrds = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if type(value) != auto else self.make_default("DtPrd")

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = None

	@property
	def FinInstrms(self):
		return self._FinInstrms

	@FinInstrms.setter
	def FinInstrms(self, value):
		self._FinInstrms = value if type(value) != auto else self.make_default("FinInstrms")

	@FinInstrms.deleter
	def FinInstrms(self):
		del self._FinInstrms
		self._FinInstrms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfRcrds', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrms', type=SecuritiesInvalidReferenceDataReport4, min=1, max=None, mutex_group=None, array=True),
	))

