from . import base_types
from .Max35Text import Max35Text
from .AnyBICDec2014Identifier import AnyBICDec2014Identifier
from .AccountIdentificationAndName7 import AccountIdentificationAndName7

class CashAccount206(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctTpDesc", "_Svcr"]
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
	def AcctTpDesc(self):
		return self._AcctTpDesc

	@AcctTpDesc.setter
	def AcctTpDesc(self, value):
		self._AcctTpDesc = value if type(value) != auto else self.make_default("AcctTpDesc")

	@AcctTpDesc.deleter
	def AcctTpDesc(self):
		del self._AcctTpDesc
		self._AcctTpDesc = None

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if type(value) != auto else self.make_default("Svcr")

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentificationAndName7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTpDesc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
	))

