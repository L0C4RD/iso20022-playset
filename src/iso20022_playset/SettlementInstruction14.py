import base_types
import CashAccount40
import ClearingSystemIdentification3Choice
import SettlementMethod2Code

class SettlementInstruction14(base_types._BaseFieldType):

	__slots__ = ["_SttlmAcct", "_SttlmMtd", "_ClrSys"]
	@property
	def SttlmAcct(self):
		return self._SttlmAcct

	@SttlmAcct.setter
	def SttlmAcct(self, value):
		self._SttlmAcct = value if type(value) != auto else self.make_default("SttlmAcct")

	@SttlmAcct.deleter
	def SttlmAcct(self):
		del self._SttlmAcct
		self._SttlmAcct = None

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if type(value) != auto else self.make_default("SttlmMtd")

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = None

	@property
	def ClrSys(self):
		return self._ClrSys

	@ClrSys.setter
	def ClrSys(self, value):
		self._ClrSys = value if type(value) != auto else self.make_default("ClrSys")

	@ClrSys.deleter
	def ClrSys(self):
		del self._ClrSys
		self._ClrSys = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=SettlementMethod2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSys', type=ClearingSystemIdentification3Choice, min=0, max=1, mutex_group=None, array=False),
	))

