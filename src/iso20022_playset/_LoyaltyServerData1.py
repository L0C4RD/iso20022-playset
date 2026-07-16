# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Min6Max8Text
from . import TransactionIdentifier1

class LoyaltyServerData1(base_types._BaseFieldType):

	__slots__ = ["_ApprvlCd", "_HstRcncltnId", "_LltySvrId", "_LltyTxId"]
	@property
	def ApprvlCd(self):
		return self._ApprvlCd

	@ApprvlCd.setter
	def ApprvlCd(self, value):
		self._ApprvlCd = value if value is not None else base_types.UninitialisedField(self, 'ApprvlCd', Min6Max8Text, False)

	@ApprvlCd.deleter
	def ApprvlCd(self):
		del self._ApprvlCd
		self._ApprvlCd = base_types.UninitialisedField(self, 'ApprvlCd', Min6Max8Text, False)

	@property
	def HstRcncltnId(self):
		return self._HstRcncltnId

	@HstRcncltnId.setter
	def HstRcncltnId(self, value):
		self._HstRcncltnId = value if value is not None else base_types.UninitialisedField(self, 'HstRcncltnId', Max35Text, False)

	@HstRcncltnId.deleter
	def HstRcncltnId(self):
		del self._HstRcncltnId
		self._HstRcncltnId = base_types.UninitialisedField(self, 'HstRcncltnId', Max35Text, False)

	@property
	def LltySvrId(self):
		return self._LltySvrId

	@LltySvrId.setter
	def LltySvrId(self, value):
		self._LltySvrId = value if value is not None else base_types.UninitialisedField(self, 'LltySvrId', Max35Text, False)

	@LltySvrId.deleter
	def LltySvrId(self):
		del self._LltySvrId
		self._LltySvrId = base_types.UninitialisedField(self, 'LltySvrId', Max35Text, False)

	@property
	def LltyTxId(self):
		return self._LltyTxId

	@LltyTxId.setter
	def LltyTxId(self, value):
		self._LltyTxId = value if value is not None else base_types.UninitialisedField(self, 'LltyTxId', TransactionIdentifier1, False)

	@LltyTxId.deleter
	def LltyTxId(self):
		del self._LltyTxId
		self._LltyTxId = base_types.UninitialisedField(self, 'LltyTxId', TransactionIdentifier1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvlCd', type=Min6Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstRcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltySvrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
	))