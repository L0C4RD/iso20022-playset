# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Algorithm8Code
from . import Parameter18

class AlgorithmIdentification34(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_Param"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if value is not None else base_types.UninitialisedField(self, 'Algo', Algorithm8Code, False)

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = base_types.UninitialisedField(self, 'Algo', Algorithm8Code, False)

	@property
	def Param(self):
		return self._Param

	@Param.setter
	def Param(self, value):
		self._Param = value if value is not None else base_types.UninitialisedField(self, 'Param', Parameter18, False)

	@Param.deleter
	def Param(self):
		del self._Param
		self._Param = base_types.UninitialisedField(self, 'Param', Parameter18, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Algorithm8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Param', type=Parameter18, min=0, max=1, mutex_group=None, array=False),
	))