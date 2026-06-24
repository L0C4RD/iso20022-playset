# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusChangeRequestAcceptanceV02 import StatusChangeRequestAcceptanceV02

class TSMT_027_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.027.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_StsChngReqAccptnc"]
		@property
		def StsChngReqAccptnc(self):
			return self._StsChngReqAccptnc

		@StsChngReqAccptnc.setter
		def StsChngReqAccptnc(self, value):
			self._StsChngReqAccptnc = value if type(value) != base_types.auto else self.make_default("StsChngReqAccptnc")

		@StsChngReqAccptnc.deleter
		def StsChngReqAccptnc(self):
			del self._StsChngReqAccptnc
			self._StsChngReqAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqAccptnc', type=StatusChangeRequestAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))