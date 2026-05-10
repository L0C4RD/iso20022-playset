from . import base_types
from ._QuantityBreakdown62 import QuantityBreakdown62
from ._Max210Text import Max210Text
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from ._SafeKeepingPlace5 import SafeKeepingPlace5
from ._CashAccountIdentification9Choice import CashAccountIdentification9Choice

class QuantityAndAccount114(base_types._BaseFieldType):

	__slots__ = ["_DnmtnChc", "_SttlmQty", "_SfkpgPlc", "_CshAcct", "_QtyBrkdwn"]
	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def DnmtnChc(self):
		return self._DnmtnChc

	@DnmtnChc.setter
	def DnmtnChc(self, value):
		self._DnmtnChc = value if type(value) != base_types.auto else self.make_default("DnmtnChc")

	@DnmtnChc.deleter
	def DnmtnChc(self):
		del self._DnmtnChc
		self._DnmtnChc = None

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != base_types.auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if type(value) != base_types.auto else self.make_default("SttlmQty")

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnChc', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown62, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
	))

