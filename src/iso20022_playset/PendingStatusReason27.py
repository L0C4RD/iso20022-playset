import base_types
import Max210Text
import PendingReason66Choice

class PendingStatusReason27(base_types._BaseFieldType):

	__slots__ = ["_RsnCd", "_AddtlRsnInf"]
	@property
	def RsnCd(self):
		return self._RsnCd

	@RsnCd.setter
	def RsnCd(self, value):
		self._RsnCd = value if type(value) != auto else self.make_default("RsnCd")

	@RsnCd.deleter
	def RsnCd(self):
		del self._RsnCd
		self._RsnCd = None

	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsnCd', type=PendingReason66Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
	))

