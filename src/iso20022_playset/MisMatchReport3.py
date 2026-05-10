from . import base_types
from .Number import Number
from .ValidationResult5 import ValidationResult5

class MisMatchReport3(base_types._BaseFieldType):

	__slots__ = ["_MisMtchInf", "_NbOfMisMtchs"]
	@property
	def MisMtchInf(self):
		return self._MisMtchInf

	@MisMtchInf.setter
	def MisMtchInf(self, value):
		self._MisMtchInf = value if type(value) != base_types.auto else self.make_default("MisMtchInf")

	@MisMtchInf.deleter
	def MisMtchInf(self):
		del self._MisMtchInf
		self._MisMtchInf = None

	@property
	def NbOfMisMtchs(self):
		return self._NbOfMisMtchs

	@NbOfMisMtchs.setter
	def NbOfMisMtchs(self, value):
		self._NbOfMisMtchs = value if type(value) != base_types.auto else self.make_default("NbOfMisMtchs")

	@NbOfMisMtchs.deleter
	def NbOfMisMtchs(self):
		del self._NbOfMisMtchs
		self._NbOfMisMtchs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MisMtchInf', type=ValidationResult5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfMisMtchs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))

