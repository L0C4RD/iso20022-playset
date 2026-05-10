from . import base_types
from .GenericIdentification175 import GenericIdentification175
from .TrueFalseIndicator import TrueFalseIndicator

class NonFinancialInstitutionSector10(base_types._BaseFieldType):

	__slots__ = ["_FdrlInstn", "_ClrThrshld", "_DrctlyLkdActvty", "_Sctr"]
	@property
	def FdrlInstn(self):
		return self._FdrlInstn

	@FdrlInstn.setter
	def FdrlInstn(self, value):
		self._FdrlInstn = value if type(value) != auto else self.make_default("FdrlInstn")

	@FdrlInstn.deleter
	def FdrlInstn(self):
		del self._FdrlInstn
		self._FdrlInstn = None

	@property
	def ClrThrshld(self):
		return self._ClrThrshld

	@ClrThrshld.setter
	def ClrThrshld(self, value):
		self._ClrThrshld = value if type(value) != auto else self.make_default("ClrThrshld")

	@ClrThrshld.deleter
	def ClrThrshld(self):
		del self._ClrThrshld
		self._ClrThrshld = None

	@property
	def DrctlyLkdActvty(self):
		return self._DrctlyLkdActvty

	@DrctlyLkdActvty.setter
	def DrctlyLkdActvty(self, value):
		self._DrctlyLkdActvty = value if type(value) != auto else self.make_default("DrctlyLkdActvty")

	@DrctlyLkdActvty.deleter
	def DrctlyLkdActvty(self):
		del self._DrctlyLkdActvty
		self._DrctlyLkdActvty = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FdrlInstn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrThrshld', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctlyLkdActvty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=GenericIdentification175, min=1, max=None, mutex_group=None, array=True),
	))

