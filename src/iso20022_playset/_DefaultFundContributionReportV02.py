# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DefaultFundReport1
from . import PartyIdentification35Choice
from . import ReportParameters2
from . import SupplementaryData1

class DefaultFundContributionReportV02(base_types._BaseFieldType):

	__slots__ = ["_ClrMmb", "_RptDtls", "_RptParams", "_SplmtryData"]
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
	def RptDtls(self):
		return self._RptDtls

	@RptDtls.setter
	def RptDtls(self, value):
		self._RptDtls = value if value is not None else base_types.UninitialisedField(self, 'RptDtls', DefaultFundReport1, True)

	@RptDtls.deleter
	def RptDtls(self):
		del self._RptDtls
		self._RptDtls = base_types.UninitialisedField(self, 'RptDtls', DefaultFundReport1, True)

	@property
	def RptParams(self):
		return self._RptParams

	@RptParams.setter
	def RptParams(self, value):
		self._RptParams = value if value is not None else base_types.UninitialisedField(self, 'RptParams', ReportParameters2, False)

	@RptParams.deleter
	def RptParams(self):
		del self._RptParams
		self._RptParams = base_types.UninitialisedField(self, 'RptParams', ReportParameters2, False)

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
		base_types.FieldEntry(name='RptDtls', type=DefaultFundReport1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptParams', type=ReportParameters2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))