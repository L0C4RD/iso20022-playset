from . import base_types
from .ReturnExcessCash1Choice import ReturnExcessCash1Choice
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class ReturnExcessCash1(base_types._BaseFieldType):

	__slots__ = ["_CshCollCcy", "_RtrXcssCshTp"]
	@property
	def CshCollCcy(self):
		return self._CshCollCcy

	@CshCollCcy.setter
	def CshCollCcy(self, value):
		self._CshCollCcy = value if type(value) != base_types.auto else self.make_default("CshCollCcy")

	@CshCollCcy.deleter
	def CshCollCcy(self):
		del self._CshCollCcy
		self._CshCollCcy = None

	@property
	def RtrXcssCshTp(self):
		return self._RtrXcssCshTp

	@RtrXcssCshTp.setter
	def RtrXcssCshTp(self, value):
		self._RtrXcssCshTp = value if type(value) != base_types.auto else self.make_default("RtrXcssCshTp")

	@RtrXcssCshTp.deleter
	def RtrXcssCshTp(self):
		del self._RtrXcssCshTp
		self._RtrXcssCshTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCollCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrXcssCshTp', type=ReturnExcessCash1Choice, min=1, max=1, mutex_group=None, array=False),
	))

