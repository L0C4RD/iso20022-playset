# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorAuthorisationRequestV14 import AcceptorAuthorisationRequestV14

class CAAA_001_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.001.001.14"
		_docname = "caaa.001.001.14"

		__slots__ = ["_AccptrAuthstnReq"]
		@property
		def AccptrAuthstnReq(self):
			return self._AccptrAuthstnReq

		@AccptrAuthstnReq.setter
		def AccptrAuthstnReq(self, value):
			self._AccptrAuthstnReq = value if type(value) != base_types.auto else self.make_default("AccptrAuthstnReq")

		@AccptrAuthstnReq.deleter
		def AccptrAuthstnReq(self):
			del self._AccptrAuthstnReq
			self._AccptrAuthstnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrAuthstnReq', type=AcceptorAuthorisationRequestV14, min=1, max=1, mutex_group=None, array=False),
		))