# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusChangeRequestV02 import StatusChangeRequestV02

class TSMT_026_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.026.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_StsChngReq"]
		@property
		def StsChngReq(self):
			return self._StsChngReq

		@StsChngReq.setter
		def StsChngReq(self, value):
			self._StsChngReq = value if type(value) != base_types.auto else self.make_default("StsChngReq")

		@StsChngReq.deleter
		def StsChngReq(self):
			del self._StsChngReq
			self._StsChngReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReq', type=StatusChangeRequestV02, min=1, max=1, mutex_group=None, array=False),
		))