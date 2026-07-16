# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import StressSize1Choice

class RiskFactor1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_StrssSz"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def StrssSz(self):
		return self._StrssSz

	@StrssSz.setter
	def StrssSz(self, value):
		self._StrssSz = value if value is not None else base_types.UninitialisedField(self, 'StrssSz', StressSize1Choice, False)

	@StrssSz.deleter
	def StrssSz(self):
		del self._StrssSz
		self._StrssSz = base_types.UninitialisedField(self, 'StrssSz', StressSize1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssSz', type=StressSize1Choice, min=1, max=1, mutex_group=None, array=False),
	))