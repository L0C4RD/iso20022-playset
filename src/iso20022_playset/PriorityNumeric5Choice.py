from . import base_types
from .GenericIdentification47 import GenericIdentification47
from .Exact4NumericText import Exact4NumericText

class PriorityNumeric5Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Nmrc"]
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
	def Nmrc(self):
		return self._Nmrc

	@Nmrc.setter
	def Nmrc(self, value):
		self._Nmrc = value if type(value) != auto else self.make_default("Nmrc")

	@Nmrc.deleter
	def Nmrc(self):
		del self._Nmrc
		self._Nmrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification47, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nmrc', type=Exact4NumericText, min=0, max=1, mutex_group=1, array=False),
	))

