# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MandateCopyRequestV04

class PAIN_017_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.017.001.04"
		_docname = "pain.017.001.04"

		__slots__ = ["_MndtCpyReq"]
		@property
		def MndtCpyReq(self):
			return self._MndtCpyReq

		@MndtCpyReq.setter
		def MndtCpyReq(self, value):
			self._MndtCpyReq = value if value is not None else base_types.UninitialisedField(self, 'MndtCpyReq', MandateCopyRequestV04, False)

		@MndtCpyReq.deleter
		def MndtCpyReq(self):
			del self._MndtCpyReq
			self._MndtCpyReq = base_types.UninitialisedField(self, 'MndtCpyReq', MandateCopyRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtCpyReq', type=MandateCopyRequestV04, min=1, max=1, mutex_group=None, array=False),
		))