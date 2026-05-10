from . import base_types
from .DateTimePeriod1 import DateTimePeriod1
from .InterestType1Choice import InterestType1Choice
from .Rate4 import Rate4
from .TaxCharges2 import TaxCharges2
from .Max35Text import Max35Text

class AccountInterest4(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_Tp", "_FrToDt", "_Rsn", "_Tax"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if type(value) != base_types.auto else self.make_default("FrToDt")

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=Rate4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=InterestType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrToDt', type=DateTimePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxCharges2, min=0, max=1, mutex_group=None, array=False),
	))

