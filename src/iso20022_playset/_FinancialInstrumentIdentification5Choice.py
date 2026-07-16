# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrument48Choice
from . import FinancialInstrument53

class FinancialInstrumentIdentification5Choice(base_types._BaseFieldType):

	__slots__ = ["_Bskt", "_Sngl"]
	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if value is not None else base_types.UninitialisedField(self, 'Bskt', FinancialInstrument53, False)

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = base_types.UninitialisedField(self, 'Bskt', FinancialInstrument53, False)

	@property
	def Sngl(self):
		return self._Sngl

	@Sngl.setter
	def Sngl(self, value):
		self._Sngl = value if value is not None else base_types.UninitialisedField(self, 'Sngl', FinancialInstrument48Choice, False)

	@Sngl.deleter
	def Sngl(self):
		del self._Sngl
		self._Sngl = base_types.UninitialisedField(self, 'Sngl', FinancialInstrument48Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bskt', type=FinancialInstrument53, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sngl', type=FinancialInstrument48Choice, min=0, max=1, mutex_group=1, array=False),
	))