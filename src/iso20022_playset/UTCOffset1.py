from . import base_types
import PlusOrMinusIndicator
import ISOTime

class UTCOffset1(base_types._BaseFieldType):

	__slots__ = ["_NbOfHrs", "_Sgn"]
	@property
	def NbOfHrs(self):
		return self._NbOfHrs

	@NbOfHrs.setter
	def NbOfHrs(self, value):
		self._NbOfHrs = value if type(value) != auto else self.make_default("NbOfHrs")

	@NbOfHrs.deleter
	def NbOfHrs(self):
		del self._NbOfHrs
		self._NbOfHrs = None

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if type(value) != auto else self.make_default("Sgn")

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfHrs', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=1, max=1, mutex_group=None, array=False),
	))

