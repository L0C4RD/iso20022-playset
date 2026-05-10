from . import base_types
from .ATMEnvironment7 import ATMEnvironment7
from .ATMCommand14 import ATMCommand14

class ATMDeviceControl3(base_types._BaseFieldType):

	__slots__ = ["_Cmd", "_Envt"]
	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != base_types.auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmd', type=ATMCommand14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=ATMEnvironment7, min=1, max=1, mutex_group=None, array=False),
	))

