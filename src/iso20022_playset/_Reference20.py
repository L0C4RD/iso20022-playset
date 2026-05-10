from . import base_types
from .Max35Text import Max35Text

class Reference20(base_types._BaseFieldType):

	__slots__ = ["_IntrstPmtRspnId", "_IntrstPmtReqId"]
	@property
	def IntrstPmtRspnId(self):
		return self._IntrstPmtRspnId

	@IntrstPmtRspnId.setter
	def IntrstPmtRspnId(self, value):
		self._IntrstPmtRspnId = value if type(value) != base_types.auto else self.make_default("IntrstPmtRspnId")

	@IntrstPmtRspnId.deleter
	def IntrstPmtRspnId(self):
		del self._IntrstPmtRspnId
		self._IntrstPmtRspnId = None

	@property
	def IntrstPmtReqId(self):
		return self._IntrstPmtReqId

	@IntrstPmtReqId.setter
	def IntrstPmtReqId(self, value):
		self._IntrstPmtReqId = value if type(value) != base_types.auto else self.make_default("IntrstPmtReqId")

	@IntrstPmtReqId.deleter
	def IntrstPmtReqId(self):
		del self._IntrstPmtReqId
		self._IntrstPmtReqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstPmtRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmtReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

