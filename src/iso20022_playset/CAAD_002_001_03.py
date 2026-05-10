import base_types
import BatchManagementResponseV03

class CAAD_002_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BtchMgmtRspn"]
		@property
		def BtchMgmtRspn(self):
			return self._BtchMgmtRspn

		@BtchMgmtRspn.setter
		def BtchMgmtRspn(self, value):
			self._BtchMgmtRspn = value if type(value) != auto else self.make_default("BtchMgmtRspn")

		@BtchMgmtRspn.deleter
		def BtchMgmtRspn(self):
			del self._BtchMgmtRspn
			self._BtchMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchMgmtRspn', type=BatchManagementResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

