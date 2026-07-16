# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusChangeRequestRejectionV02

class TSMT_029_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.029.001.02"
		_docname = "tsmt.029.001.02"

		__slots__ = ["_StsChngReqRjctn"]
		@property
		def StsChngReqRjctn(self):
			return self._StsChngReqRjctn

		@StsChngReqRjctn.setter
		def StsChngReqRjctn(self, value):
			self._StsChngReqRjctn = value if value is not None else base_types.UninitialisedField(self, 'StsChngReqRjctn', StatusChangeRequestRejectionV02, False)

		@StsChngReqRjctn.deleter
		def StsChngReqRjctn(self):
			del self._StsChngReqRjctn
			self._StsChngReqRjctn = base_types.UninitialisedField(self, 'StsChngReqRjctn', StatusChangeRequestRejectionV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqRjctn', type=StatusChangeRequestRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))