from . import base_types
from .YesNoIndicator import YesNoIndicator
from .ISODate import ISODate

class MoneyPurchaseAnnualAllowance1(base_types._BaseFieldType):

	__slots__ = ["_TrggrdDt", "_Trggrd"]
	@property
	def TrggrdDt(self):
		return self._TrggrdDt

	@TrggrdDt.setter
	def TrggrdDt(self, value):
		self._TrggrdDt = value if type(value) != auto else self.make_default("TrggrdDt")

	@TrggrdDt.deleter
	def TrggrdDt(self):
		del self._TrggrdDt
		self._TrggrdDt = None

	@property
	def Trggrd(self):
		return self._Trggrd

	@Trggrd.setter
	def Trggrd(self, value):
		self._Trggrd = value if type(value) != auto else self.make_default("Trggrd")

	@Trggrd.deleter
	def Trggrd(self):
		del self._Trggrd
		self._Trggrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrggrdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trggrd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

