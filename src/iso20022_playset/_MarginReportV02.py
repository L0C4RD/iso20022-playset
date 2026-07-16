# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarginCalculation1
from . import MarginReport2
from . import Pagination
from . import PartyIdentification35Choice
from . import ReportParameters3
from . import SupplementaryData1

class MarginReportV02(base_types._BaseFieldType):

	__slots__ = ["_ClrMmb", "_Pgntn", "_RptDtls", "_RptParams", "_RptSummry", "_SplmtryData"]
	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification35Choice, False)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification35Choice, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination, False)

	@property
	def RptDtls(self):
		return self._RptDtls

	@RptDtls.setter
	def RptDtls(self, value):
		self._RptDtls = value if value is not None else base_types.UninitialisedField(self, 'RptDtls', MarginReport2, True)

	@RptDtls.deleter
	def RptDtls(self):
		del self._RptDtls
		self._RptDtls = base_types.UninitialisedField(self, 'RptDtls', MarginReport2, True)

	@property
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if value is not None else base_types.UninitialisedField(self, 'RptParams', ReportParameters3, False)

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = base_types.UninitialisedField(self, 'RptParams', ReportParameters3, False)

	@property
	def RptSummry(self):
		return self._RptSummry

	@RptSummry.setter
	def RptSummry(self, value):
		self._RptSummry = value if value is not None else base_types.UninitialisedField(self, 'RptSummry', MarginCalculation1, False)

	@RptSummry.deleter
	def RptSummry(self):
		del self._RptSummry
		self._RptSummry = base_types.UninitialisedField(self, 'RptSummry', MarginCalculation1, False)

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
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification35Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtls', type=MarginReport2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptParams', type=ReportParameters3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSummry', type=MarginCalculation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))