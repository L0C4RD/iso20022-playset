import base_types
import Operator1Code
import Max500Text

class SearchAnd1(base_types._BaseFieldType):

	__slots__ = ["_Trgt", "_Oprtr", "_Val"]
	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if type(value) != auto else self.make_default("Trgt")

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = None

	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if type(value) != auto else self.make_default("Oprtr")

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Trgt', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oprtr', type=Operator1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max500Text, min=1, max=1, mutex_group=None, array=False),
	))

