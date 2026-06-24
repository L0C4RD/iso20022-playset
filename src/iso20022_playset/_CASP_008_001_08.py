# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIAdministrativeResponseV08 import SaleToPOIAdministrativeResponseV08

class CASP_008_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.008.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SaleToPOIAdmstvRspn"]
		@property
		def SaleToPOIAdmstvRspn(self):
			return self._SaleToPOIAdmstvRspn

		@SaleToPOIAdmstvRspn.setter
		def SaleToPOIAdmstvRspn(self, value):
			self._SaleToPOIAdmstvRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIAdmstvRspn")

		@SaleToPOIAdmstvRspn.deleter
		def SaleToPOIAdmstvRspn(self):
			del self._SaleToPOIAdmstvRspn
			self._SaleToPOIAdmstvRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIAdmstvRspn', type=SaleToPOIAdministrativeResponseV08, min=1, max=1, mutex_group=None, array=False),
		))