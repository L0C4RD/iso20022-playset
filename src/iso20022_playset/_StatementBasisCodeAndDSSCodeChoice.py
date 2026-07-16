# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification7
from . import StatementBasis1Code

class StatementBasisCodeAndDSSCodeChoice(base_types._BaseFieldType):

	__slots__ = ["_StmtBsisAsCd", "_StmtBsisAsDSS"]
	@property
	def StmtBsisAsCd(self):
		return self._StmtBsisAsCd

	@StmtBsisAsCd.setter
	def StmtBsisAsCd(self, value):
		self._StmtBsisAsCd = value if value is not None else base_types.UninitialisedField(self, 'StmtBsisAsCd', StatementBasis1Code, False)

	@StmtBsisAsCd.deleter
	def StmtBsisAsCd(self):
		del self._StmtBsisAsCd
		self._StmtBsisAsCd = base_types.UninitialisedField(self, 'StmtBsisAsCd', StatementBasis1Code, False)

	@property
	def StmtBsisAsDSS(self):
		return self._StmtBsisAsDSS

	@StmtBsisAsDSS.setter
	def StmtBsisAsDSS(self, value):
		self._StmtBsisAsDSS = value if value is not None else base_types.UninitialisedField(self, 'StmtBsisAsDSS', GenericIdentification7, False)

	@StmtBsisAsDSS.deleter
	def StmtBsisAsDSS(self):
		del self._StmtBsisAsDSS
		self._StmtBsisAsDSS = base_types.UninitialisedField(self, 'StmtBsisAsDSS', GenericIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StmtBsisAsCd', type=StatementBasis1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtBsisAsDSS', type=GenericIdentification7, min=0, max=1, mutex_group=1, array=False),
	))