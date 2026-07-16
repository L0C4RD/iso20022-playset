# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MandateSuspensionRequestV04

class PAIN_018_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.018.001.04"
		_docname = "pain.018.001.04"

		__slots__ = ["_MndtSspnsnReq"]
		@property
		def MndtSspnsnReq(self):
			return self._MndtSspnsnReq

		@MndtSspnsnReq.setter
		def MndtSspnsnReq(self, value):
			self._MndtSspnsnReq = value if value is not None else base_types.UninitialisedField(self, 'MndtSspnsnReq', MandateSuspensionRequestV04, False)

		@MndtSspnsnReq.deleter
		def MndtSspnsnReq(self):
			del self._MndtSspnsnReq
			self._MndtSspnsnReq = base_types.UninitialisedField(self, 'MndtSspnsnReq', MandateSuspensionRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtSspnsnReq', type=MandateSuspensionRequestV04, min=1, max=1, mutex_group=None, array=False),
		))