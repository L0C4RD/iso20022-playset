from . import base_types
from ._EventCompletenessStatus1Code import EventCompletenessStatus1Code
from ._EventConfirmationStatus1Code import EventConfirmationStatus1Code

class EventStatus1(base_types._BaseFieldType):

	__slots__ = ["_EvtConfSts", "_EvtCmpltnsSts"]
	@property
	def EvtConfSts(self):
		return self._EvtConfSts

	@EvtConfSts.setter
	def EvtConfSts(self, value):
		self._EvtConfSts = value if type(value) != base_types.auto else self.make_default("EvtConfSts")

	@EvtConfSts.deleter
	def EvtConfSts(self):
		del self._EvtConfSts
		self._EvtConfSts = None

	@property
	def EvtCmpltnsSts(self):
		return self._EvtCmpltnsSts

	@EvtCmpltnsSts.setter
	def EvtCmpltnsSts(self, value):
		self._EvtCmpltnsSts = value if type(value) != base_types.auto else self.make_default("EvtCmpltnsSts")

	@EvtCmpltnsSts.deleter
	def EvtCmpltnsSts(self):
		del self._EvtCmpltnsSts
		self._EvtCmpltnsSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtConfSts', type=EventConfirmationStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtCmpltnsSts', type=EventCompletenessStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

