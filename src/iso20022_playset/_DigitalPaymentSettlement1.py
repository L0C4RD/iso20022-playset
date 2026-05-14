# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashSettlementSystemPlace1Choice import CashSettlementSystemPlace1Choice
from ._Quantity83Choice import Quantity83Choice
from ._SecurityIdentification19 import SecurityIdentification19

class DigitalPaymentSettlement1(base_types._BaseFieldType):

	__slots__ = ["_CshSttlmSysPlc", "_FinInstrmId", "_Qty"]
	@property
	def CshSttlmSysPlc(self):
		return self._CshSttlmSysPlc

	@CshSttlmSysPlc.setter
	def CshSttlmSysPlc(self, value):
		self._CshSttlmSysPlc = value if type(value) != base_types.auto else self.make_default("CshSttlmSysPlc")

	@CshSttlmSysPlc.deleter
	def CshSttlmSysPlc(self):
		del self._CshSttlmSysPlc
		self._CshSttlmSysPlc = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshSttlmSysPlc', type=CashSettlementSystemPlace1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity83Choice, min=1, max=1, mutex_group=None, array=False),
	))