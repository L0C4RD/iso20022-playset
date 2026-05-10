from . import base_types
from .Max1000Text import Max1000Text
from .ISODate import ISODate
from .TradeQueryExecutionFrequency3 import TradeQueryExecutionFrequency3

class TradeRecurrentQuery7(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_QryTp", "_VldUntil"]
	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	@property
	def VldUntil(self):
		return self._VldUntil

	@VldUntil.setter
	def VldUntil(self, value):
		self._VldUntil = value if type(value) != auto else self.make_default("VldUntil")

	@VldUntil.deleter
	def VldUntil(self):
		del self._VldUntil
		self._VldUntil = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frqcy', type=TradeQueryExecutionFrequency3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QryTp', type=Max1000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldUntil', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

