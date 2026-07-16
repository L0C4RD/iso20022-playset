# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GroupHeader117
from . import ReportingRequest7
from . import SupplementaryData1

class AccountReportingRequestV07(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_RptgReq", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if value is not None else base_types.UninitialisedField(self, 'GrpHdr', GroupHeader117, False)

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = base_types.UninitialisedField(self, 'GrpHdr', GroupHeader117, False)

	@property
	def RptgReq(self):
		return self._RptgReq

	@RptgReq.setter
	def RptgReq(self, value):
		self._RptgReq = value if value is not None else base_types.UninitialisedField(self, 'RptgReq', ReportingRequest7, True)

	@RptgReq.deleter
	def RptgReq(self):
		del self._RptgReq
		self._RptgReq = base_types.UninitialisedField(self, 'RptgReq', ReportingRequest7, True)

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
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader117, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgReq', type=ReportingRequest7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))