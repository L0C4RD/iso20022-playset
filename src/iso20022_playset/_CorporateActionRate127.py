# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Percentage14Rate
from . import RateAndAmountFormat55Choice
from . import RateAndAmountFormat59Choice

class CorporateActionRate127(base_types._BaseFieldType):

	__slots__ = ["_OvrsbcptRate", "_PropsdRate", "_ReqdScndLvlTaxRate", "_ReqdWhldgTaxRate"]
	@property
	def OvrsbcptRate(self):
		return self._OvrsbcptRate

	@OvrsbcptRate.setter
	def OvrsbcptRate(self, value):
		self._OvrsbcptRate = value if value is not None else base_types.UninitialisedField(self, 'OvrsbcptRate', RateAndAmountFormat59Choice, False)

	@OvrsbcptRate.deleter
	def OvrsbcptRate(self):
		del self._OvrsbcptRate
		self._OvrsbcptRate = base_types.UninitialisedField(self, 'OvrsbcptRate', RateAndAmountFormat59Choice, False)

	@property
	def PropsdRate(self):
		return self._PropsdRate

	@PropsdRate.setter
	def PropsdRate(self, value):
		self._PropsdRate = value if value is not None else base_types.UninitialisedField(self, 'PropsdRate', Percentage14Rate, False)

	@PropsdRate.deleter
	def PropsdRate(self):
		del self._PropsdRate
		self._PropsdRate = base_types.UninitialisedField(self, 'PropsdRate', Percentage14Rate, False)

	@property
	def ReqdScndLvlTaxRate(self):
		return self._ReqdScndLvlTaxRate

	@ReqdScndLvlTaxRate.setter
	def ReqdScndLvlTaxRate(self, value):
		self._ReqdScndLvlTaxRate = value if value is not None else base_types.UninitialisedField(self, 'ReqdScndLvlTaxRate', RateAndAmountFormat55Choice, True)

	@ReqdScndLvlTaxRate.deleter
	def ReqdScndLvlTaxRate(self):
		del self._ReqdScndLvlTaxRate
		self._ReqdScndLvlTaxRate = base_types.UninitialisedField(self, 'ReqdScndLvlTaxRate', RateAndAmountFormat55Choice, True)

	@property
	def ReqdWhldgTaxRate(self):
		return self._ReqdWhldgTaxRate

	@ReqdWhldgTaxRate.setter
	def ReqdWhldgTaxRate(self, value):
		self._ReqdWhldgTaxRate = value if value is not None else base_types.UninitialisedField(self, 'ReqdWhldgTaxRate', RateAndAmountFormat55Choice, True)

	@ReqdWhldgTaxRate.deleter
	def ReqdWhldgTaxRate(self):
		del self._ReqdWhldgTaxRate
		self._ReqdWhldgTaxRate = base_types.UninitialisedField(self, 'ReqdWhldgTaxRate', RateAndAmountFormat55Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OvrsbcptRate', type=RateAndAmountFormat59Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdRate', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdScndLvlTaxRate', type=RateAndAmountFormat55Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdWhldgTaxRate', type=RateAndAmountFormat55Choice, min=0, max=None, mutex_group=None, array=True),
	))