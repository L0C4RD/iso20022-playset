from . import base_types
from ._Max35Text import Max35Text
from ._PartialSettlement2Code import PartialSettlement2Code

class AdditionalParameters16(base_types._BaseFieldType):

	__slots__ = ["_PoolId", "_AcctSvcrTxId", "_AcctOwnrTxId", "_MktInfrstrctrTxId", "_PrvsPrtlConfId", "_CorpActnEvtId", "_PrcrTxId", "_PrtlSttlm"]
	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if type(value) != base_types.auto else self.make_default("PoolId")

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = None

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if type(value) != base_types.auto else self.make_default("AcctSvcrTxId")

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = None

	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if type(value) != base_types.auto else self.make_default("AcctOwnrTxId")

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = None

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if type(value) != base_types.auto else self.make_default("MktInfrstrctrTxId")

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = None

	@property
	def PrvsPrtlConfId(self):
		return self._PrvsPrtlConfId

	@PrvsPrtlConfId.setter
	def PrvsPrtlConfId(self, value):
		self._PrvsPrtlConfId = value if type(value) != base_types.auto else self.make_default("PrvsPrtlConfId")

	@PrvsPrtlConfId.deleter
	def PrvsPrtlConfId(self):
		del self._PrvsPrtlConfId
		self._PrvsPrtlConfId = None

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != base_types.auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if type(value) != base_types.auto else self.make_default("PrcrTxId")

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = None

	@property
	def PrtlSttlm(self):
		return self._PrtlSttlm

	@PrtlSttlm.setter
	def PrtlSttlm(self, value):
		self._PrtlSttlm = value if type(value) != base_types.auto else self.make_default("PrtlSttlm")

	@PrtlSttlm.deleter
	def PrtlSttlm(self):
		del self._PrtlSttlm
		self._PrtlSttlm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsPrtlConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlm', type=PartialSettlement2Code, min=0, max=1, mutex_group=None, array=False),
	))

