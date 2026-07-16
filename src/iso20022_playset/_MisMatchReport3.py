# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number
from . import ValidationResult5

class MisMatchReport3(base_types._BaseFieldType):

	__slots__ = ["_MisMtchInf", "_NbOfMisMtchs"]
	@property
	def MisMtchInf(self):
		return self._MisMtchInf

	@MisMtchInf.setter
	def MisMtchInf(self, value):
		self._MisMtchInf = value if value is not None else base_types.UninitialisedField(self, 'MisMtchInf', ValidationResult5, True)

	@MisMtchInf.deleter
	def MisMtchInf(self):
		del self._MisMtchInf
		self._MisMtchInf = base_types.UninitialisedField(self, 'MisMtchInf', ValidationResult5, True)

	@property
	def NbOfMisMtchs(self):
		return self._NbOfMisMtchs

	@NbOfMisMtchs.setter
	def NbOfMisMtchs(self, value):
		self._NbOfMisMtchs = value if value is not None else base_types.UninitialisedField(self, 'NbOfMisMtchs', Number, False)

	@NbOfMisMtchs.deleter
	def NbOfMisMtchs(self):
		del self._NbOfMisMtchs
		self._NbOfMisMtchs = base_types.UninitialisedField(self, 'NbOfMisMtchs', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MisMtchInf', type=ValidationResult5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfMisMtchs', type=Number, min=1, max=1, mutex_group=None, array=False),
	))