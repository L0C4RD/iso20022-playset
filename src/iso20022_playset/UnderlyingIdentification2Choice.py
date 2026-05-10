import base_types
import FinancialInstrumentIdentification7Choice
import SwapLegIdentification2

class UnderlyingIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_Swp", "_Othr"]
	@property
	def Swp(self):
		return self._Swp

	@Swp.setter
	def Swp(self, value):
		self._Swp = value if type(value) != auto else self.make_default("Swp")

	@Swp.deleter
	def Swp(self):
		del self._Swp
		self._Swp = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Swp', type=SwapLegIdentification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=FinancialInstrumentIdentification7Choice, min=0, max=1, mutex_group=1, array=False),
	))

