# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAuditTrailQueryV01

class REDA_042_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.042.001.01"
		_docname = "reda.042.001.01"

		__slots__ = ["_PtyAudtTrlQry"]
		@property
		def PtyAudtTrlQry(self):
			return self._PtyAudtTrlQry

		@PtyAudtTrlQry.setter
		def PtyAudtTrlQry(self, value):
			self._PtyAudtTrlQry = value if value is not None else base_types.UninitialisedField(self, 'PtyAudtTrlQry', PartyAuditTrailQueryV01, False)

		@PtyAudtTrlQry.deleter
		def PtyAudtTrlQry(self):
			del self._PtyAudtTrlQry
			self._PtyAudtTrlQry = base_types.UninitialisedField(self, 'PtyAudtTrlQry', PartyAuditTrailQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyAudtTrlQry', type=PartyAuditTrailQueryV01, min=1, max=1, mutex_group=None, array=False),
		))