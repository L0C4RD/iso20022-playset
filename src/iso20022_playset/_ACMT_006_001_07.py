# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountManagementStatusReportV07 import AccountManagementStatusReportV07

class ACMT_006_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07"
		_docname = "acmt.006.001.07"

		__slots__ = ["_AcctMgmtStsRpt"]
		@property
		def AcctMgmtStsRpt(self):
			return self._AcctMgmtStsRpt

		@AcctMgmtStsRpt.setter
		def AcctMgmtStsRpt(self, value):
			self._AcctMgmtStsRpt = value if type(value) != base_types.auto else self.make_default("AcctMgmtStsRpt")

		@AcctMgmtStsRpt.deleter
		def AcctMgmtStsRpt(self):
			del self._AcctMgmtStsRpt
			self._AcctMgmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctMgmtStsRpt', type=AccountManagementStatusReportV07, min=1, max=1, mutex_group=None, array=False),
		))