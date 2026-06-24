# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIDeviceResponseV07 import SaleToPOIDeviceResponseV07

class CASP_017_001_07():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.017.001.07"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SaleToPOIDvcRspn"]
		@property
		def SaleToPOIDvcRspn(self):
			return self._SaleToPOIDvcRspn

		@SaleToPOIDvcRspn.setter
		def SaleToPOIDvcRspn(self, value):
			self._SaleToPOIDvcRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIDvcRspn")

		@SaleToPOIDvcRspn.deleter
		def SaleToPOIDvcRspn(self):
			del self._SaleToPOIDvcRspn
			self._SaleToPOIDvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIDvcRspn', type=SaleToPOIDeviceResponseV07, min=1, max=1, mutex_group=None, array=False),
		))