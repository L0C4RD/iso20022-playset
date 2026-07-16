# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDefaultSwapSingleName2
from . import ISINOct2015Identifier

class CreditDefaultSwapDerivative6(base_types._BaseFieldType):

	__slots__ = ["_OblgtnId", "_SnglNm", "_UndrlygCdtDfltSwpId"]
	@property
	def OblgtnId(self):
		return self._OblgtnId

	@OblgtnId.setter
	def OblgtnId(self, value):
		self._OblgtnId = value if value is not None else base_types.UninitialisedField(self, 'OblgtnId', ISINOct2015Identifier, False)

	@OblgtnId.deleter
	def OblgtnId(self):
		del self._OblgtnId
		self._OblgtnId = base_types.UninitialisedField(self, 'OblgtnId', ISINOct2015Identifier, False)

	@property
	def SnglNm(self):
		return self._SnglNm

	@SnglNm.setter
	def SnglNm(self, value):
		self._SnglNm = value if value is not None else base_types.UninitialisedField(self, 'SnglNm', CreditDefaultSwapSingleName2, False)

	@SnglNm.deleter
	def SnglNm(self):
		del self._SnglNm
		self._SnglNm = base_types.UninitialisedField(self, 'SnglNm', CreditDefaultSwapSingleName2, False)

	@property
	def UndrlygCdtDfltSwpId(self):
		return self._UndrlygCdtDfltSwpId

	@UndrlygCdtDfltSwpId.setter
	def UndrlygCdtDfltSwpId(self, value):
		self._UndrlygCdtDfltSwpId = value if value is not None else base_types.UninitialisedField(self, 'UndrlygCdtDfltSwpId', ISINOct2015Identifier, False)

	@UndrlygCdtDfltSwpId.deleter
	def UndrlygCdtDfltSwpId(self):
		del self._UndrlygCdtDfltSwpId
		self._UndrlygCdtDfltSwpId = base_types.UninitialisedField(self, 'UndrlygCdtDfltSwpId', ISINOct2015Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OblgtnId', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglNm', type=CreditDefaultSwapSingleName2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygCdtDfltSwpId', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
	))