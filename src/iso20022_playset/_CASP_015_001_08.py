# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIMessageStatusResponseV08 import SaleToPOIMessageStatusResponseV08

class CASP_015_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.015.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SaleToPOIMsgStsRspn"]
		@property
		def SaleToPOIMsgStsRspn(self):
			return self._SaleToPOIMsgStsRspn

		@SaleToPOIMsgStsRspn.setter
		def SaleToPOIMsgStsRspn(self, value):
			self._SaleToPOIMsgStsRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOIMsgStsRspn")

		@SaleToPOIMsgStsRspn.deleter
		def SaleToPOIMsgStsRspn(self):
			del self._SaleToPOIMsgStsRspn
			self._SaleToPOIMsgStsRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIMsgStsRspn', type=SaleToPOIMessageStatusResponseV08, min=1, max=1, mutex_group=None, array=False),
		))