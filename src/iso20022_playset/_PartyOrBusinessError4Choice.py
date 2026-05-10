from . import base_types
from .ErrorHandling4 import ErrorHandling4
from .SystemParty6 import SystemParty6

class PartyOrBusinessError4Choice(base_types._BaseFieldType):

	__slots__ = ["_SysPty", "_BizErr"]
	@property
	def SysPty(self):
		return self._SysPty

	@SysPty.setter
	def SysPty(self, value):
		self._SysPty = value if type(value) != base_types.auto else self.make_default("SysPty")

	@SysPty.deleter
	def SysPty(self):
		del self._SysPty
		self._SysPty = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysPty', type=SystemParty6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling4, min=1, max=None, mutex_group=1, array=True),
	))

