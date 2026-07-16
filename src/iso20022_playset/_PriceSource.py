# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PriceSource1Code

class PriceSource(base_types._BaseFieldType):

	__slots__ = ["_Nrrtv", "_PricSrc"]
	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if value is not None else base_types.UninitialisedField(self, 'Nrrtv', Max35Text, False)

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = base_types.UninitialisedField(self, 'Nrrtv', Max35Text, False)

	@property
	def PricSrc(self):
		return self._PricSrc

	@PricSrc.setter
	def PricSrc(self, value):
		self._PricSrc = value if value is not None else base_types.UninitialisedField(self, 'PricSrc', PriceSource1Code, False)

	@PricSrc.deleter
	def PricSrc(self):
		del self._PricSrc
		self._PricSrc = base_types.UninitialisedField(self, 'PricSrc', PriceSource1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nrrtv', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSrc', type=PriceSource1Code, min=1, max=1, mutex_group=None, array=False),
	))