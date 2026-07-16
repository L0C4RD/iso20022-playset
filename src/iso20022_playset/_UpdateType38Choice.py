# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecuritiesSettlementTransactionDetails53
from . import SecuritiesSettlementTransactionDetails54
from . import SecuritiesSettlementTransactionDetails55

class UpdateType38Choice(base_types._BaseFieldType):

	__slots__ = ["_Addtn", "_Deltn", "_Mod"]
	@property
	def Addtn(self):
		return self._Addtn

	@Addtn.setter
	def Addtn(self, value):
		self._Addtn = value if value is not None else base_types.UninitialisedField(self, 'Addtn', SecuritiesSettlementTransactionDetails53, False)

	@Addtn.deleter
	def Addtn(self):
		del self._Addtn
		self._Addtn = base_types.UninitialisedField(self, 'Addtn', SecuritiesSettlementTransactionDetails53, False)

	@property
	def Deltn(self):
		return self._Deltn

	@Deltn.setter
	def Deltn(self, value):
		self._Deltn = value if value is not None else base_types.UninitialisedField(self, 'Deltn', SecuritiesSettlementTransactionDetails54, False)

	@Deltn.deleter
	def Deltn(self):
		del self._Deltn
		self._Deltn = base_types.UninitialisedField(self, 'Deltn', SecuritiesSettlementTransactionDetails54, False)

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', SecuritiesSettlementTransactionDetails55, False)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', SecuritiesSettlementTransactionDetails55, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Addtn', type=SecuritiesSettlementTransactionDetails53, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Deltn', type=SecuritiesSettlementTransactionDetails54, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mod', type=SecuritiesSettlementTransactionDetails55, min=0, max=1, mutex_group=1, array=False),
	))