# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MandateCancellationRequestV08 import MandateCancellationRequestV08

class PAIN_011_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:pain.011.001.08",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_MndtCxlReq"]
		@property
		def MndtCxlReq(self):
			return self._MndtCxlReq

		@MndtCxlReq.setter
		def MndtCxlReq(self, value):
			self._MndtCxlReq = value if type(value) != base_types.auto else self.make_default("MndtCxlReq")

		@MndtCxlReq.deleter
		def MndtCxlReq(self):
			del self._MndtCxlReq
			self._MndtCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtCxlReq', type=MandateCancellationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))