# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralMarginCorrection6
from . import CollateralMarginError4
from . import CollateralMarginMarginUpdate5

class TradeReport21Choice(base_types._BaseFieldType):

	__slots__ = ["_Crrctn", "_Err", "_New", "_TradUpd"]
	@property
	def Crrctn(self):
		return self._Crrctn

	@Crrctn.setter
	def Crrctn(self, value):
		self._Crrctn = value if value is not None else base_types.UninitialisedField(self, 'Crrctn', CollateralMarginCorrection6, False)

	@Crrctn.deleter
	def Crrctn(self):
		del self._Crrctn
		self._Crrctn = base_types.UninitialisedField(self, 'Crrctn', CollateralMarginCorrection6, False)

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', CollateralMarginError4, False)

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = base_types.UninitialisedField(self, 'Err', CollateralMarginError4, False)

	@property
	def New(self):
		return self._New

	@New.setter
	def New(self, value):
		self._New = value if value is not None else base_types.UninitialisedField(self, 'New', CollateralMarginCorrection6, False)

	@New.deleter
	def New(self):
		del self._New
		self._New = base_types.UninitialisedField(self, 'New', CollateralMarginCorrection6, False)

	@property
	def TradUpd(self):
		return self._TradUpd

	@TradUpd.setter
	def TradUpd(self, value):
		self._TradUpd = value if value is not None else base_types.UninitialisedField(self, 'TradUpd', CollateralMarginMarginUpdate5, False)

	@TradUpd.deleter
	def TradUpd(self):
		del self._TradUpd
		self._TradUpd = base_types.UninitialisedField(self, 'TradUpd', CollateralMarginMarginUpdate5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Crrctn', type=CollateralMarginCorrection6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=CollateralMarginError4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='New', type=CollateralMarginCorrection6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TradUpd', type=CollateralMarginMarginUpdate5, min=0, max=1, mutex_group=1, array=False),
	))