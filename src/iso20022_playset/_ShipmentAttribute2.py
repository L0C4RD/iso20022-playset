from . import base_types
from ._ISODate import ISODate
from ._ShipmentCondition1Choice import ShipmentCondition1Choice
from ._CountryCode import CountryCode

class ShipmentAttribute2(base_types._BaseFieldType):

	__slots__ = ["_Conds", "_XpctdDt", "_CtryOfCntrPty"]
	@property
	def Conds(self):
		return self._Conds

	@Conds.setter
	def Conds(self, value):
		self._Conds = value if type(value) != base_types.auto else self.make_default("Conds")

	@Conds.deleter
	def Conds(self):
		del self._Conds
		self._Conds = None

	@property
	def CtryOfCntrPty(self):
		return self._CtryOfCntrPty

	@CtryOfCntrPty.setter
	def CtryOfCntrPty(self, value):
		self._CtryOfCntrPty = value if type(value) != base_types.auto else self.make_default("CtryOfCntrPty")

	@CtryOfCntrPty.deleter
	def CtryOfCntrPty(self):
		del self._CtryOfCntrPty
		self._CtryOfCntrPty = None

	@property
	def XpctdDt(self):
		return self._XpctdDt

	@XpctdDt.setter
	def XpctdDt(self, value):
		self._XpctdDt = value if type(value) != base_types.auto else self.make_default("XpctdDt")

	@XpctdDt.deleter
	def XpctdDt(self):
		del self._XpctdDt
		self._XpctdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Conds', type=ShipmentCondition1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfCntrPty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

