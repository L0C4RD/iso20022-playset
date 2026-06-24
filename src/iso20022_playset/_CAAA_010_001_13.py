# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorReconciliationResponseV13 import AcceptorReconciliationResponseV13

class CAAA_010_001_13():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.010.001.13"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AccptrRcncltnRspn"]
		@property
		def AccptrRcncltnRspn(self):
			return self._AccptrRcncltnRspn

		@AccptrRcncltnRspn.setter
		def AccptrRcncltnRspn(self, value):
			self._AccptrRcncltnRspn = value if type(value) != base_types.auto else self.make_default("AccptrRcncltnRspn")

		@AccptrRcncltnRspn.deleter
		def AccptrRcncltnRspn(self):
			del self._AccptrRcncltnRspn
			self._AccptrRcncltnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrRcncltnRspn', type=AcceptorReconciliationResponseV13, min=1, max=1, mutex_group=None, array=False),
		))