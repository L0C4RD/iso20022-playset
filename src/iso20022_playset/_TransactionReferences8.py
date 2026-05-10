from . import base_types
from ._Max35Text import Max35Text
from ._UUIDv4Identifier import UUIDv4Identifier
from ._PartyIdentification272 import PartyIdentification272

class TransactionReferences8(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_InstrId", "_UETR", "_EndToEndId", "_PmtInfId", "_MndtId", "_CdtrSchmeId"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if type(value) != base_types.auto else self.make_default("InstrId")

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = None

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if type(value) != base_types.auto else self.make_default("UETR")

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = None

	@property
	def EndToEndId(self):
		return self._EndToEndId

	@EndToEndId.setter
	def EndToEndId(self, value):
		self._EndToEndId = value if type(value) != base_types.auto else self.make_default("EndToEndId")

	@EndToEndId.deleter
	def EndToEndId(self):
		del self._EndToEndId
		self._EndToEndId = None

	@property
	def PmtInfId(self):
		return self._PmtInfId

	@PmtInfId.setter
	def PmtInfId(self, value):
		self._PmtInfId = value if type(value) != base_types.auto else self.make_default("PmtInfId")

	@PmtInfId.deleter
	def PmtInfId(self):
		del self._PmtInfId
		self._PmtInfId = None

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if type(value) != base_types.auto else self.make_default("MndtId")

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = None

	@property
	def CdtrSchmeId(self):
		return self._CdtrSchmeId

	@CdtrSchmeId.setter
	def CdtrSchmeId(self, value):
		self._CdtrSchmeId = value if type(value) != base_types.auto else self.make_default("CdtrSchmeId")

	@CdtrSchmeId.deleter
	def CdtrSchmeId(self):
		del self._CdtrSchmeId
		self._CdtrSchmeId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))

