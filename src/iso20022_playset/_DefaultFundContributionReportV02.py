from . import base_types
from ._ReportParameters2 import ReportParameters2
from ._SupplementaryData1 import SupplementaryData1
from ._DefaultFundReport1 import DefaultFundReport1
from ._PartyIdentification35Choice import PartyIdentification35Choice

class DefaultFundContributionReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RptParams", "_ClrMmb", "_RptDtls"]
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
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != base_types.auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	@property
	def RptDtls(self):
		return self._RptDtls

	@RptDtls.setter
	def RptDtls(self, value):
		self._RptDtls = value if type(value) != base_types.auto else self.make_default("RptDtls")

	@RptDtls.deleter
	def RptDtls(self):
		del self._RptDtls
		self._RptDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptParams', type=ReportParameters2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification35Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtls', type=DefaultFundReport1, min=1, max=None, mutex_group=None, array=True),
	))

