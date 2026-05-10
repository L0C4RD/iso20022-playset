from . import base_types
from .BondType1Code import BondType1Code
from .ISODate import ISODate

class DebtInstrument5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_IssncDt"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def IssncDt(self):
		return self._IssncDt

	@IssncDt.setter
	def IssncDt(self, value):
		self._IssncDt = value if type(value) != auto else self.make_default("IssncDt")

	@IssncDt.deleter
	def IssncDt(self):
		del self._IssncDt
		self._IssncDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=BondType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

