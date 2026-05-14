# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashAccountIdentification6Choice import CashAccountIdentification6Choice
from ._FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from ._QuantityBreakdown69 import QuantityBreakdown69
from ._RestrictedFINXMax210Text import RestrictedFINXMax210Text
from ._SafeKeepingPlace4 import SafeKeepingPlace4

class QuantityAndAccount107(base_types._BaseFieldType):

	__slots__ = ["_CshAcct", "_DnmtnChc", "_QtyBrkdwn", "_SfkpgPlc", "_SttlmQty"]
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
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnChc', type=RestrictedFINXMax210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown69, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=FinancialInstrumentQuantity36Choice, min=1, max=1, mutex_group=None, array=False),
	))