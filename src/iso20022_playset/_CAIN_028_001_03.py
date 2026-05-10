from . import base_types
from .ChargeBackResponseV03 import ChargeBackResponseV03

class CAIN_028_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ChrgBckRspn"]
		@property
		def ChrgBckRspn(self):
			return self._ChrgBckRspn

		@ChrgBckRspn.setter
		def ChrgBckRspn(self, value):
			self._ChrgBckRspn = value if type(value) != base_types.auto else self.make_default("ChrgBckRspn")

		@ChrgBckRspn.deleter
		def ChrgBckRspn(self):
			del self._ChrgBckRspn
			self._ChrgBckRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgBckRspn', type=ChargeBackResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

