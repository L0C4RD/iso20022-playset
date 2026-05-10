from . import base_types
from .Number import Number
from .ExternalDateFrequency1Code import ExternalDateFrequency1Code
from .ISODate import ISODate

class DateInformation1(base_types._BaseFieldType):

	__slots__ = ["_Nb", "_StartDt", "_Frqcy"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=ExternalDateFrequency1Code, min=1, max=1, mutex_group=None, array=False),
	))

