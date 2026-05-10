from . import base_types
from .Max35Text import Max35Text

class DocumentIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrDocId", "_AcctSvcrDocId"]
	@property
	def AcctOwnrDocId(self):
		return self._AcctOwnrDocId

	@AcctOwnrDocId.setter
	def AcctOwnrDocId(self, value):
		self._AcctOwnrDocId = value if type(value) != base_types.auto else self.make_default("AcctOwnrDocId")

	@AcctOwnrDocId.deleter
	def AcctOwnrDocId(self):
		del self._AcctOwnrDocId
		self._AcctOwnrDocId = None

	@property
	def AcctSvcrDocId(self):
		return self._AcctSvcrDocId

	@AcctSvcrDocId.setter
	def AcctSvcrDocId(self, value):
		self._AcctSvcrDocId = value if type(value) != base_types.auto else self.make_default("AcctSvcrDocId")

	@AcctSvcrDocId.deleter
	def AcctSvcrDocId(self):
		del self._AcctSvcrDocId
		self._AcctSvcrDocId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrDocId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AcctSvcrDocId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

