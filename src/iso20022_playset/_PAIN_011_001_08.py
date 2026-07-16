# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MandateCancellationRequestV08

class PAIN_011_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.011.001.08"
		_docname = "pain.011.001.08"

		__slots__ = ["_MndtCxlReq"]
		@property
		def MndtCxlReq(self):
			return self._MndtCxlReq

		@MndtCxlReq.setter
		def MndtCxlReq(self, value):
			self._MndtCxlReq = value if value is not None else base_types.UninitialisedField(self, 'MndtCxlReq', MandateCancellationRequestV08, False)

		@MndtCxlReq.deleter
		def MndtCxlReq(self):
			del self._MndtCxlReq
			self._MndtCxlReq = base_types.UninitialisedField(self, 'MndtCxlReq', MandateCancellationRequestV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtCxlReq', type=MandateCancellationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))