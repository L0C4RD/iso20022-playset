# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FixedOpenTermContract2 import FixedOpenTermContract2

class ContractTerm7Choice(base_types._BaseFieldType):

	__slots__ = ["_Fxd", "_Opn"]
	@property
	def Fxd(self):
		return self._Fxd

	@Fxd.setter
	def Fxd(self, value):
		self._Fxd = value if type(value) != base_types.auto else self.make_default("Fxd")

	@Fxd.deleter
	def Fxd(self):
		del self._Fxd
		self._Fxd = None

	@property
	def Opn(self):
		return self._Opn

	@Opn.setter
	def Opn(self, value):
		self._Opn = value if type(value) != base_types.auto else self.make_default("Opn")

	@Opn.deleter
	def Opn(self):
		del self._Opn
		self._Opn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fxd', type=FixedOpenTermContract2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Opn', type=FixedOpenTermContract2, min=0, max=1, mutex_group=1, array=False),
	))