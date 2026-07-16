# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Price7

class PriceType4Choice(base_types._BaseFieldType):

	__slots__ = ["_Indctv", "_Mkt"]
	@property
	def Indctv(self):
		return self._Indctv

	@Indctv.setter
	def Indctv(self, value):
		self._Indctv = value if value is not None else base_types.UninitialisedField(self, 'Indctv', Price7, False)

	@Indctv.deleter
	def Indctv(self):
		del self._Indctv
		self._Indctv = base_types.UninitialisedField(self, 'Indctv', Price7, False)

	@property
	def Mkt(self):
		return self._Mkt

	@Mkt.setter
	def Mkt(self, value):
		self._Mkt = value if value is not None else base_types.UninitialisedField(self, 'Mkt', Price7, False)

	@Mkt.deleter
	def Mkt(self):
		del self._Mkt
		self._Mkt = base_types.UninitialisedField(self, 'Mkt', Price7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Indctv', type=Price7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mkt', type=Price7, min=0, max=1, mutex_group=1, array=False),
	))