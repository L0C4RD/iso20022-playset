# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax140Text
from . import SubBalanceQuantity9Choice
from . import SubBalanceType14Choice

class AdditionalBalanceInformation23(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_SubBalAddtlDtls", "_SubBalTp"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity9Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity9Choice, False)

	@property
	def SubBalAddtlDtls(self):
		return self._SubBalAddtlDtls

	@SubBalAddtlDtls.setter
	def SubBalAddtlDtls(self, value):
		self._SubBalAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'SubBalAddtlDtls', RestrictedFINXMax140Text, False)

	@SubBalAddtlDtls.deleter
	def SubBalAddtlDtls(self):
		del self._SubBalAddtlDtls
		self._SubBalAddtlDtls = base_types.UninitialisedField(self, 'SubBalAddtlDtls', RestrictedFINXMax140Text, False)

	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if value is not None else base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType14Choice, False)

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType14Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity9Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalAddtlDtls', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType14Choice, min=1, max=1, mutex_group=None, array=False),
	))