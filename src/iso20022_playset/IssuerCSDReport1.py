import base_types
import SettlementInternaliserTransactionType1
import SettlementInternaliserFinancialInstrument1
import IssuerCSDIdentification1
import InternalisationData1
import SettlementInternaliserClientType1

class IssuerCSDReport1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_OvrllTtl", "_FinInstrm", "_TtlCshTrf", "_ClntTp", "_TxTp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def OvrllTtl(self):
		return self._OvrllTtl

	@OvrllTtl.setter
	def OvrllTtl(self, value):
		self._OvrllTtl = value if type(value) != auto else self.make_default("OvrllTtl")

	@OvrllTtl.deleter
	def OvrllTtl(self):
		del self._OvrllTtl
		self._OvrllTtl = None

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if type(value) != auto else self.make_default("FinInstrm")

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = None

	@property
	def TtlCshTrf(self):
		return self._TtlCshTrf

	@TtlCshTrf.setter
	def TtlCshTrf(self, value):
		self._TtlCshTrf = value if type(value) != auto else self.make_default("TtlCshTrf")

	@TtlCshTrf.deleter
	def TtlCshTrf(self):
		del self._TtlCshTrf
		self._TtlCshTrf = None

	@property
	def ClntTp(self):
		return self._ClntTp

	@ClntTp.setter
	def ClntTp(self, value):
		self._ClntTp = value if type(value) != auto else self.make_default("ClntTp")

	@ClntTp.deleter
	def ClntTp(self):
		del self._ClntTp
		self._ClntTp = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=IssuerCSDIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OvrllTtl', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=SettlementInternaliserFinancialInstrument1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCshTrf', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntTp', type=SettlementInternaliserClientType1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=SettlementInternaliserTransactionType1, min=1, max=1, mutex_group=None, array=False),
	))

