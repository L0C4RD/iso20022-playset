# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class MarginRequirement1(base_types._BaseFieldType):

	__slots__ = ["_DlvrMrgnAmt", "_RtrMrgnAmt"]
	@property
	def DlvrMrgnAmt(self):
		return self._DlvrMrgnAmt

	@DlvrMrgnAmt.setter
	def DlvrMrgnAmt(self, value):
		self._DlvrMrgnAmt = value if value is not None else base_types.UninitialisedField(self, 'DlvrMrgnAmt', ActiveCurrencyAndAmount, False)

	@DlvrMrgnAmt.deleter
	def DlvrMrgnAmt(self):
		del self._DlvrMrgnAmt
		self._DlvrMrgnAmt = base_types.UninitialisedField(self, 'DlvrMrgnAmt', ActiveCurrencyAndAmount, False)

	@property
	def RtrMrgnAmt(self):
		return self._RtrMrgnAmt

	@RtrMrgnAmt.setter
	def RtrMrgnAmt(self, value):
		self._RtrMrgnAmt = value if value is not None else base_types.UninitialisedField(self, 'RtrMrgnAmt', ActiveCurrencyAndAmount, False)

	@RtrMrgnAmt.deleter
	def RtrMrgnAmt(self):
		del self._RtrMrgnAmt
		self._RtrMrgnAmt = base_types.UninitialisedField(self, 'RtrMrgnAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrMrgnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrMrgnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))