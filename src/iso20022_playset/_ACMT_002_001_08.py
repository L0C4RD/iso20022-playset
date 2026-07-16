# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountDetailsConfirmationV08

class ACMT_002_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08"
		_docname = "acmt.002.001.08"

		__slots__ = ["_AcctDtlsConf"]
		@property
		def AcctDtlsConf(self):
			return self._AcctDtlsConf

		@AcctDtlsConf.setter
		def AcctDtlsConf(self, value):
			self._AcctDtlsConf = value if value is not None else base_types.UninitialisedField(self, 'AcctDtlsConf', AccountDetailsConfirmationV08, False)

		@AcctDtlsConf.deleter
		def AcctDtlsConf(self):
			del self._AcctDtlsConf
			self._AcctDtlsConf = base_types.UninitialisedField(self, 'AcctDtlsConf', AccountDetailsConfirmationV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctDtlsConf', type=AccountDetailsConfirmationV08, min=1, max=1, mutex_group=None, array=False),
		))