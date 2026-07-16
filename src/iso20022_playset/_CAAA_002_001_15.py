# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorAuthorisationResponseV15

class CAAA_002_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.002.001.15"
		_docname = "caaa.002.001.15"

		__slots__ = ["_AccptrAuthstnRspn"]
		@property
		def AccptrAuthstnRspn(self):
			return self._AccptrAuthstnRspn

		@AccptrAuthstnRspn.setter
		def AccptrAuthstnRspn(self, value):
			self._AccptrAuthstnRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrAuthstnRspn', AcceptorAuthorisationResponseV15, False)

		@AccptrAuthstnRspn.deleter
		def AccptrAuthstnRspn(self):
			del self._AccptrAuthstnRspn
			self._AccptrAuthstnRspn = base_types.UninitialisedField(self, 'AccptrAuthstnRspn', AcceptorAuthorisationResponseV15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrAuthstnRspn', type=AcceptorAuthorisationResponseV15, min=1, max=1, mutex_group=None, array=False),
		))