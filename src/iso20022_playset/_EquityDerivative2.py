from . import base_types
from ._EquityReturnParameter1Code import EquityReturnParameter1Code
from ._EquityDerivative3Choice import EquityDerivative3Choice

class EquityDerivative2(base_types._BaseFieldType):

	__slots__ = ["_UndrlygTp", "_Param"]
	@property
	def Param(self):
		return self._Param

	@Param.setter
	def Param(self, value):
		self._Param = value if type(value) != base_types.auto else self.make_default("Param")

	@Param.deleter
	def Param(self):
		del self._Param
		self._Param = None

	@property
	def UndrlygTp(self):
		return self._UndrlygTp

	@UndrlygTp.setter
	def UndrlygTp(self, value):
		self._UndrlygTp = value if type(value) != base_types.auto else self.make_default("UndrlygTp")

	@UndrlygTp.deleter
	def UndrlygTp(self):
		del self._UndrlygTp
		self._UndrlygTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Param', type=EquityReturnParameter1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTp', type=EquityDerivative3Choice, min=1, max=1, mutex_group=None, array=False),
	))

