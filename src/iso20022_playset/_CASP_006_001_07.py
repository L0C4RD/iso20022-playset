# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOISessionManagementResponseV07 import SaleToPOISessionManagementResponseV07

class CASP_006_001_07():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='SaleToPOISsnMgmtRspn', type=SaleToPOISessionManagementResponseV07, min=1, max=1, mutex_group=None, array=False),
		))