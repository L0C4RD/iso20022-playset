# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountReportV05

class ACMT_014_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.014.001.05"
		_docname = "acmt.014.001.05"

		__slots__ = ["_AcctRpt"]
		@property
		def AcctRpt(self):
			return self._AcctRpt

		@AcctRpt.setter
		def AcctRpt(self, value):
			self._AcctRpt = value if value is not None else base_types.UninitialisedField(self, 'AcctRpt', AccountReportV05, False)

		@AcctRpt.deleter
		def AcctRpt(self):
			del self._AcctRpt
			self._AcctRpt = base_types.UninitialisedField(self, 'AcctRpt', AccountReportV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctRpt', type=AccountReportV05, min=1, max=1, mutex_group=None, array=False),
		))