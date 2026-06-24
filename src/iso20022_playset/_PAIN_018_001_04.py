# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MandateSuspensionRequestV04 import MandateSuspensionRequestV04

class PAIN_018_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:pain.018.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_MndtSspnsnReq"]
		@property
		def MndtSspnsnReq(self):
			return self._MndtSspnsnReq

		@MndtSspnsnReq.setter
		def MndtSspnsnReq(self, value):
			self._MndtSspnsnReq = value if type(value) != base_types.auto else self.make_default("MndtSspnsnReq")

		@MndtSspnsnReq.deleter
		def MndtSspnsnReq(self):
			del self._MndtSspnsnReq
			self._MndtSspnsnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MndtSspnsnReq', type=MandateSuspensionRequestV04, min=1, max=1, mutex_group=None, array=False),
		))