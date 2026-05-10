from . import base_types
from .WithdrawalReason1Code import WithdrawalReason1Code
from .Max4Text import Max4Text

class WithdrawalReason1(base_types._BaseFieldType):

	__slots__ = ["_WdrwlRsnSubCd", "_WdrwlRsnCd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='WdrwlRsnSubCd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WdrwlRsnCd', type=WithdrawalReason1Code, min=1, max=1, mutex_group=None, array=False),
	))

