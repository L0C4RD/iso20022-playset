# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesAccountAuditTrailQueryV01

class REDA_036_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01"
		_docname = "reda.036.001.01"

		__slots__ = ["_SctiesAcctAudtTrlQry"]
		@property
		def SctiesAcctAudtTrlQry(self):
			return self._SctiesAcctAudtTrlQry

		@SctiesAcctAudtTrlQry.setter
		def SctiesAcctAudtTrlQry(self, value):
			self._SctiesAcctAudtTrlQry = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctAudtTrlQry', SecuritiesAccountAuditTrailQueryV01, False)

		@SctiesAcctAudtTrlQry.deleter
		def SctiesAcctAudtTrlQry(self):
			del self._SctiesAcctAudtTrlQry
			self._SctiesAcctAudtTrlQry = base_types.UninitialisedField(self, 'SctiesAcctAudtTrlQry', SecuritiesAccountAuditTrailQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctAudtTrlQry', type=SecuritiesAccountAuditTrailQueryV01, min=1, max=1, mutex_group=None, array=False),
		))