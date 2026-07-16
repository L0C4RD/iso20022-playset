# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesEntryType3Code
from . import SignedQuantityFormat14

class HoldingBalance13(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_BalTp"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat14, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', SignedQuantityFormat14, False)

	@property
	def BalTp(self):
		return self._BalTp

	@BalTp.setter
	def BalTp(self, value):
		self._BalTp = value if value is not None else base_types.UninitialisedField(self, 'BalTp', SecuritiesEntryType3Code, False)

	@BalTp.deleter
	def BalTp(self):
		del self._BalTp
		self._BalTp = base_types.UninitialisedField(self, 'BalTp', SecuritiesEntryType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=SignedQuantityFormat14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTp', type=SecuritiesEntryType3Code, min=1, max=1, mutex_group=None, array=False),
	))