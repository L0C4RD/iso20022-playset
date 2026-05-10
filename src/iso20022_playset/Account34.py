from . import base_types
from .PostalAddress1 import PostalAddress1
from .PartyIdentification132 import PartyIdentification132
from .Max35Text import Max35Text

class Account34(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_RegnAdr", "_AcctNm", "_AcctDsgnt", "_AcctSvcr"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def RegnAdr(self):
		return self._RegnAdr

	@RegnAdr.setter
	def RegnAdr(self, value):
		self._RegnAdr = value if type(value) != base_types.auto else self.make_default("RegnAdr")

	@RegnAdr.deleter
	def RegnAdr(self):
		del self._RegnAdr
		self._RegnAdr = None

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if type(value) != base_types.auto else self.make_default("AcctNm")

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = None

	@property
	def AcctDsgnt(self):
		return self._AcctDsgnt

	@AcctDsgnt.setter
	def AcctDsgnt(self, value):
		self._AcctDsgnt = value if type(value) != base_types.auto else self.make_default("AcctDsgnt")

	@AcctDsgnt.deleter
	def AcctDsgnt(self):
		del self._AcctDsgnt
		self._AcctDsgnt = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification132, min=1, max=1, mutex_group=None, array=False),
	))

