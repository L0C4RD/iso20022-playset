# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import OpeningConditions1

class NDFOpeningFixing1Choice(base_types._BaseFieldType):

	__slots__ = ["_OpngConds", "_OpngConfRef"]
	@property
	def OpngConds(self):
		return self._OpngConds

	@OpngConds.setter
	def OpngConds(self, value):
		self._OpngConds = value if value is not None else base_types.UninitialisedField(self, 'OpngConds', OpeningConditions1, False)

	@OpngConds.deleter
	def OpngConds(self):
		del self._OpngConds
		self._OpngConds = base_types.UninitialisedField(self, 'OpngConds', OpeningConditions1, False)

	@property
	def OpngConfRef(self):
		return self._OpngConfRef

	@OpngConfRef.setter
	def OpngConfRef(self, value):
		self._OpngConfRef = value if value is not None else base_types.UninitialisedField(self, 'OpngConfRef', Max35Text, False)

	@OpngConfRef.deleter
	def OpngConfRef(self):
		del self._OpngConfRef
		self._OpngConfRef = base_types.UninitialisedField(self, 'OpngConfRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngConds', type=OpeningConditions1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OpngConfRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))