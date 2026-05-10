from . import base_types
from ._ATMCommandIdentification1 import ATMCommandIdentification1
from ._ATMCommand5Code import ATMCommand5Code

class ATMCommand9(base_types._BaseFieldType):

	__slots__ = ["_CmdId", "_Tp"]
	@property
	def CmdId(self):
		return self._CmdId

	@CmdId.setter
	def CmdId(self, value):
		self._CmdId = value if type(value) != base_types.auto else self.make_default("CmdId")

	@CmdId.deleter
	def CmdId(self):
		del self._CmdId
		self._CmdId = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmdId', type=ATMCommandIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ATMCommand5Code, min=1, max=1, mutex_group=None, array=False),
	))

