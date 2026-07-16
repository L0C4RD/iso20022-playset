# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max70Text
from . import Quantity9
from . import YesNoIndicator

class CertifiedCharacteristics2Choice(base_types._BaseFieldType):

	__slots__ = ["_Anlys", "_HlthIndctn", "_Orgn", "_PhytosntryIndctn", "_Qlty", "_Qty", "_Wght"]
	@property
	def Anlys(self):
		return self._Anlys

	@Anlys.setter
	def Anlys(self, value):
		self._Anlys = value if value is not None else base_types.UninitialisedField(self, 'Anlys', Max70Text, False)

	@Anlys.deleter
	def Anlys(self):
		del self._Anlys
		self._Anlys = base_types.UninitialisedField(self, 'Anlys', Max70Text, False)

	@property
	def HlthIndctn(self):
		return self._HlthIndctn

	@HlthIndctn.setter
	def HlthIndctn(self, value):
		self._HlthIndctn = value if value is not None else base_types.UninitialisedField(self, 'HlthIndctn', YesNoIndicator, False)

	@HlthIndctn.deleter
	def HlthIndctn(self):
		del self._HlthIndctn
		self._HlthIndctn = base_types.UninitialisedField(self, 'HlthIndctn', YesNoIndicator, False)

	@property
	def Orgn(self):
		return self._Orgn

	@Orgn.setter
	def Orgn(self, value):
		self._Orgn = value if value is not None else base_types.UninitialisedField(self, 'Orgn', CountryCode, False)

	@Orgn.deleter
	def Orgn(self):
		del self._Orgn
		self._Orgn = base_types.UninitialisedField(self, 'Orgn', CountryCode, False)

	@property
	def PhytosntryIndctn(self):
		return self._PhytosntryIndctn

	@PhytosntryIndctn.setter
	def PhytosntryIndctn(self, value):
		self._PhytosntryIndctn = value if value is not None else base_types.UninitialisedField(self, 'PhytosntryIndctn', YesNoIndicator, False)

	@PhytosntryIndctn.deleter
	def PhytosntryIndctn(self):
		del self._PhytosntryIndctn
		self._PhytosntryIndctn = base_types.UninitialisedField(self, 'PhytosntryIndctn', YesNoIndicator, False)

	@property
	def Qlty(self):
		return self._Qlty

	@Qlty.setter
	def Qlty(self, value):
		self._Qlty = value if value is not None else base_types.UninitialisedField(self, 'Qlty', Max70Text, False)

	@Qlty.deleter
	def Qlty(self):
		del self._Qlty
		self._Qlty = base_types.UninitialisedField(self, 'Qlty', Max70Text, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Quantity9, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Quantity9, False)

	@property
	def Wght(self):
		return self._Wght

	@Wght.setter
	def Wght(self, value):
		self._Wght = value if value is not None else base_types.UninitialisedField(self, 'Wght', Quantity9, False)

	@Wght.deleter
	def Wght(self):
		del self._Wght
		self._Wght = base_types.UninitialisedField(self, 'Wght', Quantity9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Anlys', type=Max70Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='HlthIndctn', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Orgn', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PhytosntryIndctn', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qlty', type=Max70Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Wght', type=Quantity9, min=0, max=1, mutex_group=1, array=False),
	))