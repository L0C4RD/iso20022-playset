from . import base_types
from .PartyIdentification242Choice import PartyIdentification242Choice
from .PartyIdentification60 import PartyIdentification60
from .Max35Text import Max35Text

class FundIdentification5(base_types._BaseFieldType):

	__slots__ = ["_FndId", "_CtdnId", "_AcctIdWthCtdn"]
	@property
	def FndId(self):
		return self._FndId

	@FndId.setter
	def FndId(self, value):
		self._FndId = value if type(value) != base_types.auto else self.make_default("FndId")

	@FndId.deleter
	def FndId(self):
		del self._FndId
		self._FndId = None

	@property
	def CtdnId(self):
		return self._CtdnId

	@CtdnId.setter
	def CtdnId(self, value):
		self._CtdnId = value if type(value) != base_types.auto else self.make_default("CtdnId")

	@CtdnId.deleter
	def CtdnId(self):
		del self._CtdnId
		self._CtdnId = None

	@property
	def AcctIdWthCtdn(self):
		return self._AcctIdWthCtdn

	@AcctIdWthCtdn.setter
	def AcctIdWthCtdn(self, value):
		self._AcctIdWthCtdn = value if type(value) != base_types.auto else self.make_default("AcctIdWthCtdn")

	@AcctIdWthCtdn.deleter
	def AcctIdWthCtdn(self):
		del self._AcctIdWthCtdn
		self._AcctIdWthCtdn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FndId', type=PartyIdentification60, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtdnId', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctIdWthCtdn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

