# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MandateInitiationRequestV08 import MandateInitiationRequestV08

class PAIN_009_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.009.001.08"
		_docname = "pain.009.001.08"

		__slots__ = ["_MndtInitnReq"]
		@property
		def MndtInitnReq(self):
			return self._MndtInitnReq

		@MndtInitnReq.setter
		def MndtInitnReq(self, value):
			self._MndtInitnReq = value if type(value) != base_types.auto else self.make_default("MndtInitnReq")

		@MndtInitnReq.deleter
		def MndtInitnReq(self):
			del self._MndtInitnReq
			self._MndtInitnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtInitnReq', type=MandateInitiationRequestV08, min=1, max=1, mutex_group=None, array=False),
		))