# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import KeyExchangeInitiationV04

class CANM_003_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:canm.003.001.04"
		_docname = "canm.003.001.04"

		__slots__ = ["_KeyXchgInitn"]
		@property
		def KeyXchgInitn(self):
			return self._KeyXchgInitn

		@KeyXchgInitn.setter
		def KeyXchgInitn(self, value):
			self._KeyXchgInitn = value if value is not None else base_types.UninitialisedField(self, 'KeyXchgInitn', KeyExchangeInitiationV04, False)

		@KeyXchgInitn.deleter
		def KeyXchgInitn(self):
			del self._KeyXchgInitn
			self._KeyXchgInitn = base_types.UninitialisedField(self, 'KeyXchgInitn', KeyExchangeInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='KeyXchgInitn', type=KeyExchangeInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))