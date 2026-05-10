from . import base_types
import ErrorHandling3Choice
import Max140Text

class ErrorHandling5(base_types._BaseFieldType):

	__slots__ = ["_Err", "_Desc"]
	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if type(value) != auto else self.make_default("Err")

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Err', type=ErrorHandling3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

