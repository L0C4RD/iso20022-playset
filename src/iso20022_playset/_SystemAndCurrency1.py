from . import base_types
from ._SystemIdentification2Choice import SystemIdentification2Choice
from ._ActiveCurrencyCode import ActiveCurrencyCode

class SystemAndCurrency1(base_types._BaseFieldType):

	__slots__ = ["_SysId", "_SysCcy"]
	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != base_types.auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	@property
	def SysCcy(self):
		return self._SysCcy

	@SysCcy.setter
	def SysCcy(self, value):
		self._SysCcy = value if type(value) != base_types.auto else self.make_default("SysCcy")

	@SysCcy.deleter
	def SysCcy(self):
		del self._SysCcy
		self._SysCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

