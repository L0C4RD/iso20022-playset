from . import base_types
from .CashAccount40 import CashAccount40
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .UUIDv4Identifier import UUIDv4Identifier
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .OriginalGroupInformation29 import OriginalGroupInformation29
from .Max35Text import Max35Text

class UnderlyingStatementEntry5(base_types._BaseFieldType):

	__slots__ = ["_OrgnlGrpInf", "_OrgnlNtryRef", "_OrgnlAcct", "_OrgnlNtryAmt", "_OrgnlStmtId", "_OrgnlNtryValDt", "_OrgnlUETR"]
	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != base_types.auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def OrgnlNtryRef(self):
		return self._OrgnlNtryRef

	@OrgnlNtryRef.setter
	def OrgnlNtryRef(self, value):
		self._OrgnlNtryRef = value if type(value) != base_types.auto else self.make_default("OrgnlNtryRef")

	@OrgnlNtryRef.deleter
	def OrgnlNtryRef(self):
		del self._OrgnlNtryRef
		self._OrgnlNtryRef = None

	@property
	def OrgnlAcct(self):
		return self._OrgnlAcct

	@OrgnlAcct.setter
	def OrgnlAcct(self, value):
		self._OrgnlAcct = value if type(value) != base_types.auto else self.make_default("OrgnlAcct")

	@OrgnlAcct.deleter
	def OrgnlAcct(self):
		del self._OrgnlAcct
		self._OrgnlAcct = None

	@property
	def OrgnlNtryAmt(self):
		return self._OrgnlNtryAmt

	@OrgnlNtryAmt.setter
	def OrgnlNtryAmt(self, value):
		self._OrgnlNtryAmt = value if type(value) != base_types.auto else self.make_default("OrgnlNtryAmt")

	@OrgnlNtryAmt.deleter
	def OrgnlNtryAmt(self):
		del self._OrgnlNtryAmt
		self._OrgnlNtryAmt = None

	@property
	def OrgnlStmtId(self):
		return self._OrgnlStmtId

	@OrgnlStmtId.setter
	def OrgnlStmtId(self, value):
		self._OrgnlStmtId = value if type(value) != base_types.auto else self.make_default("OrgnlStmtId")

	@OrgnlStmtId.deleter
	def OrgnlStmtId(self):
		del self._OrgnlStmtId
		self._OrgnlStmtId = None

	@property
	def OrgnlNtryValDt(self):
		return self._OrgnlNtryValDt

	@OrgnlNtryValDt.setter
	def OrgnlNtryValDt(self, value):
		self._OrgnlNtryValDt = value if type(value) != base_types.auto else self.make_default("OrgnlNtryValDt")

	@OrgnlNtryValDt.deleter
	def OrgnlNtryValDt(self):
		del self._OrgnlNtryValDt
		self._OrgnlNtryValDt = None

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != base_types.auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlStmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))

