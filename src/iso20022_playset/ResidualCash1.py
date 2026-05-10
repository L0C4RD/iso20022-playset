from . import base_types
from .ActiveCurrencyCode import ActiveCurrencyCode
from .YesNoIndicator import YesNoIndicator

class ResidualCash1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_RsdlCshInd"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def RsdlCshInd(self):
		return self._RsdlCshInd

	@RsdlCshInd.setter
	def RsdlCshInd(self, value):
		self._RsdlCshInd = value if type(value) != auto else self.make_default("RsdlCshInd")

	@RsdlCshInd.deleter
	def RsdlCshInd(self):
		del self._RsdlCshInd
		self._RsdlCshInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsdlCshInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

