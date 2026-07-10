# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorBatchTransferV14 import AcceptorBatchTransferV14

class CAAA_011_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.14"
		_docname = "caaa.011.001.14"

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
			base_types.FieldEntry(name='AccptrBtchTrf', type=AcceptorBatchTransferV14, min=1, max=1, mutex_group=None, array=False),
		))