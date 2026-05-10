from . import base_types
import MarginCallResponseV05

class COLR_004_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MrgnCallRspn"]
		@property
		def MrgnCallRspn(self):
			return self._MrgnCallRspn

		@MrgnCallRspn.setter
		def MrgnCallRspn(self, value):
			self._MrgnCallRspn = value if type(value) != auto else self.make_default("MrgnCallRspn")

		@MrgnCallRspn.deleter
		def MrgnCallRspn(self):
			del self._MrgnCallRspn
			self._MrgnCallRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnCallRspn', type=MarginCallResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

