from . import base_types
from ._Max35Text import Max35Text
from ._PartyIdentification125Choice import PartyIdentification125Choice
from ._OwnerIdentification3Choice import OwnerIdentification3Choice

class InvestmentAccount77(base_types._BaseFieldType):

	__slots__ = ["_OwnrId", "_AcctId", "_AcctSvcr", "_AcctNm", "_AcctDsgnt"]
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
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if type(value) != base_types.auto else self.make_default("OwnrId")

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification125Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrId', type=OwnerIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
	))

