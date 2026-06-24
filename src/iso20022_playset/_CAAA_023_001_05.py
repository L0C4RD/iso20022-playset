# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorNonFinancialResponseV05 import AcceptorNonFinancialResponseV05

class CAAA_023_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.023.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AccptrNonFinRspn"]
		@property
		def AccptrNonFinRspn(self):
			return self._AccptrNonFinRspn

		@AccptrNonFinRspn.setter
		def AccptrNonFinRspn(self, value):
			self._AccptrNonFinRspn = value if type(value) != base_types.auto else self.make_default("AccptrNonFinRspn")

		@AccptrNonFinRspn.deleter
		def AccptrNonFinRspn(self):
			del self._AccptrNonFinRspn
			self._AccptrNonFinRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrNonFinRspn', type=AcceptorNonFinancialResponseV05, min=1, max=1, mutex_group=None, array=False),
		))