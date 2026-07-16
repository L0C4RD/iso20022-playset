# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DataSetCategory7Code
from . import Max35Text

class ATMConfigurationParameter1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Vrsn"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', DataSetCategory7Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', DataSetCategory7Code, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max35Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=DataSetCategory7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))