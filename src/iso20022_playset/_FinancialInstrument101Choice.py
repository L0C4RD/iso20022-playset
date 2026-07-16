# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAsset3
from . import FinancialInstrumentIdentification6
from . import OtherAsset2

class FinancialInstrument101Choice(base_types._BaseFieldType):

	__slots__ = ["_CshAsst", "_OthrAsst", "_Scty"]
	@property
	def CshAsst(self):
		return self._CshAsst

	@CshAsst.setter
	def CshAsst(self, value):
		self._CshAsst = value if value is not None else base_types.UninitialisedField(self, 'CshAsst', CashAsset3, False)

	@CshAsst.deleter
	def CshAsst(self):
		del self._CshAsst
		self._CshAsst = base_types.UninitialisedField(self, 'CshAsst', CashAsset3, False)

	@property
	def OthrAsst(self):
		return self._OthrAsst

	@OthrAsst.setter
	def OthrAsst(self, value):
		self._OthrAsst = value if value is not None else base_types.UninitialisedField(self, 'OthrAsst', OtherAsset2, False)

	@OthrAsst.deleter
	def OthrAsst(self):
		del self._OthrAsst
		self._OthrAsst = base_types.UninitialisedField(self, 'OthrAsst', OtherAsset2, False)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', FinancialInstrumentIdentification6, False)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', FinancialInstrumentIdentification6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAsst', type=CashAsset3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrAsst', type=OtherAsset2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Scty', type=FinancialInstrumentIdentification6, min=0, max=1, mutex_group=1, array=False),
	))