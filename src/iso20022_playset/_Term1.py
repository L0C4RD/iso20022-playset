# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Operator1Code
from . import RateOrAbsoluteValue1Choice

class Term1(base_types._BaseFieldType):

	__slots__ = ["_Oprtr", "_Val"]
	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if value is not None else base_types.UninitialisedField(self, 'Oprtr', Operator1Code, False)

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = base_types.UninitialisedField(self, 'Oprtr', Operator1Code, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', RateOrAbsoluteValue1Choice, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', RateOrAbsoluteValue1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Oprtr', type=Operator1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=RateOrAbsoluteValue1Choice, min=1, max=1, mutex_group=None, array=False),
	))