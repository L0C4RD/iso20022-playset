# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2KBinary
from . import Max35Binary
from . import Max35Text
from . import POICommunicationType2Code

class PhysicalInterfaceParameter1(base_types._BaseFieldType):

	__slots__ = ["_AccsCd", "_AddtlParams", "_IntrfcNm", "_IntrfcTp", "_SctyPrfl", "_UsrNm"]
	@property
	def AccsCd(self):
		return self._AccsCd

	@AccsCd.setter
	def AccsCd(self, value):
		self._AccsCd = value if value is not None else base_types.UninitialisedField(self, 'AccsCd', Max35Binary, False)

	@AccsCd.deleter
	def AccsCd(self):
		del self._AccsCd
		self._AccsCd = base_types.UninitialisedField(self, 'AccsCd', Max35Binary, False)

	@property
	def AddtlParams(self):
		return self._AddtlParams

	@AddtlParams.setter
	def AddtlParams(self, value):
		self._AddtlParams = value if value is not None else base_types.UninitialisedField(self, 'AddtlParams', Max2KBinary, False)

	@AddtlParams.deleter
	def AddtlParams(self):
		del self._AddtlParams
		self._AddtlParams = base_types.UninitialisedField(self, 'AddtlParams', Max2KBinary, False)

	@property
	def IntrfcNm(self):
		return self._IntrfcNm

	@IntrfcNm.setter
	def IntrfcNm(self, value):
		self._IntrfcNm = value if value is not None else base_types.UninitialisedField(self, 'IntrfcNm', Max35Text, False)

	@IntrfcNm.deleter
	def IntrfcNm(self):
		del self._IntrfcNm
		self._IntrfcNm = base_types.UninitialisedField(self, 'IntrfcNm', Max35Text, False)

	@property
	def IntrfcTp(self):
		return self._IntrfcTp

	@IntrfcTp.setter
	def IntrfcTp(self, value):
		self._IntrfcTp = value if value is not None else base_types.UninitialisedField(self, 'IntrfcTp', POICommunicationType2Code, False)

	@IntrfcTp.deleter
	def IntrfcTp(self):
		del self._IntrfcTp
		self._IntrfcTp = base_types.UninitialisedField(self, 'IntrfcTp', POICommunicationType2Code, False)

	@property
	def SctyPrfl(self):
		return self._SctyPrfl

	@SctyPrfl.setter
	def SctyPrfl(self, value):
		self._SctyPrfl = value if value is not None else base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@SctyPrfl.deleter
	def SctyPrfl(self):
		del self._SctyPrfl
		self._SctyPrfl = base_types.UninitialisedField(self, 'SctyPrfl', Max35Text, False)

	@property
	def UsrNm(self):
		return self._UsrNm

	@UsrNm.setter
	def UsrNm(self, value):
		self._UsrNm = value if value is not None else base_types.UninitialisedField(self, 'UsrNm', Max35Text, False)

	@UsrNm.deleter
	def UsrNm(self):
		del self._UsrNm
		self._UsrNm = base_types.UninitialisedField(self, 'UsrNm', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccsCd', type=Max35Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlParams', type=Max2KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrfcNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrfcTp', type=POICommunicationType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyPrfl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))