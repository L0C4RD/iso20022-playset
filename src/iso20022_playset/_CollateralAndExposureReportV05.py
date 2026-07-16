# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Agreement4
from . import Collateral53
from . import Obligation11
from . import Pagination1
from . import ReportParameters6
from . import SupplementaryData1

class CollateralAndExposureReportV05(base_types._BaseFieldType):

	__slots__ = ["_Agrmt", "_CollRpt", "_Oblgtn", "_Pgntn", "_RptParams", "_SplmtryData"]
	@property
	def Agrmt(self):
		return self._Agrmt

	@Agrmt.setter
	def Agrmt(self, value):
		self._Agrmt = value if value is not None else base_types.UninitialisedField(self, 'Agrmt', Agreement4, False)

	@Agrmt.deleter
	def Agrmt(self):
		del self._Agrmt
		self._Agrmt = base_types.UninitialisedField(self, 'Agrmt', Agreement4, False)

	@property
	def CollRpt(self):
		return self._CollRpt

	@CollRpt.setter
	def CollRpt(self, value):
		self._CollRpt = value if value is not None else base_types.UninitialisedField(self, 'CollRpt', Collateral53, True)

	@CollRpt.deleter
	def CollRpt(self):
		del self._CollRpt
		self._CollRpt = base_types.UninitialisedField(self, 'CollRpt', Collateral53, True)

	@property
	def Oblgtn(self):
		return self._Oblgtn

	@Oblgtn.setter
	def Oblgtn(self, value):
		self._Oblgtn = value if value is not None else base_types.UninitialisedField(self, 'Oblgtn', Obligation11, False)

	@Oblgtn.deleter
	def Oblgtn(self):
		del self._Oblgtn
		self._Oblgtn = base_types.UninitialisedField(self, 'Oblgtn', Obligation11, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if value is not None else base_types.UninitialisedField(self, 'RptParams', ReportParameters6, False)

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = base_types.UninitialisedField(self, 'RptParams', ReportParameters6, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agrmt', type=Agreement4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollRpt', type=Collateral53, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oblgtn', type=Obligation11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptParams', type=ReportParameters6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))