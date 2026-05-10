from . import base_types
import TransactionDetails169
import UTIIdentifier
import SupplementaryData1
import Max35Text
import AdditionalReference10

class Transaction161(base_types._BaseFieldType):

	__slots__ = ["_AcctSvcrTxId", "_ClntTrptyCollTxId", "_TxDtls", "_TrptyAgtSvcPrvdrCollInstrId", "_UnqTxIdr", "_AcctSvcrLegId", "_TradId", "_CorpActnEvtId", "_CmonId", "_MktInfrstrctrTxId", "_MstrRef", "_SplmtryData", "_AcctOwnrTxId", "_ClntRef", "_PoolId", "_CtrPtyMktInfrstrctrTxId", "_AcctOwnrLegId", "_PrcrTxId", "_TrptyAgtSvcPrvdrCollTxId", "_ClntCollInstrId"]
	@property
	def AcctSvcrTxId(self):
		return self._AcctSvcrTxId

	@AcctSvcrTxId.setter
	def AcctSvcrTxId(self, value):
		self._AcctSvcrTxId = value if type(value) != auto else self.make_default("AcctSvcrTxId")

	@AcctSvcrTxId.deleter
	def AcctSvcrTxId(self):
		del self._AcctSvcrTxId
		self._AcctSvcrTxId = None

	@property
	def ClntTrptyCollTxId(self):
		return self._ClntTrptyCollTxId

	@ClntTrptyCollTxId.setter
	def ClntTrptyCollTxId(self, value):
		self._ClntTrptyCollTxId = value if type(value) != auto else self.make_default("ClntTrptyCollTxId")

	@ClntTrptyCollTxId.deleter
	def ClntTrptyCollTxId(self):
		del self._ClntTrptyCollTxId
		self._ClntTrptyCollTxId = None

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def TrptyAgtSvcPrvdrCollInstrId(self):
		return self._TrptyAgtSvcPrvdrCollInstrId

	@TrptyAgtSvcPrvdrCollInstrId.setter
	def TrptyAgtSvcPrvdrCollInstrId(self, value):
		self._TrptyAgtSvcPrvdrCollInstrId = value if type(value) != auto else self.make_default("TrptyAgtSvcPrvdrCollInstrId")

	@TrptyAgtSvcPrvdrCollInstrId.deleter
	def TrptyAgtSvcPrvdrCollInstrId(self):
		del self._TrptyAgtSvcPrvdrCollInstrId
		self._TrptyAgtSvcPrvdrCollInstrId = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	@property
	def AcctSvcrLegId(self):
		return self._AcctSvcrLegId

	@AcctSvcrLegId.setter
	def AcctSvcrLegId(self, value):
		self._AcctSvcrLegId = value if type(value) != auto else self.make_default("AcctSvcrLegId")

	@AcctSvcrLegId.deleter
	def AcctSvcrLegId(self):
		del self._AcctSvcrLegId
		self._AcctSvcrLegId = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if type(value) != auto else self.make_default("CmonId")

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = None

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if type(value) != auto else self.make_default("MktInfrstrctrTxId")

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def AcctOwnrTxId(self):
		return self._AcctOwnrTxId

	@AcctOwnrTxId.setter
	def AcctOwnrTxId(self, value):
		self._AcctOwnrTxId = value if type(value) != auto else self.make_default("AcctOwnrTxId")

	@AcctOwnrTxId.deleter
	def AcctOwnrTxId(self):
		del self._AcctOwnrTxId
		self._AcctOwnrTxId = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def PoolId(self):
		return self._PoolId

	@PoolId.setter
	def PoolId(self, value):
		self._PoolId = value if type(value) != auto else self.make_default("PoolId")

	@PoolId.deleter
	def PoolId(self):
		del self._PoolId
		self._PoolId = None

	@property
	def CtrPtyMktInfrstrctrTxId(self):
		return self._CtrPtyMktInfrstrctrTxId

	@CtrPtyMktInfrstrctrTxId.setter
	def CtrPtyMktInfrstrctrTxId(self, value):
		self._CtrPtyMktInfrstrctrTxId = value if type(value) != auto else self.make_default("CtrPtyMktInfrstrctrTxId")

	@CtrPtyMktInfrstrctrTxId.deleter
	def CtrPtyMktInfrstrctrTxId(self):
		del self._CtrPtyMktInfrstrctrTxId
		self._CtrPtyMktInfrstrctrTxId = None

	@property
	def AcctOwnrLegId(self):
		return self._AcctOwnrLegId

	@AcctOwnrLegId.setter
	def AcctOwnrLegId(self, value):
		self._AcctOwnrLegId = value if type(value) != auto else self.make_default("AcctOwnrLegId")

	@AcctOwnrLegId.deleter
	def AcctOwnrLegId(self):
		del self._AcctOwnrLegId
		self._AcctOwnrLegId = None

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if type(value) != auto else self.make_default("PrcrTxId")

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = None

	@property
	def TrptyAgtSvcPrvdrCollTxId(self):
		return self._TrptyAgtSvcPrvdrCollTxId

	@TrptyAgtSvcPrvdrCollTxId.setter
	def TrptyAgtSvcPrvdrCollTxId(self, value):
		self._TrptyAgtSvcPrvdrCollTxId = value if type(value) != auto else self.make_default("TrptyAgtSvcPrvdrCollTxId")

	@TrptyAgtSvcPrvdrCollTxId.deleter
	def TrptyAgtSvcPrvdrCollTxId(self):
		del self._TrptyAgtSvcPrvdrCollTxId
		self._TrptyAgtSvcPrvdrCollTxId = None

	@property
	def ClntCollInstrId(self):
		return self._ClntCollInstrId

	@ClntCollInstrId.setter
	def ClntCollInstrId(self, value):
		self._ClntCollInstrId = value if type(value) != auto else self.make_default("ClntCollInstrId")

	@ClntCollInstrId.deleter
	def ClntCollInstrId(self):
		del self._ClntCollInstrId
		self._ClntCollInstrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctSvcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntTrptyCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=TransactionDetails169, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrLegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctOwnrTxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrLegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtSvcPrvdrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntCollInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

