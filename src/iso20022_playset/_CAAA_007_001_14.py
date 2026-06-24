# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationAdviceV14 import AcceptorCancellationAdviceV14

class CAAA_007_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.007.001.14"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AccptrCxlAdvc"]
		@property
		def AccptrCxlAdvc(self):
			return self._AccptrCxlAdvc

		@AccptrCxlAdvc.setter
		def AccptrCxlAdvc(self, value):
			self._AccptrCxlAdvc = value if type(value) != base_types.auto else self.make_default("AccptrCxlAdvc")

		@AccptrCxlAdvc.deleter
		def AccptrCxlAdvc(self):
			del self._AccptrCxlAdvc
			self._AccptrCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlAdvc', type=AcceptorCancellationAdviceV14, min=1, max=1, mutex_group=None, array=False),
		))