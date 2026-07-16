# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MaturityTerm2

class TimeToMaturityPeriod1(base_types._BaseFieldType):

	__slots__ = ["_End", "_Start"]
	@property
	def End(self):
		return self._End

	@End.setter
	def End(self, value):
		self._End = value if value is not None else base_types.UninitialisedField(self, 'End', MaturityTerm2, False)

	@End.deleter
	def End(self):
		del self._End
		self._End = base_types.UninitialisedField(self, 'End', MaturityTerm2, False)

	@property
	def Start(self):
		return self._Start

	@Start.setter
	def Start(self, value):
		self._Start = value if value is not None else base_types.UninitialisedField(self, 'Start', MaturityTerm2, False)

	@Start.deleter
	def Start(self):
		del self._Start
		self._Start = base_types.UninitialisedField(self, 'Start', MaturityTerm2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='End', type=MaturityTerm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Start', type=MaturityTerm2, min=0, max=1, mutex_group=None, array=False),
	))