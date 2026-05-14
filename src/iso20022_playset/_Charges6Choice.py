# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ChargesPerTransaction6 import ChargesPerTransaction6
from ._ChargesPerType6 import ChargesPerType6
from ._ChargesRecord12 import ChargesRecord12

class Charges6Choice(base_types._BaseFieldType):

	__slots__ = ["_PerTp", "_PerTx", "_Sngl"]
	@property
	def PerTp(self):
		return self._PerTp

	@PerTp.setter
	def PerTp(self, value):
		self._PerTp = value if type(value) != base_types.auto else self.make_default("PerTp")

	@PerTp.deleter
	def PerTp(self):
		del self._PerTp
		self._PerTp = None

	@property
	def PerTx(self):
		return self._PerTx

	@PerTx.setter
	def PerTx(self, value):
		self._PerTx = value if type(value) != base_types.auto else self.make_default("PerTx")

	@PerTx.deleter
	def PerTx(self):
		del self._PerTx
		self._PerTx = None

	@property
	def Sngl(self):
		return self._Sngl

	@Sngl.setter
	def Sngl(self, value):
		self._Sngl = value if type(value) != base_types.auto else self.make_default("Sngl")

	@Sngl.deleter
	def Sngl(self):
		del self._Sngl
		self._Sngl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PerTp', type=ChargesPerType6, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='PerTx', type=ChargesPerTransaction6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sngl', type=ChargesRecord12, min=0, max=1, mutex_group=1, array=False),
	))