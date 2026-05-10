from . import base_types
from ._AdditionalBusinessProcessFormat23Choice import AdditionalBusinessProcessFormat23Choice
from ._CorporateActionDate86 import CorporateActionDate86
from ._CorporateActionEventStageFormat14Choice import CorporateActionEventStageFormat14Choice
from ._IntermediateSecuritiesDistributionTypeFormat15Choice import IntermediateSecuritiesDistributionTypeFormat15Choice
from ._LotteryTypeFormat4Choice import LotteryTypeFormat4Choice

class CorporateAction85(base_types._BaseFieldType):

	__slots__ = ["_AddtlBizPrcInd", "_DtDtls", "_EvtStag", "_IntrmdtSctiesDstrbtnTp", "_LtryTp"]
	@property
	def AddtlBizPrcInd(self):
		return self._AddtlBizPrcInd

	@AddtlBizPrcInd.setter
	def AddtlBizPrcInd(self, value):
		self._AddtlBizPrcInd = value if type(value) != base_types.auto else self.make_default("AddtlBizPrcInd")

	@AddtlBizPrcInd.deleter
	def AddtlBizPrcInd(self):
		del self._AddtlBizPrcInd
		self._AddtlBizPrcInd = None

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if type(value) != base_types.auto else self.make_default("DtDtls")

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = None

	@property
	def EvtStag(self):
		return self._EvtStag

	@EvtStag.setter
	def EvtStag(self, value):
		self._EvtStag = value if type(value) != base_types.auto else self.make_default("EvtStag")

	@EvtStag.deleter
	def EvtStag(self):
		del self._EvtStag
		self._EvtStag = None

	@property
	def IntrmdtSctiesDstrbtnTp(self):
		return self._IntrmdtSctiesDstrbtnTp

	@IntrmdtSctiesDstrbtnTp.setter
	def IntrmdtSctiesDstrbtnTp(self, value):
		self._IntrmdtSctiesDstrbtnTp = value if type(value) != base_types.auto else self.make_default("IntrmdtSctiesDstrbtnTp")

	@IntrmdtSctiesDstrbtnTp.deleter
	def IntrmdtSctiesDstrbtnTp(self):
		del self._IntrmdtSctiesDstrbtnTp
		self._IntrmdtSctiesDstrbtnTp = None

	@property
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if type(value) != base_types.auto else self.make_default("LtryTp")

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat23Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate86, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecuritiesDistributionTypeFormat15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryTp', type=LotteryTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
	))

