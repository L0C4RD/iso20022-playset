# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MandateAmendmentRequestV08 import MandateAmendmentRequestV08

class PAIN_010_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.010.001.08"
		_docname = "pain.010.001.08"

		__slots__ = ["_MndtAmdmntReq"]
		@property
		def MndtAmdmntReq(self):
			return self._MndtAmdmntReq

		@MndtAmdmntReq.setter
		def MndtAmdmntReq(self, value):
			self._MndtAmdmntReq = value if type(value) != base_types.auto else self.make_default("MndtAmdmntReq")

		@MndtAmdmntReq.deleter
		def MndtAmdmntReq(self):
			del self._MndtAmdmntReq
			self._MndtAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtAmdmntReq', type=MandateAmendmentRequestV08, min=1, max=1, mutex_group=None, array=False),
		))