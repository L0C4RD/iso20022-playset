from . import base_types
from ._CorporateActionDate93 import CorporateActionDate93
from ._IntermediateSecuritiesDistributionTypeFormat18Choice import IntermediateSecuritiesDistributionTypeFormat18Choice
from ._AdditionalBusinessProcessFormat21Choice import AdditionalBusinessProcessFormat21Choice
from ._CorporateActionQuantity13 import CorporateActionQuantity13
from ._CorporateActionEventStageFormat15Choice import CorporateActionEventStageFormat15Choice
from ._LotteryTypeFormat5Choice import LotteryTypeFormat5Choice

class CorporateAction77(base_types._BaseFieldType):

	__slots__ = ["_EvtStag", "_AddtlBizPrcInd", "_LtryTp", "_IntrmdtSctiesDstrbtnTp", "_SctiesQty", "_DtDtls"]
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
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if type(value) != base_types.auto else self.make_default("LtryTp")

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = None

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
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != base_types.auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat21Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LtryTp', type=LotteryTypeFormat5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtSctiesDstrbtnTp', type=IntermediateSecuritiesDistributionTypeFormat18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=CorporateActionQuantity13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate93, min=0, max=1, mutex_group=None, array=False),
	))

