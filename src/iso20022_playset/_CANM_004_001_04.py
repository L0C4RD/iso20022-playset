# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import KeyExchangeResponseV04

class CANM_004_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:canm.004.001.04"
		_docname = "canm.004.001.04"

		__slots__ = ["_KeyXchgRspn"]
		@property
		def KeyXchgRspn(self):
			return self._KeyXchgRspn

		@KeyXchgRspn.setter
		def KeyXchgRspn(self, value):
			self._KeyXchgRspn = value if value is not None else base_types.UninitialisedField(self, 'KeyXchgRspn', KeyExchangeResponseV04, False)

		@KeyXchgRspn.deleter
		def KeyXchgRspn(self):
			del self._KeyXchgRspn
			self._KeyXchgRspn = base_types.UninitialisedField(self, 'KeyXchgRspn', KeyExchangeResponseV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='KeyXchgRspn', type=KeyExchangeResponseV04, min=1, max=1, mutex_group=None, array=False),
		))