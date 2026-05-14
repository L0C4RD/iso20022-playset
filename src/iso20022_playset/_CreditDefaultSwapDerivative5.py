# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreditDefaultSwapIndex3 import CreditDefaultSwapIndex3
from ._ISINOct2015Identifier import ISINOct2015Identifier

class CreditDefaultSwapDerivative5(base_types._BaseFieldType):

	__slots__ = ["_UndrlygCdtDfltSwpId", "_UndrlygCdtDfltSwpIndx"]
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

	@property
	def UndrlygCdtDfltSwpIndx(self):
		return self._UndrlygCdtDfltSwpIndx

	@UndrlygCdtDfltSwpIndx.setter
	def UndrlygCdtDfltSwpIndx(self, value):
		self._UndrlygCdtDfltSwpIndx = value if type(value) != base_types.auto else self.make_default("UndrlygCdtDfltSwpIndx")

	@UndrlygCdtDfltSwpIndx.deleter
	def UndrlygCdtDfltSwpIndx(self):
		del self._UndrlygCdtDfltSwpIndx
		self._UndrlygCdtDfltSwpIndx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UndrlygCdtDfltSwpId', type=ISINOct2015Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygCdtDfltSwpIndx', type=CreditDefaultSwapIndex3, min=1, max=1, mutex_group=None, array=False),
	))