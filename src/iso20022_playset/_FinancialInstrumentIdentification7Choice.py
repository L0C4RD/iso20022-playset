# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BasketDescription3 import BasketDescription3
from ._FinancialInstrumentIdentification6Choice import FinancialInstrumentIdentification6Choice

class FinancialInstrumentIdentification7Choice(base_types._BaseFieldType):

	__slots__ = ["_Bskt", "_Sngl"]
	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if type(value) != base_types.auto else self.make_default("Bskt")

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = None

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
		base_types.FieldEntry(name='Bskt', type=BasketDescription3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sngl', type=FinancialInstrumentIdentification6Choice, min=0, max=1, mutex_group=1, array=False),
	))