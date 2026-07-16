# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InterestPaymentResponseV05

class COLR_014_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.014.001.05"
		_docname = "colr.014.001.05"

		__slots__ = ["_IntrstPmtRspn"]
		@property
		def IntrstPmtRspn(self):
			return self._IntrstPmtRspn

		@IntrstPmtRspn.setter
		def IntrstPmtRspn(self, value):
			self._IntrstPmtRspn = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtRspn', InterestPaymentResponseV05, False)

		@IntrstPmtRspn.deleter
		def IntrstPmtRspn(self):
			del self._IntrstPmtRspn
			self._IntrstPmtRspn = base_types.UninitialisedField(self, 'IntrstPmtRspn', InterestPaymentResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtRspn', type=InterestPaymentResponseV05, min=1, max=1, mutex_group=None, array=False),
		))