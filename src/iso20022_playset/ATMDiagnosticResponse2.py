import base_types
import ATMEnvironment6
import ATMCommand7

class ATMDiagnosticResponse2(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_Cmd"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=ATMEnvironment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
	))

