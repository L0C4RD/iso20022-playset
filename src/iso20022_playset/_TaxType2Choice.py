# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import TaxType9Code

class TaxType2Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrTaxTp", "_Tp"]
	@property
	def OthrTaxTp(self):
		return self._OthrTaxTp

	@OthrTaxTp.setter
	def OthrTaxTp(self, value):
		self._OthrTaxTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTaxTp', Max35Text, False)

	@OthrTaxTp.deleter
	def OthrTaxTp(self):
		del self._OthrTaxTp
		self._OthrTaxTp = base_types.UninitialisedField(self, 'OthrTaxTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TaxType9Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TaxType9Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrTaxTp', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType9Code, min=0, max=1, mutex_group=1, array=False),
	))