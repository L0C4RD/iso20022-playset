from . import base_types
from ._IncentivePremiumType2Choice import IncentivePremiumType2Choice
from ._Max350Text import Max350Text
from ._PriceRateOrAmount8Choice import PriceRateOrAmount8Choice
from ._DateFormat3Choice import DateFormat3Choice

class IncentivePremium6(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Desc", "_PmtDt", "_Amt"]
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
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def PmtDt(self):
		return self._PmtDt

	@PmtDt.setter
	def PmtDt(self, value):
		self._PmtDt = value if type(value) != base_types.auto else self.make_default("PmtDt")

	@PmtDt.deleter
	def PmtDt(self):
		del self._PmtDt
		self._PmtDt = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=IncentivePremiumType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDt', type=DateFormat3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=PriceRateOrAmount8Choice, min=1, max=1, mutex_group=None, array=False),
	))

