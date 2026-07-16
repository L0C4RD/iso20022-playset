# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusChangeRequestV02

class TSMT_026_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02"
		_docname = "tsmt.026.001.02"

		__slots__ = ["_StsChngReq"]
		@property
		def StsChngReq(self):
			return self._StsChngReq

		@StsChngReq.setter
		def StsChngReq(self, value):
			self._StsChngReq = value if value is not None else base_types.UninitialisedField(self, 'StsChngReq', StatusChangeRequestV02, False)

		@StsChngReq.deleter
		def StsChngReq(self):
			del self._StsChngReq
			self._StsChngReq = base_types.UninitialisedField(self, 'StsChngReq', StatusChangeRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReq', type=StatusChangeRequestV02, min=1, max=1, mutex_group=None, array=False),
		))