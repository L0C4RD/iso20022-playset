# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusChangeRequestRejectionV02 import StatusChangeRequestRejectionV02

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
			self._StsChngReqRjctn = value if type(value) != base_types.auto else self.make_default("StsChngReqRjctn")

		@StsChngReqRjctn.deleter
		def StsChngReqRjctn(self):
			del self._StsChngReqRjctn
			self._StsChngReqRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqRjctn', type=StatusChangeRequestRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))