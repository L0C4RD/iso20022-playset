# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyStatusAdviceV01 import PartyStatusAdviceV01

class REDA_016_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.016.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_PtyStsAdvc"]
		@property
		def PtyStsAdvc(self):
			return self._PtyStsAdvc

		@PtyStsAdvc.setter
		def PtyStsAdvc(self, value):
			self._PtyStsAdvc = value if type(value) != base_types.auto else self.make_default("PtyStsAdvc")

		@PtyStsAdvc.deleter
		def PtyStsAdvc(self):
			del self._PtyStsAdvc
			self._PtyStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyStsAdvc', type=PartyStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))