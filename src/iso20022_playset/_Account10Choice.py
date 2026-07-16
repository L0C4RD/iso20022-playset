# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccountIdentification5Choice
from . import CashAccountIdentification9Choice

class Account10Choice(base_types._BaseFieldType):

	__slots__ = ["_ChrgsAcct", "_CshAcct", "_TaxAcct"]
	@property
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcct', CashAccountIdentification5Choice, False)

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = base_types.UninitialisedField(self, 'ChrgsAcct', CashAccountIdentification5Choice, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification9Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification9Choice, False)

	@property
	def TaxAcct(self):
		return self._TaxAcct

	@TaxAcct.setter
	def TaxAcct(self, value):
		self._TaxAcct = value if value is not None else base_types.UninitialisedField(self, 'TaxAcct', CashAccountIdentification5Choice, False)

	@TaxAcct.deleter
	def TaxAcct(self):
		del self._TaxAcct
		self._TaxAcct = base_types.UninitialisedField(self, 'TaxAcct', CashAccountIdentification5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=1, array=False),
	))