# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10KText
from . import Max35Text
from . import PartyType28Code

class RiskInputData2(base_types._BaseFieldType):

	__slots__ = ["_NttyTp", "_OthrNttyTp", "_Tp", "_Val"]
	@property
	def NttyTp(self):
		return self._NttyTp

	@NttyTp.setter
	def NttyTp(self, value):
		self._NttyTp = value if value is not None else base_types.UninitialisedField(self, 'NttyTp', PartyType28Code, False)

	@NttyTp.deleter
	def NttyTp(self):
		del self._NttyTp
		self._NttyTp = base_types.UninitialisedField(self, 'NttyTp', PartyType28Code, False)

	@property
	def OthrNttyTp(self):
		return self._OthrNttyTp

	@OthrNttyTp.setter
	def OthrNttyTp(self, value):
		self._OthrNttyTp = value if value is not None else base_types.UninitialisedField(self, 'OthrNttyTp', Max35Text, False)

	@OthrNttyTp.deleter
	def OthrNttyTp(self):
		del self._OthrNttyTp
		self._OthrNttyTp = base_types.UninitialisedField(self, 'OthrNttyTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max10KText, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max10KText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NttyTp', type=PartyType28Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNttyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max10KText, min=1, max=1, mutex_group=None, array=False),
	))