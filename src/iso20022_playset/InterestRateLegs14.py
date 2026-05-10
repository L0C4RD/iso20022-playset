import base_types
import InterestRate33Choice

class InterestRateLegs14(base_types._BaseFieldType):

	__slots__ = ["_FrstLeg", "_ScndLeg"]
	@property
	def FrstLeg(self):
		return self._FrstLeg

	@FrstLeg.setter
	def FrstLeg(self, value):
		self._FrstLeg = value if type(value) != auto else self.make_default("FrstLeg")

	@FrstLeg.deleter
	def FrstLeg(self):
		del self._FrstLeg
		self._FrstLeg = None

	@property
	def ScndLeg(self):
		return self._ScndLeg

	@ScndLeg.setter
	def ScndLeg(self, value):
		self._ScndLeg = value if type(value) != auto else self.make_default("ScndLeg")

	@ScndLeg.deleter
	def ScndLeg(self):
		del self._ScndLeg
		self._ScndLeg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstLeg', type=InterestRate33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLeg', type=InterestRate33Choice, min=0, max=1, mutex_group=None, array=False),
	))

