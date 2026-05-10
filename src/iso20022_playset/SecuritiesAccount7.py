import base_types
import Max35Text
import PartyIdentification2Choice

class SecuritiesAccount7(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnrId"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def AcctOwnrId(self):
		return self._AcctOwnrId

	@AcctOwnrId.setter
	def AcctOwnrId(self, value):
		self._AcctOwnrId = value if type(value) != auto else self.make_default("AcctOwnrId")

	@AcctOwnrId.deleter
	def AcctOwnrId(self):
		del self._AcctOwnrId
		self._AcctOwnrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

