# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Amount2Choice import Amount2Choice
from ._CashSubBalanceTypeAndQuantityBreakdown3 import CashSubBalanceTypeAndQuantityBreakdown3
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._GenericIdentification37 import GenericIdentification37
from ._Max350Text import Max350Text
from ._PriorityNumeric4Choice import PriorityNumeric4Choice

class IntraBalance5(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_BalTo", "_CshSubBalId", "_InstrPrcgAddtlDtls", "_Prty", "_SttlmAmt", "_SttlmDt"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if type(value) != base_types.auto else self.make_default("BalFr")

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = None

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if type(value) != base_types.auto else self.make_default("BalTo")

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = None

	@property
	def CshSubBalId(self):
		return self._CshSubBalId

	@CshSubBalId.setter
	def CshSubBalId(self, value):
		self._CshSubBalId = value if type(value) != base_types.auto else self.make_default("CshSubBalId")

	@CshSubBalId.deleter
	def CshSubBalId(self):
		del self._CshSubBalId
		self._CshSubBalId = None

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if type(value) != base_types.auto else self.make_default("InstrPrcgAddtlDtls")

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSubBalId', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
	))