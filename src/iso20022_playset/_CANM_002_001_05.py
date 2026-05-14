from . import base_types
from ._NetworkManagementResponseV05 import NetworkManagementResponseV05

class CANM_002_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_NtwkMgmtRspn"]
		@property
		def NtwkMgmtRspn(self):
			return self._NtwkMgmtRspn

		@NtwkMgmtRspn.setter
		def NtwkMgmtRspn(self, value):
			self._NtwkMgmtRspn = value if type(value) != base_types.auto else self.make_default("NtwkMgmtRspn")

		@NtwkMgmtRspn.deleter
		def NtwkMgmtRspn(self):
			del self._NtwkMgmtRspn
			self._NtwkMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NtwkMgmtRspn', type=NetworkManagementResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

