import base_types
import MarginCallRequestV05

class COLR_003_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MrgnCallReq"]
		@property
		def MrgnCallReq(self):
			return self._MrgnCallReq

		@MrgnCallReq.setter
		def MrgnCallReq(self, value):
			self._MrgnCallReq = value if type(value) != auto else self.make_default("MrgnCallReq")

		@MrgnCallReq.deleter
		def MrgnCallReq(self):
			del self._MrgnCallReq
			self._MrgnCallReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnCallReq', type=MarginCallRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

