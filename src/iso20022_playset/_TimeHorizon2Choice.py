# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import TimeFrame9Choice

class TimeHorizon2Choice(base_types._BaseFieldType):

	__slots__ = ["_NbOfYrs", "_TmFrame"]
	@property
	def NbOfYrs(self):
		return self._NbOfYrs

	@NbOfYrs.setter
	def NbOfYrs(self, value):
		self._NbOfYrs = value if value is not None else base_types.UninitialisedField(self, 'NbOfYrs', DecimalNumber, False)

	@NbOfYrs.deleter
	def NbOfYrs(self):
		del self._NbOfYrs
		self._NbOfYrs = base_types.UninitialisedField(self, 'NbOfYrs', DecimalNumber, False)

	@property
	def TmFrame(self):
		return self._TmFrame

	@TmFrame.setter
	def TmFrame(self, value):
		self._TmFrame = value if value is not None else base_types.UninitialisedField(self, 'TmFrame', TimeFrame9Choice, False)

	@TmFrame.deleter
	def TmFrame(self):
		del self._TmFrame
		self._TmFrame = base_types.UninitialisedField(self, 'TmFrame', TimeFrame9Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfYrs', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TmFrame', type=TimeFrame9Choice, min=0, max=1, mutex_group=1, array=False),
	))