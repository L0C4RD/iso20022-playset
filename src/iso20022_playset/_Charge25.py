# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChargesDetails4
from . import FreightCharges1Code

class Charge25(base_types._BaseFieldType):

	__slots__ = ["_Chrgs", "_Tp"]
	@property
	def Chrgs(self):
		return self._Chrgs

	@Chrgs.setter
	def Chrgs(self, value):
		self._Chrgs = value if value is not None else base_types.UninitialisedField(self, 'Chrgs', ChargesDetails4, True)

	@Chrgs.deleter
	def Chrgs(self):
		del self._Chrgs
		self._Chrgs = base_types.UninitialisedField(self, 'Chrgs', ChargesDetails4, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', FreightCharges1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', FreightCharges1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chrgs', type=ChargesDetails4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=FreightCharges1Code, min=1, max=1, mutex_group=None, array=False),
	))