# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAuditTrailQueryV01

class REDA_033_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.033.001.01"
		_docname = "reda.033.001.01"

		__slots__ = ["_SctiesAudtTrlQry"]
		@property
		def SctiesAudtTrlQry(self):
			return self._SctiesAudtTrlQry

		@SctiesAudtTrlQry.setter
		def SctiesAudtTrlQry(self, value):
			self._SctiesAudtTrlQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesAudtTrlQry', SecuritiesAuditTrailQueryV01, False)

		@SctiesAudtTrlQry.deleter
		def SctiesAudtTrlQry(self):
			del self._SctiesAudtTrlQry
			self._SctiesAudtTrlQry = base_types.UninitialisedField(self, 'SctiesAudtTrlQry', SecuritiesAuditTrailQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAudtTrlQry', type=SecuritiesAuditTrailQueryV01, min=1, max=1, mutex_group=None, array=False),
		))