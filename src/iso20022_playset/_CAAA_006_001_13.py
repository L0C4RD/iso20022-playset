# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationResponseV13 import AcceptorCancellationResponseV13

class CAAA_006_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.006.001.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AccptrCxlRspn"]
		@property
		def AccptrCxlRspn(self):
			return self._AccptrCxlRspn

		@AccptrCxlRspn.setter
		def AccptrCxlRspn(self, value):
			self._AccptrCxlRspn = value if type(value) != base_types.auto else self.make_default("AccptrCxlRspn")

		@AccptrCxlRspn.deleter
		def AccptrCxlRspn(self):
			del self._AccptrCxlRspn
			self._AccptrCxlRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlRspn', type=AcceptorCancellationResponseV13, min=1, max=1, mutex_group=None, array=False),
		))