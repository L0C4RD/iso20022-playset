from . import base_types
import AccountManagementStatusReportV07

class ACMT_006_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctMgmtStsRpt"]
		@property
		def AcctMgmtStsRpt(self):
			return self._AcctMgmtStsRpt

		@AcctMgmtStsRpt.setter
		def AcctMgmtStsRpt(self, value):
			self._AcctMgmtStsRpt = value if type(value) != auto else self.make_default("AcctMgmtStsRpt")

		@AcctMgmtStsRpt.deleter
		def AcctMgmtStsRpt(self):
			del self._AcctMgmtStsRpt
			self._AcctMgmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctMgmtStsRpt', type=AccountManagementStatusReportV07, min=1, max=1, mutex_group=None, array=False),
		))

