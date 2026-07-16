# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CollateralType22Choice

class TripartyCollateralAndAmount1(base_types._BaseFieldType):

	__slots__ = ["_CollTp", "_Trpty"]
	@property
	def CollTp(self):
		return self._CollTp

	@CollTp.setter
	def CollTp(self, value):
		self._CollTp = value if value is not None else base_types.UninitialisedField(self, 'CollTp', CollateralType22Choice, False)

	@CollTp.deleter
	def CollTp(self):
		del self._CollTp
		self._CollTp = base_types.UninitialisedField(self, 'CollTp', CollateralType22Choice, False)

	@property
	def Trpty(self):
		return self._Trpty

	@Trpty.setter
	def Trpty(self, value):
		self._Trpty = value if value is not None else base_types.UninitialisedField(self, 'Trpty', ActiveCurrencyAndAmount, False)

	@Trpty.deleter
	def Trpty(self):
		del self._Trpty
		self._Trpty = base_types.UninitialisedField(self, 'Trpty', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollTp', type=CollateralType22Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trpty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))