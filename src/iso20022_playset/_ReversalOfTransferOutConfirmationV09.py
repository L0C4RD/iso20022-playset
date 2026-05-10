from . import base_types
from .Max35Text import Max35Text
from .AdditionalReference10 import AdditionalReference10
from .MarketPracticeVersion1 import MarketPracticeVersion1
from .MessageIdentification1 import MessageIdentification1
from .AdditionalReference11 import AdditionalReference11
from .TransferReference16 import TransferReference16
from .CopyInformation5 import CopyInformation5

class ReversalOfTransferOutConfirmationV09(base_types._BaseFieldType):

	__slots__ = ["_MktPrctcVrsn", "_PoolRef", "_MsgId", "_CpyDtls", "_RltdRef", "_PrvsRef", "_RvslRefs", "_MstrRef"]
	@property
	def MktPrctcVrsn(self):
		return self._MktPrctcVrsn

	@MktPrctcVrsn.setter
	def MktPrctcVrsn(self, value):
		self._MktPrctcVrsn = value if type(value) != base_types.auto else self.make_default("MktPrctcVrsn")

	@MktPrctcVrsn.deleter
	def MktPrctcVrsn(self):
		del self._MktPrctcVrsn
		self._MktPrctcVrsn = None

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
	def RvslRefs(self):
		return self._RvslRefs

	@RvslRefs.setter
	def RvslRefs(self, value):
		self._RvslRefs = value if type(value) != base_types.auto else self.make_default("RvslRefs")

	@RvslRefs.deleter
	def RvslRefs(self):
		del self._RvslRefs
		self._RvslRefs = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRefs', type=TransferReference16, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

