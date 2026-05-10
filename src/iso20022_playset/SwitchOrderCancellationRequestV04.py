from . import base_types
import InvestmentFundOrder9
import AdditionalReference8
import MessageIdentification1
import AdditionalReference9
import CopyInformation4
import Max35Text

class SwitchOrderCancellationRequestV04(base_types._BaseFieldType):

	__slots__ = ["_PrvsRef", "_MstrRef", "_MsgId", "_CpyDtls", "_OrdrRefs", "_PoolRef"]
	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

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
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def CpyDtls(self):
		return self._CpyDtls

	@CpyDtls.setter
	def CpyDtls(self, value):
		self._CpyDtls = value if type(value) != auto else self.make_default("CpyDtls")

	@CpyDtls.deleter
	def CpyDtls(self):
		del self._CpyDtls
		self._CpyDtls = None

	@property
	def OrdrRefs(self):
		return self._OrdrRefs

	@OrdrRefs.setter
	def OrdrRefs(self, value):
		self._OrdrRefs = value if type(value) != auto else self.make_default("OrdrRefs")

	@OrdrRefs.deleter
	def OrdrRefs(self):
		del self._OrdrRefs
		self._OrdrRefs = None

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if type(value) != auto else self.make_default("PoolRef")

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRefs', type=InvestmentFundOrder9, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference9, min=0, max=1, mutex_group=None, array=False),
	))

