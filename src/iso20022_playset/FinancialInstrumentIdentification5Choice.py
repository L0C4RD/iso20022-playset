import base_types
import FinancialInstrument48Choice
import FinancialInstrument53

class FinancialInstrumentIdentification5Choice(base_types._BaseFieldType):

	__slots__ = ["_Sngl", "_Bskt"]
	@property
	def Sngl(self):
		return self._Sngl

	@Sngl.setter
	def Sngl(self, value):
		self._Sngl = value if type(value) != auto else self.make_default("Sngl")

	@Sngl.deleter
	def Sngl(self):
		del self._Sngl
		self._Sngl = None

	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if type(value) != auto else self.make_default("Bskt")

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sngl', type=FinancialInstrument48Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Bskt', type=FinancialInstrument53, min=0, max=1, mutex_group=1, array=False),
	))

