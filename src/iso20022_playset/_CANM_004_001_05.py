# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import KeyExchangeResponseV05

class CANM_004_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:canm.004.001.05"
		_docname = "canm.004.001.05"

		__slots__ = ["_KeyXchgRspn"]
		@property
		def KeyXchgRspn(self):
			return self._KeyXchgRspn

		@KeyXchgRspn.setter
		def KeyXchgRspn(self, value):
			self._KeyXchgRspn = value if value is not None else base_types.UninitialisedField(self, 'KeyXchgRspn', KeyExchangeResponseV05, False)

		@KeyXchgRspn.deleter
		def KeyXchgRspn(self):
			del self._KeyXchgRspn
			self._KeyXchgRspn = base_types.UninitialisedField(self, 'KeyXchgRspn', KeyExchangeResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='KeyXchgRspn', type=KeyExchangeResponseV05, min=1, max=1, mutex_group=None, array=False),
		))