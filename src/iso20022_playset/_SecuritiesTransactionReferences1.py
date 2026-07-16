# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class SecuritiesTransactionReferences1(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrTxId", "_AcctSvcrTxId", "_MktInfrstrctrTxId", "_PrcgId"]
	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrTxId', Max35Text, False)

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = base_types.UninitialisedField(self, 'AcctOwnrTxId', Max35Text, False)

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = base_types.UninitialisedField(self, 'AcctSvcrTxId', Max35Text, False)

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', Max35Text, False)

	@property
	def PrcgId(self):
		return self._PrcgId

	@PrcgId.setter
	def PrcgId(self, value):
		self._PrcgId = value if value is not None else base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	@PrcgId.deleter
	def PrcgId(self):
		del self._PrcgId
		self._PrcgId = base_types.UninitialisedField(self, 'PrcgId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))