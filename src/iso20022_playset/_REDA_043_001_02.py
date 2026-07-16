# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAuditTrailReportV02

class REDA_043_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.043.001.02"
		_docname = "reda.043.001.02"

		__slots__ = ["_PtyAudtTrlRpt"]
		@property
		def PtyAudtTrlRpt(self):
			return self._PtyAudtTrlRpt

		@PtyAudtTrlRpt.setter
		def PtyAudtTrlRpt(self, value):
			self._PtyAudtTrlRpt = value if value is not None else base_types.UninitialisedField(self, 'PtyAudtTrlRpt', PartyAuditTrailReportV02, False)

		@PtyAudtTrlRpt.deleter
		def PtyAudtTrlRpt(self):
			del self._PtyAudtTrlRpt
			self._PtyAudtTrlRpt = base_types.UninitialisedField(self, 'PtyAudtTrlRpt', PartyAuditTrailReportV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyAudtTrlRpt', type=PartyAuditTrailReportV02, min=1, max=1, mutex_group=None, array=False),
		))