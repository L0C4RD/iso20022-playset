# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class AcknowledgementDetails1Choice(base_types._BaseFieldType):

	__slots__ = ["_PayInCallRef", "_PayInSchdlRef"]
	@property
	def PayInCallRef(self):
		return self._PayInCallRef

	@PayInCallRef.setter
	def PayInCallRef(self, value):
		self._PayInCallRef = value if value is not None else base_types.UninitialisedField(self, 'PayInCallRef', Max35Text, False)

	@PayInCallRef.deleter
	def PayInCallRef(self):
		del self._PayInCallRef
		self._PayInCallRef = base_types.UninitialisedField(self, 'PayInCallRef', Max35Text, False)

	@property
	def PayInSchdlRef(self):
		return self._PayInSchdlRef

	@PayInSchdlRef.setter
	def PayInSchdlRef(self, value):
		self._PayInSchdlRef = value if value is not None else base_types.UninitialisedField(self, 'PayInSchdlRef', Max35Text, False)

	@PayInSchdlRef.deleter
	def PayInSchdlRef(self):
		del self._PayInSchdlRef
		self._PayInSchdlRef = base_types.UninitialisedField(self, 'PayInSchdlRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PayInCallRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PayInSchdlRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))