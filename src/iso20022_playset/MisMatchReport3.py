import base_types
import ValidationResult5
import Number

class MisMatchReport3(base_types._BaseFieldType):

	__slots__ = ["_NbOfMisMtchs", "_MisMtchInf"]
	@property
	def NbOfMisMtchs(self):
		return self._NbOfMisMtchs

	@NbOfMisMtchs.setter
	def NbOfMisMtchs(self, value):
		self._NbOfMisMtchs = value if type(value) != auto else self.make_default("NbOfMisMtchs")

	@NbOfMisMtchs.deleter
	def NbOfMisMtchs(self):
		del self._NbOfMisMtchs
		self._NbOfMisMtchs = None

	@property
	def MisMtchInf(self):
		return self._MisMtchInf

	@MisMtchInf.setter
	def MisMtchInf(self, value):
		self._MisMtchInf = value if type(value) != auto else self.make_default("MisMtchInf")

	@MisMtchInf.deleter
	def MisMtchInf(self):
		del self._MisMtchInf
		self._MisMtchInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfMisMtchs', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MisMtchInf', type=ValidationResult5, min=0, max=None, mutex_group=None, array=True),
	))

