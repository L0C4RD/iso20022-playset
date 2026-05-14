# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BenchmarkCurveName2Code import BenchmarkCurveName2Code
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._Max25Text import Max25Text

class BenchmarkCurveName6Choice(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_Indx", "_Nm"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != base_types.auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != base_types.auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indx', type=BenchmarkCurveName2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nm', type=Max25Text, min=0, max=1, mutex_group=1, array=False),
	))