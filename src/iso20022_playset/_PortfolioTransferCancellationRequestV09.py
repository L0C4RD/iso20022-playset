from . import base_types
from ._AdditionalReference10 import AdditionalReference10
from ._AdditionalReference11 import AdditionalReference11
from ._MarketPracticeVersion1 import MarketPracticeVersion1
from ._Max35Text import Max35Text
from ._MessageIdentification1 import MessageIdentification1
from ._TransferReference14 import TransferReference14

class PortfolioTransferCancellationRequestV09(base_types._BaseFieldType):

	__slots__ = ["_MktPrctcVrsn", "_MsgRef", "_MstrRef", "_PoolRef", "_PrvsRef", "_RltdRef", "_TrfRefs"]
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
	def MsgRef(self):
		return self._MsgRef

	@MsgRef.setter
	def MsgRef(self, value):
		self._MsgRef = value if type(value) != base_types.auto else self.make_default("MsgRef")

	@MsgRef.deleter
	def MsgRef(self):
		del self._MsgRef
		self._MsgRef = None

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
	def TrfRefs(self):
		return self._TrfRefs

	@TrfRefs.setter
	def TrfRefs(self, value):
		self._TrfRefs = value if type(value) != base_types.auto else self.make_default("TrfRefs")

	@TrfRefs.deleter
	def TrfRefs(self):
		del self._TrfRefs
		self._TrfRefs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfRefs', type=TransferReference14, min=1, max=1, mutex_group=None, array=False),
	))

