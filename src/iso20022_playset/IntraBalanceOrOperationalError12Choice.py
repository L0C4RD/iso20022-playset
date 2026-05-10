import base_types
import ErrorHandling5
import IntraBalanceModification7

class IntraBalanceOrOperationalError12Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_Mods"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	@property
	def Mods(self):
		return self._Mods

	@Mods.setter
	def Mods(self, value):
		self._Mods = value if type(value) != auto else self.make_default("Mods")

	@Mods.deleter
	def Mods(self):
		del self._Mods
		self._Mods = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Mods', type=IntraBalanceModification7, min=1, max=None, mutex_group=1, array=True),
	))

