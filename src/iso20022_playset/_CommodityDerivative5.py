# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max25Text

class CommodityDerivative5(base_types._BaseFieldType):

	__slots__ = ["_AvrgTmChrtr", "_Sz"]
	@property
	def AvrgTmChrtr(self):
		return self._AvrgTmChrtr

	@AvrgTmChrtr.setter
	def AvrgTmChrtr(self, value):
		self._AvrgTmChrtr = value if value is not None else base_types.UninitialisedField(self, 'AvrgTmChrtr', Max25Text, False)

	@AvrgTmChrtr.deleter
	def AvrgTmChrtr(self):
		del self._AvrgTmChrtr
		self._AvrgTmChrtr = base_types.UninitialisedField(self, 'AvrgTmChrtr', Max25Text, False)

	@property
	def Sz(self):
		return self._Sz

	@Sz.setter
	def Sz(self, value):
		self._Sz = value if value is not None else base_types.UninitialisedField(self, 'Sz', Max25Text, False)

	@Sz.deleter
	def Sz(self):
		del self._Sz
		self._Sz = base_types.UninitialisedField(self, 'Sz', Max25Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgTmChrtr', type=Max25Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sz', type=Max25Text, min=1, max=1, mutex_group=None, array=False),
	))