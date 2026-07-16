# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgentCADeactivationCancellationRequestV01

class SEEV_029_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.029.001.01"
		_docname = "seev.029.001.01"

		__slots__ = ["_AgtCADeactvtnCxlReq"]
		@property
		def AgtCADeactvtnCxlReq(self):
			return self._AgtCADeactvtnCxlReq

		@AgtCADeactvtnCxlReq.setter
		def AgtCADeactvtnCxlReq(self, value):
			self._AgtCADeactvtnCxlReq = value if value is not None else base_types.UninitialisedField(self, 'AgtCADeactvtnCxlReq', AgentCADeactivationCancellationRequestV01, False)

		@AgtCADeactvtnCxlReq.deleter
		def AgtCADeactvtnCxlReq(self):
			del self._AgtCADeactvtnCxlReq
			self._AgtCADeactvtnCxlReq = base_types.UninitialisedField(self, 'AgtCADeactvtnCxlReq', AgentCADeactivationCancellationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AgtCADeactvtnCxlReq', type=AgentCADeactivationCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))