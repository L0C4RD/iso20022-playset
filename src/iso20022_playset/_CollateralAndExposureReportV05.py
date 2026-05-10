from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .Collateral53 import Collateral53
from .Pagination1 import Pagination1
from .Obligation11 import Obligation11
from .ReportParameters6 import ReportParameters6
from .Agreement4 import Agreement4

class CollateralAndExposureReportV05(base_types._BaseFieldType):

	__slots__ = ["_Pgntn", "_SplmtryData", "_RptParams", "_Oblgtn", "_Agrmt", "_CollRpt"]
	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if type(value) != base_types.auto else self.make_default("RptParams")

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = None

	@property
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if type(value) != base_types.auto else self.make_default("Oblgtn")

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = None

	@property
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if type(value) != base_types.auto else self.make_default("Agrmt")

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = None

	@property
	def CollRpt(self):
		return self._CollRpt

	@CollRpt.setter
	def CollRpt(self, value):
		self._CollRpt = value if type(value) != base_types.auto else self.make_default("CollRpt")

	@CollRpt.deleter
	def CollRpt(self):
		del self._CollRpt
		self._CollRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptParams', type=ReportParameters6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oblgtn', type=Obligation11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollRpt', type=Collateral53, min=1, max=None, mutex_group=None, array=True),
	))

