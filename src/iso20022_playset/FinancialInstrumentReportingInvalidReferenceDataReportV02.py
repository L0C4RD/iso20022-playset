import base_types
import SupplementaryData1
import Number
import SecuritiesInvalidReferenceDataReport4
import Period4Choice

class FinancialInstrumentReportingInvalidReferenceDataReportV02(base_types._BaseFieldType):

	__slots__ = ["_FinInstrms", "_DtPrd", "_SplmtryData", "_NbOfRcrds"]
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
	def NbOfRcrds(self):
		return self._NbOfRcrds

	@NbOfRcrds.setter
	def NbOfRcrds(self, value):
		self._NbOfRcrds = value if type(value) != auto else self.make_default("NbOfRcrds")

	@NbOfRcrds.deleter
	def NbOfRcrds(self):
		del self._NbOfRcrds
		self._NbOfRcrds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrms', type=SecuritiesInvalidReferenceDataReport4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtPrd', type=Period4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfRcrds', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

