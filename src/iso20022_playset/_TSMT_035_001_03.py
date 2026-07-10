# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusExtensionRequestV03 import StatusExtensionRequestV03

class TSMT_035_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.035.001.03"
		_docname = "tsmt.035.001.03"

		__slots__ = ["_StsXtnsnReq"]
		@property
		def StsXtnsnReq(self):
			return self._StsXtnsnReq

		@StsXtnsnReq.setter
		def StsXtnsnReq(self, value):
			self._StsXtnsnReq = value if type(value) != base_types.auto else self.make_default("StsXtnsnReq")

		@StsXtnsnReq.deleter
		def StsXtnsnReq(self):
			del self._StsXtnsnReq
			self._StsXtnsnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnReq', type=StatusExtensionRequestV03, min=1, max=1, mutex_group=None, array=False),
		))