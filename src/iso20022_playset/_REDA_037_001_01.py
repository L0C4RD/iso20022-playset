# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountAuditTrailReportV01

class REDA_037_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.037.001.01"
		_docname = "reda.037.001.01"

		__slots__ = ["_SctiesAcctAudtTrlRpt"]
		@property
		def SctiesAcctAudtTrlRpt(self):
			return self._SctiesAcctAudtTrlRpt

		@SctiesAcctAudtTrlRpt.setter
		def SctiesAcctAudtTrlRpt(self, value):
			self._SctiesAcctAudtTrlRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctAudtTrlRpt', SecuritiesAccountAuditTrailReportV01, False)

		@SctiesAcctAudtTrlRpt.deleter
		def SctiesAcctAudtTrlRpt(self):
			del self._SctiesAcctAudtTrlRpt
			self._SctiesAcctAudtTrlRpt = base_types.UninitialisedField(self, 'SctiesAcctAudtTrlRpt', SecuritiesAccountAuditTrailReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctAudtTrlRpt', type=SecuritiesAccountAuditTrailReportV01, min=1, max=1, mutex_group=None, array=False),
		))