from . import base_types
from ._ErrorHandling5 import ErrorHandling5
from ._IntraBalanceModification7 import IntraBalanceModification7

class IntraBalanceOrOperationalError12Choice(base_types._BaseFieldType):

	__slots__ = ["_Mods", "_OprlErr"]
	@property
	def Mods(self):
		return self._Mods

	@Mods.setter
	def Mods(self, value):
		self._Mods = value if type(value) != base_types.auto else self.make_default("Mods")

	@Mods.deleter
	def Mods(self):
		del self._Mods
		self._Mods = None

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mods', type=IntraBalanceModification7, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

