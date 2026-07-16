# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Derivative3
from . import FinancialInstrument59
from . import RepurchaseAgreement3

class Product1Choice(base_types._BaseFieldType):

	__slots__ = ["_Deriv", "_SctiesFincgTx", "_Scty"]
	@property
	def Deriv(self):
		return self._Deriv

	@Deriv.setter
	def Deriv(self, value):
		self._Deriv = value if value is not None else base_types.UninitialisedField(self, 'Deriv', Derivative3, False)

	@Deriv.deleter
	def Deriv(self):
		del self._Deriv
		self._Deriv = base_types.UninitialisedField(self, 'Deriv', Derivative3, False)

	@property
	def SctiesFincgTx(self):
		return self._SctiesFincgTx

	@SctiesFincgTx.setter
	def SctiesFincgTx(self, value):
		self._SctiesFincgTx = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgTx', RepurchaseAgreement3, False)

	@SctiesFincgTx.deleter
	def SctiesFincgTx(self):
		del self._SctiesFincgTx
		self._SctiesFincgTx = base_types.UninitialisedField(self, 'SctiesFincgTx', RepurchaseAgreement3, False)

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if value is not None else base_types.UninitialisedField(self, 'Scty', FinancialInstrument59, False)

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = base_types.UninitialisedField(self, 'Scty', FinancialInstrument59, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Deriv', type=Derivative3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgTx', type=RepurchaseAgreement3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Scty', type=FinancialInstrument59, min=0, max=1, mutex_group=1, array=False),
	))