# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IndependentAmount1 import IndependentAmount1
from ._IndependentAmount2 import IndependentAmount2

class AggregatedIndependentAmount1(base_types._BaseFieldType):

	__slots__ = ["_NetOpnPos", "_OthrAmt", "_Trad", "_ValAtRsk"]
	@property
	def NetOpnPos(self):
		return self._NetOpnPos

	@NetOpnPos.setter
	def NetOpnPos(self, value):
		self._NetOpnPos = value if type(value) != base_types.auto else self.make_default("NetOpnPos")

	@NetOpnPos.deleter
	def NetOpnPos(self):
		del self._NetOpnPos
		self._NetOpnPos = None

	@property
	def OthrAmt(self):
		return self._OthrAmt

	@OthrAmt.setter
	def OthrAmt(self, value):
		self._OthrAmt = value if type(value) != base_types.auto else self.make_default("OthrAmt")

	@OthrAmt.deleter
	def OthrAmt(self):
		del self._OthrAmt
		self._OthrAmt = None

	@property
	def Trad(self):
		return self._Trad

	@Trad.setter
	def Trad(self, value):
		self._Trad = value if type(value) != base_types.auto else self.make_default("Trad")

	@Trad.deleter
	def Trad(self):
		del self._Trad
		self._Trad = None

	@property
	def ValAtRsk(self):
		return self._ValAtRsk

	@ValAtRsk.setter
	def ValAtRsk(self, value):
		self._ValAtRsk = value if type(value) != base_types.auto else self.make_default("ValAtRsk")

	@ValAtRsk.deleter
	def ValAtRsk(self):
		del self._ValAtRsk
		self._ValAtRsk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetOpnPos', type=IndependentAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmt', type=IndependentAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Trad', type=IndependentAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAtRsk', type=IndependentAmount1, min=0, max=1, mutex_group=None, array=False),
	))