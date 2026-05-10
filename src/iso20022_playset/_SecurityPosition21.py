from . import base_types
from ._SecurityIdentification19 import SecurityIdentification19
from ._EligiblePosition19 import EligiblePosition19

class SecurityPosition21(base_types._BaseFieldType):

	__slots__ = ["_Pos", "_FinInstrmId"]
	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if type(value) != base_types.auto else self.make_default("Pos")

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pos', type=EligiblePosition19, min=0, max=1000, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

