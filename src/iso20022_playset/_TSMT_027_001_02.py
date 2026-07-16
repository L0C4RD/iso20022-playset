# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusChangeRequestAcceptanceV02

class TSMT_027_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02"
		_docname = "tsmt.027.001.02"

		__slots__ = ["_StsChngReqAccptnc"]
		@property
		def StsChngReqAccptnc(self):
			return self._StsChngReqAccptnc

		@StsChngReqAccptnc.setter
		def StsChngReqAccptnc(self, value):
			self._StsChngReqAccptnc = value if value is not None else base_types.UninitialisedField(self, 'StsChngReqAccptnc', StatusChangeRequestAcceptanceV02, False)

		@StsChngReqAccptnc.deleter
		def StsChngReqAccptnc(self):
			del self._StsChngReqAccptnc
			self._StsChngReqAccptnc = base_types.UninitialisedField(self, 'StsChngReqAccptnc', StatusChangeRequestAcceptanceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqAccptnc', type=StatusChangeRequestAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))