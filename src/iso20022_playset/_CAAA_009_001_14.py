# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorReconciliationRequestV14 import AcceptorReconciliationRequestV14

class CAAA_009_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.009.001.14"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AccptrRcncltnReq"]
		@property
		def AccptrRcncltnReq(self):
			return self._AccptrRcncltnReq

		@AccptrRcncltnReq.setter
		def AccptrRcncltnReq(self, value):
			self._AccptrRcncltnReq = value if type(value) != base_types.auto else self.make_default("AccptrRcncltnReq")

		@AccptrRcncltnReq.deleter
		def AccptrRcncltnReq(self):
			del self._AccptrRcncltnReq
			self._AccptrRcncltnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrRcncltnReq', type=AcceptorReconciliationRequestV14, min=1, max=1, mutex_group=None, array=False),
		))