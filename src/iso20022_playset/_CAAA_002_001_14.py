# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorAuthorisationResponseV14 import AcceptorAuthorisationResponseV14

class CAAA_002_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:caaa.002.001.14",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_AccptrAuthstnRspn"]
		@property
		def AccptrAuthstnRspn(self):
			return self._AccptrAuthstnRspn

		@AccptrAuthstnRspn.setter
		def AccptrAuthstnRspn(self, value):
			self._AccptrAuthstnRspn = value if type(value) != base_types.auto else self.make_default("AccptrAuthstnRspn")

		@AccptrAuthstnRspn.deleter
		def AccptrAuthstnRspn(self):
			del self._AccptrAuthstnRspn
			self._AccptrAuthstnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrAuthstnRspn', type=AcceptorAuthorisationResponseV14, min=1, max=1, mutex_group=None, array=False),
		))