# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBusinessProcessFormat18Choice
from . import CorporateActionDate85
from . import CorporateActionEventStageFormat14Choice
from . import CorporateActionQuantity12
from . import IntermediateSecuritiesDistributionTypeFormat19Choice
from . import LotteryTypeFormat4Choice

class CorporateAction91(base_types._BaseFieldType):

	__slots__ = ["_AddtlBizPrcInd", "_DtDtls", "_EvtStag", "_FllwngEvtTpInd", "_LtryTp", "_SctiesQty"]
	@property
	def AddtlBizPrcInd(self):
		return self._AddtlBizPrcInd

	@AddtlBizPrcInd.setter
	def AddtlBizPrcInd(self, value):
		self._AddtlBizPrcInd = value if value is not None else base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat18Choice, True)

	@AddtlBizPrcInd.deleter
	def AddtlBizPrcInd(self):
		del self._AddtlBizPrcInd
		self._AddtlBizPrcInd = base_types.UninitialisedField(self, 'AddtlBizPrcInd', AdditionalBusinessProcessFormat18Choice, True)

	@property
	def DtDtls(self):
		return self._DtDtls

	@DtDtls.setter
	def DtDtls(self, value):
		self._DtDtls = value if value is not None else base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate85, False)

	@DtDtls.deleter
	def DtDtls(self):
		del self._DtDtls
		self._DtDtls = base_types.UninitialisedField(self, 'DtDtls', CorporateActionDate85, False)

	@property
	def EvtStag(self):
		return self._EvtStag

	@EvtStag.setter
	def EvtStag(self, value):
		self._EvtStag = value if value is not None else base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStageFormat14Choice, False)

	@EvtStag.deleter
	def EvtStag(self):
		del self._EvtStag
		self._EvtStag = base_types.UninitialisedField(self, 'EvtStag', CorporateActionEventStageFormat14Choice, False)

	@property
	def FllwngEvtTpInd(self):
		return self._FllwngEvtTpInd

	@FllwngEvtTpInd.setter
	def FllwngEvtTpInd(self, value):
		self._FllwngEvtTpInd = value if value is not None else base_types.UninitialisedField(self, 'FllwngEvtTpInd', IntermediateSecuritiesDistributionTypeFormat19Choice, False)

	@FllwngEvtTpInd.deleter
	def FllwngEvtTpInd(self):
		del self._FllwngEvtTpInd
		self._FllwngEvtTpInd = base_types.UninitialisedField(self, 'FllwngEvtTpInd', IntermediateSecuritiesDistributionTypeFormat19Choice, False)

	@property
	def LtryTp(self):
		return self._LtryTp

	@LtryTp.setter
	def LtryTp(self, value):
		self._LtryTp = value if value is not None else base_types.UninitialisedField(self, 'LtryTp', LotteryTypeFormat4Choice, False)

	@LtryTp.deleter
	def LtryTp(self):
		del self._LtryTp
		self._LtryTp = base_types.UninitialisedField(self, 'LtryTp', LotteryTypeFormat4Choice, False)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', CorporateActionQuantity12, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', CorporateActionQuantity12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlBizPrcInd', type=AdditionalBusinessProcessFormat18Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtDtls', type=CorporateActionDate85, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtStag', type=CorporateActionEventStageFormat14Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FllwngEvtTpInd', type=IntermediateSecuritiesDistributionTypeFormat19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LtryTp', type=LotteryTypeFormat4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=CorporateActionQuantity12, min=0, max=1, mutex_group=None, array=False),
	))