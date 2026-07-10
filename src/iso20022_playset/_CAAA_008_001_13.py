# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCancellationAdviceResponseV13 import AcceptorCancellationAdviceResponseV13

class CAAA_008_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.008.001.13"
		_docname = "caaa.008.001.13"

		__slots__ = ["_AccptrCxlAdvcRspn"]
		@property
		def AccptrCxlAdvcRspn(self):
			return self._AccptrCxlAdvcRspn

		@AccptrCxlAdvcRspn.setter
		def AccptrCxlAdvcRspn(self, value):
			self._AccptrCxlAdvcRspn = value if type(value) != base_types.auto else self.make_default("AccptrCxlAdvcRspn")

		@AccptrCxlAdvcRspn.deleter
		def AccptrCxlAdvcRspn(self):
			del self._AccptrCxlAdvcRspn
			self._AccptrCxlAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCxlAdvcRspn', type=AcceptorCancellationAdviceResponseV13, min=1, max=1, mutex_group=None, array=False),
		))