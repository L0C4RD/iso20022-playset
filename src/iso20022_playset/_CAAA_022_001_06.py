# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorNonFinancialRequestV06 import AcceptorNonFinancialRequestV06

class CAAA_022_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.022.001.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AccptrNonFinReq"]
		@property
		def AccptrNonFinReq(self):
			return self._AccptrNonFinReq

		@AccptrNonFinReq.setter
		def AccptrNonFinReq(self, value):
			self._AccptrNonFinReq = value if type(value) != base_types.auto else self.make_default("AccptrNonFinReq")

		@AccptrNonFinReq.deleter
		def AccptrNonFinReq(self):
			del self._AccptrNonFinReq
			self._AccptrNonFinReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrNonFinReq', type=AcceptorNonFinancialRequestV06, min=1, max=1, mutex_group=None, array=False),
		))