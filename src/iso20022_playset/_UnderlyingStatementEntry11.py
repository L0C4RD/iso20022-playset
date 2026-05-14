# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._CashAccount40 import CashAccount40
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._Max35Text import Max35Text
from ._OriginalGroupInformation33 import OriginalGroupInformation33
from ._UUIDv4Identifier import UUIDv4Identifier

class UnderlyingStatementEntry11(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAcct", "_OrgnlGrpInf", "_OrgnlNtryAmt", "_OrgnlNtryRef", "_OrgnlNtryValDt", "_OrgnlStmtId", "_OrgnlUETR"]
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
		base_types.FieldEntry(name='OrgnlAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation33, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlNtryValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlStmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
	))