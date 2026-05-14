# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Algorithm7Code import Algorithm7Code
from ._PublicRSAKey1 import PublicRSAKey1

class PublicRSAKey2(base_types._BaseFieldType):

	__slots__ = ["_Algo", "_PblcKeyVal"]
	@property
	def Algo(self):
		return self._Algo

	@Algo.setter
	def Algo(self, value):
		self._Algo = value if type(value) != base_types.auto else self.make_default("Algo")

	@Algo.deleter
	def Algo(self):
		del self._Algo
		self._Algo = None

	@property
	def PblcKeyVal(self):
		return self._PblcKeyVal

	@PblcKeyVal.setter
	def PblcKeyVal(self, value):
		self._PblcKeyVal = value if type(value) != base_types.auto else self.make_default("PblcKeyVal")

	@PblcKeyVal.deleter
	def PblcKeyVal(self):
		del self._PblcKeyVal
		self._PblcKeyVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Algo', type=Algorithm7Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblcKeyVal', type=PublicRSAKey1, min=1, max=1, mutex_group=None, array=False),
	))