from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max140Text import Max140Text
from ._Number import Number
from ._EntryStatus1Code import EntryStatus1Code
from ._Max35Text import Max35Text
from ._DateAndDateTime2Choice import DateAndDateTime2Choice

class CashEntry2(base_types._BaseFieldType):

	__slots__ = ["_StmtId", "_Sts", "_Dt", "_Amt", "_Id", "_AddtlNtryInf", "_AcctSvcrRef"]
	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if type(value) != base_types.auto else self.make_default("StmtId")

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

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

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def AddtlNtryInf(self):
		return self._AddtlNtryInf

	@AddtlNtryInf.setter
	def AddtlNtryInf(self, value):
		self._AddtlNtryInf = value if type(value) != base_types.auto else self.make_default("AddtlNtryInf")

	@AddtlNtryInf.deleter
	def AddtlNtryInf(self):
		del self._AddtlNtryInf
		self._AddtlNtryInf = None

	@property
	def AcctSvcrRef(self):
		return self._AcctSvcrRef

	@AcctSvcrRef.setter
	def AcctSvcrRef(self, value):
		self._AcctSvcrRef = value if type(value) != base_types.auto else self.make_default("AcctSvcrRef")

	@AcctSvcrRef.deleter
	def AcctSvcrRef(self):
		del self._AcctSvcrRef
		self._AcctSvcrRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=EntryStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlNtryInf', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcrRef', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

