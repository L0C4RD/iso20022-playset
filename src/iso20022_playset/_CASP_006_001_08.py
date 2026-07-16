# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SaleToPOISessionManagementResponseV08

class CASP_006_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:casp.006.001.08"
		_docname = "casp.006.001.08"

		__slots__ = ["_SaleToPOISsnMgmtRspn"]
		@property
		def SaleToPOISsnMgmtRspn(self):
			return self._SaleToPOISsnMgmtRspn

		@SaleToPOISsnMgmtRspn.setter
		def SaleToPOISsnMgmtRspn(self, value):
			self._SaleToPOISsnMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOISsnMgmtRspn', SaleToPOISessionManagementResponseV08, False)

		@SaleToPOISsnMgmtRspn.deleter
		def SaleToPOISsnMgmtRspn(self):
			del self._SaleToPOISsnMgmtRspn
			self._SaleToPOISsnMgmtRspn = base_types.UninitialisedField(self, 'SaleToPOISsnMgmtRspn', SaleToPOISessionManagementResponseV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOISsnMgmtRspn', type=SaleToPOISessionManagementResponseV08, min=1, max=1, mutex_group=None, array=False),
		))