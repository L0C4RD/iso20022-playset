# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIServiceRequestV07 import SaleToPOIServiceRequestV07

class CASP_001_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:casp.001.001.07",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SaleToPOISvcReq"]
		@property
		def SaleToPOISvcReq(self):
			return self._SaleToPOISvcReq

		@SaleToPOISvcReq.setter
		def SaleToPOISvcReq(self, value):
			self._SaleToPOISvcReq = value if type(value) != base_types.auto else self.make_default("SaleToPOISvcReq")

		@SaleToPOISvcReq.deleter
		def SaleToPOISvcReq(self):
			del self._SaleToPOISvcReq
			self._SaleToPOISvcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISvcReq', type=SaleToPOIServiceRequestV07, min=1, max=1, mutex_group=None, array=False),
		))