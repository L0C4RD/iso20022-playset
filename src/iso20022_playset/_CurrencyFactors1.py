# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgreedRate2
from . import CurrencyCode
from . import ImpliedCurrencyAndAmount
from . import PercentageRate

class CurrencyFactors1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_MinPayInAmt", "_Rate", "_ShrtPosLmt", "_VoltlyMrgn"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', CurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', CurrencyCode, False)

	@property
	def MinPayInAmt(self):
		return self._MinPayInAmt

	@MinPayInAmt.setter
	def MinPayInAmt(self, value):
		self._MinPayInAmt = value if value is not None else base_types.UninitialisedField(self, 'MinPayInAmt', ImpliedCurrencyAndAmount, False)

	@MinPayInAmt.deleter
	def MinPayInAmt(self):
		del self._MinPayInAmt
		self._MinPayInAmt = base_types.UninitialisedField(self, 'MinPayInAmt', ImpliedCurrencyAndAmount, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', AgreedRate2, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', AgreedRate2, False)

	@property
	def ShrtPosLmt(self):
		return self._ShrtPosLmt

	@ShrtPosLmt.setter
	def ShrtPosLmt(self, value):
		self._ShrtPosLmt = value if value is not None else base_types.UninitialisedField(self, 'ShrtPosLmt', ImpliedCurrencyAndAmount, False)

	@ShrtPosLmt.deleter
	def ShrtPosLmt(self):
		del self._ShrtPosLmt
		self._ShrtPosLmt = base_types.UninitialisedField(self, 'ShrtPosLmt', ImpliedCurrencyAndAmount, False)

	@property
	def VoltlyMrgn(self):
		return self._VoltlyMrgn

	@VoltlyMrgn.setter
	def VoltlyMrgn(self, value):
		self._VoltlyMrgn = value if value is not None else base_types.UninitialisedField(self, 'VoltlyMrgn', PercentageRate, False)

	@VoltlyMrgn.deleter
	def VoltlyMrgn(self):
		del self._VoltlyMrgn
		self._VoltlyMrgn = base_types.UninitialisedField(self, 'VoltlyMrgn', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=CurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinPayInAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=AgreedRate2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtPosLmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoltlyMrgn', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))