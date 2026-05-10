import base_types
import Max35Text
import TransactionIdentifier1
import Min6Max8Text

class LoyaltyServerData1(base_types._BaseFieldType):

	__slots__ = ["_LltyTxId", "_LltySvrId", "_ApprvlCd", "_HstRcncltnId"]
	@property
	def LltyTxId(self):
		return self._LltyTxId

	@LltyTxId.setter
	def LltyTxId(self, value):
		self._LltyTxId = value if type(value) != auto else self.make_default("LltyTxId")

	@LltyTxId.deleter
	def LltyTxId(self):
		del self._LltyTxId
		self._LltyTxId = None

	@property
	def LltySvrId(self):
		return self._LltySvrId

	@LltySvrId.setter
	def LltySvrId(self, value):
		self._LltySvrId = value if type(value) != auto else self.make_default("LltySvrId")

	@LltySvrId.deleter
	def LltySvrId(self):
		del self._LltySvrId
		self._LltySvrId = None

	@property
	def ApprvlCd(self):
		return self._ApprvlCd

	@ApprvlCd.setter
	def ApprvlCd(self, value):
		self._ApprvlCd = value if type(value) != auto else self.make_default("ApprvlCd")

	@ApprvlCd.deleter
	def ApprvlCd(self):
		del self._ApprvlCd
		self._ApprvlCd = None

	@property
	def HstRcncltnId(self):
		return self._HstRcncltnId

	@HstRcncltnId.setter
	def HstRcncltnId(self, value):
		self._HstRcncltnId = value if type(value) != auto else self.make_default("HstRcncltnId")

	@HstRcncltnId.deleter
	def HstRcncltnId(self):
		del self._HstRcncltnId
		self._HstRcncltnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltySvrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApprvlCd', type=Min6Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

