from . import base_types
from .BICIdentification1 import BICIdentification1
from .ISODateTime import ISODateTime
from .Activity1 import Activity1

class ActivityDetails1(base_types._BaseFieldType):

	__slots__ = ["_Initr", "_DtTm", "_Actvty"]
	@property
	def Initr(self):
		return self._Initr

	@Initr.setter
	def Initr(self, value):
		self._Initr = value if type(value) != auto else self.make_default("Initr")

	@Initr.deleter
	def Initr(self):
		del self._Initr
		self._Initr = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def Actvty(self):
		return self._Actvty

	@Actvty.setter
	def Actvty(self, value):
		self._Actvty = value if type(value) != auto else self.make_default("Actvty")

	@Actvty.deleter
	def Actvty(self):
		del self._Actvty
		self._Actvty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Initr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actvty', type=Activity1, min=1, max=1, mutex_group=None, array=False),
	))

