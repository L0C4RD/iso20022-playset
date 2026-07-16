# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgreementType2Choice
from . import Max350Text
from . import Max50Text

class MasterAgreement7(base_types._BaseFieldType):

	__slots__ = ["_OthrMstrAgrmtDtls", "_Tp", "_Vrsn"]
	@property
	def OthrMstrAgrmtDtls(self):
		return self._OthrMstrAgrmtDtls

	@OthrMstrAgrmtDtls.setter
	def OthrMstrAgrmtDtls(self, value):
		self._OthrMstrAgrmtDtls = value if value is not None else base_types.UninitialisedField(self, 'OthrMstrAgrmtDtls', Max350Text, False)

	@OthrMstrAgrmtDtls.deleter
	def OthrMstrAgrmtDtls(self):
		del self._OthrMstrAgrmtDtls
		self._OthrMstrAgrmtDtls = base_types.UninitialisedField(self, 'OthrMstrAgrmtDtls', Max350Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', AgreementType2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', AgreementType2Choice, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max50Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max50Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrMstrAgrmtDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=AgreementType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))