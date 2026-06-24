# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOISessionManagementResponseV08 import SaleToPOISessionManagementResponseV08

class CASP_006_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.006.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SaleToPOISsnMgmtRspn"]
		@property
		def SaleToPOISsnMgmtRspn(self):
			return self._SaleToPOISsnMgmtRspn

		@SaleToPOISsnMgmtRspn.setter
		def SaleToPOISsnMgmtRspn(self, value):
			self._SaleToPOISsnMgmtRspn = value if type(value) != base_types.auto else self.make_default("SaleToPOISsnMgmtRspn")

		@SaleToPOISsnMgmtRspn.deleter
		def SaleToPOISsnMgmtRspn(self):
			del self._SaleToPOISsnMgmtRspn
			self._SaleToPOISsnMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISsnMgmtRspn', type=SaleToPOISessionManagementResponseV08, min=1, max=1, mutex_group=None, array=False),
		))