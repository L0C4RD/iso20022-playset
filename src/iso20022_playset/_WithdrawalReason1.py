# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max4Text
from . import WithdrawalReason1Code

class WithdrawalReason1(base_types._BaseFieldType):

	__slots__ = ["_WdrwlRsnCd", "_WdrwlRsnSubCd"]
	@property
	def WdrwlRsnCd(self):
		return self._WdrwlRsnCd

	@WdrwlRsnCd.setter
	def WdrwlRsnCd(self, value):
		self._WdrwlRsnCd = value if value is not None else base_types.UninitialisedField(self, 'WdrwlRsnCd', WithdrawalReason1Code, False)

	@WdrwlRsnCd.deleter
	def WdrwlRsnCd(self):
		del self._WdrwlRsnCd
		self._WdrwlRsnCd = base_types.UninitialisedField(self, 'WdrwlRsnCd', WithdrawalReason1Code, False)

	@property
	def WdrwlRsnSubCd(self):
		return self._WdrwlRsnSubCd

	@WdrwlRsnSubCd.setter
	def WdrwlRsnSubCd(self, value):
		self._WdrwlRsnSubCd = value if value is not None else base_types.UninitialisedField(self, 'WdrwlRsnSubCd', Max4Text, False)

	@WdrwlRsnSubCd.deleter
	def WdrwlRsnSubCd(self):
		del self._WdrwlRsnSubCd
		self._WdrwlRsnSubCd = base_types.UninitialisedField(self, 'WdrwlRsnSubCd', Max4Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='WdrwlRsnCd', type=WithdrawalReason1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WdrwlRsnSubCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
	))