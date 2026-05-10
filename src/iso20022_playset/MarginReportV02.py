import base_types
import MarginReport2
import Pagination
import SupplementaryData1
import PartyIdentification35Choice
import MarginCalculation1
import ReportParameters3

class MarginReportV02(base_types._BaseFieldType):

	__slots__ = ["_ClrMmb", "_RptDtls", "_RptSummry", "_RptParams", "_Pgntn", "_SplmtryData"]
	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	@property
	def RptDtls(self):
		return self._RptDtls

	@RptDtls.setter
	def RptDtls(self, value):
		self._RptDtls = value if type(value) != auto else self.make_default("RptDtls")

	@RptDtls.deleter
	def RptDtls(self):
		del self._RptDtls
		self._RptDtls = None

	@property
	def RptSummry(self):
		return self._RptSummry

	@RptSummry.setter
	def RptSummry(self, value):
		self._RptSummry = value if type(value) != auto else self.make_default("RptSummry")

	@RptSummry.deleter
	def RptSummry(self):
		del self._RptSummry
		self._RptSummry = None

	@property
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if type(value) != auto else self.make_default("RptParams")

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification35Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtls', type=MarginReport2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptSummry', type=MarginCalculation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptParams', type=ReportParameters3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

