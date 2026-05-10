from . import base_types
from ._CreditDefaultSwapSingleName2 import CreditDefaultSwapSingleName2
from ._ISINOct2015Identifier import ISINOct2015Identifier

class CreditDefaultSwapDerivative6(base_types._BaseFieldType):

	__slots__ = ["_SnglNm", "_OblgtnId", "_UndrlygCdtDfltSwpId"]
	@property
	def SnglNm(self):
		return self._SnglNm

	@SnglNm.setter
	def SnglNm(self, value):
		self._SnglNm = value if type(value) != base_types.auto else self.make_default("SnglNm")

	@SnglNm.deleter
	def SnglNm(self):
		del self._SnglNm
		self._SnglNm = None

	@property
	def OblgtnId(self):
		return self._OblgtnId

	@OblgtnId.setter
	def OblgtnId(self, value):
		self._OblgtnId = value if type(value) != base_types.auto else self.make_default("OblgtnId")

	@OblgtnId.deleter
	def OblgtnId(self):
		del self._OblgtnId
		self._OblgtnId = None

	@property
	def UndrlygCdtDfltSwpId(self):
		return self._UndrlygCdtDfltSwpId

	@UndrlygCdtDfltSwpId.setter
	def UndrlygCdtDfltSwpId(self, value):
		self._UndrlygCdtDfltSwpId = value if type(value) != base_types.auto else self.make_default("UndrlygCdtDfltSwpId")

	@UndrlygCdtDfltSwpId.deleter
	def UndrlygCdtDfltSwpId(self):
		del self._UndrlygCdtDfltSwpId
		self._UndrlygCdtDfltSwpId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SnglNm', type=CreditDefaultSwapSingleName2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OblgtnId', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygCdtDfltSwpId', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
	))

