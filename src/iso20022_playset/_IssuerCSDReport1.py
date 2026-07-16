# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InternalisationData1
from . import IssuerCSDIdentification1
from . import SettlementInternaliserClientType1
from . import SettlementInternaliserFinancialInstrument1
from . import SettlementInternaliserTransactionType1

class IssuerCSDReport1(base_types._BaseFieldType):

	__slots__ = ["_ClntTp", "_FinInstrm", "_Id", "_OvrllTtl", "_TtlCshTrf", "_TxTp"]
	@property
	def ClntTp(self):
		return self._ClntTp

	@ClntTp.setter
	def ClntTp(self, value):
		self._ClntTp = value if value is not None else base_types.UninitialisedField(self, 'ClntTp', SettlementInternaliserClientType1, False)

	@ClntTp.deleter
	def ClntTp(self):
		del self._ClntTp
		self._ClntTp = base_types.UninitialisedField(self, 'ClntTp', SettlementInternaliserClientType1, False)

	@property
	def FinInstrm(self):
		return self._FinInstrm

	@FinInstrm.setter
	def FinInstrm(self, value):
		self._FinInstrm = value if value is not None else base_types.UninitialisedField(self, 'FinInstrm', SettlementInternaliserFinancialInstrument1, False)

	@FinInstrm.deleter
	def FinInstrm(self):
		del self._FinInstrm
		self._FinInstrm = base_types.UninitialisedField(self, 'FinInstrm', SettlementInternaliserFinancialInstrument1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', IssuerCSDIdentification1, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', IssuerCSDIdentification1, False)

	@property
	def OvrllTtl(self):
		return self._OvrllTtl

	@OvrllTtl.setter
	def OvrllTtl(self, value):
		self._OvrllTtl = value if value is not None else base_types.UninitialisedField(self, 'OvrllTtl', InternalisationData1, False)

	@OvrllTtl.deleter
	def OvrllTtl(self):
		del self._OvrllTtl
		self._OvrllTtl = base_types.UninitialisedField(self, 'OvrllTtl', InternalisationData1, False)

	@property
	def TtlCshTrf(self):
		return self._TtlCshTrf

	@TtlCshTrf.setter
	def TtlCshTrf(self, value):
		self._TtlCshTrf = value if value is not None else base_types.UninitialisedField(self, 'TtlCshTrf', InternalisationData1, False)

	@TtlCshTrf.deleter
	def TtlCshTrf(self):
		del self._TtlCshTrf
		self._TtlCshTrf = base_types.UninitialisedField(self, 'TtlCshTrf', InternalisationData1, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', SettlementInternaliserTransactionType1, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', SettlementInternaliserTransactionType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntTp', type=SettlementInternaliserClientType1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrm', type=SettlementInternaliserFinancialInstrument1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=IssuerCSDIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OvrllTtl', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCshTrf', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=SettlementInternaliserTransactionType1, min=1, max=1, mutex_group=None, array=False),
	))