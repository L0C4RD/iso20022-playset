from . import base_types
from ._Frequency36Choice import Frequency36Choice
from ._SequenceType2Code import SequenceType2Code
from ._ISODate import ISODate
from ._DatePeriod3 import DatePeriod3

class MandateOccurrences5(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_SeqTp", "_FrstColltnDt", "_FnlColltnDt", "_Drtn"]
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

	@property
	def SeqTp(self):
		return self._SeqTp

	@SeqTp.setter
	def SeqTp(self, value):
		self._SeqTp = value if type(value) != base_types.auto else self.make_default("SeqTp")

	@SeqTp.deleter
	def SeqTp(self):
		del self._SeqTp
		self._SeqTp = None

	@property
	def FrstColltnDt(self):
		return self._FrstColltnDt

	@FrstColltnDt.setter
	def FrstColltnDt(self, value):
		self._FrstColltnDt = value if type(value) != base_types.auto else self.make_default("FrstColltnDt")

	@FrstColltnDt.deleter
	def FrstColltnDt(self):
		del self._FrstColltnDt
		self._FrstColltnDt = None

	@property
	def FnlColltnDt(self):
		return self._FnlColltnDt

	@FnlColltnDt.setter
	def FnlColltnDt(self, value):
		self._FnlColltnDt = value if type(value) != base_types.auto else self.make_default("FnlColltnDt")

	@FnlColltnDt.deleter
	def FnlColltnDt(self):
		del self._FnlColltnDt
		self._FnlColltnDt = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frqcy', type=Frequency36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqTp', type=SequenceType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=DatePeriod3, min=0, max=1, mutex_group=None, array=False),
	))

