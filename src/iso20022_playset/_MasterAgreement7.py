from . import base_types
from .AgreementType2Choice import AgreementType2Choice
from .Max50Text import Max50Text
from .Max350Text import Max350Text

class MasterAgreement7(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Vrsn", "_OthrMstrAgrmtDtls"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def OthrMstrAgrmtDtls(self):
		return self._OthrMstrAgrmtDtls

	@OthrMstrAgrmtDtls.setter
	def OthrMstrAgrmtDtls(self, value):
		self._OthrMstrAgrmtDtls = value if type(value) != base_types.auto else self.make_default("OthrMstrAgrmtDtls")

	@OthrMstrAgrmtDtls.deleter
	def OthrMstrAgrmtDtls(self):
		del self._OthrMstrAgrmtDtls
		self._OthrMstrAgrmtDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=AgreementType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrMstrAgrmtDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

