import base_types
import Max35Text
import POICommunicationType2Code
import Max35Binary
import Max2KBinary

class PhysicalInterfaceParameter1(base_types._BaseFieldType):

	__slots__ = ["_SctyPrfl", "_IntrfcNm", "_IntrfcTp", "_AccsCd", "_UsrNm", "_AddtlParams"]
	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if type(value) != auto else self.make_default("SctyPrfl")

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = None

	@property
	def IntrfcNm(self):
		return self._IntrfcNm

	@IntrfcNm.setter
	def IntrfcNm(self, value):
		self._IntrfcNm = value if type(value) != auto else self.make_default("IntrfcNm")

	@IntrfcNm.deleter
	def IntrfcNm(self):
		del self._IntrfcNm
		self._IntrfcNm = None

	@property
	def IntrfcTp(self):
		return self._IntrfcTp

	@IntrfcTp.setter
	def IntrfcTp(self, value):
		self._IntrfcTp = value if type(value) != auto else self.make_default("IntrfcTp")

	@IntrfcTp.deleter
	def IntrfcTp(self):
		del self._IntrfcTp
		self._IntrfcTp = None

	@property
	def AccsCd(self):
		return self._AccsCd

	@AccsCd.setter
	def AccsCd(self, value):
		self._AccsCd = value if type(value) != auto else self.make_default("AccsCd")

	@AccsCd.deleter
	def AccsCd(self):
		del self._AccsCd
		self._AccsCd = None

	@property
	def UsrNm(self):
		return self._UsrNm

	@UsrNm.setter
	def UsrNm(self, value):
		self._UsrNm = value if type(value) != auto else self.make_default("UsrNm")

	@UsrNm.deleter
	def UsrNm(self):
		del self._UsrNm
		self._UsrNm = None

	@property
	def AddtlParams(self):
		return self._AddtlParams

	@AddtlParams.setter
	def AddtlParams(self, value):
		self._AddtlParams = value if type(value) != auto else self.make_default("AddtlParams")

	@AddtlParams.deleter
	def AddtlParams(self):
		del self._AddtlParams
		self._AddtlParams = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrfcNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrfcTp', type=POICommunicationType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccsCd', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlParams', type=Max2KBinary, min=0, max=1, mutex_group=None, array=False),
	))

