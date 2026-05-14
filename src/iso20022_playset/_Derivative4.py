# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Future4 import Future4
from ._Option15 import Option15

class Derivative4(base_types._BaseFieldType):

	__slots__ = ["_Futr", "_Optn"]
	@property
	def Futr(self):
		return self._Futr

	@Futr.setter
	def Futr(self, value):
		self._Futr = value if type(value) != base_types.auto else self.make_default("Futr")

	@Futr.deleter
	def Futr(self):
		del self._Futr
		self._Futr = None

	@property
	def Optn(self):
		return self._Optn

	@Optn.setter
	def Optn(self, value):
		self._Optn = value if type(value) != base_types.auto else self.make_default("Optn")

	@Optn.deleter
	def Optn(self):
		del self._Optn
		self._Optn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Futr', type=Future4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Optn', type=Option15, min=0, max=1, mutex_group=None, array=False),
	))