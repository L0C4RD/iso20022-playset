# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import References44Choice

class TransactionIdentifications52(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrTxId", "_AcctSvcrTxId", "_CtrPtyMktInfrstrctrTxId", "_MktInfrstrctrTxId", "_NonceId", "_PrcrTxId"]
	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrTxId', References44Choice, False)

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = base_types.UninitialisedField(self, 'AcctOwnrTxId', References44Choice, False)

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
	def CtrPtyMktInfrstrctrTxId(self):
		return self._CtrPtyMktInfrstrctrTxId

	@CtrPtyMktInfrstrctrTxId.setter
	def CtrPtyMktInfrstrctrTxId(self, value):
		self._CtrPtyMktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', Max35Text, False)

	@CtrPtyMktInfrstrctrTxId.deleter
	def CtrPtyMktInfrstrctrTxId(self):
		del self._CtrPtyMktInfrstrctrTxId
		self._CtrPtyMktInfrstrctrTxId = base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', Max35Text, False)

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
	def NonceId(self):
		return self._NonceId

	@NonceId.setter
	def NonceId(self, value):
		self._NonceId = value if value is not None else base_types.UninitialisedField(self, 'NonceId', Max35Text, False)

	@NonceId.deleter
	def NonceId(self):
		del self._NonceId
		self._NonceId = base_types.UninitialisedField(self, 'NonceId', Max35Text, False)

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if value is not None else base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = base_types.UninitialisedField(self, 'PrcrTxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrTxId', type=References44Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))