from . import base_types
from ._PenaltyStatus2Choice import PenaltyStatus2Choice
from ._PenaltyStatusReason2 import PenaltyStatusReason2

class PenaltyStatus2(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_Sts"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=PenaltyStatusReason2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=PenaltyStatus2Choice, min=1, max=1, mutex_group=None, array=False),
	))

