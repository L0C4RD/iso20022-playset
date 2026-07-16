# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max500Text
from . import Operator1Code

class SearchAnd1(base_types._BaseFieldType):

	__slots__ = ["_Oprtr", "_Trgt", "_Val"]
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
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if value is not None else base_types.UninitialisedField(self, 'Trgt', Max500Text, False)

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = base_types.UninitialisedField(self, 'Trgt', Max500Text, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max500Text, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max500Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Oprtr', type=Operator1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
	))