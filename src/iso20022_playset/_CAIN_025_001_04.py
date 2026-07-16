# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddendumInitiationV04

class CAIN_025_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.025.001.04"
		_docname = "cain.025.001.04"

		__slots__ = ["_AdddmInitn"]
		@property
		def AdddmInitn(self):
			return self._AdddmInitn

		@AdddmInitn.setter
		def AdddmInitn(self, value):
			self._AdddmInitn = value if value is not None else base_types.UninitialisedField(self, 'AdddmInitn', AddendumInitiationV04, False)

		@AdddmInitn.deleter
		def AdddmInitn(self):
			del self._AdddmInitn
			self._AdddmInitn = base_types.UninitialisedField(self, 'AdddmInitn', AddendumInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdddmInitn', type=AddendumInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))