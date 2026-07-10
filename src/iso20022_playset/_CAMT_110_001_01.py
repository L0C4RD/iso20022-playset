# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvestigationRequestV01 import InvestigationRequestV01

class CAMT_110_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.110.001.01"
		_docname = "camt.110.001.01"

		__slots__ = ["_InvstgtnReq"]
		@property
		def InvstgtnReq(self):
			return self._InvstgtnReq

		@InvstgtnReq.setter
		def InvstgtnReq(self, value):
			self._InvstgtnReq = value if type(value) != base_types.auto else self.make_default("InvstgtnReq")

		@InvstgtnReq.deleter
		def InvstgtnReq(self):
			del self._InvstgtnReq
			self._InvstgtnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvstgtnReq', type=InvestigationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))