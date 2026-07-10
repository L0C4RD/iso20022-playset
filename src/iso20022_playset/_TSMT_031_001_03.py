# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusExtensionRequestAcceptanceV03 import StatusExtensionRequestAcceptanceV03

class TSMT_031_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.031.001.03"
		_docname = "tsmt.031.001.03"

		__slots__ = ["_StsXtnsnReqAccptnc"]
		@property
		def StsXtnsnReqAccptnc(self):
			return self._StsXtnsnReqAccptnc

		@StsXtnsnReqAccptnc.setter
		def StsXtnsnReqAccptnc(self, value):
			self._StsXtnsnReqAccptnc = value if type(value) != base_types.auto else self.make_default("StsXtnsnReqAccptnc")

		@StsXtnsnReqAccptnc.deleter
		def StsXtnsnReqAccptnc(self):
			del self._StsXtnsnReqAccptnc
			self._StsXtnsnReqAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnReqAccptnc', type=StatusExtensionRequestAcceptanceV03, min=1, max=1, mutex_group=None, array=False),
		))