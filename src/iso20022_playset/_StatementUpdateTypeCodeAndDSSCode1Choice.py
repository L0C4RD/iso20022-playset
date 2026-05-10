from . import base_types
from ._StatementUpdateType1Code import StatementUpdateType1Code
from ._GenericIdentification7 import GenericIdentification7

class StatementUpdateTypeCodeAndDSSCode1Choice(base_types._BaseFieldType):

	__slots__ = ["_StmtUpdTpAsCd", "_StmtUpdTpAsDSS"]
	@property
	def StmtUpdTpAsCd(self):
		return self._StmtUpdTpAsCd

	@StmtUpdTpAsCd.setter
	def StmtUpdTpAsCd(self, value):
		self._StmtUpdTpAsCd = value if type(value) != base_types.auto else self.make_default("StmtUpdTpAsCd")

	@StmtUpdTpAsCd.deleter
	def StmtUpdTpAsCd(self):
		del self._StmtUpdTpAsCd
		self._StmtUpdTpAsCd = None

	@property
	def StmtUpdTpAsDSS(self):
		return self._StmtUpdTpAsDSS

	@StmtUpdTpAsDSS.setter
	def StmtUpdTpAsDSS(self, value):
		self._StmtUpdTpAsDSS = value if type(value) != base_types.auto else self.make_default("StmtUpdTpAsDSS")

	@StmtUpdTpAsDSS.deleter
	def StmtUpdTpAsDSS(self):
		del self._StmtUpdTpAsDSS
		self._StmtUpdTpAsDSS = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtUpdTpAsCd', type=StatementUpdateType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtUpdTpAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
	))

