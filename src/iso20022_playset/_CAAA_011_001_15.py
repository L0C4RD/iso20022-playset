# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorBatchTransferV15 import AcceptorBatchTransferV15

class CAAA_011_001_15():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caaa.011.001.15"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AccptrBtchTrf"]
		@property
		def AccptrBtchTrf(self):
			return self._AccptrBtchTrf

		@AccptrBtchTrf.setter
		def AccptrBtchTrf(self, value):
			self._AccptrBtchTrf = value if type(value) != base_types.auto else self.make_default("AccptrBtchTrf")

		@AccptrBtchTrf.deleter
		def AccptrBtchTrf(self):
			del self._AccptrBtchTrf
			self._AccptrBtchTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrBtchTrf', type=AcceptorBatchTransferV15, min=1, max=1, mutex_group=None, array=False),
		))