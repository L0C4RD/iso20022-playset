from . import base_types
from ._CopyInformation4 import CopyInformation4
from ._RedemptionMultipleOrder6 import RedemptionMultipleOrder6
from ._AdditionalReference8 import AdditionalReference8
from ._MessageIdentification1 import MessageIdentification1
from ._Extension1 import Extension1
from ._AdditionalReference9 import AdditionalReference9

class RedemptionOrderV04(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_CpyDtls", "_PoolRef", "_PrvsRef", "_Xtnsn", "_MltplOrdrDtls"]
	@property
	def CpyDtls(self):
		return self._CpyDtls

	@CpyDtls.setter
	def CpyDtls(self, value):
		self._CpyDtls = value if type(value) != base_types.auto else self.make_default("CpyDtls")

	@CpyDtls.deleter
	def CpyDtls(self):
		del self._CpyDtls
		self._CpyDtls = None

	@property
	def MltplOrdrDtls(self):
		return self._MltplOrdrDtls

	@MltplOrdrDtls.setter
	def MltplOrdrDtls(self, value):
		self._MltplOrdrDtls = value if type(value) != base_types.auto else self.make_default("MltplOrdrDtls")

	@MltplOrdrDtls.deleter
	def MltplOrdrDtls(self):
		del self._MltplOrdrDtls
		self._MltplOrdrDtls = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if type(value) != base_types.auto else self.make_default("PoolRef")

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MltplOrdrDtls', type=RedemptionMultipleOrder6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))

