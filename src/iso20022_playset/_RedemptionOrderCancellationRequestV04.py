# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference8
from . import AdditionalReference9
from . import CopyInformation4
from . import InvestmentFundOrder9
from . import Max35Text
from . import MessageIdentification1

class RedemptionOrderCancellationRequestV04(base_types._BaseFieldType):

	__slots__ = ["_CpyDtls", "_MsgId", "_MstrRef", "_OrdrRefs", "_PoolRef", "_PrvsRef"]
	@property
	def CpyDtls(self):
		return self._CpyDtls

	@CpyDtls.setter
	def CpyDtls(self, value):
		self._CpyDtls = value if value is not None else base_types.UninitialisedField(self, 'CpyDtls', CopyInformation4, False)

	@CpyDtls.deleter
	def CpyDtls(self):
		del self._CpyDtls
		self._CpyDtls = base_types.UninitialisedField(self, 'CpyDtls', CopyInformation4, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def OrdrRefs(self):
		return self._OrdrRefs

	@OrdrRefs.setter
	def OrdrRefs(self, value):
		self._OrdrRefs = value if value is not None else base_types.UninitialisedField(self, 'OrdrRefs', InvestmentFundOrder9, True)

	@OrdrRefs.deleter
	def OrdrRefs(self):
		del self._OrdrRefs
		self._OrdrRefs = base_types.UninitialisedField(self, 'OrdrRefs', InvestmentFundOrder9, True)

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if value is not None else base_types.UninitialisedField(self, 'PoolRef', AdditionalReference9, False)

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = base_types.UninitialisedField(self, 'PoolRef', AdditionalReference9, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference8, False)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CpyDtls', type=CopyInformation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRefs', type=InvestmentFundOrder9, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference8, min=0, max=1, mutex_group=None, array=False),
	))