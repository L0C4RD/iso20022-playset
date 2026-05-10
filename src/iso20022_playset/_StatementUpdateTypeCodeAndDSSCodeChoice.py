from . import base_types
from .GenericIdentification7 import GenericIdentification7
from .StatementUpdateTypeCode import StatementUpdateTypeCode

class StatementUpdateTypeCodeAndDSSCodeChoice(base_types._BaseFieldType):

	__slots__ = ["_StmtUpdTpAsDSS", "_StmtUpdTpAsCd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtUpdTpAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtUpdTpAsCd', type=StatementUpdateTypeCode, min=0, max=1, mutex_group=1, array=False),
	))

