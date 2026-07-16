# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BasketDescription3
from . import FinancialInstrumentIdentification6Choice

class FinancialInstrumentIdentification7Choice(base_types._BaseFieldType):

	__slots__ = ["_Bskt", "_Sngl"]
	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if value is not None else base_types.UninitialisedField(self, 'Bskt', BasketDescription3, False)

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = base_types.UninitialisedField(self, 'Bskt', BasketDescription3, False)

	@property
	def Sngl(self):
		return self._Sngl

	@Sngl.setter
	def Sngl(self, value):
		self._Sngl = value if value is not None else base_types.UninitialisedField(self, 'Sngl', FinancialInstrumentIdentification6Choice, False)

	@Sngl.deleter
	def Sngl(self):
		del self._Sngl
		self._Sngl = base_types.UninitialisedField(self, 'Sngl', FinancialInstrumentIdentification6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bskt', type=BasketDescription3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sngl', type=FinancialInstrumentIdentification6Choice, min=0, max=1, mutex_group=1, array=False),
	))