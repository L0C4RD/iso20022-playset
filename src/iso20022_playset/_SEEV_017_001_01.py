# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCAGlobalDistributionAuthorisationRequestV01 import AgentCAGlobalDistributionAuthorisationRequestV01

class SEEV_017_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.017.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AgtCAGblDstrbtnAuthstnReq"]
		@property
		def AgtCAGblDstrbtnAuthstnReq(self):
			return self._AgtCAGblDstrbtnAuthstnReq

		@AgtCAGblDstrbtnAuthstnReq.setter
		def AgtCAGblDstrbtnAuthstnReq(self, value):
			self._AgtCAGblDstrbtnAuthstnReq = value if type(value) != base_types.auto else self.make_default("AgtCAGblDstrbtnAuthstnReq")

		@AgtCAGblDstrbtnAuthstnReq.deleter
		def AgtCAGblDstrbtnAuthstnReq(self):
			del self._AgtCAGblDstrbtnAuthstnReq
			self._AgtCAGblDstrbtnAuthstnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCAGblDstrbtnAuthstnReq', type=AgentCAGlobalDistributionAuthorisationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))