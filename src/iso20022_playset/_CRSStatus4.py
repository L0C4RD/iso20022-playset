# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CRSSource1Choice
from . import CRSStatus3Choice
from . import CountryCode

class CRSStatus4(base_types._BaseFieldType):

	__slots__ = ["_Src", "_Tp", "_XcptnlRptgCtry"]
	@property
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if value is not None else base_types.UninitialisedField(self, 'Src', CRSSource1Choice, False)

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = base_types.UninitialisedField(self, 'Src', CRSSource1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CRSStatus3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CRSStatus3Choice, False)

	@property
	def XcptnlRptgCtry(self):
		return self._XcptnlRptgCtry

	@XcptnlRptgCtry.setter
	def XcptnlRptgCtry(self, value):
		self._XcptnlRptgCtry = value if value is not None else base_types.UninitialisedField(self, 'XcptnlRptgCtry', CountryCode, False)

	@XcptnlRptgCtry.deleter
	def XcptnlRptgCtry(self):
		del self._XcptnlRptgCtry
		self._XcptnlRptgCtry = base_types.UninitialisedField(self, 'XcptnlRptgCtry', CountryCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Src', type=CRSSource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CRSStatus3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XcptnlRptgCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))