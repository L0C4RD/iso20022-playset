from . import base_types
from ._Max35Text import Max35Text

class AcknowledgementDetails1Choice(base_types._BaseFieldType):

	__slots__ = ["_PayInSchdlRef", "_PayInCallRef"]
	@property
	def PayInCallRef(self):
		return self._PayInCallRef

	@PayInCallRef.setter
	def PayInCallRef(self, value):
		self._PayInCallRef = value if type(value) != base_types.auto else self.make_default("PayInCallRef")

	@PayInCallRef.deleter
	def PayInCallRef(self):
		del self._PayInCallRef
		self._PayInCallRef = None

	@property
	def PayInSchdlRef(self):
		return self._PayInSchdlRef

	@PayInSchdlRef.setter
	def PayInSchdlRef(self, value):
		self._PayInSchdlRef = value if type(value) != base_types.auto else self.make_default("PayInSchdlRef")

	@PayInSchdlRef.deleter
	def PayInSchdlRef(self):
		del self._PayInSchdlRef
		self._PayInSchdlRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PayInCallRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PayInSchdlRef', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

