# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChequeCancellationReason1Choice
from . import ChequePartyRole1Code
from . import Max140Text

class ChequeCancellationReason1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Orgtr", "_Rsn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@property
	def Orgtr(self):
		return self._Orgtr

	@Orgtr.setter
	def Orgtr(self, value):
		self._Orgtr = value if value is not None else base_types.UninitialisedField(self, 'Orgtr', ChequePartyRole1Code, False)

	@Orgtr.deleter
	def Orgtr(self):
		del self._Orgtr
		self._Orgtr = base_types.UninitialisedField(self, 'Orgtr', ChequePartyRole1Code, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', ChequeCancellationReason1Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', ChequeCancellationReason1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Orgtr', type=ChequePartyRole1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ChequeCancellationReason1Choice, min=1, max=1, mutex_group=None, array=False),
	))