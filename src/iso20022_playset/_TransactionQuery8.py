# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import QueryType2Code
from . import TransactionCriteria8Choice

class TransactionQuery8(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_TxCrit"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if value is not None else base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = base_types.UninitialisedField(self, 'QryTp', QueryType2Code, False)

	@property
	def TxCrit(self):
		return self._TxCrit

	@TxCrit.setter
	def TxCrit(self, value):
		self._TxCrit = value if value is not None else base_types.UninitialisedField(self, 'TxCrit', TransactionCriteria8Choice, False)

	@TxCrit.deleter
	def TxCrit(self):
		del self._TxCrit
		self._TxCrit = base_types.UninitialisedField(self, 'TxCrit', TransactionCriteria8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCrit', type=TransactionCriteria8Choice, min=0, max=1, mutex_group=None, array=False),
	))