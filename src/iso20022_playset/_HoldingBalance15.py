# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SafekeepingPlaceFormat42Choice
from . import SecuritiesEntryType2Code
from . import SignedQuantityFormat15

class HoldingBalance15(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_BalTp", "_SfkpgPlc"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat15, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat15, False)

	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if value is not None else base_types.UninitialisedField(self, 'BalTp', SecuritiesEntryType2Code, False)

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = base_types.UninitialisedField(self, 'BalTp', SecuritiesEntryType2Code, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat42Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat42Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTp', type=SecuritiesEntryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat42Choice, min=0, max=1, mutex_group=None, array=False),
	))