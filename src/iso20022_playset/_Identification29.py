# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax16Text
from . import RestrictedFINXMax52Text

class Identification29(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrTxId", "_AcctSvcrTxId", "_BsktId", "_CmonId", "_CorpActnEvtId", "_CtrPtyMktInfrstrctrTxId", "_IndxId", "_ListId", "_MktInfrstrctrTxId", "_MstrId", "_PoolId", "_PrcrTxId", "_PrgmId", "_TradId"]
	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrTxId', RestrictedFINXMax16Text, False)

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = base_types.UninitialisedField(self, 'AcctOwnrTxId', RestrictedFINXMax16Text, False)

	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrTxId', RestrictedFINXMax16Text, False)

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = base_types.UninitialisedField(self, 'AcctSvcrTxId', RestrictedFINXMax16Text, False)

	@property
	def BsktId(self):
		return self._BsktId

	@BsktId.setter
	def BsktId(self, value):
		self._BsktId = value if value is not None else base_types.UninitialisedField(self, 'BsktId', RestrictedFINXMax16Text, False)

	@BsktId.deleter
	def BsktId(self):
		del self._BsktId
		self._BsktId = base_types.UninitialisedField(self, 'BsktId', RestrictedFINXMax16Text, False)

	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if value is not None else base_types.UninitialisedField(self, 'CmonId', RestrictedFINXMax16Text, False)

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = base_types.UninitialisedField(self, 'CmonId', RestrictedFINXMax16Text, False)

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtId', RestrictedFINXMax16Text, False)

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = base_types.UninitialisedField(self, 'CorpActnEvtId', RestrictedFINXMax16Text, False)

	@property
	def CtrPtyMktInfrstrctrTxId(self):
		return self._CtrPtyMktInfrstrctrTxId

	@CtrPtyMktInfrstrctrTxId.setter
	def CtrPtyMktInfrstrctrTxId(self, value):
		self._CtrPtyMktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', RestrictedFINXMax16Text, False)

	@CtrPtyMktInfrstrctrTxId.deleter
	def CtrPtyMktInfrstrctrTxId(self):
		del self._CtrPtyMktInfrstrctrTxId
		self._CtrPtyMktInfrstrctrTxId = base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', RestrictedFINXMax16Text, False)

	@property
	def IndxId(self):
		return self._IndxId

	@IndxId.setter
	def IndxId(self, value):
		self._IndxId = value if value is not None else base_types.UninitialisedField(self, 'IndxId', RestrictedFINXMax16Text, False)

	@IndxId.deleter
	def IndxId(self):
		del self._IndxId
		self._IndxId = base_types.UninitialisedField(self, 'IndxId', RestrictedFINXMax16Text, False)

	@property
	def ListId(self):
		return self._ListId

	@ListId.setter
	def ListId(self, value):
		self._ListId = value if value is not None else base_types.UninitialisedField(self, 'ListId', RestrictedFINXMax16Text, False)

	@ListId.deleter
	def ListId(self):
		del self._ListId
		self._ListId = base_types.UninitialisedField(self, 'ListId', RestrictedFINXMax16Text, False)

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', RestrictedFINXMax16Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', RestrictedFINXMax16Text, False)

	@property
	def MstrId(self):
		return self._MstrId

	@MstrId.setter
	def MstrId(self, value):
		self._MstrId = value if value is not None else base_types.UninitialisedField(self, 'MstrId', RestrictedFINXMax16Text, False)

	@MstrId.deleter
	def MstrId(self):
		del self._MstrId
		self._MstrId = base_types.UninitialisedField(self, 'MstrId', RestrictedFINXMax16Text, False)

	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if value is not None else base_types.UninitialisedField(self, 'PoolId', RestrictedFINXMax16Text, False)

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = base_types.UninitialisedField(self, 'PoolId', RestrictedFINXMax16Text, False)

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if value is not None else base_types.UninitialisedField(self, 'PrcrTxId', RestrictedFINXMax16Text, False)

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = base_types.UninitialisedField(self, 'PrcrTxId', RestrictedFINXMax16Text, False)

	@property
	def PrgmId(self):
		return self._PrgmId

	@PrgmId.setter
	def PrgmId(self, value):
		self._PrgmId = value if value is not None else base_types.UninitialisedField(self, 'PrgmId', RestrictedFINXMax16Text, False)

	@PrgmId.deleter
	def PrgmId(self):
		del self._PrgmId
		self._PrgmId = base_types.UninitialisedField(self, 'PrgmId', RestrictedFINXMax16Text, False)

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if value is not None else base_types.UninitialisedField(self, 'TradId', RestrictedFINXMax52Text, True)

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = base_types.UninitialisedField(self, 'TradId', RestrictedFINXMax52Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrTxId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ListId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrgmId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=RestrictedFINXMax52Text, min=0, max=None, mutex_group=None, array=True),
	))