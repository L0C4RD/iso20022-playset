# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAuditTrailReportV01

class REDA_034_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.034.001.01"
		_docname = "reda.034.001.01"

		__slots__ = ["_SctiesAudtTrlRpt"]
		@property
		def SctiesAudtTrlRpt(self):
			return self._SctiesAudtTrlRpt

		@SctiesAudtTrlRpt.setter
		def SctiesAudtTrlRpt(self, value):
			self._SctiesAudtTrlRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesAudtTrlRpt', SecuritiesAuditTrailReportV01, False)

		@SctiesAudtTrlRpt.deleter
		def SctiesAudtTrlRpt(self):
			del self._SctiesAudtTrlRpt
			self._SctiesAudtTrlRpt = base_types.UninitialisedField(self, 'SctiesAudtTrlRpt', SecuritiesAuditTrailReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAudtTrlRpt', type=SecuritiesAuditTrailReportV01, min=1, max=1, mutex_group=None, array=False),
		))