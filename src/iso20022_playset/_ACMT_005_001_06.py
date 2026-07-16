# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestForAccountManagementStatusReportV06

class ACMT_005_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06"
		_docname = "acmt.005.001.06"

		__slots__ = ["_ReqForAcctMgmtStsRpt"]
		@property
		def ReqForAcctMgmtStsRpt(self):
			return self._ReqForAcctMgmtStsRpt

		@ReqForAcctMgmtStsRpt.setter
		def ReqForAcctMgmtStsRpt(self, value):
			self._ReqForAcctMgmtStsRpt = value if value is not None else base_types.UninitialisedField(self, 'ReqForAcctMgmtStsRpt', RequestForAccountManagementStatusReportV06, False)

		@ReqForAcctMgmtStsRpt.deleter
		def ReqForAcctMgmtStsRpt(self):
			del self._ReqForAcctMgmtStsRpt
			self._ReqForAcctMgmtStsRpt = base_types.UninitialisedField(self, 'ReqForAcctMgmtStsRpt', RequestForAccountManagementStatusReportV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ReqForAcctMgmtStsRpt', type=RequestForAccountManagementStatusReportV06, min=1, max=1, mutex_group=None, array=False),
		))