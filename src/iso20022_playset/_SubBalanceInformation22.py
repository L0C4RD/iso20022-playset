# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalBalanceInformation22
from . import Max140Text
from . import SubBalanceQuantity8Choice
from . import SubBalanceType11Choice

class SubBalanceInformation22(base_types._BaseFieldType):

	__slots__ = ["_AddtlBalBrkdwnDtls", "_Qty", "_SubBalAddtlDtls", "_SubBalTp"]
	@property
	def AddtlBalBrkdwnDtls(self):
		return self._AddtlBalBrkdwnDtls

	@AddtlBalBrkdwnDtls.setter
	def AddtlBalBrkdwnDtls(self, value):
		self._AddtlBalBrkdwnDtls = value if value is not None else base_types.UninitialisedField(self, 'AddtlBalBrkdwnDtls', AdditionalBalanceInformation22, True)

	@AddtlBalBrkdwnDtls.deleter
	def AddtlBalBrkdwnDtls(self):
		del self._AddtlBalBrkdwnDtls
		self._AddtlBalBrkdwnDtls = base_types.UninitialisedField(self, 'AddtlBalBrkdwnDtls', AdditionalBalanceInformation22, True)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity8Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity8Choice, False)

	@property
	def SubBalAddtlDtls(self):
		return self._SubBalAddtlDtls

	@SubBalAddtlDtls.setter
	def SubBalAddtlDtls(self, value):
		self._SubBalAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'SubBalAddtlDtls', Max140Text, False)

	@SubBalAddtlDtls.deleter
	def SubBalAddtlDtls(self):
		del self._SubBalAddtlDtls
		self._SubBalAddtlDtls = base_types.UninitialisedField(self, 'SubBalAddtlDtls', Max140Text, False)

	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if value is not None else base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType11Choice, False)

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = base_types.UninitialisedField(self, 'SubBalTp', SubBalanceType11Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlBalBrkdwnDtls', type=AdditionalBalanceInformation22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalAddtlDtls', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SubBalanceType11Choice, min=1, max=1, mutex_group=None, array=False),
	))