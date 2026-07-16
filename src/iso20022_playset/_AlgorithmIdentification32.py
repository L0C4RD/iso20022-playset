# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Algorithm28Code
from . import Parameter12

class AlgorithmIdentification32(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_Param"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if value is not None else base_types.UninitialisedField(self, 'Algo', Algorithm28Code, False)

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = base_types.UninitialisedField(self, 'Algo', Algorithm28Code, False)

	@property
	def Param(self):
		return self._Param

	@Param.setter
	def Param(self, value):
		self._Param = value if value is not None else base_types.UninitialisedField(self, 'Param', Parameter12, False)

	@Param.deleter
	def Param(self):
		del self._Param
		self._Param = base_types.UninitialisedField(self, 'Param', Parameter12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Algorithm28Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Param', type=Parameter12, min=0, max=1, mutex_group=None, array=False),
	))