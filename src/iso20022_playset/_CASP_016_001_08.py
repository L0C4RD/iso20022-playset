# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIDeviceRequestV08 import SaleToPOIDeviceRequestV08

class CASP_016_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.016.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SaleToPOIDvcReq"]
		@property
		def SaleToPOIDvcReq(self):
			return self._SaleToPOIDvcReq

		@SaleToPOIDvcReq.setter
		def SaleToPOIDvcReq(self, value):
			self._SaleToPOIDvcReq = value if type(value) != base_types.auto else self.make_default("SaleToPOIDvcReq")

		@SaleToPOIDvcReq.deleter
		def SaleToPOIDvcReq(self):
			del self._SaleToPOIDvcReq
			self._SaleToPOIDvcReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIDvcReq', type=SaleToPOIDeviceRequestV08, min=1, max=1, mutex_group=None, array=False),
		))