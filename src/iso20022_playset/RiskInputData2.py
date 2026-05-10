import base_types
import Max10KText
import PartyType28Code
import Max35Text

class RiskInputData2(base_types._BaseFieldType):

	__slots__ = ["_OthrNttyTp", "_Val", "_NttyTp", "_Tp"]
	@property
	def OthrNttyTp(self):
		return self._OthrNttyTp

	@OthrNttyTp.setter
	def OthrNttyTp(self, value):
		self._OthrNttyTp = value if type(value) != auto else self.make_default("OthrNttyTp")

	@OthrNttyTp.deleter
	def OthrNttyTp(self):
		del self._OthrNttyTp
		self._OthrNttyTp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if type(value) != auto else self.make_default("NttyTp")

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrNttyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max10KText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyTp', type=PartyType28Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

