# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MaintenanceDelegationResponseV08 import MaintenanceDelegationResponseV08

class CATM_006_001_08():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catm.006.001.08"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_MntncDlgtnRspn"]
		@property
		def MntncDlgtnRspn(self):
			return self._MntncDlgtnRspn

		@MntncDlgtnRspn.setter
		def MntncDlgtnRspn(self, value):
			self._MntncDlgtnRspn = value if type(value) != base_types.auto else self.make_default("MntncDlgtnRspn")

		@MntncDlgtnRspn.deleter
		def MntncDlgtnRspn(self):
			del self._MntncDlgtnRspn
			self._MntncDlgtnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MntncDlgtnRspn', type=MaintenanceDelegationResponseV08, min=1, max=1, mutex_group=None, array=False),
		))