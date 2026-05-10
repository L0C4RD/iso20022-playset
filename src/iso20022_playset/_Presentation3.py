from . import base_types
from ._Max256Text import Max256Text
from ._Channel1Choice import Channel1Choice
from ._DocumentFormat1Choice import DocumentFormat1Choice

class Presentation3(base_types._BaseFieldType):

	__slots__ = ["_Frmt", "_Chanl", "_Adr"]
	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if type(value) != base_types.auto else self.make_default("Frmt")

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = None

	@property
	def Chanl(self):
		return self._Chanl

	@Chanl.setter
	def Chanl(self, value):
		self._Chanl = value if type(value) != base_types.auto else self.make_default("Chanl")

	@Chanl.deleter
	def Chanl(self):
		del self._Chanl
		self._Chanl = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frmt', type=DocumentFormat1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chanl', type=Channel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

