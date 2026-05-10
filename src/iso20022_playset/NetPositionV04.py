import base_types
import PartyIdentification253Choice
import Pagination1
import ReportParameters7
import NetPosition4
import SupplementaryData1

class NetPositionV04(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_ClrMmb", "_NetPosRpt", "_ClrSgmt", "_Pgntn", "_RptParams"]
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
	def NetPosRpt(self):
		return self._NetPosRpt

	@NetPosRpt.setter
	def NetPosRpt(self, value):
		self._NetPosRpt = value if type(value) != auto else self.make_default("NetPosRpt")

	@NetPosRpt.deleter
	def NetPosRpt(self):
		del self._NetPosRpt
		self._NetPosRpt = None

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if type(value) != auto else self.make_default("ClrSgmt")

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = None

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
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if type(value) != auto else self.make_default("RptParams")

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetPosRpt', type=NetPosition4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptParams', type=ReportParameters7, min=1, max=1, mutex_group=None, array=False),
	))

