from . import base_types
import GenericIdentification7
import StatementBasis1Code

class StatementBasisCodeAndDSSCodeChoice(base_types._BaseFieldType):

	__slots__ = ["_StmtBsisAsCd", "_StmtBsisAsDSS"]
	@property
	def StmtBsisAsCd(self):
		return self._StmtBsisAsCd

	@StmtBsisAsCd.setter
	def StmtBsisAsCd(self, value):
		self._StmtBsisAsCd = value if type(value) != auto else self.make_default("StmtBsisAsCd")

	@StmtBsisAsCd.deleter
	def StmtBsisAsCd(self):
		del self._StmtBsisAsCd
		self._StmtBsisAsCd = None

	@property
	def StmtBsisAsDSS(self):
		return self._StmtBsisAsDSS

	@StmtBsisAsDSS.setter
	def StmtBsisAsDSS(self, value):
		self._StmtBsisAsDSS = value if type(value) != auto else self.make_default("StmtBsisAsDSS")

	@StmtBsisAsDSS.deleter
	def StmtBsisAsDSS(self):
		del self._StmtBsisAsDSS
		self._StmtBsisAsDSS = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtBsisAsCd', type=StatementBasis1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtBsisAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
	))

