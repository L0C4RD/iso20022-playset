import base_types
import FloatingInterestRate8
import PercentageRate

class InterestRate8Choice(base_types._BaseFieldType):

	__slots__ = ["_Fltg", "_Fxd"]
	@property
	def Fltg(self):
		return self._Fltg

	@Fltg.setter
	def Fltg(self, value):
		self._Fltg = value if type(value) != auto else self.make_default("Fltg")

	@Fltg.deleter
	def Fltg(self):
		del self._Fltg
		self._Fltg = None

	@property
	def Fxd(self):
		return self._Fxd

	@Fxd.setter
	def Fxd(self, value):
		self._Fxd = value if type(value) != auto else self.make_default("Fxd")

	@Fxd.deleter
	def Fxd(self):
		del self._Fxd
		self._Fxd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fltg', type=FloatingInterestRate8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Fxd', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

