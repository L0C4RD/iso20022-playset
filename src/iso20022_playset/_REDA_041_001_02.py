# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyActivityAdviceV02 import PartyActivityAdviceV02

class REDA_041_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.041.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_PtyActvtyAdvc"]
		@property
		def PtyActvtyAdvc(self):
			return self._PtyActvtyAdvc

		@PtyActvtyAdvc.setter
		def PtyActvtyAdvc(self, value):
			self._PtyActvtyAdvc = value if type(value) != base_types.auto else self.make_default("PtyActvtyAdvc")

		@PtyActvtyAdvc.deleter
		def PtyActvtyAdvc(self):
			del self._PtyActvtyAdvc
			self._PtyActvtyAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyActvtyAdvc', type=PartyActivityAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))