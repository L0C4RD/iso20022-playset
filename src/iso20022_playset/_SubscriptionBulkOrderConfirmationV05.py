from . import base_types
from ._AdditionalReference10 import AdditionalReference10
from ._AdditionalReference11 import AdditionalReference11
from ._CopyInformation5 import CopyInformation5
from ._Extension1 import Extension1
from ._MessageIdentification1 import MessageIdentification1
from ._SubscriptionBulkExecution05 import SubscriptionBulkExecution05

class SubscriptionBulkOrderConfirmationV05(base_types._BaseFieldType):

	__slots__ = ["_BlkExctnDtls", "_CpyDtls", "_MsgId", "_PoolRef", "_PrvsRef", "_RltdRef", "_Xtnsn"]
	@property
	def BlkExctnDtls(self):
		return self._BlkExctnDtls

	@BlkExctnDtls.setter
	def BlkExctnDtls(self, value):
		self._BlkExctnDtls = value if type(value) != base_types.auto else self.make_default("BlkExctnDtls")

	@BlkExctnDtls.deleter
	def BlkExctnDtls(self):
		del self._BlkExctnDtls
		self._BlkExctnDtls = None

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
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

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
		base_types.FieldEntry(name='BlkExctnDtls', type=SubscriptionBulkExecution05, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))

