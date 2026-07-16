# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StandingOrderIdentification8
from . import StandingOrderIdentification9

class StandingOrderOrAll4Choice(base_types._BaseFieldType):

	__slots__ = ["_AllStgOrdrs", "_StgOrdr"]
	@property
	def AllStgOrdrs(self):
		return self._AllStgOrdrs

	@AllStgOrdrs.setter
	def AllStgOrdrs(self, value):
		self._AllStgOrdrs = value if value is not None else base_types.UninitialisedField(self, 'AllStgOrdrs', StandingOrderIdentification9, True)

	@AllStgOrdrs.deleter
	def AllStgOrdrs(self):
		del self._AllStgOrdrs
		self._AllStgOrdrs = base_types.UninitialisedField(self, 'AllStgOrdrs', StandingOrderIdentification9, True)

	@property
	def StgOrdr(self):
		return self._StgOrdr

	@StgOrdr.setter
	def StgOrdr(self, value):
		self._StgOrdr = value if value is not None else base_types.UninitialisedField(self, 'StgOrdr', StandingOrderIdentification8, True)

	@StgOrdr.deleter
	def StgOrdr(self):
		del self._StgOrdr
		self._StgOrdr = base_types.UninitialisedField(self, 'StgOrdr', StandingOrderIdentification8, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllStgOrdrs', type=StandingOrderIdentification9, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='StgOrdr', type=StandingOrderIdentification8, min=1, max=None, mutex_group=1, array=True),
	))