# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgentCADeactivationCancellationRequestV01 import AgentCADeactivationCancellationRequestV01

class SEEV_029_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.029.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AgtCADeactvtnCxlReq"]
		@property
		def AgtCADeactvtnCxlReq(self):
			return self._AgtCADeactvtnCxlReq

		@AgtCADeactvtnCxlReq.setter
		def AgtCADeactvtnCxlReq(self, value):
			self._AgtCADeactvtnCxlReq = value if type(value) != base_types.auto else self.make_default("AgtCADeactvtnCxlReq")

		@AgtCADeactvtnCxlReq.deleter
		def AgtCADeactvtnCxlReq(self):
			del self._AgtCADeactvtnCxlReq
			self._AgtCADeactvtnCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADeactvtnCxlReq', type=AgentCADeactivationCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))