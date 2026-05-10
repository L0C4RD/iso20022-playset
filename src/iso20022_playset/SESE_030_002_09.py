from . import base_types
from .SecuritiesSettlementConditionsModificationRequest002V09 import SecuritiesSettlementConditionsModificationRequest002V09

class SESE_030_002_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmCondsModReq"]
		@property
		def SctiesSttlmCondsModReq(self):
			return self._SctiesSttlmCondsModReq

		@SctiesSttlmCondsModReq.setter
		def SctiesSttlmCondsModReq(self, value):
			self._SctiesSttlmCondsModReq = value if type(value) != base_types.auto else self.make_default("SctiesSttlmCondsModReq")

		@SctiesSttlmCondsModReq.deleter
		def SctiesSttlmCondsModReq(self):
			del self._SctiesSttlmCondsModReq
			self._SctiesSttlmCondsModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondsModReq', type=SecuritiesSettlementConditionsModificationRequest002V09, min=1, max=1, mutex_group=None, array=False),
		))

