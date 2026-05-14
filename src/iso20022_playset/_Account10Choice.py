# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CashAccountIdentification5Choice import CashAccountIdentification5Choice
from ._CashAccountIdentification9Choice import CashAccountIdentification9Choice

class Account10Choice(base_types._BaseFieldType):

	__slots__ = ["_ChrgsAcct", "_CshAcct", "_TaxAcct"]
	@property
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if type(value) != base_types.auto else self.make_default("ChrgsAcct")

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def TaxAcct(self):
		return self._TaxAcct

	@TaxAcct.setter
	def TaxAcct(self, value):
		self._TaxAcct = value if type(value) != base_types.auto else self.make_default("TaxAcct")

	@TaxAcct.deleter
	def TaxAcct(self):
		del self._TaxAcct
		self._TaxAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TaxAcct', type=CashAccountIdentification5Choice, min=0, max=1, mutex_group=1, array=False),
	))