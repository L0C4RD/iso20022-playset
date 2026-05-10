from . import base_types
from ._StatementBasis1Code import StatementBasis1Code
from ._GenericIdentification7 import GenericIdentification7

class StatementBasisCodeAndDSSCodeChoice(base_types._BaseFieldType):

	__slots__ = ["_StmtBsisAsDSS", "_StmtBsisAsCd"]
	@property
	def StmtBsisAsCd(self):
		return self._StmtBsisAsCd

	@StmtBsisAsCd.setter
	def StmtBsisAsCd(self, value):
		self._StmtBsisAsCd = value if type(value) != base_types.auto else self.make_default("StmtBsisAsCd")

	@StmtBsisAsCd.deleter
	def StmtBsisAsCd(self):
		del self._StmtBsisAsCd
		self._StmtBsisAsCd = None

	@property
	def StmtBsisAsDSS(self):
		return self._StmtBsisAsDSS

	@StmtBsisAsDSS.setter
	def StmtBsisAsDSS(self, value):
		self._StmtBsisAsDSS = value if type(value) != base_types.auto else self.make_default("StmtBsisAsDSS")

	@StmtBsisAsDSS.deleter
	def StmtBsisAsDSS(self):
		del self._StmtBsisAsDSS
		self._StmtBsisAsDSS = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtBsisAsCd', type=StatementBasis1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtBsisAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
	))

