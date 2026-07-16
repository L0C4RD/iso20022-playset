# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EquityDerivative3Choice
from . import EquityReturnParameter1Code

class EquityDerivative2(base_types._BaseFieldType):

	__slots__ = ["_Param", "_UndrlygTp"]
	@property
	def Param(self):
		return self._Param

	@Param.setter
	def Param(self, value):
		self._Param = value if value is not None else base_types.UninitialisedField(self, 'Param', EquityReturnParameter1Code, False)

	@Param.deleter
	def Param(self):
		del self._Param
		self._Param = base_types.UninitialisedField(self, 'Param', EquityReturnParameter1Code, False)

	@property
	def UndrlygTp(self):
		return self._UndrlygTp

	@UndrlygTp.setter
	def UndrlygTp(self, value):
		self._UndrlygTp = value if value is not None else base_types.UninitialisedField(self, 'UndrlygTp', EquityDerivative3Choice, False)

	@UndrlygTp.deleter
	def UndrlygTp(self):
		del self._UndrlygTp
		self._UndrlygTp = base_types.UninitialisedField(self, 'UndrlygTp', EquityDerivative3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Param', type=EquityReturnParameter1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygTp', type=EquityDerivative3Choice, min=1, max=1, mutex_group=None, array=False),
	))