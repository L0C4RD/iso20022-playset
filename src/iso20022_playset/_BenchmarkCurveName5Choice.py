# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BenchmarkCurveName2Code
from . import Max25Text

class BenchmarkCurveName5Choice(base_types._BaseFieldType):

	__slots__ = ["_Indx", "_Nm"]
	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if value is not None else base_types.UninitialisedField(self, 'Indx', BenchmarkCurveName2Code, False)

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = base_types.UninitialisedField(self, 'Indx', BenchmarkCurveName2Code, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max25Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max25Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Indx', type=BenchmarkCurveName2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nm', type=Max25Text, min=0, max=1, mutex_group=1, array=False),
	))