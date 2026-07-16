# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UnderlyingEquityType3Code
from . import UnderlyingEquityType4Code
from . import UnderlyingEquityType5Code
from . import UnderlyingEquityType6Code

class EquityDerivative3Choice(base_types._BaseFieldType):

	__slots__ = ["_Bskt", "_Indx", "_Othr", "_SnglNm"]
	@property
	def Bskt(self):
		return self._Bskt

	@Bskt.setter
	def Bskt(self, value):
		self._Bskt = value if value is not None else base_types.UninitialisedField(self, 'Bskt', UnderlyingEquityType3Code, False)

	@Bskt.deleter
	def Bskt(self):
		del self._Bskt
		self._Bskt = base_types.UninitialisedField(self, 'Bskt', UnderlyingEquityType3Code, False)

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if value is not None else base_types.UninitialisedField(self, 'Indx', UnderlyingEquityType4Code, False)

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = base_types.UninitialisedField(self, 'Indx', UnderlyingEquityType4Code, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', UnderlyingEquityType6Code, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', UnderlyingEquityType6Code, False)

	@property
	def SnglNm(self):
		return self._SnglNm

	@SnglNm.setter
	def SnglNm(self, value):
		self._SnglNm = value if value is not None else base_types.UninitialisedField(self, 'SnglNm', UnderlyingEquityType5Code, False)

	@SnglNm.deleter
	def SnglNm(self):
		del self._SnglNm
		self._SnglNm = base_types.UninitialisedField(self, 'SnglNm', UnderlyingEquityType5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bskt', type=UnderlyingEquityType3Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indx', type=UnderlyingEquityType4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=UnderlyingEquityType6Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SnglNm', type=UnderlyingEquityType5Code, min=0, max=1, mutex_group=1, array=False),
	))