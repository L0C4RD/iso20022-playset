# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EventCompletenessStatus1Code
from . import EventConfirmationStatus1Code

class CorporateActionEventStatus1(base_types._BaseFieldType):

	__slots__ = ["_EvtCmpltnsSts", "_EvtConfSts"]
	@property
	def EvtCmpltnsSts(self):
		return self._EvtCmpltnsSts

	@EvtCmpltnsSts.setter
	def EvtCmpltnsSts(self, value):
		self._EvtCmpltnsSts = value if value is not None else base_types.UninitialisedField(self, 'EvtCmpltnsSts', EventCompletenessStatus1Code, False)

	@EvtCmpltnsSts.deleter
	def EvtCmpltnsSts(self):
		del self._EvtCmpltnsSts
		self._EvtCmpltnsSts = base_types.UninitialisedField(self, 'EvtCmpltnsSts', EventCompletenessStatus1Code, False)

	@property
	def EvtConfSts(self):
		return self._EvtConfSts

	@EvtConfSts.setter
	def EvtConfSts(self, value):
		self._EvtConfSts = value if value is not None else base_types.UninitialisedField(self, 'EvtConfSts', EventConfirmationStatus1Code, False)

	@EvtConfSts.deleter
	def EvtConfSts(self):
		del self._EvtConfSts
		self._EvtConfSts = base_types.UninitialisedField(self, 'EvtConfSts', EventConfirmationStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtCmpltnsSts', type=EventCompletenessStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtConfSts', type=EventConfirmationStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))