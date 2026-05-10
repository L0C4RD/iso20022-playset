import base_types
import CardManagementResponseV03

class CAIN_024_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CardMgmtRspn"]
		@property
		def CardMgmtRspn(self):
			return self._CardMgmtRspn

		@CardMgmtRspn.setter
		def CardMgmtRspn(self, value):
			self._CardMgmtRspn = value if type(value) != auto else self.make_default("CardMgmtRspn")

		@CardMgmtRspn.deleter
		def CardMgmtRspn(self):
			del self._CardMgmtRspn
			self._CardMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CardMgmtRspn', type=CardManagementResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

