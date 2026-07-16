# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40

class SettlementInstruction16(base_types._BaseFieldType):

	__slots__ = ["_InstdRmbrsmntAgt", "_InstdRmbrsmntAgtAcct", "_InstgRmbrsmntAgt", "_InstgRmbrsmntAgtAcct"]
	@property
	def InstdRmbrsmntAgt(self):
		return self._InstdRmbrsmntAgt

	@InstdRmbrsmntAgt.setter
	def InstdRmbrsmntAgt(self, value):
		self._InstdRmbrsmntAgt = value if value is not None else base_types.UninitialisedField(self, 'InstdRmbrsmntAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstdRmbrsmntAgt.deleter
	def InstdRmbrsmntAgt(self):
		del self._InstdRmbrsmntAgt
		self._InstdRmbrsmntAgt = base_types.UninitialisedField(self, 'InstdRmbrsmntAgt', BranchAndFinancialInstitutionIdentification8, False)

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
		self._InstgRmbrsmntAgt = value if value is not None else base_types.UninitialisedField(self, 'InstgRmbrsmntAgt', BranchAndFinancialInstitutionIdentification8, False)

	@InstgRmbrsmntAgt.deleter
	def InstgRmbrsmntAgt(self):
		del self._InstgRmbrsmntAgt
		self._InstgRmbrsmntAgt = base_types.UninitialisedField(self, 'InstgRmbrsmntAgt', BranchAndFinancialInstitutionIdentification8, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))