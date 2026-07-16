# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Extended350Code
from . import SecuritiesBalanceType2Code
from . import SubBalanceQuantity1Choice

class AdditionalBalanceInformation2(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_SubBalTp", "_XtndedSubBalTp"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', SubBalanceQuantity1Choice, False)

	@property
	def SubBalTp(self):
		return self._SubBalTp

	@SubBalTp.setter
	def SubBalTp(self, value):
		self._SubBalTp = value if value is not None else base_types.UninitialisedField(self, 'SubBalTp', SecuritiesBalanceType2Code, False)

	@SubBalTp.deleter
	def SubBalTp(self):
		del self._SubBalTp
		self._SubBalTp = base_types.UninitialisedField(self, 'SubBalTp', SecuritiesBalanceType2Code, False)

	@property
	def XtndedSubBalTp(self):
		return self._XtndedSubBalTp

	@XtndedSubBalTp.setter
	def XtndedSubBalTp(self, value):
		self._XtndedSubBalTp = value if value is not None else base_types.UninitialisedField(self, 'XtndedSubBalTp', Extended350Code, False)

	@XtndedSubBalTp.deleter
	def XtndedSubBalTp(self):
		del self._XtndedSubBalTp
		self._XtndedSubBalTp = base_types.UninitialisedField(self, 'XtndedSubBalTp', Extended350Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=SubBalanceQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBalTp', type=SecuritiesBalanceType2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedSubBalTp', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))