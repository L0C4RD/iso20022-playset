import base_types
import SettlementTotalData1Choice

class SettlementDailyFailureReason3(base_types._BaseFieldType):

	__slots__ = ["_FaildCsh", "_FaildScties"]
	@property
	def FaildCsh(self):
		return self._FaildCsh

	@FaildCsh.setter
	def FaildCsh(self, value):
		self._FaildCsh = value if type(value) != auto else self.make_default("FaildCsh")

	@FaildCsh.deleter
	def FaildCsh(self):
		del self._FaildCsh
		self._FaildCsh = None

	@property
	def FaildScties(self):
		return self._FaildScties

	@FaildScties.setter
	def FaildScties(self, value):
		self._FaildScties = value if type(value) != auto else self.make_default("FaildScties")

	@FaildScties.deleter
	def FaildScties(self):
		del self._FaildScties
		self._FaildScties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FaildCsh', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaildScties', type=SettlementTotalData1Choice, min=1, max=1, mutex_group=None, array=False),
	))

