from . import base_types
from .Max35Text import Max35Text
from .AdditionalReference8 import AdditionalReference8
from .CopyInformation4 import CopyInformation4
from .InvestmentFundOrder11 import InvestmentFundOrder11
from .MessageIdentification1 import MessageIdentification1
from .AdditionalReference9 import AdditionalReference9
from .YesNoIndicator import YesNoIndicator

class SubscriptionBulkOrderConfirmationCancellationInstructionV02(base_types._BaseFieldType):

	__slots__ = ["_AmdmntInd", "_PoolRef", "_CpyDtls", "_MsgId", "_PrvsRef", "_MstrRef", "_OrdrRefs", "_RltdRef"]
	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if type(value) != base_types.auto else self.make_default("AmdmntInd")

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = None

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
	def OrdrRefs(self):
		return self._OrdrRefs

	@OrdrRefs.setter
	def OrdrRefs(self, value):
		self._OrdrRefs = value if type(value) != base_types.auto else self.make_default("OrdrRefs")

	@OrdrRefs.deleter
	def OrdrRefs(self):
		del self._OrdrRefs
		self._OrdrRefs = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRefs', type=InvestmentFundOrder11, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference8, min=0, max=1, mutex_group=None, array=False),
	))

