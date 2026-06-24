# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAElectionAmendmentRequestV01 import AgentCAElectionAmendmentRequestV01

class SEEV_013_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.013.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AgtCAElctnAmdmntReq"]
		@property
		def AgtCAElctnAmdmntReq(self):
			return self._AgtCAElctnAmdmntReq

		@AgtCAElctnAmdmntReq.setter
		def AgtCAElctnAmdmntReq(self, value):
			self._AgtCAElctnAmdmntReq = value if type(value) != base_types.auto else self.make_default("AgtCAElctnAmdmntReq")

		@AgtCAElctnAmdmntReq.deleter
		def AgtCAElctnAmdmntReq(self):
			del self._AgtCAElctnAmdmntReq
			self._AgtCAElctnAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAElctnAmdmntReq', type=AgentCAElectionAmendmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))