# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40

class SettlementInstruction16(base_types._BaseFieldType):

	__slots__ = ["_InstdRmbrsmntAgt", "_InstdRmbrsmntAgtAcct", "_InstgRmbrsmntAgt", "_InstgRmbrsmntAgtAcct"]
	@property
	def InstdRmbrsmntAgt(self):
		return self._InstdRmbrsmntAgt

	@InstdRmbrsmntAgt.setter
	def InstdRmbrsmntAgt(self, value):
		self._InstdRmbrsmntAgt = value if type(value) != base_types.auto else self.make_default("InstdRmbrsmntAgt")

	@InstdRmbrsmntAgt.deleter
	def InstdRmbrsmntAgt(self):
		del self._InstdRmbrsmntAgt
		self._InstdRmbrsmntAgt = None

	@property
	def InstdRmbrsmntAgtAcct(self):
		return self._InstdRmbrsmntAgtAcct

	@InstdRmbrsmntAgtAcct.setter
	def InstdRmbrsmntAgtAcct(self, value):
		self._InstdRmbrsmntAgtAcct = value if type(value) != base_types.auto else self.make_default("InstdRmbrsmntAgtAcct")

	@InstdRmbrsmntAgtAcct.deleter
	def InstdRmbrsmntAgtAcct(self):
		del self._InstdRmbrsmntAgtAcct
		self._InstdRmbrsmntAgtAcct = None

	@property
	def InstgRmbrsmntAgt(self):
		return self._InstgRmbrsmntAgt

	@InstgRmbrsmntAgt.setter
	def InstgRmbrsmntAgt(self, value):
		self._InstgRmbrsmntAgt = value if type(value) != base_types.auto else self.make_default("InstgRmbrsmntAgt")

	@InstgRmbrsmntAgt.deleter
	def InstgRmbrsmntAgt(self):
		del self._InstgRmbrsmntAgt
		self._InstgRmbrsmntAgt = None

	@property
	def InstgRmbrsmntAgtAcct(self):
		return self._InstgRmbrsmntAgtAcct

	@InstgRmbrsmntAgtAcct.setter
	def InstgRmbrsmntAgtAcct(self, value):
		self._InstgRmbrsmntAgtAcct = value if type(value) != base_types.auto else self.make_default("InstgRmbrsmntAgtAcct")

	@InstgRmbrsmntAgtAcct.deleter
	def InstgRmbrsmntAgtAcct(self):
		del self._InstgRmbrsmntAgtAcct
		self._InstgRmbrsmntAgtAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstdRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgRmbrsmntAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))