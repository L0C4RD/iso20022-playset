from . import base_types
from .GenericIdentification30 import GenericIdentification30
from .ResponseStatus2Code import ResponseStatus2Code

class ResponseStatus9Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Cd"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=ResponseStatus2Code, min=0, max=1, mutex_group=1, array=False),
	))

