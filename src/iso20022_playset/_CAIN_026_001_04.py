# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddendumResponseV04

class CAIN_026_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.026.001.04"
		_docname = "cain.026.001.04"

		__slots__ = ["_AdddmRspn"]
		@property
		def AdddmRspn(self):
			return self._AdddmRspn

		@AdddmRspn.setter
		def AdddmRspn(self, value):
			self._AdddmRspn = value if value is not None else base_types.UninitialisedField(self, 'AdddmRspn', AddendumResponseV04, False)

		@AdddmRspn.deleter
		def AdddmRspn(self):
			del self._AdddmRspn
			self._AdddmRspn = base_types.UninitialisedField(self, 'AdddmRspn', AddendumResponseV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdddmRspn', type=AddendumResponseV04, min=1, max=1, mutex_group=None, array=False),
		))