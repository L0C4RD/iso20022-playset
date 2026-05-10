import base_types
import SecuritiesSettlementConditionsModificationRequestV10

class SESE_030_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesSttlmCondsModReq"]
		@property
		def SctiesSttlmCondsModReq(self):
			return self._SctiesSttlmCondsModReq

		@SctiesSttlmCondsModReq.setter
		def SctiesSttlmCondsModReq(self, value):
			self._SctiesSttlmCondsModReq = value if type(value) != auto else self.make_default("SctiesSttlmCondsModReq")

		@SctiesSttlmCondsModReq.deleter
		def SctiesSttlmCondsModReq(self):
			del self._SctiesSttlmCondsModReq
			self._SctiesSttlmCondsModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesSttlmCondsModReq', type=SecuritiesSettlementConditionsModificationRequestV10, min=1, max=1, mutex_group=None, array=False),
		))

