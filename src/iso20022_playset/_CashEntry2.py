# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DateAndDateTime2Choice
from . import EntryStatus1Code
from . import Max140Text
from . import Max35Text
from . import Number

class CashEntry2(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcrRef", "_AddtlNtryInf", "_Amt", "_Dt", "_Id", "_StmtId", "_Sts"]
	@property
	def AcctSvcrRef(self):
		return self._AcctSvcrRef

	@AcctSvcrRef.setter
	def AcctSvcrRef(self, value):
		self._AcctSvcrRef = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrRef', Number, False)

	@AcctSvcrRef.deleter
	def AcctSvcrRef(self):
		del self._AcctSvcrRef
		self._AcctSvcrRef = base_types.UninitialisedField(self, 'AcctSvcrRef', Number, False)

	@property
	def AddtlNtryInf(self):
		return self._AddtlNtryInf

	@AddtlNtryInf.setter
	def AddtlNtryInf(self, value):
		self._AddtlNtryInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlNtryInf', Max140Text, True)

	@AddtlNtryInf.deleter
	def AddtlNtryInf(self):
		del self._AddtlNtryInf
		self._AddtlNtryInf = base_types.UninitialisedField(self, 'AddtlNtryInf', Max140Text, True)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DateAndDateTime2Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if value is not None else base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', EntryStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', EntryStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcrRef', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlNtryInf', type=Max140Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=EntryStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))