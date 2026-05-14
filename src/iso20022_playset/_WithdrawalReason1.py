# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max4Text import Max4Text
from ._WithdrawalReason1Code import WithdrawalReason1Code

class WithdrawalReason1(base_types._BaseFieldType):

	__slots__ = ["_WdrwlRsnCd", "_WdrwlRsnSubCd"]
	@property
	def WdrwlRsnCd(self):
		return self._WdrwlRsnCd

	@WdrwlRsnCd.setter
	def WdrwlRsnCd(self, value):
		self._WdrwlRsnCd = value if type(value) != base_types.auto else self.make_default("WdrwlRsnCd")

	@WdrwlRsnCd.deleter
	def WdrwlRsnCd(self):
		del self._WdrwlRsnCd
		self._WdrwlRsnCd = None

	@property
	def WdrwlRsnSubCd(self):
		return self._WdrwlRsnSubCd

	@WdrwlRsnSubCd.setter
	def WdrwlRsnSubCd(self, value):
		self._WdrwlRsnSubCd = value if type(value) != base_types.auto else self.make_default("WdrwlRsnSubCd")

	@WdrwlRsnSubCd.deleter
	def WdrwlRsnSubCd(self):
		del self._WdrwlRsnSubCd
		self._WdrwlRsnSubCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='WdrwlRsnCd', type=WithdrawalReason1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WdrwlRsnSubCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
	))