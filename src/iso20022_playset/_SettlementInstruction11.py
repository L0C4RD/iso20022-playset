# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification6
from . import CashAccount40
from . import ClearingSystemIdentification3Choice
from . import SettlementMethod1Code

class SettlementInstruction11(base_types._BaseFieldType):

	__slots__ = ["_ClrSys", "_InstdRmbrsmntAgt", "_InstdRmbrsmntAgtAcct", "_InstgRmbrsmntAgt", "_InstgRmbrsmntAgtAcct", "_SttlmAcct", "_SttlmMtd", "_ThrdRmbrsmntAgt", "_ThrdRmbrsmntAgtAcct"]
	@property
	def ClrSys(self):
		return self._ClrSys

	@ClrSys.setter
	def ClrSys(self, value):
		self._ClrSys = value if value is not None else base_types.UninitialisedField(self, 'ClrSys', ClearingSystemIdentification3Choice, False)

	@ClrSys.deleter
	def ClrSys(self):
		del self._ClrSys
		self._ClrSys = base_types.UninitialisedField(self, 'ClrSys', ClearingSystemIdentification3Choice, False)

	@property
	def InstdRmbrsmntAgt(self):
		return self._InstdRmbrsmntAgt

	@InstdRmbrsmntAgt.setter
	def InstdRmbrsmntAgt(self, value):
		self._InstdRmbrsmntAgt = value if value is not None else base_types.UninitialisedField(self, 'InstdRmbrsmntAgt', BranchAndFinancialInstitutionIdentification6, False)

	@InstdRmbrsmntAgt.deleter
	def InstdRmbrsmntAgt(self):
		del self._InstdRmbrsmntAgt
		self._InstdRmbrsmntAgt = base_types.UninitialisedField(self, 'InstdRmbrsmntAgt', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def InstdRmbrsmntAgtAcct(self):
		return self._InstdRmbrsmntAgtAcct

	@InstdRmbrsmntAgtAcct.setter
	def InstdRmbrsmntAgtAcct(self, value):
		self._InstdRmbrsmntAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'InstdRmbrsmntAgtAcct', CashAccount40, False)

	@InstdRmbrsmntAgtAcct.deleter
	def InstdRmbrsmntAgtAcct(self):
		del self._InstdRmbrsmntAgtAcct
		self._InstdRmbrsmntAgtAcct = base_types.UninitialisedField(self, 'InstdRmbrsmntAgtAcct', CashAccount40, False)

	@property
	def InstgRmbrsmntAgt(self):
		return self._InstgRmbrsmntAgt

	@InstgRmbrsmntAgt.setter
	def InstgRmbrsmntAgt(self, value):
		self._InstgRmbrsmntAgt = value if value is not None else base_types.UninitialisedField(self, 'InstgRmbrsmntAgt', BranchAndFinancialInstitutionIdentification6, False)

	@InstgRmbrsmntAgt.deleter
	def InstgRmbrsmntAgt(self):
		del self._InstgRmbrsmntAgt
		self._InstgRmbrsmntAgt = base_types.UninitialisedField(self, 'InstgRmbrsmntAgt', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def InstgRmbrsmntAgtAcct(self):
		return self._InstgRmbrsmntAgtAcct

	@InstgRmbrsmntAgtAcct.setter
	def InstgRmbrsmntAgtAcct(self, value):
		self._InstgRmbrsmntAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'InstgRmbrsmntAgtAcct', CashAccount40, False)

	@InstgRmbrsmntAgtAcct.deleter
	def InstgRmbrsmntAgtAcct(self):
		del self._InstgRmbrsmntAgtAcct
		self._InstgRmbrsmntAgtAcct = base_types.UninitialisedField(self, 'InstgRmbrsmntAgtAcct', CashAccount40, False)

	@property
	def SttlmAcct(self):
		return self._SttlmAcct

	@SttlmAcct.setter
	def SttlmAcct(self, value):
		self._SttlmAcct = value if value is not None else base_types.UninitialisedField(self, 'SttlmAcct', CashAccount40, False)

	@SttlmAcct.deleter
	def SttlmAcct(self):
		del self._SttlmAcct
		self._SttlmAcct = base_types.UninitialisedField(self, 'SttlmAcct', CashAccount40, False)

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if value is not None else base_types.UninitialisedField(self, 'SttlmMtd', SettlementMethod1Code, False)

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = base_types.UninitialisedField(self, 'SttlmMtd', SettlementMethod1Code, False)

	@property
	def ThrdRmbrsmntAgt(self):
		return self._ThrdRmbrsmntAgt

	@ThrdRmbrsmntAgt.setter
	def ThrdRmbrsmntAgt(self, value):
		self._ThrdRmbrsmntAgt = value if value is not None else base_types.UninitialisedField(self, 'ThrdRmbrsmntAgt', BranchAndFinancialInstitutionIdentification6, False)

	@ThrdRmbrsmntAgt.deleter
	def ThrdRmbrsmntAgt(self):
		del self._ThrdRmbrsmntAgt
		self._ThrdRmbrsmntAgt = base_types.UninitialisedField(self, 'ThrdRmbrsmntAgt', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def ThrdRmbrsmntAgtAcct(self):
		return self._ThrdRmbrsmntAgtAcct

	@ThrdRmbrsmntAgtAcct.setter
	def ThrdRmbrsmntAgtAcct(self, value):
		self._ThrdRmbrsmntAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'ThrdRmbrsmntAgtAcct', CashAccount40, False)

	@ThrdRmbrsmntAgtAcct.deleter
	def ThrdRmbrsmntAgtAcct(self):
		del self._ThrdRmbrsmntAgtAcct
		self._ThrdRmbrsmntAgtAcct = base_types.UninitialisedField(self, 'ThrdRmbrsmntAgtAcct', CashAccount40, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSys', type=ClearingSystemIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=SettlementMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrdRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))