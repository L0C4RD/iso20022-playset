# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification7
from . import StatementUpdateTypeCode

class StatementUpdateTypeCodeAndDSSCodeChoice(base_types._BaseFieldType):

	__slots__ = ["_StmtUpdTpAsCd", "_StmtUpdTpAsDSS"]
	@property
	def StmtUpdTpAsCd(self):
		return self._StmtUpdTpAsCd

	@StmtUpdTpAsCd.setter
	def StmtUpdTpAsCd(self, value):
		self._StmtUpdTpAsCd = value if value is not None else base_types.UninitialisedField(self, 'StmtUpdTpAsCd', StatementUpdateTypeCode, False)

	@StmtUpdTpAsCd.deleter
	def StmtUpdTpAsCd(self):
		del self._StmtUpdTpAsCd
		self._StmtUpdTpAsCd = base_types.UninitialisedField(self, 'StmtUpdTpAsCd', StatementUpdateTypeCode, False)

	@property
	def StmtUpdTpAsDSS(self):
		return self._StmtUpdTpAsDSS

	@StmtUpdTpAsDSS.setter
	def StmtUpdTpAsDSS(self, value):
		self._StmtUpdTpAsDSS = value if value is not None else base_types.UninitialisedField(self, 'StmtUpdTpAsDSS', GenericIdentification7, False)

	@StmtUpdTpAsDSS.deleter
	def StmtUpdTpAsDSS(self):
		del self._StmtUpdTpAsDSS
		self._StmtUpdTpAsDSS = base_types.UninitialisedField(self, 'StmtUpdTpAsDSS', GenericIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtUpdTpAsCd', type=StatementUpdateTypeCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtUpdTpAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
	))