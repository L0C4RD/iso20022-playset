# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StandingOrderIdentification8
from . import StandingOrderOrError10Choice

class StandingOrderReport3(base_types._BaseFieldType):

	__slots__ = ["_StgOrdrId", "_StgOrdrOrErr"]
	@property
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrId', StandingOrderIdentification8, False)

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = base_types.UninitialisedField(self, 'StgOrdrId', StandingOrderIdentification8, False)

	@property
	def StgOrdrOrErr(self):
		return self._StgOrdrOrErr

	@StgOrdrOrErr.setter
	def StgOrdrOrErr(self, value):
		self._StgOrdrOrErr = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrOrErr', StandingOrderOrError10Choice, False)

	@StgOrdrOrErr.deleter
	def StgOrdrOrErr(self):
		del self._StgOrdrOrErr
		self._StgOrdrOrErr = base_types.UninitialisedField(self, 'StgOrdrOrErr', StandingOrderOrError10Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StgOrdrId', type=StandingOrderIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrOrErr', type=StandingOrderOrError10Choice, min=1, max=1, mutex_group=None, array=False),
	))