# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusExtensionRequestRejectionV03

class TSMT_033_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.033.001.03"
		_docname = "tsmt.033.001.03"

		__slots__ = ["_StsXtnsnReqRjctn"]
		@property
		def StsXtnsnReqRjctn(self):
			return self._StsXtnsnReqRjctn

		@StsXtnsnReqRjctn.setter
		def StsXtnsnReqRjctn(self, value):
			self._StsXtnsnReqRjctn = value if value is not None else base_types.UninitialisedField(self, 'StsXtnsnReqRjctn', StatusExtensionRequestRejectionV03, False)

		@StsXtnsnReqRjctn.deleter
		def StsXtnsnReqRjctn(self):
			del self._StsXtnsnReqRjctn
			self._StsXtnsnReqRjctn = base_types.UninitialisedField(self, 'StsXtnsnReqRjctn', StatusExtensionRequestRejectionV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnReqRjctn', type=StatusExtensionRequestRejectionV03, min=1, max=1, mutex_group=None, array=False),
		))