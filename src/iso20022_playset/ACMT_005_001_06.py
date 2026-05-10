from . import base_types
from .RequestForAccountManagementStatusReportV06 import RequestForAccountManagementStatusReportV06

class ACMT_005_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ReqForAcctMgmtStsRpt"]
		@property
		def ReqForAcctMgmtStsRpt(self):
			return self._ReqForAcctMgmtStsRpt

		@ReqForAcctMgmtStsRpt.setter
		def ReqForAcctMgmtStsRpt(self, value):
			self._ReqForAcctMgmtStsRpt = value if type(value) != auto else self.make_default("ReqForAcctMgmtStsRpt")

		@ReqForAcctMgmtStsRpt.deleter
		def ReqForAcctMgmtStsRpt(self):
			del self._ReqForAcctMgmtStsRpt
			self._ReqForAcctMgmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForAcctMgmtStsRpt', type=RequestForAccountManagementStatusReportV06, min=1, max=1, mutex_group=None, array=False),
		))

